"""Offline checks that config/areas.geojson assigns landmark points to the intended areas."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from areas import Areas, miles_between  # noqa: E402


@pytest.fixture(scope="module")
def areas():
    return Areas()


@pytest.mark.parametrize("lon, lat, area_id", [
    (-97.7431, 30.2747, "dt_core"),            # Texas Capitol, Congress Ave at 11th St
    (-97.7384, 30.2587, "dt_rainey"),           # Rainey St
    (-97.7470, 30.2650, "dt_2nd_warehouse"),    # 2nd St at Colorado
    (-97.7497, 30.2490, "soco"),                # S Congress at Elizabeth St
    (-97.7686, 30.2493, "slamar"),              # S Lamar at Oltorf area
    (-97.7212, 30.2560, "east_holly_ecc"),      # E Cesar Chavez corridor
    (-97.7265, 30.2635, "east_6th_7th"),        # E 6th St east of I-35
    (-97.7240, 30.2720, "east_12th"),           # E 12th St
])
def test_landmarks(areas, lon, lat, area_id):
    assert areas.assign(lon, lat)["area_id"] == area_id


def test_home_rings(areas):
    home = areas.home
    r = areas.assign(home["lon"], home["lat"])
    assert r["home_1mi"] and r["distance_mi"] == 0
    far = areas.assign(-97.7431, 30.2747)
    assert not far["home_2mi"] and far["distance_mi"] > 3


def test_fallbacks(areas):
    assert areas.assign(city="Round Rock")["cluster"] == "Round Rock / Georgetown"
    assert areas.assign(city="AUSTIN", zip_code="78745-1234")["cluster"] == "Austin: Far South"
    assert areas.assign(city="AUSTIN")["hub_tier"] == "unassigned"


def test_hub_names_do_not_collide_with_clusters(areas):
    hubs = {p["hub"] for p in areas.props if p["hub"]}
    clusters = {p["name"] for p in areas.props if p["tier"] == "offhub_cluster"}
    assert not hubs & clusters


def test_miles_between():
    assert miles_between(-97.74, 30.27, -97.74, 30.27 + 1 / 69.05) == pytest.approx(1, rel=0.01)
