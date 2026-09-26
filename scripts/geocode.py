"""Offline address geocoder on City of Austin street centerlines (data.austintexas.gov 8hf2-pdmb).

Interpolates a house number along the matching street segment's address range.
Accuracy is block level, which is enough for area assignment and radius checks.
Covers the City of Austin street network only; suburbs fall back to city/ZIP.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from shapely.geometry import shape

from common import DATA_DIR, TIMEOUT, session

CACHE = DATA_DIR / "geo_cache" / "streets_all.geojson"
URL = "https://data.austintexas.gov/resource/8hf2-pdmb.geojson"

WORDS = {"STREET": "ST", "AVENUE": "AVE", "AV": "AVE", "BOULEVARD": "BLVD", "ROAD": "RD", "DRIVE": "DR", "LANE": "LN",
         "PARKWAY": "PKWY", "HIGHWAY": "HWY", "CIRCLE": "CIR", "COURT": "CT", "PLACE": "PL", "TRAIL": "TRL",
         "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W", "FIRST": "1ST", "SECOND": "2ND", "THIRD": "3RD",
         "INTERSTATE": "IH", "I": "IH", "SERVICE": "SVRD", "FRONTAGE": "SVRD", "SVC": "SVRD", "FWY": "", "EXPY": "",
         "MLK": "MARTIN LUTHER KING JR", "MARTIN LUTHER KING": "MARTIN LUTHER KING JR"}
UNIT = re.compile(r"\b(STE|SUITE|UNIT|BLDG|BUILDING|APT|SPC|SPACE|RM|ROOM|FL|FLOOR|LOT|NO)\b.*$|#.*$")


def normalize(address: str) -> tuple[int, str] | None:
    a = re.sub(r"[.,]", " ", str(address or "").upper())
    a = re.sub(r"\bI-?35\b", "IH 35", a)
    a = UNIT.sub("", a)
    m = re.match(r"\s*(\d+)[A-Z]?\s+(.*)", a)
    if not m:
        return None
    words = [WORDS.get(w, w) for w in m.group(2).split()]
    street = " ".join(w for w in words if w)
    street = street.replace("MARTIN LUTHER KING JR JR", "MARTIN LUTHER KING JR")
    return int(m.group(1)), street


class Geocoder:
    def __init__(self, path: Path = CACHE):
        if not path.exists():
            r = session().get(URL, params={"$select": "the_geom,full_street_name,left_from_address,left_to_address,"
                                           "right_from_address,right_to_address", "$limit": 200000}, timeout=TIMEOUT * 10)
            r.raise_for_status()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(r.content)
        self.by_name: dict[str, list] = defaultdict(list)
        for f in json.loads(path.read_text())["features"]:
            p, g = f["properties"], f["geometry"]
            if not g or not p.get("full_street_name"):
                continue
            nums = [int(float(p[k])) for k in ("left_from_address", "left_to_address", "right_from_address", "right_to_address")
                    if p.get(k) not in (None, "", "0")]
            if nums:
                self.by_name[p["full_street_name"]].append((min(nums), max(nums), g))
        self.bare = defaultdict(list)  # street name without a leading direction
        for name in self.by_name:
            self.bare[re.sub(r"^[NSEW] ", "", name)].append(name)

    def locate(self, address, zip_code=None) -> tuple[float, float] | None:
        parsed = normalize(address)
        if not parsed:
            return None
        num, street = parsed
        spelled = re.sub(r"^([NSEW]) ", lambda m: {"N": "NORTH ", "S": "SOUTH ", "E": "EAST ", "W": "WEST "}[m.group(1)], street)
        if street in self.by_name:
            names = [street]
        elif spelled in self.by_name:  # e.g. West Lynn St is named WEST LYNN ST, not W LYNN ST
            names = [spelled]
        else:
            names = self.bare.get(re.sub(r"^[NSEW] ", "", street), [])
        best = None
        for name in names:
            for lo, hi, g in self.by_name[name]:
                if lo <= num <= hi:
                    geom = shape(g)
                    line = geom if geom.geom_type == "LineString" else max(geom.geoms, key=lambda x: x.length)
                    pt = line.interpolate((num - lo) / max(hi - lo, 1), normalized=True)
                    span = hi - lo
                    if best is None or span < best[0]:
                        best = (span, (round(pt.x, 6), round(pt.y, 6)))
        return best[1] if best else None
