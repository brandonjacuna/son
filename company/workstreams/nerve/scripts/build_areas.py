"""Build config/areas.geojson (draft hub, sub-section, off-hub, and home-zone polygons).

Usage: python scripts/build_areas.py [--refresh]

Geometry comes from City of Austin open data only:
- Neighborhood Planning Areas (data.austintexas.gov inrm-c3ee) for the lake and
  highway edges and for the off-hub clusters.
- Street Centerline (data.austintexas.gov 8hf2-pdmb) for the street-defined edges
  in BRIEF.md section 6.

Every polygon is a DRAFT until Brandon approves it. Edit the RULES below, rerun,
and review the map; do not hand-edit the GeoJSON.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from shapely import set_precision
from shapely.geometry import LineString, Point, Polygon, box, mapping, shape
from shapely.ops import split, substring, transform, unary_union

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import CONFIG_DIR, DATA_DIR, TIMEOUT, session  # noqa: E402

CACHE = DATA_DIR / "geo_cache"
OUT = CONFIG_DIR / "areas.geojson"

NPA_URL = "https://data.austintexas.gov/resource/inrm-c3ee.geojson"
STREETS_URL = "https://data.austintexas.gov/resource/8hf2-pdmb.geojson"
STREETS_BOX = (30.33, -97.84, 30.17, -97.66)  # north, west, south, east

HOME_ADDRESS = "207 E St. Elmo Rd"
HOME_STREET, HOME_NUMBER = "E ST ELMO RD", 207
MILE_M = 1609.344

# Local equirectangular projection around downtown: metres, good to <0.1% here.
LAT0, LON0 = 30.27, -97.74
KX, KY = 111_320 * math.cos(math.radians(LAT0)), 110_574


def to_m(geom):
    return transform(lambda x, y, z=None: ((np.asarray(x) - LON0) * KX, (np.asarray(y) - LAT0) * KY), geom)


def to_ll(geom):
    return transform(lambda x, y, z=None: (np.asarray(x) / KX + LON0, np.asarray(y) / KY + LAT0), geom)


# ---------------------------------------------------------------- data

def fetch(name: str, url: str, params: dict, refresh: bool) -> dict:
    path = CACHE / f"{name}.geojson"
    if refresh or not path.exists():
        r = session().get(url, params=params, timeout=TIMEOUT * 5)
        r.raise_for_status()
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_text(r.text)
    return json.loads(path.read_text())


def load(refresh: bool):
    npa = fetch("npa", NPA_URL, {"$limit": 5000}, refresh)
    n, w, s, e = STREETS_BOX
    streets = fetch("streets", STREETS_URL, {
        "$where": f"within_box(the_geom, {n}, {w}, {s}, {e})",
        "$select": "the_geom,full_street_name,left_from_address,left_to_address,right_from_address,right_to_address",
        "$limit": 100000}, refresh)
    return npa, streets


class Streets:
    def __init__(self, fc: dict):
        self.features = [(f["properties"], to_m(shape(f["geometry"]))) for f in fc["features"] if f["geometry"]]

    def segments(self, pattern: str, bbox_ll=None):
        rx = re.compile(pattern)
        clip = to_m(box(*bbox_ll)) if bbox_ll else None
        out = []
        for props, g in self.features:
            if rx.fullmatch(props.get("full_street_name") or "") and (clip is None or g.intersects(clip)):
                out.append(g)
        if not out:
            raise ValueError(f"no street segments match {pattern!r}")
        return out

    def spine(self, pattern: str, bbox_ll=None, step: float = 120.0) -> LineString:
        """One smooth line through every segment matching `pattern` (divided roads and ramps averaged)."""
        pts = np.array([c for g in self.segments(pattern, bbox_ll) for part in getattr(g, "geoms", [g])
                        for c in part.coords])[:, :2]
        centre = pts.mean(axis=0)
        axis = np.linalg.svd(pts - centre)[2][0]
        normal = np.array([-axis[1], axis[0]])
        t, u = (pts - centre) @ axis, (pts - centre) @ normal
        edges = np.arange(t.min(), t.max() + step, step)
        coords = []
        for lo, hi in zip(edges[:-1], edges[1:]):
            m = (t >= lo) & (t < hi)
            if m.any():
                coords.append(centre + axis * t[m].mean() + normal * u[m].mean())
        return LineString(coords)


def extend(line: LineString, d: float = 100_000) -> LineString:
    c = list(line.coords)
    def ext(a, b):
        v = np.subtract(a, b)
        return tuple(np.add(a, v / np.linalg.norm(v) * d))
    return LineString([ext(c[0], c[1]), *c, ext(c[-1], c[-2])])


WORLD = box(-40_000, -40_000, 40_000, 40_000)


def side(line: LineString, ref_ll: tuple[float, float]):
    """Half of the working area on the same side of `line` (extended) as the reference point."""
    ref = to_m(Point(ref_ll))
    for piece in split(WORLD, extend(line)).geoms:
        if piece.contains(ref):
            return piece
    raise ValueError("reference point not on either side of the line")


def corridor(line: LineString, a: LineString, b: LineString, half_width: float):
    """Buffer of `line` between its crossings with `a` and `b`."""
    line = extend(line, 2_000)  # a boundary street may stop short of the crossing (e.g. S Congress at the river)
    ta, tb = (line.project(line.intersection(extend(x)).centroid) for x in (a, b))
    return substring(line, min(ta, tb), max(ta, tb)).buffer(half_width, cap_style="flat")


def tidy(name: str) -> str:
    return re.sub(r"\b(Mlk|Rmma|Ut)\b", lambda m: m.group(0).upper(), name.title())


def home_point(streets: Streets) -> Point:
    """Interpolate the home address along its centerline segment's address range."""
    for props, g in streets.features:
        if props.get("full_street_name") != HOME_STREET:
            continue
        lo = int(props.get("left_from_address") or props.get("right_from_address") or 0)
        hi = int(props.get("left_to_address") or props.get("right_to_address") or 0)
        if lo <= HOME_NUMBER <= hi:
            line = g if g.geom_type == "LineString" else max(g.geoms, key=lambda p: p.length)
            return line.interpolate((HOME_NUMBER - lo) / max(hi - lo, 1), normalized=True)
    raise ValueError(f"{HOME_ADDRESS} not found in centerlines")


# ---------------------------------------------------------------- rules

def build(npa_fc: dict, streets_fc: dict) -> dict:
    st = Streets(streets_fc)
    npas = [(f["properties"], to_m(shape(f["geometry"]))) for f in npa_fc["features"]]

    def npa(*names):
        return unary_union([g for p, g in npas if p["planning_area_name"] in names]).buffer(0)

    core = (-97.80, 30.22, -97.68, 30.30)
    i35 = st.spine(r"(N |S )?IH 35( SVRD)? [NS]B", (-97.76, 30.24, -97.70, 30.30))
    lamar_s = st.spine(r"S LAMAR BLVD( NB| SB| SVRD NB| SVRD SB)?", (-97.80, 30.22, -97.75, 30.265))
    congress_s = st.spine(r"S CONGRESS AVE", (-97.76, 30.22, -97.73, 30.262))
    congress = st.spine(r"CONGRESS AVE", core)
    cesar = st.spine(r"[EW] CESAR CHAVEZ ST", (-97.76, 30.255, -97.735, 30.27))
    riverside = st.spine(r"[EW] RIVERSIDE DR", (-97.76, 30.25, -97.74, 30.265))
    oltorf = st.spine(r"[EW] OLTORF ST", (-97.77, 30.22, -97.73, 30.245))
    barton = st.spine(r"BARTON SPRINGS RD", (-97.78, 30.255, -97.755, 30.27))
    ben_white = st.spine(r"[EW] BEN WHITE BLVD( SVRD)? [EW]B", (-97.80, 30.21, -97.76, 30.235))
    sixth_w = st.spine(r"W 6TH ST", (-97.755, 30.26, -97.742, 30.275))
    red_river = st.spine(r"RED RIVER ST", (-97.74, 30.258, -97.73, 30.275))
    fifth_e = st.spine(r"E 5TH ST", (-97.735, 30.25, -97.69, 30.27))
    seventh_e = st.spine(r"E 7TH ST", (-97.735, 30.25, -97.69, 30.27))
    eleventh_e = st.spine(r"E 11TH ST", (-97.737, 30.26, -97.715, 30.28))
    mlk_e = st.spine(r"E MARTIN LUTHER KING JR BLVD", (-97.735, 30.275, -97.70, 30.29))
    pleasant_valley = st.spine(r"N PLEASANT VALLEY RD", (-97.72, 30.245, -97.70, 30.265))
    airport = st.spine(r"AIRPORT BLVD", (-97.72, 30.26, -97.69, 30.30))
    manor = st.spine(r"MANOR RD", (-97.73, 30.278, -97.69, 30.295))
    berkman = st.spine(r"BERKMAN DR", (-97.705, 30.28, -97.69, 30.30))
    first_s = st.spine(r"S 1ST ST", (-97.77, 30.22, -97.745, 30.262))

    downtown = npa("DOWNTOWN")
    rainey = downtown & side(cesar, (-97.738, 30.255)) & side(red_river, (-97.735, 30.259))
    warehouse = downtown & side(sixth_w, (-97.748, 30.262)) & side(congress, (-97.75, 30.265))
    downtown_core = downtown - rainey - warehouse

    soco = corridor(congress_s, cesar, oltorf, 250) - downtown
    slamar = (corridor(lamar_s, barton, ben_white, 250) | corridor(first_s, riverside, oltorf, 250)) - downtown - soco

    east_base = (npa("EAST CESAR CHAVEZ", "HOLLY", "CENTRAL EAST AUSTIN", "GOVALLE", "CHESTNUT",
                     "UPPER BOGGY CREEK", "MLK", "ROSEWOOD", "JOHNSTON TERRACE")
                 & side(i35, (-97.72, 30.265)))
    inside_pv = side(pleasant_valley, (-97.72, 30.26))
    holly = east_base & inside_pv & side(fifth_e, (-97.72, 30.252))
    e67 = (east_base & inside_pv & ((side(fifth_e, (-97.72, 30.275)) & side(seventh_e, (-97.72, 30.252)))
                                    | extend(seventh_e).buffer(150))) - holly
    e12 = ((east_base & side(airport, (-97.725, 30.275)) & side(mlk_e, (-97.72, 30.27))
            & (side(eleventh_e, (-97.72, 30.285)) | extend(eleventh_e).buffer(150))) - e67 - holly)
    manor_rd = (corridor(manor, i35, berkman, 200) & side(i35, (-97.72, 30.285))) - e12

    features = []

    def add(geom, area_id, name, tier, hub, subsection, rule, status="draft"):
        geom = geom.buffer(0)
        if geom.is_empty:
            raise ValueError(f"{area_id} is empty; check its rule")
        features.append({"type": "Feature", "geometry": mapping(set_precision(to_ll(geom.simplify(3)), 1e-6)), "properties": {
            "area_id": area_id, "name": name, "tier": tier, "hub": hub, "subsection": subsection,
            "status": status, "rule": rule, "area_sq_mi": round(geom.area / MILE_M**2, 3)}})

    # Hub boundaries approved by Brandon 2026-09-26: Rainey and 2nd St / Warehouse are their own hubs,
    # S 1st St joins South Lamar, Manor Rd is an East sub-section through the Tillery St block.
    ok = "approved"
    add(downtown_core, "dt_core", "Downtown", "hub", "Downtown", None,
        "Downtown NPA (Lady Bird Lake to MLK, Lamar to I-35) minus Rainey Street and 2nd Street / Warehouse", ok)
    add(rainey, "dt_rainey", "Rainey Street", "hub", "Rainey Street", None,
        "Downtown NPA south of Cesar Chavez and east of Red River St", ok)
    add(warehouse, "dt_2nd_warehouse", "2nd Street / Warehouse", "hub", "2nd Street / Warehouse", None,
        "Downtown NPA south of W 6th St and west of Congress Ave", ok)
    add(soco, "soco", "South Congress", "hub", "South Congress", None,
        "S Congress Ave from the river to Oltorf St, 250 m (about 2 to 3 blocks) either side", ok)
    add(slamar, "slamar", "South Lamar", "hub", "South Lamar", None,
        "S Lamar Blvd from Barton Springs Rd to Ben White Blvd, plus S 1st St from Riverside Dr to Oltorf St, "
        "250 m either side", ok)
    add(holly, "east_holly_ecc", "Holly / East Cesar Chavez", "subsection", "East Austin", "Holly / East Cesar Chavez",
        "East of I-35, west of Pleasant Valley Rd, south of E 5th St to the lake", ok)
    add(e67, "east_6th_7th", "East 6th / 7th", "subsection", "East Austin", "East 6th / 7th",
        "East of I-35, west of Pleasant Valley Rd, E 5th St to E 7th St plus 150 m north of 7th", ok)
    add(e12, "east_12th", "East 12th and north", "subsection", "East Austin", "East 12th and north",
        "East of I-35, west of Airport Blvd, 150 m south of E 11th St north to MLK Jr Blvd", ok)
    add(manor_rd, "east_manor", "Manor Road", "subsection", "East Austin", "Manor Road",
        "Manor Rd from I-35 to Berkman Dr (past the Tillery St block), 200 m either side", ok)

    hubs = unary_union([to_m(shape(f["geometry"])) for f in features])
    clusters: dict[str, list] = {}
    members: dict[str, set] = {}
    for p, g in npas:
        cname = p.get("combined_npa") or p["planning_area_name"]
        clusters.setdefault(cname, []).append(g)
        members.setdefault(cname, set()).add(p["planning_area_name"])
    hub_names = {f["properties"]["hub"] for f in features}
    for cname, geoms in sorted(clusters.items()):
        geom = unary_union(geoms).buffer(0) - hubs
        if geom.area < 0.05 * MILE_M**2:
            continue
        label = tidy(re.sub(r"\s+Combined NPA$", "", cname, flags=re.I))
        if label in hub_names:  # e.g. the South Congress NPA group is St. Elmo, not the SoCo hub
            label = " / ".join(tidy(m) for m in sorted(members[cname]))
        slug = re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")
        add(geom, f"off_{slug}", label, "offhub_cluster", None, None,
            f"City of Austin neighborhood planning area group '{cname}' minus hubs")

    home = home_point(st)
    for miles in (1, 2):
        add(home.buffer(miles * MILE_M, quad_segs=32), f"home_{miles}mi", f"Home zone {miles} mi", "overlay",
            None, None, f"{miles}-mile radius around {HOME_ADDRESS} (address interpolated on the street centerline)",
            status="fixed")

    hx, hy = to_ll(home).coords[0]
    return {"type": "FeatureCollection", "name": "son_nerve_areas",
            "metadata": {"status": "Hubs approved by Brandon 2026-09-26; off-hub clusters and fallbacks still draft", "home": {"address": HOME_ADDRESS,
                         "lon": round(hx, 6), "lat": round(hy, 6)},
                         "sources": ["data.austintexas.gov inrm-c3ee", "data.austintexas.gov 8hf2-pdmb"],
                         "fallback": "config/area_fallbacks.json"},
            "features": features}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--refresh", action="store_true", help="re-download the city GIS layers")
    args = ap.parse_args(argv)
    fc = build(*load(args.refresh))
    OUT.write_text(json.dumps(fc, separators=(",", ":")))
    for f in fc["features"]:
        p = f["properties"]
        print(f"{p['tier']:15} {p['area_id']:34} {p['area_sq_mi']:8.3f} sq mi  {p['status']}")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
