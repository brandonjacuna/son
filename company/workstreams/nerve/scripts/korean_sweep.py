"""Korean micro-watch sweep (BRIEF.md section 8): find every Korean concept in the metro.

Usage: python scripts/korean_sweep.py

Scans TABC pending applications and licenses, Comptroller sales tax permits,
Mixed Beverage Gross Receipts, and Austin inspections for Korean names and terms,
groups hits across sources by address, assigns areas, and writes:
  data/korean_sweep/candidates.csv   one row per candidate venue, for Brandon to confirm
  data/korean_sweep/hits.csv         every matching source record
  data/korean_sweep/run_health.json
`tier` comes from config/korean_watch.json: direct_comp (Oseyo) or awareness.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import timedelta
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from areas import Areas  # noqa: E402
from common import DATA_DIR, TIMEOUT, classify_error, now_utc, redact, session, write_run_health  # noqa: E402
from geocode import Geocoder  # noqa: E402

OUT = DATA_DIR / "korean_sweep"
WATCH = Path(__file__).resolve().parent.parent / "config" / "korean_watch.json"

# Strong: unambiguous Korean food words, places, and Korean-origin chains.
STRONG = ["KOREA", "SEOUL", "HANSIK", "KBBQ", "K-BBQ", "K BBQ", "BIBIMBAP", "BIBIMBOP", "GALBI", "KALBI", "SOJU",
          "POCHA", "BANCHAN", "KIMCHI", "BULGOGI", "TTEOK", "TOKBOKKI", "DUKBOKKI", "JJIGAE", "JJIM", "GANGNAM",
          "BUSAN", "JEJU", "HANGUK", "SAMGYUP", "SAMGYEOPSAL", "JAPCHAE", "NAENGMYEON", "SUNDUBU", "SOONDUBU",
          "TOFU HOUSE", "HANOK", "BONCHON", "KYOCHON", "PELICANA", "CUPBOP", "CHI'LANTRO", "CHILANTRO", "KORIENTE",
          "OSEYO", "H MART", "HMART", "BBQ CHICKEN", "BB.Q", "GEN KOREAN", "CHIMAEK", "MAKGEOLLI", "HOTTEOK",
          "KTOWN", "K-TOWN", "HANAROO", "BAP BAP"]
# Weak: often Korean, often not. Kept for review, never auto-confirmed.
WEAK = ["ARIRANG", "OPPA", "NOONA", "UNNIE", "DAEBAK", "MANDU", "GOGI", "KIM'S", "MIGA", "SURA", "HANA ", "BAP ",
        "MAMA KIM", "CHIKIN", "K-POP", "KPOP", "K POP", "K-FOOD", "K FOOD", "SEOUL"]
WEAK = [w for w in WEAK if w not in STRONG]

METRO_COUNTY_NAMES = ["Travis", "Williamson", "Hays", "Bastrop", "Caldwell"]
METRO_COUNTY_CODES = ["227", "246", "105", "011", "11", "028", "28"]

FOOD_NAICS = re.compile(r"^(7225|72241|72233|72232|311811|312120|4451|44511|445)")


def term_rx(terms, whole_word: bool):
    """Leading word boundary always; trailing only for weak terms (strong ones prefix e.g. KOREAN, JJIMDAK)."""
    tail = r"(?![A-Z])" if whole_word else ""
    return re.compile("|".join(r"(?<![A-Z])" + re.escape(t.strip()) + tail for t in terms))


STRONG_RX, WEAK_RX = term_rx(STRONG, False), term_rx(WEAK, True)


def like_clause(fields: list[str]) -> str:
    terms = sorted({t.strip().replace("'", "''") for t in STRONG + WEAK})
    return "(" + " OR ".join(f"upper({f}) like '%{t}%'" for f in fields for t in terms) + ")"


def match(*names) -> tuple[str | None, list[str]]:
    text = " | ".join(str(n).upper() for n in names if isinstance(n, str) and n)
    strong = sorted({m.group(0).strip() for m in STRONG_RX.finditer(text)})
    if strong:
        return "strong", strong
    weak = sorted({m.group(0).strip() for m in WEAK_RX.finditer(text)})
    return ("weak", weak) if weak else (None, [])


def soql(s, domain: str, dataset: str, params: dict) -> list[dict]:
    rows, offset = [], 0
    while True:
        r = s.get(f"https://{domain}/resource/{dataset}.json", params={**params, "$limit": 5000, "$offset": offset},
                  timeout=TIMEOUT * 2)
        r.raise_for_status()
        batch = r.json()
        rows += batch
        if len(batch) < 5000:
            return rows
        offset += 5000


# ---------------------------------------------------------------- per source

def tabc_pending(s):
    where = f"{like_clause(['trade_name', 'owner'])} AND county in ({','.join(repr(c) for c in METRO_COUNTY_NAMES)})"
    for r in soql(s, "data.texas.gov", "mxm5-tdpj", {"$where": where}):
        yield {"source": "tabc_pending", "record_id": r.get("applicationid"), "name": r.get("trade_name") or r.get("owner"),
               "owner": r.get("owner"), "address": r.get("address"), "city": r.get("city"), "zip": r.get("zip"),
               "status": f"pending: {r.get('applicationstatus')}", "license_type": r.get("license_type"),
               "date": (r.get("submission_date") or "")[:10], "date_kind": "application submitted"}


def tabc_licenses(s):
    where = f"{like_clause(['trade_name', 'owner'])} AND county in ({','.join(repr(c) for c in METRO_COUNTY_NAMES)})"
    for r in soql(s, "data.texas.gov", "7hf9-qc9f", {"$where": where}):
        yield {"source": "tabc_licenses", "record_id": r.get("license_id"), "name": r.get("trade_name") or r.get("owner"),
               "owner": r.get("owner"), "address": r.get("address"), "city": r.get("city"), "zip": r.get("zip"),
               "status": r.get("primary_status") or r.get("license_status"), "license_type": r.get("license_type"),
               "date": (r.get("original_issue_date") or "")[:10], "date_kind": "original issue",
               "status_change_date": (r.get("status_change_date") or "")[:10]}


def sales_tax_permits(s):
    where = f"{like_clause(['outlet_name', 'taxpayer_name'])} AND outlet_county_code in ({','.join(repr(c) for c in METRO_COUNTY_CODES)})"
    for r in soql(s, "data.texas.gov", "jrea-zgmq", {"$where": where}):
        yield {"source": "sales_tax_permits", "record_id": f"{r.get('taxpayer_number')}-{r.get('outlet_number')}",
               "name": r.get("outlet_name"), "owner": r.get("taxpayer_name"), "address": r.get("outlet_address"),
               "city": r.get("outlet_city"), "zip": r.get("outlet_zip_code"), "status": "active permit",
               "naics": r.get("outlet_naics_code"), "date": (r.get("outlet_first_sales_date") or "")[:10],
               "date_kind": "first sales"}


def mixed_bev(s):
    since = (now_utc() - timedelta(days=365)).date().isoformat()  # trailing 12 obligation months
    base = f"{like_clause(['location_name', 'taxpayer_name'])} AND location_county in ({','.join(repr(c) for c in METRO_COUNTY_CODES)})"
    group = "tabc_permit_number,location_name,taxpayer_name,location_address,location_city,location_zip"
    rows = soql(s, "data.texas.gov", "naix-2893", {
        "$select": f"{group},max(obligation_end_date_yyyymmdd) AS last_period,min(obligation_end_date_yyyymmdd) AS first_period,count(*) AS months",
        "$where": base, "$group": group})
    t12 = {r["tabc_permit_number"]: r for r in soql(s, "data.texas.gov", "naix-2893", {
        "$select": "tabc_permit_number,sum(total_receipts) AS receipts,count(*) AS n,min(obligation_end_date_yyyymmdd) AS p0,max(obligation_end_date_yyyymmdd) AS p1",
        "$where": f"{base} AND obligation_end_date_yyyymmdd >= '{since}' AND obligation_end_date_yyyymmdd <= '{now_utc().date()}'",
        "$group": "tabc_permit_number"})}
    for r in rows:
        t = t12.get(r["tabc_permit_number"], {})
        yield {"source": "mixed_bev", "record_id": r.get("tabc_permit_number"), "name": r.get("location_name"),
               "owner": r.get("taxpayer_name"), "address": r.get("location_address"), "city": r.get("location_city"),
               "zip": r.get("location_zip"), "status": f"reported {r.get('first_period', '')[:7]} to {r.get('last_period', '')[:7]}",
               "date": (r.get("last_period") or "")[:10], "date_kind": "last receipts period",
               "receipts_recent": float(t["receipts"]) if t.get("receipts") else None,
               "receipts_window": f"{t['p0'][:7]} to {t['p1'][:7]} ({t['n']} months)" if t else None}


def atx_inspections(s):
    group = "facility_id,restaurant_name,address,zip_code,lat,lng"
    rows = soql(s, "data.austintexas.gov", "ecmv-9xxi", {
        "$select": f"{group},max(inspection_date) AS last_inspection,min(inspection_date) AS first_inspection,count(*) AS n",
        "$where": like_clause(["restaurant_name"]), "$group": group})
    for r in rows:
        addr = r.get("address") or ""
        yield {"source": "atx_inspections", "record_id": r.get("facility_id"), "name": r.get("restaurant_name"),
               "address": addr.split(" Austin ")[0].split(" Travis County")[0].strip(), "city": "AUSTIN",
               "zip": r.get("zip_code"), "status": f"inspected {r.get('first_inspection', '')[:10]} to {r.get('last_inspection', '')[:10]}",
               "date": (r.get("last_inspection") or "")[:10], "date_kind": "last inspection",
               "lat": float(r["lat"]) if r.get("lat") else None, "lon": float(r["lng"]) if r.get("lng") else None}


SOURCES = {"tabc_pending": tabc_pending, "tabc_licenses": tabc_licenses, "sales_tax_permits": sales_tax_permits,
           "mixed_bev": mixed_bev, "atx_inspections": atx_inspections}


# ---------------------------------------------------------------- grouping

ABBREV = {"STREET": "ST", "AVENUE": "AVE", "BOULEVARD": "BLVD", "ROAD": "RD", "DRIVE": "DR", "LANE": "LN",
          "PARKWAY": "PKWY", "HIGHWAY": "HWY", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W", "SUITE": "STE",
          "INTERSTATE": "IH", "I-35": "IH 35", "I35": "IH 35", "FREEWAY": "FWY", "TRAIL": "TRL"}


def address_key(address, zip_code) -> str:
    a = re.sub(r"[^A-Z0-9 ]", " ", str(address or "").upper())
    a = re.split(r"\b(STE|SUITE|UNIT|BLDG|#|APT|SPC)\b", a)[0]
    words = [ABBREV.get(w, w) for w in a.split()]
    num = next((w for w in words if w.isdigit()), "")
    rest = [w for w in words if w != num and w not in {"N", "S", "E", "W"}][:1]
    return f"{num} {' '.join(rest)} {str(zip_code or '')[:5]}".strip()


NAME_NOISE = re.compile(r"^((PF|SV|OOB|THE)\s*-?\s+)|\b(LLC|INC|LTD|CO|CORP|RESTAURANT|CAFE)\b|[^A-Z0-9 ]")


def name_key(name) -> str:
    """First distinctive word of a venue name: groups CHI'LANTRO 1, LLC with Chi'Lantro, splits plaza neighbours."""
    words = NAME_NOISE.sub(" ", str(name or "").upper().replace("'", "")).split()
    return words[0] if words else ""


def activity(g: pd.DataFrame) -> str:
    """Evidence-based status. Never 'closed' from one source: stale evidence only reads 'no recent activity'."""
    today = now_utc().date()
    def last(src):
        d = g.loc[g["source"] == src, "date"].replace("", None).dropna()
        return pd.Timestamp(d.max()).date() if len(d) else None
    mb, insp = last("mixed_bev"), last("atx_inspections")
    if mb and (today - mb).days <= 120:
        return f"operating: receipts through {mb:%Y-%m}"
    if insp and (today - insp).days <= 365:
        return f"operating: inspected {insp}"
    if (g["source"] == "tabc_pending").any():
        return "pipeline: TABC application pending"
    lic = g[g["source"] == "tabc_licenses"]
    if len(lic) and lic["status"].astype(str).str.contains("Active", case=False).any():
        return "licensed, no receipts or inspection on file"
    newest = max([d for d in (mb, insp) if d], default=None)
    return f"no recent activity (last evidence {newest})" if newest else "no activity evidence (permit only)"


def weak_is_noise(r) -> bool:
    """Weak terms count only in a venue name, and only for a food or alcohol business."""
    in_name = WEAK_RX.search(str(r.get("name") or "").upper())
    non_food = r["source"] == "sales_tax_permits" and not r["food_naics"]
    return r["strength"] == "weak" and (not in_name or non_food)


def main() -> int:
    s = session()
    areas, geo = Areas(), Geocoder()
    results, hits = [], []
    for key, fn in SOURCES.items():
        res = {"key": key, "name": f"Korean sweep: {key}", "status": "ok", "row_count": 0, "fields": [], "freshness": {}, "notes": []}
        try:
            rows = list(fn(s))
            res["row_count"] = len(rows)
            hits += rows
        except Exception as exc:  # noqa: BLE001
            res["status"] = classify_error(exc)
            res["notes"].append(redact(f"{type(exc).__name__}: {exc}")[:300])
        print(f"{key}: {res['status']} {res['row_count']} raw hits", flush=True)
        results.append(res)

    df = pd.DataFrame(hits)
    df[["strength", "terms"]] = df.apply(lambda r: pd.Series(match(r.get("name"), r.get("owner"))), axis=1)
    df = df[df["strength"].notna()].copy()
    df["terms"] = df["terms"].map(", ".join)
    df["food_naics"] = df.get("naics", pd.Series(dtype=str)).fillna("").map(lambda n: bool(FOOD_NAICS.match(n)) if n else None)
    df = df[~df.apply(weak_is_noise, axis=1)].copy()
    # Strong terms found only in a non-food sales tax permit (e.g. an association or a staffing firm) are not venues.
    df = df[~((df["source"] == "sales_tax_permits") & (df["food_naics"] == False))].copy()  # noqa: E712
    df["addr_key"] = [f"{address_key(a, z)} | {name_key(n)}" for a, z, n in zip(df["address"], df["zip"], df["name"])]

    OUT.mkdir(parents=True, exist_ok=True)
    df.sort_values(["addr_key", "source"]).to_csv(OUT / "hits.csv", index=False)

    watch = json.loads(WATCH.read_text())
    def tier(names) -> str:
        text = " | ".join(str(n).upper() for n in names)
        if any(x.upper() in text for x in watch.get("exclude", [])):
            return "excluded"
        return "direct_comp" if any(x.upper() in text for x in watch["direct_comp"]) else watch["default_tier"]

    cands = []
    for key, g in df.groupby("addr_key", sort=False):
        pick = g.sort_values("source", key=lambda c: c.map({"atx_inspections": 0, "tabc_licenses": 1, "tabc_pending": 2,
                                                             "mixed_bev": 3, "sales_tax_permits": 4})).iloc[0]
        lat, lon, how = None, None, None
        with_ll = g.dropna(subset=["lat"]) if "lat" in g else g.iloc[0:0]
        if len(with_ll):
            lat, lon, how = with_ll.iloc[0]["lat"], with_ll.iloc[0]["lon"], "inspection lat/lon"
        else:
            pt = geo.locate(pick["address"], pick["zip"]) if str(pick["city"]).upper() == "AUSTIN" else None
            if pt:
                lon, lat, how = pt[0], pt[1], "street centerline"
        a = areas.assign(lon, lat, city=pick["city"], zip_code=pick["zip"])
        mb = g[g["source"] == "mixed_bev"]
        cands.append({
            "tier": tier(list(g["name"].dropna()) + list(g.get("owner", pd.Series()).dropna())), "strength": "strong" if (g["strength"] == "strong").any() else "weak",
            "name": pick["name"], "other_names": "; ".join(sorted(set(g["name"].dropna()) - {pick["name"]}))[:200],
            "owner": "; ".join(sorted(set(g.get("owner", pd.Series()).dropna())))[:120],
            "address": pick["address"], "city": str(pick["city"]).title(), "zip": str(pick["zip"] or "")[:5],
            "terms": ", ".join(sorted(set(", ".join(g["terms"]).split(", ")))),
            "sources": ", ".join(sorted(g["source"].unique())), "n_sources": g["source"].nunique(),
            "statuses": " | ".join(f"{r.source}: {r.status}" for r in g.itertuples()),
            "activity": activity(g),
            "latest_date": g["date"].replace("", None).dropna().max() if g["date"].notna().any() else None,
            "pending_application": (g["source"] == "tabc_pending").any(),
            "receipts_recent": mb["receipts_recent"].sum() if len(mb) and mb["receipts_recent"].notna().any() else None,
            "receipts_window": mb["receipts_window"].dropna().iloc[0] if len(mb) and mb["receipts_window"].notna().any() else None,
            "food_naics": None if g["food_naics"].isna().all() else bool(g["food_naics"].fillna(False).any()),
            "hub": a["hub"], "subsection": a["subsection"], "cluster": a["cluster"], "area_method": a["method"],
            "located_by": how, "distance_mi": a["distance_mi"], "home_2mi": a["home_2mi"], "lat": lat, "lon": lon,
            "addr_key": key})
    out = pd.DataFrame(cands)
    out["_t"] = out["tier"].map({"direct_comp": 0}).fillna(1)
    out = out.sort_values(["_t", "strength", "n_sources", "name"], ascending=[True, True, False, True]).drop(columns="_t")
    out.to_csv(OUT / "candidates.csv", index=False)
    results.append({"key": "korean_sweep", "name": "Korean sweep candidates", "status": "ok", "row_count": len(out),
                    "fields": list(out.columns), "freshness": {"run_at": now_utc().isoformat(timespec="seconds")},
                    "notes": [f"{(out.strength == 'strong').sum()} strong, {(out.strength == 'weak').sum()} weak; all unconfirmed"]})
    write_run_health(OUT / "run_health.json", "korean_sweep", results)
    print(f"{len(out)} candidates ({(out.strength == 'strong').sum()} strong) -> {OUT / 'candidates.csv'}")
    return 0 if all(r["status"] == "ok" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
