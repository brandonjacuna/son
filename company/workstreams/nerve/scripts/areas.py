"""Assign a venue to hub, sub-section, off-hub cluster, and home-zone ring.

    from areas import Areas
    Areas().assign(lon, lat, city="AUSTIN", zip_code="78704")

Order: polygon in config/areas.geojson, then city name, then ZIP
(config/area_fallbacks.json), then 'Unassigned'.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from shapely.geometry import Point, shape
from shapely.strtree import STRtree

CONFIG = Path(__file__).resolve().parent.parent / "config"
EARTH_MI = 3958.7613
NEAR_DEG = 0.0005  # about 50 m


def miles_between(lon1, lat1, lon2, lat2) -> float:
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2
    return 2 * EARTH_MI * math.asin(math.sqrt(a))


class Areas:
    def __init__(self, areas_path: Path = CONFIG / "areas.geojson", fallbacks_path: Path = CONFIG / "area_fallbacks.json"):
        fc = json.loads(Path(areas_path).read_text())
        self.home = fc["metadata"]["home"]
        feats = [f for f in fc["features"] if f["properties"]["tier"] != "overlay"]
        self.props = [f["properties"] for f in feats]
        self.geoms = [shape(f["geometry"]) for f in feats]
        self.tree = STRtree(self.geoms)
        fb = json.loads(Path(fallbacks_path).read_text())
        self.by_city = {c.upper(): g for g, cities in fb["suburban_groups_by_city"].items() for c in cities}
        self.by_zip = {z: g for g, zips in fb["clusters_by_zip"].items() for z in zips}

    def assign(self, lon=None, lat=None, city: str | None = None, zip_code: str | None = None) -> dict:
        out = {"area_id": None, "hub": None, "subsection": None, "cluster": None, "hub_tier": "unassigned",
               "method": None, "distance_mi": None, "home_1mi": False, "home_2mi": False}
        if lon is not None and lat is not None and not (math.isnan(lon) or math.isnan(lat)):
            d = miles_between(self.home["lon"], self.home["lat"], lon, lat)
            out.update(distance_mi=round(d, 2), home_1mi=d <= 1, home_2mi=d <= 2)
            pt = Point(lon, lat)
            hits = [i for i in self.tree.query(pt) if self.geoms[i].covers(pt)]
            # Hubs and sub-sections win over off-hub clusters if edges overlap.
            hits.sort(key=lambda i: self.props[i]["tier"] == "offhub_cluster")
            if not hits:
                # A point geocoded onto a boundary street can fall in a sliver between polygons.
                near = self.tree.query_nearest(pt, max_distance=NEAR_DEG)
                hits = [int(i) for i in near]
            if hits:
                p = self.props[hits[0]]
                out.update(area_id=p["area_id"], hub=p["hub"], subsection=p["subsection"], method="polygon",
                           cluster=None if p["hub"] else p["name"], hub_tier="hub" if p["hub"] else "off_hub")
                return out
        group = self.by_city.get((city or "").strip().upper())
        if group is None and zip_code:
            group = self.by_zip.get(str(zip_code).strip()[:5])
            method = "zip"
        else:
            method = "city"
        if group:
            out.update(cluster=group, hub_tier="off_hub", method=method)
        return out
