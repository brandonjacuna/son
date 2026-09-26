"""R3 digest-build: compute the weekly digest from the store and write it as Markdown.

Usage: python scripts/build_digest.py [--delivery YYYY-MM-DD] [--draft]

Reads data/store (R1 and R2 output), config (areas, taxonomy, peers, Korean watch, events).
Writes data/digests/<delivery>.md and data/digests/<delivery>.facts.json. Sections 1 and 9
(the ranked changes and "So what for Son") are written from the facts file by the R3 routine;
this script fills them with rule-based text so a run without the routine still reads.

Rules (BRIEF section 9): a receipts month counts only when at least 90% of last year's
reporters for that month have filed; cells under 8 venues roll up; every number carries its
period; openings and closings are never inferred from one source alone (single-source items
are labelled as signals, not as openings or closings).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from areas import Areas  # noqa: E402
from common import CONFIG_DIR, DATA_DIR, now_utc  # noqa: E402
from geocode import Geocoder  # noqa: E402
from venue_evidence import name_word, street_parts  # noqa: E402

STORE, OUT = DATA_DIR / "store", DATA_DIR / "digests"
VENUES = STORE / "venues.csv"
MIN_CELL = 8
# TABC on-premise retail types (mixed beverage, wine and beer on-premise, beer on-premise, private clubs,
# food and beverage certificate, brewpub). Excludes package stores, convenience stores, and temporary event permits.
ON_PREMISE = {"MB", "BG", "BE", "N", "NB", "NE", "FB", "BP"}
TRAVIS, WILLIAMSON, HAYS = "227", "246", "105"
NAICS_FORMAT = {}
TAX = json.loads((CONFIG_DIR / "taxonomy.json").read_text())
for f in TAX["formats"]:
    for n in f["naics"]:
        NAICS_FORMAT[n] = f["id"]
FORMAT_LABEL = {f["id"]: f["label"] for f in TAX["formats"]}
OVERRIDE = {name.upper(): fmt for fmt, names in TAX["overrides"].items() if not fmt.startswith("_") for name in names}


def money(x: float) -> str:
    return f"${x / 1e6:,.1f}M" if abs(x) >= 1e6 else f"${x:,.0f}"


def pct(x) -> str:
    return "n/a" if x is None or pd.isna(x) else f"{x:+.1f}%"


def fmt_released(m: dict) -> str:
    r = m.get("released")
    if not r:
        return f"not published by the API; first stored {m['vintage']}"
    try:
        return pd.Timestamp(r).strftime("%Y-%m-%d")
    except ValueError:
        return str(r)[:10]


def fmt_value(m: dict) -> str:
    if m["series"].startswith("alloc:"):
        return money(m["value"])
    if "GASREGW" in m["series"]:
        return f"${m['value']:.2f}"
    return f"{m['value']:,.1f}"


def month_name(p: str) -> str:
    return pd.Timestamp(p + "-01").strftime("%b %Y")


# ---------------------------------------------------------------- readable formatting

SMALL = {"y", "de", "del", "la", "las", "los", "el", "of", "and", "the", "at", "on", "in", "a", "an", "for"}
KEEP_UPPER = {"LLC", "ATX", "BBQ", "IHOP", "MOD", "II", "III", "IV", "USA", "TX", "UT", "ACL", "DJS", "MRC", "HQ", "KBBQ", "N", "S", "E", "W"}
SHORT = {
    "bls:SMU48124207000000001": "Austin hospitality jobs", "bls:SMU48124200000000001": "Austin total jobs",
    "bls:LAUMT481242000000003": "Austin unemployment", "alloc:austin": "Austin sales tax",
    "tssos:rev": "Texas service sector revenue", "tssos:bact": "Texas service sector activity",
    "tssos:sell": "Texas service selling prices", "tssos:wgs": "Texas service wages",
    "bls:CUUR0300SEFV": "Restaurant prices (CPI, South)", "bls:CUUR0000SEFV": "Restaurant prices (CPI, US)",
    "fred:UMCSENT": "Consumer sentiment", "fred:GASREGW": "Gas, US regular",
}
MACRO_GROUPS = [
    ("Jobs", ["bls:SMU48124207000000001", "bls:SMU48124200000000001", "bls:LAUMT481242000000003"]),
    ("Spending", ["alloc:austin", "tssos:rev", "tssos:bact"]),
    ("Prices and costs", ["bls:CUUR0300SEFV", "bls:CUUR0000SEFV", "tssos:sell", "tssos:wgs", "fred:GASREGW"]),
    ("Sentiment", ["fred:UMCSENT"]),
]
HEALTH_NAME = {"warn": "WARN layoff notices", "aus_passengers": "Airport passengers", "mixed_bev": "Alcohol sales",
               "tabc_pending": "TABC applications", "tabc_licenses": "TABC licenses", "sales_tax_permits": "Sales tax permits",
               "atx_inspections": "Austin inspections", "atx_permits": "Austin building permits"}
LICENSE = {"MB": "full bar", "BG": "beer and wine", "BE": "beer", "N": "private club", "NB": "private club",
           "NE": "private club", "FB": "food and beverage certificate", "BP": "brewpub"}


def nice_name(s) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    s = re.sub(r",?\s+(LLC|INC|L\.L\.C\.|LTD|CORP)\.?$", "", s, flags=re.I)
    if s.upper() != s:
        return s
    words = []
    for wd in s.split(" "):
        core = re.sub(r"[^A-Z0-9]", "", wd)
        if words and core.lower() in SMALL:
            words.append(wd.lower())
        else:
            words.append(wd if core in KEEP_UPPER or any(ch.isdigit() for ch in wd) and len(core) <= 3 else wd.capitalize())
    return " ".join(words).replace("'S ", "'s ").replace("'S", "'s") if s else s


def nice_addr(s) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip().rstrip(".")
    s = re.split(r"\s+(?:Austin|Bee Cave|Sunset Valley|Round Rock|Cedar Park),? TX", s, flags=re.I)[0]
    return nice_name(s) if s.upper() == s else s


def pct_s(x) -> str:
    if x is None or pd.isna(x):
        return "n/a"
    return f"{x:+.0f}%" if abs(x) >= 10 else f"{x:+.1f}%"


def pct_s_str(change: str | None) -> str:
    return (change or "n/a").replace(" YoY", " vs last year")


def money_s(x) -> str:
    x = float(x)
    if abs(x) >= 1e6:
        return f"${x / 1e6:,.1f}M"
    if abs(x) >= 1e4:
        return f"${x / 1e3:,.0f}K"
    return f"${x:,.0f}"


def pretty_date(d) -> str:
    ts = pd.Timestamp(str(d)[:10])
    return f"{ts:%b} {ts.day}"


def reading(m: dict) -> str:
    sid, v = m["series"], m["value"]
    val = {"alloc": money_s(v)}.get(sid.split(":")[0])
    if val is None:
        if "GASREGW" in sid:
            val = f"${v:.2f}"
        elif sid.endswith("003"):
            val = f"{v:.1f}%"
        elif sid.startswith("bls:SMU"):
            val = f"{v * 1000:,.0f} jobs"
        elif sid.startswith("bls:CUUR"):
            return pct_s_str(m["change"]) if m["change"] else f"index {v:.1f}"
        elif sid.startswith("tssos:"):
            val = f"index {v:.1f}"
        else:
            val = f"{v:,.1f}"
    return f"{val}, {pct_s_str(m['change'])}" if m["change"] else val


def flag(r) -> str:
    return " †" if pd.notna(r.yoy) and abs(r.yoy) >= 50 else ""


def short_area(r) -> str:
    if r.subsection:
        return r.subsection
    return r.hub or (r.cluster or "")


def what(r) -> str:
    s = _what(r)
    return s[:1].upper() + s[1:]


def _what(r) -> str:
    lt = re.search(r"license type (\w+)", str(r.detail))
    lic = LICENSE.get(lt.group(1), lt.group(1)) if lt else ""
    if r.source == "New sales tax outlet":
        fmt = re.sub(r"\s*\(NAICS \d+\)", "", str(r.detail)).lower()
        return f"registered to sell ({fmt})"
    if r.source == "TABC license issued":
        return f"liquor license issued ({lic})"
    if r.source == "TABC pending application":
        return f"applied for a liquor license ({lic})"
    if r.source == "TABC status change":
        status = re.search(r"status now ([^,;]+)", str(r.detail))
        base = f"{lic} license {status.group(1).lower() if status else 'changed'}"
        return base + (", replaced by a new license" if getattr(r, "kind", "") == "license_change" else "")
    if r.source == "Austin building permit":
        return "food-use building permit"
    if r.source == "First Austin inspection":
        return "first health inspection"
    return r.source.lower()


def peer_change(note: str) -> str:
    for part in re.split(r"(?<=\.)\s+", note):
        if re.search(r"RELOCATED|Relocated|lease|check for a new permit|moved", part):
            s = part.replace("RELOCATED: ", "").replace("RELOCATED ", "Moved ").replace("Open per 2026 coverage, but s", "Open per 2026 coverage, but s").strip()
            s = s[:1].upper() + s[1:]
            return s if s.endswith(".") else s + "."
    return note


# ---------------------------------------------------------------- venues and receipts

def build_venues(mb: pd.DataFrame, areas: Areas, geo: Geocoder) -> pd.DataFrame:
    """One row per receipts-filing location with format and area; geocodes are cached."""
    v = mb.sort_values("period").drop_duplicates(["tabc_permit_number", "location_number"], keep="last")
    v = v[["tabc_permit_number", "location_number", "taxpayer_number", "location_name", "location_address",
           "location_city", "location_zip", "location_county"]].copy()
    v["venue_id"] = v["tabc_permit_number"] + "|" + v["location_number"]
    cache = pd.read_csv(VENUES, dtype=str).set_index("venue_id") if VENUES.exists() else pd.DataFrame()
    permits = pd.read_csv(STORE / "current" / "sales_tax_permits.csv", dtype=str)
    naics = permits.set_index(["taxpayer_number", "outlet_number"])["outlet_naics_code"].to_dict()
    rows = []
    for r in v.itertuples():
        if r.venue_id in cache.index and cache.loc[r.venue_id, "location_address"] == r.location_address:
            rows.append(cache.loc[r.venue_id].to_dict() | {"venue_id": r.venue_id})
            continue
        pt = geo.locate(r.location_address) if str(r.location_city).upper() == "AUSTIN" else None
        a = areas.assign(*(pt or (None, None)), city=r.location_city, zip_code=str(r.location_zip)[:5])
        code = naics.get((r.taxpayer_number, r.location_number), "")
        fmt = OVERRIDE.get(str(r.location_name).upper()) or NAICS_FORMAT.get(code, "unclassified")
        rows.append({**r._asdict(), "naics": code, "format": fmt, "lon": pt[0] if pt else None, "lat": pt[1] if pt else None,
                     **{k: a[k] for k in ("area_id", "hub", "subsection", "cluster", "distance_mi")}})
    out = pd.DataFrame(rows).drop(columns=["Index"], errors="ignore")
    # Venues that could not be placed take the most common area among placed venues in the same ZIP.
    out["zip5"] = out["location_zip"].astype(str).str[:5]
    placed = out[out["hub"].notna() | out["cluster"].notna()]
    key = placed.apply(lambda r: f"{r['hub']}|{r['subsection']}|{r['cluster']}|{r['area_id']}", axis=1)
    majority = key.groupby(placed["zip5"]).agg(lambda s: s.value_counts().index[0]).to_dict()
    for i in out.index[out["hub"].isna() & out["cluster"].isna()]:
        k = majority.get(out.at[i, "zip5"])
        if k:
            hub, sub, cl, aid = (None if v in ("nan", "None") else v for v in k.split("|"))
            out.loc[i, ["hub", "subsection", "cluster", "area_id", "area_method"]] = [hub, sub, cl, aid, "zip_majority"]
    out.to_csv(VENUES, index=False)
    return out


def area_label(r) -> str:
    if isinstance(r.get("hub"), str) and r["hub"]:
        return r["hub"] if r["hub"] != "East Austin" else f"East Austin: {r['subsection']}"
    return f"Off-hub: {r['cluster']}" if isinstance(r.get("cluster"), str) and r["cluster"] else "Unassigned"


def complete_months(mb: pd.DataFrame) -> tuple[list[str], dict]:
    counts = mb.groupby("period")["tabc_permit_number"].nunique()
    status = {}
    for p, n in counts.items():
        prior = (pd.Timestamp(p + "-01") - pd.DateOffset(years=1)).strftime("%Y-%m")
        base = counts.get(prior)
        status[p] = {"reporters": int(n), "prior_year": int(base) if base else None,
                     "share": round(n / base, 3) if base else None}
    done = [p for p, s in status.items() if s["share"] is not None and s["share"] >= 0.9]
    return sorted(done), status


def window(latest: str, n: int = 3) -> tuple[list[str], list[str]]:
    end = pd.Timestamp(latest + "-01")
    cur = [(end - pd.DateOffset(months=i)).strftime("%Y-%m") for i in range(n - 1, -1, -1)]
    prev = [(pd.Timestamp(p + "-01") - pd.DateOffset(years=1)).strftime("%Y-%m") for p in cur]
    return cur, prev


def cell_stats(mb: pd.DataFrame, venues: pd.DataFrame, by: str, cur: list[str], prev: list[str], scope_counties) -> pd.DataFrame:
    x = mb[mb["location_county"].isin(scope_counties)].copy()
    x["total"] = pd.to_numeric(x["total_receipts"], errors="coerce").fillna(0)
    x["venue_id"] = x["tabc_permit_number"] + "|" + x["location_number"]
    a = x[x["period"].isin(cur)].groupby("venue_id")["total"].sum()
    b = x[x["period"].isin(prev)].groupby("venue_id")["total"].sum()
    per = pd.DataFrame({"cur": a, "prev": b}).fillna(0).join(venues.set_index("venue_id")[[by]], how="left")
    per[by] = per[by].fillna("Unassigned")
    same = per[(per.cur > 0) & (per.prev > 0)]
    g = per.groupby(by).agg(cur=("cur", "sum"), prev=("prev", "sum"), venues=("cur", lambda s: int((s > 0).sum())))
    g["same_venues"] = same.groupby(by).size()
    g["breadth"] = (same.assign(up=same.cur > same.prev).groupby(by)["up"].mean() * 100).round(0)
    g["same_yoy"] = ((same.groupby(by)["cur"].sum() / same.groupby(by)["prev"].sum() - 1) * 100).round(1)
    g["yoy"] = ((g.cur / g.prev - 1) * 100).round(1)
    g = g.fillna({"same_venues": 0})
    small = g[g.same_venues < MIN_CELL]
    if len(small):
        rolled = pd.DataFrame([{"cur": small.cur.sum(), "prev": small.prev.sum(), "venues": small.venues.sum(),
                                "same_venues": small.same_venues.sum(), "breadth": None, "same_yoy": None,
                                "yoy": round((small.cur.sum() / small.prev.sum() - 1) * 100, 1) if small.prev.sum() else None}],
                              index=[f"Rolled up ({len(small)} cells under {MIN_CELL} venues)"])
        g = pd.concat([g[g.same_venues >= MIN_CELL], rolled])
    return g.sort_values("cur", ascending=False)


# ---------------------------------------------------------------- weekly events from R1 state

def weekly_items(start: date, end: date, areas: Areas, geo: Geocoder) -> pd.DataFrame:
    cur = STORE / "current"
    items = []

    def add(src, kind, name, address, city, zip_code, when, detail, lat=None, lon=None):
        items.append(dict(source=src, kind=kind, name=name, address=address, city=city, zip=str(zip_code or "")[:5],
                          date=when, detail=detail, lat=lat, lon=lon))

    def inwin(s):
        d = pd.to_datetime(s, errors="coerce").dt.date
        return (d >= start) & (d <= end)

    p = pd.read_csv(cur / "tabc_pending.csv", dtype=str)
    p = p[p["license_type"].isin(ON_PREMISE)]
    for r in p[inwin(p["submission_date"])].itertuples():
        add("TABC pending application", "pipeline", r.trade_name if isinstance(r.trade_name, str) else r.owner,
            r.address, r.city, r.zip, r.submission_date[:10], f"license type {r.license_type}, status {r.applicationstatus}")
    lic = pd.read_csv(cur / "tabc_licenses.csv", dtype=str)
    lic = lic[lic["license_type"].isin(ON_PREMISE)]
    for r in lic[inwin(lic["original_issue_date"])].itertuples():
        add("TABC license issued", "opening_signal", r.trade_name if isinstance(r.trade_name, str) else r.owner,
            r.address, r.city, r.zip, r.original_issue_date[:10], f"license type {r.license_type}")
    gone = lic[inwin(lic["status_change_date"]) & ~lic["primary_status"].fillna("").str.contains("Active")]
    for r in gone.itertuples():
        add("TABC status change", "closing_signal", r.trade_name if isinstance(r.trade_name, str) else r.owner,
            r.address, r.city, r.zip, r.status_change_date[:10], f"status now {r.primary_status}, license type {r.license_type}")
    st = pd.read_csv(cur / "sales_tax_permits.csv", dtype=str)
    for r in st[inwin(st["outlet_permit_issue_date"])].itertuples():
        fmt = FORMAT_LABEL.get(NAICS_FORMAT.get(r.outlet_naics_code, ""), "Unclassified")
        add("New sales tax outlet", "opening_signal", r.outlet_name, r.outlet_address, r.outlet_city, r.outlet_zip_code,
            r.outlet_permit_issue_date[:10], f"{fmt} (NAICS {r.outlet_naics_code})")
    ins = pd.read_csv(cur / "atx_inspections.csv", dtype=str)
    first = ins.assign(d=pd.to_datetime(ins["inspection_date"], errors="coerce")).sort_values("d").drop_duplicates("facility_id")
    for r in first[inwin(first["inspection_date"])].itertuples():
        add("First Austin inspection", "opening_signal", r.restaurant_name, str(r.address).split(" Austin")[0], "AUSTIN",
            r.zip_code, r.inspection_date[:10], f"{r.process_description}, score {r.score}", r.lat, r.lng)
    bp = pd.read_csv(cur / "atx_permits.csv", dtype=str)
    for r in bp[inwin(bp["issue_date"])].itertuples():
        add("Austin building permit", "pipeline", str(r.description)[:110], r.original_address1, r.original_city or "AUSTIN",
            r.original_zip, r.issue_date[:10], f"{r.work_class}, {r.status_current}", r.latitude, r.longitude)
    df = pd.DataFrame(items)
    if df.empty:
        return df
    placed = []
    for r in df.itertuples():
        lat, lon = pd.to_numeric(r.lat, errors="coerce"), pd.to_numeric(r.lon, errors="coerce")
        if (pd.isna(lat) or pd.isna(lon)) and str(r.city or "").upper() == "AUSTIN":
            pt = geo.locate(r.address)
            lon, lat = pt if pt else (None, None)
        a = areas.assign(None if pd.isna(lon) else float(lon), None if pd.isna(lat) else float(lat), city=r.city, zip_code=r.zip)
        placed.append(a)
    df = pd.concat([df.drop(columns=["lat", "lon"]), pd.DataFrame(placed)], axis=1)
    df["area"] = df.apply(area_label, axis=1)
    df["address"] = df["address"].astype(str).str.rstrip(". ")
    # A surrendered license next to a new one at the same address is a license change, not a closing.
    akey = df["address"].str.upper().str.extract(r"^(\d+ \S+)")[0]
    opened = set(akey[df["kind"] == "opening_signal"].dropna())
    swap = (df["kind"] == "closing_signal") & akey.isin(opened)
    df.loc[swap, "kind"] = "license_change"
    df.loc[swap, "detail"] = df.loc[swap, "detail"] + "; a new license was issued at the same address this week, so this reads as a license change"
    return df


# ---------------------------------------------------------------- macro

def macro_panel(delivery: date) -> list[dict]:
    s = pd.read_csv(STORE / "series.csv", dtype=str)
    s = s.sort_values("vintage").drop_duplicates(["series_id", "period"], keep="last")
    s["value"] = pd.to_numeric(s["value"], errors="coerce")
    meta = json.loads((STORE / "series_meta.json").read_text())
    wanted = ["bls:SMU48124200000000001", "bls:SMU48124207000000001", "bls:LAUMT481242000000003", "alloc:austin",
              "tssos:rev", "tssos:bact", "tssos:sell", "tssos:wgs", "bls:CUUR0300SEFV", "bls:CUUR0000SEFV",
              "fred:GASREGW", "fred:UMCSENT"]
    out = []
    for sid in wanted:
        x = s[s.series_id == sid].sort_values("period")
        if x.empty:
            continue
        last = x.iloc[-1]
        p = pd.Timestamp(last.period)
        target = p - pd.DateOffset(years=1)
        near = x[(pd.to_datetime(x.period) <= target) & (pd.to_datetime(x.period) > target - pd.DateOffset(days=7))]
        prior = near.tail(1)
        diffusion = sid.startswith("tssos:") or sid.endswith("003") or "UMCSENT" in sid
        if prior.empty:
            chg = None
        elif diffusion:
            chg = f"{last.value - prior.iloc[0].value:+.1f} pts YoY"
        else:
            chg = f"{(last.value / prior.iloc[0].value - 1) * 100:+.1f}% YoY"
        freq = meta.get(sid, {}).get("frequency", "")
        period = p.strftime("%b %d, %Y") if "Week" in freq else p.strftime("%b %Y")
        age = max(0, (pd.Timestamp(delivery) - (p + (pd.DateOffset(days=7) if "Week" in freq else pd.offsets.MonthEnd(0)))).days)
        out.append({"series": sid, "label": meta.get(sid, {}).get("label", sid), "period": period,
                    "value": last.value, "change": chg, "source": meta.get(sid, {}).get("source", ""),
                    "released": meta.get(sid, {}).get("released"), "vintage": last.vintage, "days_old": age})
    return out


# ---------------------------------------------------------------- peers and Korean

def peer_receipts(mb: pd.DataFrame, peers: pd.DataFrame, cur: list[str], prev: list[str]) -> pd.DataFrame:
    x = mb.copy()
    x["total"] = pd.to_numeric(x["total_receipts"], errors="coerce").fillna(0)
    addr = x["location_address"].str.upper()
    rows = []
    for r in peers.itertuples():
        parts = street_parts(r.address)
        if not parts:
            rows.append({"name": r.name, "cur": None, "prev": None})
            continue
        num, word = parts
        nw = name_word(r.name)
        m = x[addr.str.startswith(num + " ") & addr.str.contains(word, regex=False)
              & (x["location_name"].str.upper().str.contains(nw, regex=False) | x["taxpayer_number"].isna())]
        c, pv = m[m.period.isin(cur)].total.sum(), m[m.period.isin(prev)].total.sum()
        rows.append({"name": r.name, "cur": c if len(m) else None, "prev": pv if len(m) else None,
                     "last_period": m.period.max() if len(m) else None})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- render

def render(delivery: date, draft: bool) -> tuple[str, dict]:
    start, end = delivery - timedelta(days=7), delivery - timedelta(days=1)
    data_end = min(end, now_utc().date())
    areas, geo = Areas(), Geocoder()
    mb = pd.read_csv(STORE / "mixed_bev.csv", dtype=str)
    venues = build_venues(mb, areas, geo)
    venues["area"] = venues.apply(area_label, axis=1)
    venues["format_label"] = venues["format"].map(FORMAT_LABEL).fillna("Unclassified")
    done, rstatus = complete_months(mb)
    latest = done[-1]
    cur, prev = window(latest)
    scope = [TRAVIS, WILLIAMSON, HAYS]
    metro = cell_stats(mb, venues.assign(all="Metro"), "all", cur, prev, scope).iloc[0]
    by_area = cell_stats(mb, venues, "area", cur, prev, scope)
    by_fmt = cell_stats(mb, venues, "format_label", cur, prev, scope)
    wk = weekly_items(start, data_end, areas, geo)
    home = wk[wk["home_2mi"]] if len(wk) else wk
    peers = pd.read_csv(CONFIG_DIR / "peers_draft.csv", dtype=str, keep_default_na=False)
    pr = peer_receipts(mb, peers, cur, prev)
    korean = pd.read_csv(DATA_DIR / "korean_sweep" / "candidates.csv", dtype=str, keep_default_na=False)
    macro = macro_panel(delivery)
    events = pd.read_csv(CONFIG_DIR / "events.csv", dtype=str)
    ev_win = events[(events.start_date <= f"{cur[-1]}-31") & (events.end_date >= f"{cur[0]}-01")]
    ev_prev = events[(events.start_date <= f"{prev[-1]}-31") & (events.end_date >= f"{prev[0]}-01")]
    ev_next = events[(events.start_date >= delivery.isoformat())
                     & (events.start_date <= (delivery + timedelta(days=45)).isoformat())]
    health = {}
    for f in ["data/store/run_health.json", "data/store/releases_health.json"]:
        p = DATA_DIR.parent / f
        if p.exists():
            health[f] = json.loads(p.read_text())
    lateness = rstatus.get(cur[-1], {})
    unfinished = [p for p in sorted(rstatus)[-3:] if p not in done]

    wlabel = f"Week of {start:%b} {start.day} to {delivery:%b} {delivery.day}"
    title = f"{'DRAFT ' if draft else ''}{delivery.isoformat()} | {wlabel}"
    rng = f"{month_name(cur[0])[:3]} to {month_name(cur[-1])}"  # e.g. "Jun to Aug 2026"
    mm = {m["series"]: m for m in macro}
    pm = peers.merge(pr, on="name", how="left")
    comp = next((r for r in pm.itertuples() if r.inclusion == "direct_comp"), None)
    comp_yoy = ((comp.cur / comp.prev - 1) * 100) if comp is not None and pd.notna(comp.cur) and comp.prev else None
    hub_rows = by_area[~by_area.index.str.startswith(("Off-hub", "Rolled", "Unassigned"))]
    off_rows = by_area[by_area.index.str.startswith("Off-hub")]
    hub_yoy = (hub_rows.cur.sum() / hub_rows.prev.sum() - 1) * 100 if len(hub_rows) else None
    off_yoy = (off_rows.cur.sum() / off_rows.prev.sum() - 1) * 100 if len(off_rows) else None
    others = wk[wk["hub"].isna() & ~wk["home_2mi"]] if len(wk) else wk
    in_hubs = wk[wk["hub"].notna() & ~wk["home_2mi"]] if len(wk) else wk

    W = []
    w = W.append

    def rule():
        w("")
        w("---")
        w("")

    # Header and bottom line
    w(f"# {title}")
    w("")
    w(f"*Austin metro weekly industry digest for Sŏn. Travis, Williamson, and Hays counties, with 207 E St. Elmo Rd as home base. "
      f"Records through {data_end:%b} {data_end.day}, {data_end.year}.*")
    if draft:
        w("")
        w("> **Draft for founder review.** Daily change tracking started Sep 26, so this week's openings and closings are read "
          "from the dates on each record.")
    bl = OUT / f"{delivery.isoformat()}.bottomline.md"
    w("")
    if bl.exists():
        w(f"> **Bottom line.** {bl.read_text().strip()}")
    else:
        line = (f"Alcohol sales across the metro are {pct_s(metro.yoy)} vs last year ({rng}), but venues open both years are "
                f"{pct_s(metro.same_yoy)}, so growth is coming from new openings.")
        if comp_yoy is not None:
            line += f" Oseyo, the direct comp, is {pct_s(comp_yoy)}."
        w(f"> **Bottom line.** {line}")

    # 1. What changed
    rule()
    w("## 1. What changed this week")
    w("")
    items = []
    if comp_yoy is not None and abs(comp_yoy) >= 25:
        items.append((1, "Alert", f"Oseyo alcohol sales {pct_s(comp_yoy)} vs last year",
                      f"{money_s(comp.cur)} for {rng}, against {money_s(comp.prev)} a year earlier."))
    if len(home):
        names = ", ".join(f"{nice_name(r.name)} ({r.distance_mi:.1f} mi)" for r in home.sort_values("distance_mi").itertuples())
        tier = "Act" if home["home_1mi"].any() else "Alert"
        items.append((0 if tier == "Act" else 1, tier, f"{len(home)} new {'record' if len(home) == 1 else 'records'} within 2 miles of the site", names + "."))
    items.append((2, "Watch", f"Existing venues are flat ({pct_s(metro.same_yoy)})",
                  f"Metro alcohol sales are {pct_s(metro.yoy)} for {rng}, but only {metro.breadth:.0f}% of venues open both years grew."))
    if "alloc:austin" in mm:
        a = mm["alloc:austin"]
        items.append((2, "Watch", f"Austin sales tax {pct_s_str(a['change'])}", f"{money_s(a['value'])} paid in {a['period']} (Comptroller)."))
    if "tssos:wgs" in mm and "tssos:sell" in mm:
        items.append((2, "Watch", "Wages rising faster than prices",
                      f"Texas service firms: wages index {mm['tssos:wgs']['value']:.1f}, selling prices {mm['tssos:sell']['value']:.1f} ({mm['tssos:wgs']['period']}, Dallas Fed)."))
    for i, (_, tier, head, body) in enumerate(sorted(items, key=lambda x: x[0])[:5], 1):
        w(f"{i}. **{tier}: {head}.** {body}")

    # 2. New this week
    rule()
    w("## 2. New this week")
    w("")
    w("| Release | Period | Reading |")
    w("|---|---|---|")
    for sid in ["bls:SMU48124207000000001", "bls:SMU48124200000000001", "bls:LAUMT481242000000003", "alloc:austin",
                "tssos:rev", "bls:CUUR0300SEFV", "fred:UMCSENT", "fred:GASREGW"]:
        if sid in mm:
            m = mm[sid]
            w(f"| {SHORT[sid]} | {m['period']} | {reading(m)} |")
    w(f"| Alcohol sales, venue level | {month_name(cur[-1])} | {lateness.get('share', 0) * 100:.0f}% of venues have filed |")

    # 3. Openings, closings, pipeline
    rule()
    w("## 3. Openings, closings, pipeline")
    w("")
    if len(wk):
        c = wk.groupby("source").size()
        parts = [f"{c.get(k, 0)} {label}" for k, label in [
            ("New sales tax outlet", "new food businesses registered"), ("TABC license issued", "liquor licenses issued"),
            ("TABC pending application", "liquor license applications"), ("TABC status change", "licenses surrendered or expired"),
            ("Austin building permit", "food-use building permits"), ("First Austin inspection", "first health inspections")] if c.get(k, 0)]
        w("This week: " + ", ".join(parts) + ". Each is a single-source signal until a second source confirms it.")
        w("")
        w("### Within 2 miles of the site")
        w("")
        if len(home):
            for r in home.sort_values("distance_mi").itertuples():
                w(f"- **{nice_name(r.name)}**, {nice_addr(r.address)} ({r.distance_mi:.1f} mi). {what(r)}, {pretty_date(r.date)}.")
        else:
            w("- Nothing new within 2 miles.")
        w("")
        w("### In the hubs")
        w("")
        if len(in_hubs):
            w("| Hub | Business | What happened |")
            w("|---|---|---|")
            for r in in_hubs.sort_values(["area", "date"]).itertuples():
                w(f"| {r.area} | {nice_name(r.name)[:60]} | {what(r)}, {pretty_date(r.date)} |")
        else:
            w("- Nothing new in the hubs.")
        if len(others):
            busiest = others.groupby("area").size().sort_values(ascending=False)
            w("")
            w("### Rest of the metro")
            w("")
            w(f"{len(others)} more records across {len(busiest)} areas. Busiest: "
              + ", ".join(f"{a.replace('Off-hub: ', '')} ({n})" for a, n in busiest.head(4).items()) + ". Full list in the appendix.")
    else:
        w("No records dated this week in any daily source.")

    # 4. Area heatmap
    rule()
    w(f"## 4. Area heatmap")
    w("")
    w(f"Alcohol sales, {rng}, compared with the same months last year. *Same venues* counts only places open in both years. "
      f"*Growing* is the share of those venues whose sales rose.")
    w("")
    w("| Hub | Alcohol sales | vs last year | Same venues | Growing | Venues |")
    w("|---|---|---|---|---|---|")
    for name, r in hub_rows.sort_values("cur", ascending=False).iterrows():
        w(f"| {name} | {money_s(r.cur)} | {pct_s(r.yoy)}{flag(r)} | {pct_s(r.same_yoy)} | {r.breadth:.0f}% | {int(r.venues)} |")
    w(f"| **Metro** | **{money_s(metro.cur)}** | **{pct_s(metro.yoy)}** | **{pct_s(metro.same_yoy)}** | **{metro.breadth:.0f}%** | **{int(metro.venues):,}** |")
    w("")
    if hub_yoy is not None and off_yoy is not None:
        w(f"Hubs combined **{pct_s(hub_yoy)}**, off-hub areas combined **{pct_s(off_yoy)}**.")
        w("")
    ranked_off = off_rows[off_rows.same_venues >= MIN_CELL].copy()
    ranked_off.index = ranked_off.index.str.replace("Off-hub: ", "", regex=False)
    up, down = ranked_off.sort_values("same_yoy", ascending=False).head(4), ranked_off.sort_values("same_yoy").head(4)
    w("**Off-hub, strongest (same venues):** " + "; ".join(f"{n} {pct_s(r.same_yoy)}{' †' if abs(r.same_yoy) >= 50 else ''}" for n, r in up.iterrows()) + ".")
    w("")
    w("**Off-hub, weakest (same venues):** " + "; ".join(f"{n} {pct_s(r.same_yoy)}" for n, r in down.iterrows()) + ".")
    if any(flag(r) for _, r in hub_rows.iterrows()) or (up.same_yoy.abs() >= 50).any():
        w("")
        w("*† Swing of 50% or more, usually a handful of venues opening, reopening, or changing how they file. Check the venues before acting on it.*")

    # 5. Concept types
    rule()
    w("## 5. Concept-type scorecard")
    w("")
    w(f"Alcohol sales by format, {rng}.")
    w("")
    w("| Format | Alcohol sales | vs last year | Same venues | Growing | Venues |")
    w("|---|---|---|---|---|---|")
    order = by_fmt.index.str.startswith(("Unclassified", "Rolled"))
    for name, r in pd.concat([by_fmt[~order], by_fmt[order]]).iterrows():
        br = "" if pd.isna(r.breadth) else f"{r.breadth:.0f}%"
        w(f"| {name} | {money_s(r.cur)} | {pct_s(r.yoy)} | {pct_s(r.same_yoy)} | {br} | {int(r.venues):,} |")
    w("")
    w("*Fine dining and upscale casual need a manual list (public data does not show price point), so they are not split out yet.*")

    # 6. Macro
    rule()
    w("## 6. Macro panel")
    for group, sids in MACRO_GROUPS:
        rows = [mm[s] for s in sids if s in mm]
        if not rows:
            continue
        w("")
        w(f"**{group}**")
        for m in rows:
            w(f"- {SHORT[m['series']]}: {reading(m)} ({m['period']}){' · ' + str(m['days_old']) + ' days old' if m['days_old'] > 45 else ''}")
    w("")
    w("**Not available this week:** airport passengers and WARN layoff notices (both sources stale, see Data health).")

    # 7. Peers
    rule()
    w("## 7. Peer watchlist")
    w("")
    if comp is not None:
        w("### Direct comp: Oseyo")
        w("")
        k = korean[korean["tier"] == "direct_comp"]
        w(f"Alcohol sales **{money_s(comp.cur)}** for {rng}, **{pct_s(comp_yoy)}** vs last year"
          + (f"; {money_s(float(k.iloc[0].receipts_recent))} over the last 12 months." if len(k) and k.iloc[0].receipts_recent else "."))
        w("")
    have = pm[pm["cur"].fillna(0) > 0]
    have = have[(have["inclusion"] != "direct_comp") & (have["name"] != "Hestia Bar")].copy()
    have["yoy"] = (have["cur"] / have["prev"] - 1) * 100
    w(f"### Peers with alcohol sales on file ({rng})")
    w("")
    w("| Peer | Area | Alcohol sales | vs last year |")
    w("|---|---|---|---|")
    for r in have.sort_values("yoy", ascending=False, na_position="first").itertuples():
        yoy = "new this year" if not r.prev else pct_s(r.yoy)
        tag = " (Emmer & Rye group)" if r.inclusion == "emmer_and_rye_group" or r.name in ("Hestia", "Kalimotxo") else ""
        w(f"| {r.name}{tag} | {short_area(r)} | {money_s(r.cur)} | {yoy} |")
    w("")
    w("*Hestia Bar files under Hestia.*")
    w("")
    none = pm[(pm["cur"].fillna(0) == 0) & (pm["name"] != "Hestia Bar")]
    w("**No alcohol sales on file** (trucks, BYOB, beer-and-wine permits under another name, or recent moves): "
      + ", ".join(none["name"]) + ".")
    w("")
    notes = pm[pm["notes"].str.contains("RELOCATED|Relocated|lease|check for a new permit", regex=True)]
    if len(notes):
        w("**Changes to know**")
        for r in notes.itertuples():
            w(f"- **{r.name}:** {peer_change(r.notes)}")
        w("")
    w("### Korean micro-watch")
    w("")
    op = korean[korean["activity"].str.startswith("operating")]
    w(f"- {len(korean)} Korean concepts tracked across the metro; {len(op)} show sales or inspections in the last year. "
      "Oseyo is the only direct comp; the rest are tracked for awareness.")
    kn = wk[wk["name"].fillna("").str.upper().str.contains("KOREA|SEOUL|KBBQ|BIBIMBAP|GALBI|SOJU|POCHA|KIMCHI|BULGOGI|OSEYO")] if len(wk) else wk
    if len(kn):
        for (n, a), g in kn.groupby(["name", "address"]):
            w(f"- **{nice_name(n)}**, {nice_addr(a)}: " + "; ".join(what(r) for r in g.itertuples()) + ".")
    else:
        w("- No new Korean records this week.")

    # 8. News
    rule()
    w("## 8. News and chatter")
    w("")
    w("News feeds connect in Phase 2. Until then this section stays empty rather than guessing.")

    # 9. So what
    rule()
    s9 = OUT / f"{delivery.isoformat()}.section9.md"
    if s9.exists():
        w(s9.read_text().rstrip())
    else:
        w("## 9. So what for Sŏn")
        w("")
        w(f"- **Demand:** metro alcohol sales {pct_s(metro.yoy)}, same venues {pct_s(metro.same_yoy)} ({rng}).")
        if comp_yoy is not None:
            w(f"- **Direct comp:** Oseyo {pct_s(comp_yoy)}.")
        w(f"- **Home zone:** {len(home)} new records within 2 miles.")
        if len(ev_next):
            w("- **Coming up:** " + "; ".join(f"{r.name} ({pretty_date(r.start_date)})" for r in ev_next.itertuples()) + ".")

    # 10. Data health
    rule()
    w("## 10. Data health")
    w("")
    rs = [r for h in health.values() for r in h.get("results", []) if r["key"] not in ("home_zone",)]
    bad = [r for r in rs if r["status"] not in ("ok",)]
    w(f"**{len(rs) - len(bad)} of {len(rs)} sources ran clean.** "
      f"Alcohol sales for {month_name(cur[-1])} are {lateness.get('share', 0) * 100:.0f}% filed, enough to include; "
      "months under 90% filed are held out of comparisons.")
    for r in bad:
        note = "; ".join(r.get("notes", []))
        note = (note[:1].upper() + note[1:]).rstrip(".") + "." if note else ""
        w(f"- **{HEALTH_NAME.get(r['key'], r['name'])}: {r['status']}.** {note}")
    def ev_names(df):
        names = sorted(set(re.sub(r"(:.*| \d{4}.*)$", "", n) for n in df["name"]))
        return ", ".join(names)
    if len(ev_prev) or len(ev_win):
        w(f"- **Calendar check:** {' '.join(prev[0].split('-')[:1])} comparison months had {ev_names(ev_prev) or 'no major events'}; "
          f"this year's had {ev_names(ev_win) or 'no major events'}. Differences can move the year-over-year numbers.")

    # Appendix
    rule()
    w("## Appendix")
    w("")
    w("### All areas")
    w("")
    w("| Area | Alcohol sales | vs last year | Same venues | Growing | Venues |")
    w("|---|---|---|---|---|---|")
    for name, r in by_area.iterrows():
        br = "" if pd.isna(r.breadth) else f"{r.breadth:.0f}%"
        w(f"| {name.replace('Off-hub: ', '')} | {money_s(r.cur)} | {pct_s(r.yoy)} | {pct_s(r.same_yoy)} | {br} | {int(r.venues)} |")
    if len(others):
        w("")
        w("### Other new records this week")
        w("")
        for area, g in others.groupby("area"):
            w(f"- **{area.replace('Off-hub: ', '')}:** " + "; ".join(sorted(set(nice_name(n) for n in g["name"].dropna())))[:400])
    w("")
    w("### How to read this")
    w("")
    w("- **Alcohol sales** are Texas Mixed Beverage Gross Receipts: what each licensed venue reports monthly to the Comptroller. "
      "They cover alcohol only, so food-led and BYOB places are under-counted.")
    w("- **Same venues** compares only places that filed in both years, which strips out openings and closings.")
    w(f"- Areas with fewer than {MIN_CELL} same venues are combined. Openings and closings are called only with two sources.")

    facts = {"delivery": delivery.isoformat(), "title": title, "window": {"daily": [start.isoformat(), data_end.isoformat()],
             "receipts_cur": cur, "receipts_prev": prev},
             "metro": metro.to_dict(), "home_items": home.to_dict("records") if len(home) else [],
             "weekly_counts": wk.groupby("source").size().to_dict() if len(wk) else {}, "macro": macro,
             "upcoming_events": ev_next[["name", "start_date", "end_date", "scope", "expected_impact"]].to_dict("records")}
    return "\n".join(W) + "\n", facts


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--delivery", help="delivery Monday, YYYY-MM-DD (default: next Monday)")
    ap.add_argument("--draft", action="store_true")
    args = ap.parse_args(argv)
    today = now_utc().date()
    delivery = date.fromisoformat(args.delivery) if args.delivery else today + timedelta(days=(7 - today.weekday()) % 7 or 7)
    md, facts = render(delivery, args.draft)
    if "—" in md:
        raise SystemExit("digest contains an em dash; fix the template text")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{delivery.isoformat()}.md").write_text(md)
    (OUT / f"{delivery.isoformat()}.facts.json").write_text(json.dumps(facts, indent=2, default=str))
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
