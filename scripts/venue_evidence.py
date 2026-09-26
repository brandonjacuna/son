"""Add operating evidence to a venue CSV: latest alcohol receipts period and latest inspection.

Usage: python scripts/venue_evidence.py config/peers_draft.csv [--address-col address]

Matches on street number, street name, and the first distinctive word of the venue name,
so other tenants at a shared address (hotels, food halls) are not counted.
Evidence only: a missing match is 'no record', never 'closed' (BRIEF section 9).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assign_areas import split_address  # noqa: E402
from common import TIMEOUT, now_utc, session  # noqa: E402
from geocode import normalize  # noqa: E402

DIRS = {"N", "S", "E", "W"}
STOP = {"THE", "LA", "LE", "EL", "BAR", "CAFE", "RESTAURANT"}


def name_word(name: str) -> str:
    """First distinctive word of a venue name, for matching trade names across sources."""
    words = [w for w in re.sub(r"[^A-Z0-9 ]", " ", str(name).upper().replace("'", "")).split() if w not in STOP]
    return words[0] if words else ""


def street_parts(address: str) -> tuple[str, str] | None:
    parsed = normalize(split_address(address)[0])
    if not parsed:
        return None
    num, street = parsed
    words = [w for w in street.split() if w not in DIRS]
    return str(num), (words[0] if words else "")


def latest(s, domain, dataset, select, where) -> dict:
    r = s.get(f"https://{domain}/resource/{dataset}.json", params={"$select": select, "$where": where}, timeout=TIMEOUT)
    r.raise_for_status()
    rows = r.json()
    return rows[0] if rows else {}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--address-col", default="address")
    args = ap.parse_args(argv)
    s = session()
    df = pd.read_csv(args.csv, dtype=str, keep_default_na=False)
    today = now_utc().date().isoformat()
    out = []
    for addr, vname in zip(df[args.address_col], df["name"]):
        parts = street_parts(addr)
        if not parts:
            out.append({"last_receipts": "", "receipts_name": "", "last_inspection": "", "inspection_name": "", "evidence": "no address"})
            continue
        num, word = (p.replace("'", "''") for p in parts)
        nw = name_word(vname)
        mb = latest(s, "data.texas.gov", "naix-2893",
                    "max(obligation_end_date_yyyymmdd) AS last, max(location_name) AS name",
                    f"starts_with(upper(location_address), '{num} ') AND upper(location_address) like '%{word}%' "
                    f"AND obligation_end_date_yyyymmdd <= '{today}' AND location_county = '227' "
                    f"AND (upper(location_name) like '%{nw}%' OR upper(taxpayer_name) like '%{nw}%')")
        insp = latest(s, "data.austintexas.gov", "ecmv-9xxi", "max(inspection_date) AS last, max(restaurant_name) AS name",
                      f"starts_with(upper(address), '{num} ') AND upper(address) like '%{word}%' "
                      f"AND upper(restaurant_name) like '%{nw}%'")
        mb_last, in_last = (mb.get("last") or "")[:10], (insp.get("last") or "")[:10]
        ev = []
        if mb_last:
            ev.append(f"receipts through {mb_last[:7]}")
        if in_last:
            ev.append(f"inspected {in_last}")
        out.append({"last_receipts": mb_last, "receipts_name": mb.get("name", ""), "last_inspection": in_last,
                    "inspection_name": insp.get("name", ""), "evidence": "; ".join(ev) or "no record under this name at this address"})
    cols = ["last_receipts", "receipts_name", "last_inspection", "inspection_name", "evidence"]
    res = pd.concat([df.drop(columns=[c for c in cols if c in df.columns]), pd.DataFrame(out)], axis=1)
    res.to_csv(args.csv, index=False)
    print(res[["name", "evidence", "receipts_name", "inspection_name"]].to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
