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
    W = []
    w = W.append
    w(f"# {title}")
    w("")
    w(f"Austin metro (Travis, Williamson, Hays), with a named focus on 1 and 2 miles around 207 E St. Elmo Rd. "
      f"Daily records cover {start:%b %d} to {data_end:%b %d, %Y}. Built {now_utc():%Y-%m-%d %H:%M} UTC.")
    if draft:
        w("")
        w("> DRAFT: first full run, for founder review. The daily change history starts 2026-09-26, so this week's "
          "openings and closings come from record dates in each source rather than from day-over-day diffs.")

    # 1. What changed (rule-based ranking; the R3 routine rewrites this from the facts file)
    w("")
    w("## 1. What changed this week")
    ranked = []
    for r in home.itertuples() if len(home) else []:
        tier = "Act" if r.home_1mi or r.kind == "closing_signal" else "Alert"
        ranked.append((0 if tier == "Act" else 1, f"**{tier}:** {r.source} within {r.distance_mi} mi of 207 E St. Elmo Rd: {r.name}, {r.address} ({r.date}). {r.detail}."))
    peers_df = pd.read_csv(CONFIG_DIR / "peers_draft.csv", dtype=str, keep_default_na=False)
    comp_r = peer_receipts(mb, peers_df[peers_df["inclusion"] == "direct_comp"], cur, prev)
    for r in comp_r.itertuples():
        if r.prev and r.cur and abs(r.cur / r.prev - 1) >= 0.25:
            ranked.append((1, f"**Alert:** Direct comp {r.name} alcohol receipts {pct((r.cur / r.prev - 1) * 100)} YoY for "
                              f"{month_name(cur[0])} to {month_name(cur[-1])} ({money(r.cur)} vs {money(r.prev)})."))
    ranked.append((2, f"**Watch:** Metro alcohol receipts {pct(metro.yoy)} YoY for {month_name(cur[0])} to {month_name(cur[-1])} "
                      f"({money(metro.cur)} vs {money(metro.prev)}), with {metro.breadth:.0f}% of {int(metro.same_venues):,} same venues up."))
    alloc = next((m for m in macro if m["series"] == "alloc:austin"), None)
    if alloc:
        ranked.append((2, f"**Watch:** City of Austin sales tax allocation {alloc['change']} ({alloc['period']} payment, Comptroller)."))
    tss = next((m for m in macro if m["series"] == "tssos:rev"), None)
    if tss:
        ranked.append((2, f"**Watch:** Texas service sector revenue index {tss['value']:.1f} in {tss['period']} ({tss['change']}), Dallas Fed."))
    for _, line in sorted(ranked)[:5]:
        w(f"- {line}")

    # 2. New this week
    w("")
    w("## 2. New this week: data releases")
    w("")
    w("| Release | Latest period | Value | Change | Source released |")
    w("|---|---|---|---|---|")
    for m in macro:
        rel = fmt_released(m)
        w(f"| {m['label']} | {m['period']} | {fmt_value(m)} | {m['change'] or 'n/a'} | {rel} |")
    w(f"| Mixed Beverage Gross Receipts (venue level) | {month_name(latest)} complete; "
      f"{', '.join(month_name(p) for p in unfinished) or 'none'} still filing | | | data.texas.gov naix-2893 |")

    # 3. Openings, closings, pipeline
    w("")
    w("## 3. Openings, closings, pipeline")
    if len(wk):
        c = wk.groupby("source").size().to_dict()
        w("")
        w("Counts for the week, Travis / Williamson / Hays: " + ", ".join(f"{k}: {v}" for k, v in sorted(c.items())) + ".")
        w("Each item below is a single-source signal. An opening or closing is called only when a second source confirms it.")
        w("")
        w("**Inside 2 miles of 207 E St. Elmo Rd**")
        if len(home):
            for r in home.sort_values("distance_mi").itertuples():
                w(f"- {r.distance_mi} mi, {r.name}, {r.address}: {r.source} {r.date}. {r.detail}.")
        else:
            w("- Nothing new inside 2 miles this week.")
        hubs = wk[wk["hub"].notna() & ~wk["home_2mi"]]
        w("")
        w("**In the hubs**")
        if len(hubs):
            for r in hubs.sort_values(["area", "date"]).itertuples():
                w(f"- {r.area}: {r.name}, {r.address}. {r.source} {r.date}. {r.detail}.")
        else:
            w("- Nothing new in the hubs this week.")
        rest = wk[wk["hub"].isna() & ~wk["home_2mi"]]
        if len(rest):
            w("")
            w("**Elsewhere in the metro, by area**")
            for area, g in rest.groupby("area"):
                names = "; ".join(sorted(set(str(n)[:60] for n in g["name"].dropna())))[:400]
                w(f"- {area} ({len(g)}): {names}")
    else:
        w("- No records dated this week in any daily source.")

    # 4. Area heatmap
    w("")
    w(f"## 4. Area heatmap: alcohol receipts, {month_name(cur[0])} to {month_name(cur[-1])} vs a year earlier")
    w("")
    w(f"Mixed Beverage Gross Receipts (alcohol sales only). {month_name(cur[-1])} is {lateness.get('share', 0) * 100:.0f}% filed "
      f"against the same month last year. Breadth is the share of venues filing in both periods whose receipts rose. "
      f"Cells under {MIN_CELL} same venues are rolled up.")
    w("")
    w("| Area | Receipts (3 mo) | YoY, all filers | YoY, same venues | Breadth | Venues filing |")
    w("|---|---|---|---|---|---|")
    for name, r in by_area.iterrows():
        br = "" if pd.isna(r.breadth) else f"{r.breadth:.0f}%"
        w(f"| {name} | {money(r.cur)} | {pct(r.yoy)} | {pct(r.same_yoy)} | {br} | {int(r.venues):,} |")
    w(f"| **Metro** | **{money(metro.cur)}** | **{pct(metro.yoy)}** | **{pct(metro.same_yoy)}** | **{metro.breadth:.0f}%** | **{int(metro.venues):,}** |")
    hub_rows = by_area[~by_area.index.str.startswith(("Off-hub", "Rolled", "Unassigned"))]
    off_rows = by_area[by_area.index.str.startswith("Off-hub")]
    if len(hub_rows) and len(off_rows):
        hy = (hub_rows.cur.sum() / hub_rows.prev.sum() - 1) * 100
        oy = (off_rows.cur.sum() / off_rows.prev.sum() - 1) * 100
        w("")
        w(f"Hubs combined {pct(hy)} vs off-hub clusters combined {pct(oy)}.")

    # 5. Concept-type scorecard
    w("")
    w("## 5. Concept-type scorecard")
    w("")
    w("Same receipts window. Format comes from the Comptroller NAICS code on the matching sales tax outlet, "
      "or the manual list for fine dining and upscale casual; unmatched venues stay unclassified.")
    w("")
    w("| Format | Receipts (3 mo) | YoY, all filers | YoY, same venues | Breadth | Venues filing |")
    w("|---|---|---|---|---|---|")
    for name, r in by_fmt.iterrows():
        br = "" if pd.isna(r.breadth) else f"{r.breadth:.0f}%"
        w(f"| {name} | {money(r.cur)} | {pct(r.yoy)} | {pct(r.same_yoy)} | {br} | {int(r.venues):,} |")

    # 6. Macro panel
    w("")
    w("## 6. Macro panel")
    w("")
    w("| Indicator | Period | Value | Change | Days since period end |")
    w("|---|---|---|---|---|")
    for m in macro:
        w(f"| {m['label']} | {m['period']} | {fmt_value(m)} | {m['change'] or 'n/a'} | {m['days_old']} |")
    w("| AUS passengers | not available | | | source stale, see Data Health |")
    wr = pd.read_csv(STORE / "warn.csv", dtype=str)
    recent = wr[wr["notice_date"] >= (pd.Timestamp(delivery) - pd.DateOffset(days=90)).isoformat()]
    w(f"| WARN notices, three counties, last 90 days | through {wr['notice_date'].max()[:10]} | {len(recent)} notices, "
      f"{pd.to_numeric(recent['total_layoff_number'], errors='coerce').sum():,.0f} jobs | | source stale, see Data Health |")

    # 7. Peer watchlist and Korean micro-watch
    w("")
    w("## 7. Peer watchlist")
    w("")
    w(f"Alcohol receipts {month_name(cur[0])} to {month_name(cur[-1])} vs a year earlier, matched by address and name. "
      "Reservation availability and live ratings start with the Phase 2 peer-pulse check.")
    w("")
    w("| Peer | Area | Receipts (3 mo) | YoY | Status and notes |")
    w("|---|---|---|---|---|")
    pm = peers.merge(pr, on="name", how="left")
    for r in pm.itertuples():
        area = r.hub if r.hub else (f"Off-hub: {r.cluster}" if r.cluster else "")
        if r.subsection:
            area = f"{r.hub}: {r.subsection}"
        if r.name == "Hestia Bar":
            rec, yoy = "filed under Hestia", ""
        elif pd.isna(r.cur):
            rec, yoy = "no receipts on file", ""
        elif not r.cur and not r.prev:
            rec, yoy = "no receipts in either period", ""
        elif not r.cur and r.prev:
            rec, yoy = f"none filed; last period {month_name(r.last_period)}", ""
        else:
            rec = money(r.cur)
            yoy = pct((r.cur / r.prev - 1) * 100) if r.prev else "new since last year"
        tag = {"direct_comp": "Direct comp. ", "emmer_and_rye_group": "Emmer & Rye group. "}.get(r.inclusion, "")
        note = re.sub(r"\s+", " ", f"{tag}{r.notes}")
        note = note if len(note) <= 240 else note[:240].rsplit(" ", 1)[0] + "..."
        w(f"| {r.name} | {area} | {rec} | {yoy} | {note} |")
    w("")
    w("### Korean micro-watch")
    op = korean[korean["activity"].str.startswith("operating")]
    w(f"- {len(korean)} Korean concepts tracked in the metro, {len(op)} with receipts or inspections in the last year. "
      "Oseyo is the direct comp; the rest are tracked for awareness.")
    for r in korean[korean["tier"] == "direct_comp"].itertuples():
        w(f"- Oseyo, {r.address}: {r.activity}. Alcohol receipts {money(float(r.receipts_recent))} for {r.receipts_window}.")
    kn = wk[wk["name"].fillna("").str.upper().str.contains("KOREA|SEOUL|KBBQ|BIBIMBAP|GALBI|SOJU|POCHA|KIMCHI|BULGOGI|OSEYO")] if len(wk) else wk
    kn = kn.groupby(["name", "address"], as_index=False).agg({"source": lambda s: " and ".join(sorted(set(s))), "detail": "; ".join}) if len(kn) else kn
    w(f"- New Korean records this week: {len(kn)}." + "".join(f" {r.name}, {r.address}: {r.source} ({r.detail})." for r in kn.itertuples()))

    # 8. News
    w("")
    w("## 8. News and chatter")
    w("- News feeds are not connected yet (Phase 2). No headlines are reported until they are.")

    # 9. So what: the R3 routine writes data/digests/<delivery>.section9.md; rule-based fallback otherwise
    w("")
    s9 = OUT / f"{delivery.isoformat()}.section9.md"
    if s9.exists():
        w(s9.read_text().rstrip())
    else:
        w("## 9. So what for Sŏn")
        w(f"- Demand: metro alcohol receipts are {pct(metro.yoy)} YoY across all filers and {pct(metro.same_yoy)} for venues "
          f"open in both periods ({month_name(cur[0])} to {month_name(cur[-1])}).")
        comp = next((r for r in pm.itertuples() if r.inclusion == "direct_comp"), None)
        if comp is not None and pd.notna(comp.cur) and comp.prev:
            w(f"- Competition: Oseyo receipts {pct((comp.cur / comp.prev - 1) * 100)} YoY for the same window.")
        mm = {m["series"]: m for m in macro}
        if "bls:CUUR0300SEFV" in mm and "tssos:wgs" in mm:
            w(f"- Cost and pricing: CPI food away from home in the South is {mm['bls:CUUR0300SEFV']['change']} "
              f"({mm['bls:CUUR0300SEFV']['period']}). Texas service firms report wage pressure at {mm['tssos:wgs']['value']:.1f} "
              f"and selling prices at {mm['tssos:sell']['value']:.1f} on the Dallas Fed index ({mm['tssos:wgs']['period']}).")
        if "bls:SMU48124207000000001" in mm:
            w(f"- Labor: Austin leisure and hospitality employment is {mm['bls:SMU48124207000000001']['value']:.1f}k, "
              f"{mm['bls:SMU48124207000000001']['change']} ({mm['bls:SMU48124207000000001']['period']}, preliminary); "
              f"metro unemployment {mm['bls:LAUMT481242000000003']['value']:.1f}% ({mm['bls:LAUMT481242000000003']['period']}).")
        w(f"- Home zone: {len(home)} new records inside 2 miles of 207 E St. Elmo Rd this week.")
        if len(ev_next):
            w("- Coming up: " + "; ".join(f"{r.name} ({r.start_date} to {r.end_date})" for r in ev_next.itertuples()) + ".")

    # 10. Data health
    w("")
    w("## 10. Data health")
    w("")
    w("| Source | Status | Notes |")
    w("|---|---|---|")
    for f, h in health.items():
        for r in h.get("results", []):
            note = "; ".join(r.get("notes", []))[:160]
            w(f"| {r['name']} | {r['status']} | {note} |")
    held = ", ".join(f"{month_name(p)} {rstatus[p]['share'] * 100:.0f}%" for p in unfinished if rstatus[p]["share"]) or "none"
    w(f"| Receipts completeness | {month_name(cur[-1])} {lateness.get('share', 0) * 100:.0f}% filed | "
      f"{held} held out of YoY |")
    ev_note = "; ".join(f"{r.name}" for r in pd.concat([ev_win, ev_prev]).itertuples())
    if ev_note:
        w(f"| Calendar in the comparison window | note | {ev_note[:300]} |")

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
