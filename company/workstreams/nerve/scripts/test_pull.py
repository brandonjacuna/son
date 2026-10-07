"""Test-pull every Phase 1 source and report row counts, fields, and freshness.

Usage: python scripts/test_pull.py [--only KEY ...] [--sample N]

Writes data/test_pulls/run_health.json, data/test_pulls/report.md, and a
sample Parquet file per tabular source. Nothing here is a production ingest:
it verifies dataset IDs, field names, and update cadence against the live
sources (BRIEF.md section 5).
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA_DIR, TIMEOUT, classify_error, env, now_utc, redact, session, write_run_health  # noqa: E402

OUT_DIR = DATA_DIR / "test_pulls"

# Socrata datasets. `expect` holds substrings that should appear in at least one
# field name; a miss means the brief's assumption about the dataset needs review.
# `order` is the substring of the date field that best reflects freshness.
SOCRATA = [
    {"key": "tabc_pending", "name": "TABC pending original license applications", "domain": "data.texas.gov",
     "id": "mxm5-tdpj", "expect": ["trade", "address", "city", "license"], "order": "date"},
    {"key": "tabc_licenses", "name": "TABC license information", "domain": "data.texas.gov",
     "id": "7hf9-qc9f", "expect": ["license", "status", "trade", "address"], "order": "issue"},
    {"key": "sales_tax_permits", "name": "Comptroller active sales tax permit holders", "domain": "data.texas.gov",
     "id": "jrea-zgmq", "expect": ["naics", "first", "outlet", "city"], "order": "permit_issue"},
    {"key": "mixed_bev", "name": "Mixed Beverage Gross Receipts", "domain": "data.texas.gov",
     "id": "naix-2893", "expect": ["taxpayer", "location", "obligation", "total"], "order": "obligation"},
    {"key": "atx_inspections", "name": "Austin food establishment inspections", "domain": "data.austintexas.gov",
     "id": "ecmv-9xxi", "expect": ["facility", "score", "inspection", "address"], "order": "inspection"},
    {"key": "atx_permits", "name": "Austin issued construction permits", "domain": "data.austintexas.gov",
     "id": "3syk-w9eu", "expect": ["permit", "work_class", "issue", "description"], "order": "issue"},
    {"key": "sales_tax_alloc_city", "name": "Comptroller sales tax allocation, city", "domain": "data.texas.gov",
     "id": "vfba-b57j", "expect": ["city", "payment", "report_month"], "order": "date",
     "period": ("report_year", "report_month")},
]

DATE_TYPES = {"calendar_date", "floating_timestamp", "fixed_timestamp", "date"}

# Austin-Round Rock-San Marcos MSA (CBSA 12420), leisure and hospitality, all employees.
FRED_SERIES = ["AUSLEIHA175MFRBDAL", "AUST448LEIHN"]
BLS_SERIES = "SMU48124207000000001"

TSSOS_URL = "https://www.dallasfed.org/research/surveys/tssos"
COMPTROLLER_ALLOC_URL = "https://comptroller.texas.gov/transparency/local/allocations/sales-tax/"
FLYAUSTIN_URL = "https://www.flyaustin.com/"

MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE_TEXT = re.compile(rf"\b({MONTHS})\s+(\d{{1,2}},\s+)?(20\d\d)\b")


# ---------------------------------------------------------------- helpers

def result(key: str, name: str, **kw) -> dict:
    return {"key": key, "name": name, "status": "ok", "row_count": None, "fields": [],
            "freshness": {}, "notes": [], **kw}


def fail(res: dict, exc: Exception) -> dict:
    res["status"] = classify_error(exc)
    res["notes"].append(redact(f"{type(exc).__name__}: {exc}")[:300])
    return res


def parse_ts(value) -> datetime | None:
    if value in (None, ""):
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc)
    try:
        ts = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    return ts if ts.tzinfo else ts.replace(tzinfo=timezone.utc)


def days_old(ts: datetime | None) -> int | None:
    return None if ts is None else (now_utc() - ts).days


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links.append((self._href, " ".join("".join(self._text).split())))
            self._href = None


def page_links(html: str, base: str) -> list[tuple[str, str]]:
    p = LinkParser()
    p.feed(html)
    return [(urljoin(base, href), text) for href, text in p.links]


def latest_date_text(html: str) -> str | None:
    """Most recent 'Month [D,] YYYY' string on a page. A hint, not a release date."""
    best: tuple[date, str] | None = None
    for m in DATE_TEXT.finditer(re.sub(r"<[^>]+>", " ", html)):
        month = datetime.strptime(m.group(1), "%B").month
        day = int(m.group(2).rstrip(", ")) if m.group(2) else 1
        try:
            d = date(int(m.group(3)), month, day)
        except ValueError:
            continue
        if d <= now_utc().date() and (best is None or d > best[0]):
            best = (d, m.group(0))
    return best[1] if best else None


# ---------------------------------------------------------------- Socrata

def probe_socrata(s, src: dict, sample: int) -> dict:
    res = result(src["key"], src["name"], source=f"{src['domain']} {src['id']}")
    base = f"https://{src['domain']}"
    try:
        meta = s.get(f"{base}/api/views/{src['id']}.json", timeout=TIMEOUT)
        meta.raise_for_status()
        meta = meta.json()
        res["dataset_title"] = meta.get("name")
        cols = [c for c in meta.get("columns", []) if not c.get("fieldName", "").startswith(":")]
        res["fields"] = [f"{c['fieldName']} ({c.get('dataTypeName')})" for c in cols]
        names = [c["fieldName"] for c in cols]
        missing = [e for e in src["expect"] if not any(e in n.lower() for n in names)]
        if missing:
            res["notes"].append(f"expected field substrings not found: {missing}")
        updated = parse_ts(meta.get("rowsUpdatedAt"))
        res["freshness"]["portal_rows_updated_at"] = updated.isoformat() if updated else None
        res["freshness"]["portal_days_since_update"] = days_old(updated)

        r = s.get(f"{base}/resource/{src['id']}.json", params={"$select": "count(*) AS n"}, timeout=TIMEOUT)
        r.raise_for_status()
        res["row_count"] = int(r.json()[0]["n"])

        date_cols = [c["fieldName"] for c in cols if c.get("dataTypeName") in DATE_TYPES]
        maxes = {}
        for col in date_cols[:8]:
            r = s.get(f"{base}/resource/{src['id']}.json", params={"$select": f"max({col}) AS m"}, timeout=TIMEOUT)
            r.raise_for_status()
            maxes[col] = (r.json() or [{}])[0].get("m")
        res["freshness"]["max_by_date_field"] = maxes
        order = next((c for c in date_cols if src["order"] in c.lower()), date_cols[0] if date_cols else None)
        if order:
            latest = parse_ts(maxes.get(order))
            res["freshness"]["latest_record_field"] = order
            if latest and latest > now_utc():
                # Some fields carry scheduled or period-end dates; report the latest one already past.
                res["notes"].append(f"{order} has future dates (max {latest.date()}); freshness uses the latest past date")
                today = now_utc().date().isoformat()
                r = s.get(f"{base}/resource/{src['id']}.json",
                          params={"$select": f"max({order}) AS m", "$where": f"{order} <= '{today}'"}, timeout=TIMEOUT)
                r.raise_for_status()
                latest = parse_ts((r.json() or [{}])[0].get("m"))
            res["freshness"]["latest_record"] = latest.date().isoformat() if latest else None
        elif src.get("period"):
            y, m = src["period"]
            r = s.get(f"{base}/resource/{src['id']}.json",
                      params={"$select": f"{y},{m}", "$order": f"{y} DESC, {m} DESC", "$limit": 1}, timeout=TIMEOUT)
            r.raise_for_status()
            row = (r.json() or [{}])[0]
            if row.get(y) and row.get(m):
                res["freshness"]["latest_record"] = f"{int(float(row[y]))}-{int(float(row[m])):02d}"
        else:
            res["notes"].append("no typed date field; freshness from portal update time only")

        params = {"$limit": sample}
        if order:
            params["$order"] = f"{order} DESC"
        r = s.get(f"{base}/resource/{src['id']}.json", params=params, timeout=TIMEOUT)
        r.raise_for_status()
        df = pd.DataFrame(r.json())
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        df.to_parquet(OUT_DIR / f"{src['key']}_sample.parquet", index=False)
        res["sample_rows"] = len(df)
        if missing:
            res["status"] = "needs_review"
    except Exception as exc:  # noqa: BLE001 - every failure is reported, never raised
        return fail(res, exc)
    return res


# ---------------------------------------------------------------- FRED / BLS

def probe_fred(s) -> list[dict]:
    key = env("FRED_API_KEY")
    out = []
    for sid in FRED_SERIES:
        res = result(f"fred_{sid.lower()}", f"FRED {sid}", source=f"api.stlouisfed.org {sid}")
        if not key:
            res["status"] = "needs_key"
            res["notes"].append("FRED_API_KEY not set in .env")
            out.append(res)
            continue
        try:
            base = "https://api.stlouisfed.org/fred"
            q = {"series_id": sid, "api_key": key, "file_type": "json"}
            r = s.get(f"{base}/series", params=q, timeout=TIMEOUT)
            r.raise_for_status()
            info = r.json()["seriess"][0]
            res["dataset_title"] = info["title"]
            r = s.get(f"{base}/series/observations", params=q, timeout=TIMEOUT)
            r.raise_for_status()
            obs = r.json()["observations"]
            res["row_count"] = len(obs)
            res["fields"] = ["date", "value", f"units: {info['units']}", f"frequency: {info['frequency']}",
                             f"seasonal adjustment: {info['seasonal_adjustment_short']}"]
            last = obs[-1] if obs else {}
            res["freshness"] = {"last_updated": info["last_updated"], "observation_start": info["observation_start"],
                                "observation_end": info["observation_end"], "latest_value": last.get("value")}
        except Exception as exc:  # noqa: BLE001
            fail(res, exc)
            if res["status"] == "http_400":
                res["status"] = "not_found"
        out.append(res)
    return out


def probe_bls(s) -> dict:
    res = result("bls_ces_austin_lh", "BLS CES Austin MSA leisure and hospitality", source=f"api.bls.gov {BLS_SERIES}")
    year = now_utc().year
    body = {"seriesid": [BLS_SERIES], "startyear": str(year - 9), "endyear": str(year), "catalog": True}
    if env("BLS_API_KEY"):
        body["registrationkey"] = env("BLS_API_KEY")
    else:
        res["notes"].append("BLS_API_KEY not set; keyless v2 limits apply (25 queries/day, 10 years, no catalog)")
    try:
        r = s.post("https://api.bls.gov/publicAPI/v2/timeseries/data/", json=body, timeout=TIMEOUT)
        r.raise_for_status()
        payload = r.json()
        if payload.get("status") != "REQUEST_SUCCEEDED":
            res["status"] = "error"
            res["notes"].extend(payload.get("message", []))
            return res
        series = payload["Results"]["series"][0]
        data = series.get("data", [])
        res["row_count"] = len(data)
        res["fields"] = sorted({k for d in data for k in d})
        if series.get("catalog"):
            res["dataset_title"] = series["catalog"].get("series_title")
        latest = data[0] if data else {}
        res["freshness"] = {"latest_period": f"{latest.get('year')}-{latest.get('period')}",
                            "latest_value": latest.get("value"),
                            "preliminary": any(f.get("code") == "P" for f in latest.get("footnotes", []) if f)}
        res["notes"].extend(m for m in payload.get("message", []) if m)
    except Exception as exc:  # noqa: BLE001
        return fail(res, exc)
    return res


# ---------------------------------------------------------------- HTML release pages

def probe_release_page(s, key: str, name: str, url: str, link_filter) -> dict:
    """Fetch an official release page, list its data links, and report the latest date text on it."""
    res = result(key, name, source=url)
    try:
        r = s.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        links = [(u, t) for u, t in page_links(r.text, r.url) if link_filter(u, t)]
        res["row_count"] = None
        res["fields"] = [f"{t or '(no text)'} -> {u}" for u, t in links[:15]]
        res["freshness"] = {"latest_date_text_on_page": latest_date_text(r.text)}
        res["notes"].append(f"{len(links)} candidate data links; table shape confirmed after the file is chosen")
        res["status"] = "needs_review"
    except Exception as exc:  # noqa: BLE001
        return fail(res, exc)
    return res


def is_data_file(u: str, t: str) -> bool:
    return bool(re.search(r"\.(xlsx?|csv|pdf)(\?|$)", u, re.I))


def probe_tssos(s) -> dict:
    return probe_release_page(s, "dallasfed_tssos", "Dallas Fed Texas Service Sector Outlook", TSSOS_URL,
                              lambda u, t: is_data_file(u, t) or ("tssos" in u.lower() and "data" in (u + t).lower()))


def probe_comptroller_alloc(s) -> list[dict]:
    page = probe_release_page(s, "comptroller_alloc", "Comptroller local sales tax allocations", COMPTROLLER_ALLOC_URL,
                              lambda u, t: is_data_file(u, t) or "alloc" in u.lower())
    # A structured copy on the open data portal beats a web page, if one exists.
    cat = result("comptroller_alloc_catalog", "data.texas.gov catalog search: sales tax allocations",
                 source="data.texas.gov /api/catalog/v1")
    try:
        r = s.get("https://data.texas.gov/api/catalog/v1",
                  params={"q": "sales tax allocation", "only": "dataset", "limit": 10}, timeout=TIMEOUT)
        r.raise_for_status()
        hits = r.json().get("results", [])
        cat["fields"] = [f"{h['resource']['id']}: {h['resource']['name']} (updated {h['resource'].get('data_updated_at')})"
                         for h in hits]
        cat["row_count"] = len(hits)
        cat["status"] = "needs_review"
        cat["notes"].append("candidate datasets; choose one and add it to the Socrata list")
    except Exception as exc:  # noqa: BLE001
        fail(cat, exc)
    return [page, cat]


def probe_aus(s) -> dict:
    res = probe_release_page(s, "aus_passengers", "AUS passenger traffic", FLYAUSTIN_URL,
                             lambda u, t: re.search(r"passenger|statistic|traffic|facts", u + " " + t, re.I))
    if res["status"] == "needs_review" and res["fields"]:
        # Follow the first statistics link one level down to find the monthly files.
        stats_url = res["fields"][0].split(" -> ")[-1]
        sub = probe_release_page(s, "aus_passengers", "AUS passenger traffic", stats_url, is_data_file)
        sub["notes"].insert(0, f"followed from homepage to {stats_url}")
        return sub
    return res


# ---------------------------------------------------------------- report

def render_report(results: list[dict]) -> str:
    lines = [f"# Phase 1 test pull, {now_utc():%Y-%m-%d %H:%M} UTC", ""]
    lines.append("| Source | Status | Rows | Freshness |")
    lines.append("|---|---|---|---|")
    for r in results:
        f = r["freshness"]
        fresh = (f.get("latest_record") or f.get("observation_end") or f.get("latest_period")
                 or f.get("latest_date_text_on_page") or "")
        if f.get("portal_days_since_update") is not None:
            fresh += f" (portal updated {f['portal_days_since_update']}d ago)"
        rows = "" if r["row_count"] is None else f"{r['row_count']:,}"
        lines.append(f"| {r['name']} | {r['status']} | {rows} | {fresh} |")
    for r in results:
        lines += ["", f"## {r['name']}", f"- Source: `{r.get('source')}`", f"- Status: {r['status']}"]
        if r.get("dataset_title"):
            lines.append(f"- Title on source: {r['dataset_title']}")
        for k, v in r["freshness"].items():
            lines.append(f"- {k}: {v}")
        for n in r["notes"]:
            lines.append(f"- Note: {n}")
        if r["fields"]:
            lines.append("- Fields:")
            lines += [f"  - `{fld}`" for fld in r["fields"]]
    return redact("\n".join(lines) + "\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", nargs="*", help="source keys to run (prefix match)")
    ap.add_argument("--sample", type=int, default=1000, help="rows to save per Socrata dataset")
    args = ap.parse_args(argv)

    s = session()
    jobs = [(src["key"], lambda src=src: [probe_socrata(s, src, args.sample)]) for src in SOCRATA]
    jobs += [("fred", lambda: probe_fred(s)), ("bls", lambda: [probe_bls(s)]),
             ("dallasfed_tssos", lambda: [probe_tssos(s)]), ("comptroller_alloc", lambda: probe_comptroller_alloc(s)),
             ("aus_passengers", lambda: [probe_aus(s)])]
    results = []
    for key, job in jobs:
        if args.only and not any(key.startswith(o) for o in args.only):
            continue
        print(f"probing {key} ...", flush=True)
        results.extend(job())

    write_run_health(OUT_DIR / "run_health.json", "test_pull", results)
    report = render_report(results)
    (OUT_DIR / "report.md").write_text(report)
    print(report)
    return 0 if all(r["status"] in ("ok", "needs_review") for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
