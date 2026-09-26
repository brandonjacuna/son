"""Offline tests for address parsing (no network, no centerline file needed)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from assign_areas import split_address  # noqa: E402
from geocode import normalize  # noqa: E402
from korean_sweep import match, name_key  # noqa: E402


def test_normalize():
    assert normalize("1100 E. 5th Street, Suite 100") == (1100, "E 5TH ST")
    assert normalize("9500 S Interstate 35") == (9500, "S IH 35")
    assert normalize("6929 Airport Blvd Ste 176 # Bunit") == (6929, "AIRPORT BLVD")
    assert normalize("Nope") is None


def test_split_address_skips_building_name():
    assert split_address("South Congress Hotel, 1603 S Congress Ave, Austin, TX 78704") == \
        ("1603 S Congress Ave", "Austin", "78704")
    assert split_address("5200 Brodie Ln, Sunset Valley, TX 78745-2586") == ("5200 Brodie Ln", "Sunset Valley", "78745")


def test_korean_terms():
    assert match("Oseyo Restaurant")[0] == "strong"
    assert match("KOREAN AMERICAN BBQ")[1] == ["KOREA"]
    assert match("KIM'S CLEANERS")[0] == "weak"
    assert match("BAPTIST CHURCH CAFE")[0] is None  # weak terms need whole words
    assert match("Franklin Barbecue")[0] is None


def test_name_key_groups_variants():
    assert name_key("CHI'LANTRO 1, LLC") == name_key("Chi'Lantro - Parmer") == "CHILANTRO"
    assert name_key("PF - Gen Korean BBQ House") == "GEN"
