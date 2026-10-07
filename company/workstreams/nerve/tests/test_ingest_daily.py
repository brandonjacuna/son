"""Offline tests for the R1 snapshot diff."""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import ingest_daily as ing  # noqa: E402


def frame(rows):
    return pd.DataFrame(rows).astype("string")


def test_diff_new_removed_and_status_change():
    cfg = ing.SOURCES["tabc_licenses"]
    prev = frame([{"license_id": "1", "primary_status": "Active", "license_status": "Active"},
                  {"license_id": "2", "primary_status": "Active", "license_status": "Active"}])
    cur = frame([{"license_id": "2", "primary_status": "Suspended", "license_status": "Active"},
                 {"license_id": "3", "primary_status": "Active", "license_status": "Active"}])
    ch = ing.diff(prev, cur, cfg)
    got = sorted(zip(ch["_k"], ch["change"]))
    assert got == [("1", "removed"), ("2", "status_change"), ("3", "new")]
    assert ch.loc[ch["change"] == "status_change", "detail"].iloc[0] == "primary_status: Active -> Suspended"


def test_diff_flags_first_inspection_at_a_new_facility():
    cfg = ing.SOURCES["atx_inspections"]
    prev = frame([{"inspectionid": "10", "facility_id": "A"}])
    cur = frame([{"inspectionid": "10", "facility_id": "A"}, {"inspectionid": "11", "facility_id": "A"},
                 {"inspectionid": "12", "facility_id": "B"}])
    ch = ing.diff(prev, cur, cfg).set_index("_k")["change"]
    assert ch["11"] == "new" and ch["12"] == "new_facility"


def test_slim_keeps_diff_and_mapped_fields_only():
    cfg = ing.SOURCES["tabc_pending"]
    df = frame([{"applicationid": "1", "applicationstatus": "Received", "trade_name": "X", "owner": "Y",
                 "address": "1 Main", "city": "Austin", "zip": "78704", "submission_date": "2026-09-01",
                 "license_type": "MB", "gun_sign": "", "country": "US"}])
    assert "gun_sign" not in ing.slim(df, cfg).columns and "trade_name" in ing.slim(df, cfg).columns


def test_permits_scope_is_two_years_of_commercial_building_permits():
    w = ing.permits_where(pd.Timestamp("2026-09-26").date())
    assert "issue_date >= '2024-09-26'" in w and "permittype = 'BP'" in w and "RESTAURANT" in w
