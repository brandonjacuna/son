"""R2 ingest-releases: pull the periodic releases and store every value by vintage.

Usage: python scripts/ingest_releases.py [--only KEY ...]

Writes
  data/store/series.csv        long table: series_id, period, value, vintage (first date this value was seen).
                               A revised value gets a new row, so every vintage is kept.
  data/store/series_meta.json  title, units, source, release date or last_updated per series
  data/store/mixed_bev.csv     venue-month alcohol receipts, Travis / Williamson / Hays, since 2023.
                               The trailing 6 months are re-pulled each run because filings back-fill.
  data/store/warn.csv          WARN layoff notices in the three counties
  data/store/releases_health.json
AUS passenger reports are PDFs behind a viewer and the page stops at November 2025; the source
is reported as stale in Data Health until a machine-readable feed is found.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA_DIR, TIMEOUT, classify_error, env, now_utc, redact, session, write_run_health  # noqa: E402

STORE = DATA_DIR / "store"
SERIES, META = STORE / "series.csv", STORE / "series_meta.json"
MIXED_BEV, WARN = STORE / "mixed_bev.csv", STORE / "warn.csv"

FRED = {  # id: short label
    "AUST448LEIHN": "Austin MSA leisure and hospitality jobs (NSA, thousands)",
    "AUSLEIHA175MFRBDAL": "Austin MSA leisure and hospitality jobs (SA, Dallas Fed, thousands)",
    "TXUR": "Texas unemployment rate (SA, %)",
    "GASREGW": "US regular gasoline price (weekly, $/gal)",
    "UMCSENT": "University of Michigan consumer sentiment",
}
BLS = {
    "SMU48124200000000001": "Austin MSA total nonfarm jobs (NSA, thousands)",
    "SMU48124207000000001": "Austin MSA leisure and hospitality jobs (NSA, thousands)",
    "LAUMT481242000000003": "Austin MSA unemployment rate (NSA, %)",
    "CUUR0000SEFV": "CPI food away from home, US city average (NSA)",
    "CUUR0300SEFV": "CPI food away from home, South urban (NSA)",
}
TSSOS_URL = "https://www.dallasfed.org/~/media/Documents/research/surveys/tssos/documents/tssos_alldata_sa.xls"
TSSOS = {"rev": "revenue", "frev": "revenue, six months ahead", "emp": "employment", "wgs": "wages and benefits",
         "sell": "selling prices", "inp": "input prices", "bact": "general business activity",
         "fbact": "general business activity, six months ahead", "uncr": "outlook uncertainty"}
ALLOC_CITIES = ["Austin", "Round Rock", "Georgetown", "Cedar Park", "Pflugerville", "Leander", "San Marcos", "Kyle",
                "Buda", "Lakeway", "Bee Cave", "West Lake Hills", "Hutto", "Manor", "Dripping Springs", "Sunset Valley"]
COUNTY_CODES = "('227','246','105')"
WARN_COUNTIES = "('Travis','Williamson','Hays')"


def upsert_series(rows: list[dict], today: str) -> int:
    """Append values not seen before (new periods or revisions); returns rows added."""
    new = pd.DataFrame(rows, columns=["series_id", "period", "value"]).dropna(subset=["value"])
    new["value"] = new["value"].astype(str)
    old = pd.read_csv(SERIES, dtype=str) if SERIES.exists() else pd.DataFrame(columns=["series_id", "period", "value", "vintage"])
    latest = old.sort_values("vintage").drop_duplicates(["series_id", "period"], keep="last")
    m = new.merge(latest, on=["series_id", "period"], how="left", suffixes=("", "_old"))
    add = m[m["value_old"].isna() | (m["value"] != m["value_old"])][["series_id", "period", "value"]].assign(vintage=today)
    if len(add):
        pd.concat([old, add]).sort_values(["series_id", "period", "vintage"]).to_csv(SERIES, index=False)
    return len(add)


def fred(s, meta, rows):
    key = env("FRED_API_KEY")
    if not key:
        raise RuntimeError("FRED_API_KEY not set")
    for sid, label in FRED.items():
        q = {"series_id": sid, "api_key": key, "file_type": "json"}
        info = s.get("https://api.stlouisfed.org/fred/series", params=q, timeout=TIMEOUT).json()["seriess"][0]
        obs = s.get("https://api.stlouisfed.org/fred/series/observations",
                    params={**q, "observation_start": "2018-01-01"}, timeout=TIMEOUT).json()["observations"]
        rows += [{"series_id": f"fred:{sid}", "period": o["date"], "value": o["value"]} for o in obs if o["value"] != "."]
        meta[f"fred:{sid}"] = {"label": label, "title": info["title"], "units": info["units"], "frequency": info["frequency"],
                               "released": info["last_updated"], "source": f"FRED {sid}"}


def bls(s, meta, rows):
    year = now_utc().year
    body = {"seriesid": list(BLS), "startyear": str(year - 8), "endyear": str(year), "catalog": True}
    if env("BLS_API_KEY"):
        body["registrationkey"] = env("BLS_API_KEY")
    p = s.post("https://api.bls.gov/publicAPI/v2/timeseries/data/", json=body, timeout=TIMEOUT).json()
    if p.get("status") != "REQUEST_SUCCEEDED":
        raise RuntimeError("; ".join(p.get("message", [])) or "BLS request failed")
    for ser in p["Results"]["series"]:
        sid = ser["seriesID"]
        for d in ser["data"]:
            if d["period"].startswith("M") and d["period"] != "M13":
                rows.append({"series_id": f"bls:{sid}", "period": f"{d['year']}-{d['period'][1:]}-01", "value": d["value"]})
        latest = ser["data"][0] if ser["data"] else {}
        meta[f"bls:{sid}"] = {"label": BLS[sid], "title": (ser.get("catalog") or {}).get("series_title", BLS[sid]),
                              "frequency": "Monthly", "preliminary_latest": any((f or {}).get("code") == "P" for f in latest.get("footnotes", [])),
                              "released": None, "source": f"BLS {sid}"}


def tssos(s, meta, rows):
    r = s.get(TSSOS_URL, timeout=TIMEOUT)
    r.raise_for_status()
    df = pd.read_excel(io.BytesIO(r.content))
    df["period"] = pd.to_datetime(df["date"], format="%b-%y").dt.strftime("%Y-%m-01")
    for col, label in TSSOS.items():
        rows += [{"series_id": f"tssos:{col}", "period": p, "value": v} for p, v in zip(df["period"], df[col]) if pd.notna(v)]
        meta[f"tssos:{col}"] = {"label": f"Texas service sector: {label} (SA diffusion index)", "frequency": "Monthly",
                                "released": r.headers.get("Last-Modified"), "source": "Dallas Fed TSSOS"}


def allocations(s, meta, rows):
    cities = ",".join(f"'{c}'" for c in ALLOC_CITIES)
    data = s.get("https://data.texas.gov/resource/vfba-b57j.json",
                 params={"$where": f"city in ({cities}) AND report_period_type = 'MONTHLY' AND report_year >= 2019",
                         "$limit": 50000}, timeout=TIMEOUT).json()
    for d in data:
        sid = f"alloc:{d['city'].lower().replace(' ', '_')}"
        rows.append({"series_id": sid, "period": f"{int(float(d['report_year']))}-{int(float(d['report_month'])):02d}-01",
                     "value": d["net_payment_this_period"]})
        meta[sid] = {"label": f"Sales tax allocation, {d['city']} ($, month paid)", "frequency": "Monthly",
                     "released": None, "source": "Comptroller vfba-b57j"}


def mixed_bev(s, today: str) -> dict:
    """Venue-month receipts. Full history on first run, trailing 6 months after that (back-fills)."""
    since = "2023-01-01" if not MIXED_BEV.exists() else (pd.Timestamp(today) - pd.DateOffset(months=6)).strftime("%Y-%m-01")
    cols = ("tabc_permit_number,taxpayer_number,location_number,location_name,location_address,location_city,location_zip,"
            "location_county,obligation_end_date_yyyymmdd,liquor_receipts,wine_receipts,beer_receipts,cover_charge_receipts,total_receipts")
    rows, offset = [], 0
    while True:
        batch = s.get("https://data.texas.gov/resource/naix-2893.json", params={
            "$select": cols, "$where": f"location_county in {COUNTY_CODES} AND obligation_end_date_yyyymmdd >= '{since}' "
                                       f"AND obligation_end_date_yyyymmdd <= '{today}'",
            "$order": ":id", "$limit": 50000, "$offset": offset}, timeout=TIMEOUT * 3).json()
        rows += batch
        if len(batch) < 50000:
            break
        offset += 50000
    new = pd.DataFrame(rows).astype(str)
    new["period"] = new.pop("obligation_end_date_yyyymmdd").str[:7]
    key = ["tabc_permit_number", "location_number", "period"]
    if MIXED_BEV.exists():
        old = pd.read_csv(MIXED_BEV, dtype=str)
        new = pd.concat([old[old["period"] < since[:7]], new]).drop_duplicates(key, keep="last")
    new.sort_values(key).to_csv(MIXED_BEV, index=False)
    counts = new.groupby("period").size()
    return {"rows": len(new), "since": since, "latest_period": counts.index.max(), "reporters_by_period": counts.tail(14).to_dict()}


def warn(s) -> dict:
    data = s.get("https://data.texas.gov/resource/8w53-c4f6.json",
                 params={"$where": f"county_name in {WARN_COUNTIES}", "$limit": 50000}, timeout=TIMEOUT).json()
    df = pd.DataFrame(data).astype(str)
    df.sort_values("notice_date").to_csv(WARN, index=False)
    meta = s.get("https://data.texas.gov/api/views/8w53-c4f6.json", timeout=TIMEOUT).json()
    updated = pd.Timestamp(meta.get("rowsUpdatedAt", 0), unit="s", tz="UTC")
    return {"rows": len(df), "latest_notice": df["notice_date"].max()[:10] if len(df) else None,
            "portal_updated": updated.date().isoformat(), "days_since_update": (now_utc() - updated).days}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", nargs="*")
    args = ap.parse_args(argv)
    today = now_utc().date().isoformat()
    s = session()
    STORE.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META.read_text()) if META.exists() else {}
    results = []
    jobs = {"fred": fred, "bls": bls, "tssos": tssos, "allocations": allocations}
    for key, fn in jobs.items():
        if args.only and key not in args.only:
            continue
        res = {"key": key, "name": key, "status": "ok", "row_count": None, "fields": [], "freshness": {}, "notes": []}
        rows: list[dict] = []
        try:
            fn(s, meta, rows)
            res["row_count"] = upsert_series(rows, today)
            res["notes"].append(f"{res['row_count']} new or revised values")
        except Exception as exc:  # noqa: BLE001
            res["status"] = classify_error(exc) if not isinstance(exc, (RuntimeError, KeyError)) else "error"
            res["notes"].append(redact(f"{type(exc).__name__}: {exc}")[:300])
        results.append(res)
        print(f"{key}: {res['status']} {res['notes'][-1]}", flush=True)
    for key, fn in {"mixed_bev": lambda: mixed_bev(s, today), "warn": lambda: warn(s)}.items():
        if args.only and key not in args.only:
            continue
        res = {"key": key, "name": key, "status": "ok", "row_count": None, "fields": [], "freshness": {}, "notes": []}
        try:
            info = fn()
            res["row_count"], res["freshness"] = info.pop("rows"), info
            if info.get("days_since_update", 0) > 45:
                res["status"] = "stale"
                res["notes"].append(f"portal not updated for {info['days_since_update']} days")
        except Exception as exc:  # noqa: BLE001
            res["status"] = classify_error(exc)
            res["notes"].append(redact(f"{type(exc).__name__}: {exc}")[:300])
        results.append(res)
        print(f"{key}: {res['status']} rows={res['row_count']} {res['notes']}", flush=True)
    results.append({"key": "aus_passengers", "name": "AUS passenger traffic", "status": "stale", "row_count": None,
                    "fields": [], "freshness": {"latest_report_listed": "2025-11"},
                    "notes": ["flyaustin.com lists monthly PDFs only through November 2025 and serves them through a "
                              "viewer, not as files; no figure is reported until a machine-readable source is found"]})
    META.write_text(json.dumps(meta, indent=2, sort_keys=True))
    write_run_health(STORE / "releases_health.json", "ingest_releases", results)
    return 0 if all(r["status"] in ("ok", "stale") for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
