"""Add area columns (hub, sub-section, cluster, home-zone distance) to a CSV of venues.

Usage: python scripts/assign_areas.py config/peers_draft.csv [--address-col address]

Parses city and ZIP from a full address ("123 Main St, Austin, TX 78701") when the
CSV has no separate columns. Rewrites the file in place; reruns are idempotent.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from areas import Areas  # noqa: E402
from geocode import Geocoder  # noqa: E402

COLS = ["lat", "lon", "located_by", "area_id", "hub", "subsection", "cluster", "distance_mi", "home_1mi", "home_2mi"]


def split_address(full: str) -> tuple[str, str | None, str | None]:
    parts = [p.strip() for p in str(full or "").split(",")]
    street = next((p for p in parts if re.match(r"^\d", p)), "")  # skips a leading building name
    zip_m = re.search(r"\b(\d{5})(?:-\d{4})?\b\s*$", str(full or ""))
    after = parts[parts.index(street) + 1:] if street in parts else parts[1:]
    city = next((p for p in after if p and not re.match(r"^(TX|Texas)\b|^(Ste|Suite|Unit|Bldg)\b|^\d", p, re.I)), None)
    return street, city, zip_m.group(1) if zip_m else None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--address-col", default="address")
    args = ap.parse_args(argv)
    df = pd.read_csv(args.csv, dtype=str, keep_default_na=False)
    areas, geo = Areas(), Geocoder()
    rows = []
    for full in df[args.address_col]:
        street, city, zip_code = split_address(full)
        pt = geo.locate(street) if street and (city or "Austin").upper() == "AUSTIN" else None
        a = areas.assign(*(pt or (None, None)), city=city, zip_code=zip_code)
        rows.append({"lat": pt[1] if pt else "", "lon": pt[0] if pt else "", "located_by": "street centerline" if pt else "",
                     **{k: ("" if a[k] is None else a[k]) for k in COLS[3:]}})
    out = pd.concat([df.drop(columns=[c for c in COLS if c in df.columns]), pd.DataFrame(rows)], axis=1)
    out.to_csv(args.csv, index=False)
    print(out[["name", "area_id", "hub", "subsection", "cluster", "distance_mi"]].to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
