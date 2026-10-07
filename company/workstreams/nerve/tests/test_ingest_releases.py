"""Offline test: series values are stored by vintage and revisions are kept."""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import ingest_releases as rel  # noqa: E402


def test_upsert_keeps_revisions(tmp_path, monkeypatch):
    monkeypatch.setattr(rel, "SERIES", tmp_path / "series.csv")
    rows = [{"series_id": "x", "period": "2026-07-01", "value": "1.0"}]
    assert rel.upsert_series(rows, "2026-09-01") == 1
    assert rel.upsert_series(rows, "2026-09-08") == 0                      # unchanged: nothing added
    rows2 = rows + [{"series_id": "x", "period": "2026-08-01", "value": "2.0"}]
    rows2[0]["value"] = "1.1"                                              # July revised
    assert rel.upsert_series(rows2, "2026-09-15") == 2
    df = pd.read_csv(tmp_path / "series.csv", dtype=str)
    july = df[df.period == "2026-07-01"]
    assert list(july.value) == ["1.0", "1.1"] and list(july.vintage) == ["2026-09-01", "2026-09-15"]
