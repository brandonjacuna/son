"""R1 ingest-daily: snapshot the daily sources, diff against the last snapshot, queue home-zone signals.

Usage: python scripts/ingest_daily.py [--only KEY ...] [--date YYYY-MM-DD]

Sources (BRIEF section 4): TABC pending applications and licenses, Comptroller sales tax
permits (food NAICS), Austin food inspections, Austin building permits for food uses.
Scope: Travis, Williamson, Hays (ClickUp template).

Writes
  data/store/current/<source>.csv       slim state per source (keys, watched fields, mapped fields),
                                        sorted by key so git stores only the daily delta
  data/store/changes/<date>.parquet     new / removed / status-changed records, with areas
  data/signals/queue.jsonl              changes within 2 miles of 207 E St. Elmo Rd (R3 or the
                                        ClickUp push drains it)
  data/store/run_health.json
A first run for a source only sets its baseline; it never reports the whole table as new.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import timedelta
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from areas import Areas  # noqa: E402
from common import DATA_DIR, TIMEOUT, classify_error, now_utc, redact, session, write_run_health  # noqa: E402
from geocode import Geocoder  # noqa: E402

STORE = DATA_DIR / "store"
CURRENT, CHANGES = STORE / "current", STORE / "changes"
QUEUE = DATA_DIR / "signals" / "queue.jsonl"

COUNTIES = "('Travis','Williamson','Hays')"
COUNTY_CODES = "('227','246','105')"
FOOD_NAICS = "((outlet_naics_code >= 722000 AND outlet_naics_code < 723000) OR outlet_naics_code in (311811,312120,312130,312140))"
FOOD_WORDS = ["RESTAURANT", " BAR", "CAFE", "BREWERY", "COFFEE", "COMMERCIAL KITCHEN", "FOOD SERVICE", "TAQUERIA",
              "EATING", "DINING", "BAKERY", "WINE", "COCKTAIL", "PIZZ", "SUSHI", "KITCHEN AND BAR"]

# key: unique id; watch: fields whose change is a status change; map: source field -> common field.
SOURCES = {
    "tabc_pending": {
        "domain": "data.texas.gov", "id": "mxm5-tdpj", "where": f"county in {COUNTIES}",
        "key": ["applicationid"], "watch": ["applicationstatus"],
        "map": {"name": "trade_name", "owner": "owner", "address": "address", "city": "city", "zip": "zip",
                "date": "submission_date", "kind": "license_type", "status": "applicationstatus"}},
    "tabc_licenses": {
        "domain": "data.texas.gov", "id": "7hf9-qc9f", "where": f"county in {COUNTIES}",
        "key": ["license_id"], "watch": ["primary_status", "license_status"], "extra": ["status_change_date"],
        "map": {"name": "trade_name", "owner": "owner", "address": "address", "city": "city", "zip": "zip",
                "date": "original_issue_date", "kind": "license_type", "status": "primary_status"}},
    "sales_tax_permits": {
        "domain": "data.texas.gov", "id": "jrea-zgmq", "where": f"outlet_county_code in {COUNTY_CODES} AND {FOOD_NAICS}",
        "key": ["taxpayer_number", "outlet_number"], "watch": [], "extra": ["outlet_permit_issue_date"],
        "map": {"name": "outlet_name", "owner": "taxpayer_name", "address": "outlet_address", "city": "outlet_city",
                "zip": "outlet_zip_code", "date": "outlet_first_sales_date", "kind": "outlet_naics_code"}},
    "atx_inspections": {
        "domain": "data.austintexas.gov", "id": "ecmv-9xxi", "where": "1=1",
        "key": ["inspectionid"], "watch": [], "new_entity": "facility_id",
        "map": {"name": "restaurant_name", "address": "address", "zip": "zip_code", "date": "inspection_date",
                "kind": "process_description", "status": "score", "lat": "lat", "lon": "lng"}},
    "atx_permits": {
        "domain": "data.austintexas.gov", "id": "3syk-w9eu",
        "where": None,  # built in main(): trailing two years of commercial building permits for food uses
        "key": ["permit_number"], "watch": ["status_current"],
        "map": {"name": "description", "owner": "applicant_org", "address": "original_address1", "city": "original_city",
                "zip": "original_zip", "date": "issue_date", "kind": "work_class", "status": "status_current",
                "lat": "latitude", "lon": "longitude"}},
}


def permits_where(today) -> str:
    since = (today - timedelta(days=730)).isoformat()
    words = " OR ".join(f"upper(description) like '%{w}%'" for w in FOOD_WORDS)
    return f"issue_date >= '{since}' AND permit_class_mapped = 'Commercial' AND permittype = 'BP' AND ({words})"


def fetch(s, cfg: dict) -> pd.DataFrame:
    rows, offset = [], 0
    while True:
        r = s.get(f"https://{cfg['domain']}/resource/{cfg['id']}.json",
                  params={"$where": cfg["where"], "$limit": 50000, "$offset": offset, "$order": ":id"}, timeout=TIMEOUT * 3)
        r.raise_for_status()
        batch = r.json()
        rows += batch
        if len(batch) < 50000:
            break
        offset += 50000
    df = pd.DataFrame(rows)
    for c in df.columns:  # nested geo columns do not survive parquet round trips cleanly
        if df[c].map(lambda v: isinstance(v, (dict, list))).any():
            df[c] = df[c].map(lambda v: json.dumps(v) if isinstance(v, (dict, list)) else v)
    return df.astype("string")


def slim(df: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    cols = list(dict.fromkeys([*cfg["key"], *cfg["watch"], *([cfg["new_entity"]] if cfg.get("new_entity") else []),
                               *cfg.get("extra", []),
                               *cfg["map"].values()]))
    return df[[c for c in cols if c in df.columns]].copy()


def keyed(df: pd.DataFrame, key: list[str]) -> pd.Series:
    return df[key].fillna("").agg("|".join, axis=1)


def diff(prev: pd.DataFrame, cur: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    k_prev, k_cur = keyed(prev, cfg["key"]), keyed(cur, cfg["key"])
    prev, cur = prev.assign(_k=k_prev).drop_duplicates("_k"), cur.assign(_k=k_cur).drop_duplicates("_k")
    new = cur[~cur["_k"].isin(prev["_k"])].assign(change="new", detail="")
    removed = prev[~prev["_k"].isin(cur["_k"])].assign(change="removed", detail="no longer in the source")
    if cfg.get("new_entity"):  # an inspection at a facility never seen before is an opening signal
        ent = cfg["new_entity"]
        new.loc[~new[ent].isin(prev[ent]), "change"] = "new_facility"
    out = [new, removed]
    if cfg["watch"]:
        both = cur.merge(prev[["_k", *cfg["watch"]]], on="_k", suffixes=("", "_prev"))
        for f in cfg["watch"]:
            ch = both[both[f].fillna("") != both[f"{f}_prev"].fillna("")]
            if len(ch):
                out.append(ch.assign(change="status_change", detail=[f"{f}: {a} -> {b}" for a, b in zip(ch[f"{f}_prev"], ch[f])]))
    return pd.concat(out, ignore_index=True) if out else cur.iloc[0:0]


def normalize(ch: pd.DataFrame, key: str, cfg: dict, areas: Areas, geo: Geocoder, day: str) -> pd.DataFrame:
    m = cfg["map"]
    out = pd.DataFrame({"run_date": day, "source": key, "change": ch["change"], "detail": ch["detail"], "record_id": ch["_k"]})
    for f in ["name", "owner", "address", "city", "zip", "date", "kind", "status", "lat", "lon"]:
        out[f] = ch[m[f]].values if f in m and m[f] in ch else None
    if "owner" in m:  # TABC and permits often leave the trade name blank
        out["name"] = out["name"].fillna(out["owner"])
    if key == "atx_inspections":
        out["city"] = "AUSTIN"
        out["address"] = out["address"].str.split(r" (?:Austin|Travis County)", regex=True).str[0]
    assigned = []
    for r in out.itertuples():
        lat, lon = pd.to_numeric(r.lat, errors="coerce"), pd.to_numeric(r.lon, errors="coerce")
        if (pd.isna(lat) or pd.isna(lon)) and str(r.city or "").upper() == "AUSTIN":
            pt = geo.locate(r.address)
            lon, lat = pt if pt else (None, None)
        a = areas.assign(None if pd.isna(lon) else float(lon), None if pd.isna(lat) else float(lat),
                         city=r.city, zip_code=str(r.zip or "")[:5])
        assigned.append({"lat": lat, "lon": lon, **{k: a[k] for k in ("area_id", "hub", "subsection", "cluster",
                                                                        "distance_mi", "home_1mi", "home_2mi")}})
    return pd.concat([out.drop(columns=["lat", "lon"]), pd.DataFrame(assigned)], axis=1)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--date", help="run date override, YYYY-MM-DD")
    args = ap.parse_args(argv)
    today = pd.Timestamp(args.date).date() if args.date else now_utc().date()
    day = today.isoformat()
    SOURCES["atx_permits"]["where"] = permits_where(today)
    s, areas, geo = session(), Areas(), Geocoder()
    CURRENT.mkdir(parents=True, exist_ok=True)
    CHANGES.mkdir(parents=True, exist_ok=True)
    results, changes = [], []
    for key, cfg in SOURCES.items():
        if args.only and key not in args.only:
            continue
        res = {"key": key, "name": key, "status": "ok", "row_count": None, "fields": [], "freshness": {}, "notes": []}
        try:
            cur = fetch(s, cfg)
            res["row_count"] = len(cur)
            if cur.empty:
                raise ValueError("source returned no rows; keeping the previous snapshot")
            cur = slim(cur, cfg)
            path = CURRENT / f"{key}.csv"
            if path.exists():
                ch = diff(pd.read_csv(path, dtype=str, keep_default_na=False).replace("", pd.NA).astype("string"), cur, cfg)
                if len(ch) > 0.2 * max(len(cur), 1):
                    res["status"] = "needs_review"
                    res["notes"].append(f"{len(ch)} changes is over 20% of the table; likely a schema or scope change, "
                                        "not reported as signals")
                elif len(ch):
                    changes.append(normalize(ch, key, cfg, areas, geo, day))
                res["freshness"]["changes"] = ch["change"].value_counts().to_dict() if len(ch) else {}
            else:
                res["notes"].append("first run: baseline set, no changes reported")
            cur.sort_values(cfg["key"]).to_csv(path, index=False)
        except Exception as exc:  # noqa: BLE001 - reported in run health, never raised
            res["status"] = classify_error(exc) if not isinstance(exc, ValueError) else "error"
            res["notes"].append(redact(f"{type(exc).__name__}: {exc}")[:300])
        print(f"{key}: {res['status']} rows={res['row_count']} {res['freshness'].get('changes', '')}", flush=True)
        results.append(res)

    if changes:
        allch = pd.concat(changes, ignore_index=True).astype({"zip": "string", "date": "string", "status": "string"})
        day_file = CHANGES / f"{day}.parquet"
        if day_file.exists():  # a rerun on the same day replaces only the sources it ran
            earlier = pd.read_parquet(day_file)
            allch = pd.concat([earlier[~earlier["source"].isin(allch["source"])], allch], ignore_index=True)
        allch.to_parquet(day_file, index=False)
        home = allch[allch["home_2mi"] == True]  # noqa: E712
        if len(home):
            QUEUE.parent.mkdir(parents=True, exist_ok=True)
            with QUEUE.open("a") as f:
                for r in home.to_dict("records"):
                    f.write(json.dumps({k: (None if pd.isna(v) else v) for k, v in r.items()}, default=str) + "\n")
        results.append({"key": "home_zone", "name": "Home-zone signals queued", "status": "ok", "row_count": len(home),
                        "fields": [], "freshness": {}, "notes": []})
    write_run_health(STORE / "run_health.json", "ingest_daily", results)
    return 0 if all(r["status"] in ("ok", "needs_review") for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
