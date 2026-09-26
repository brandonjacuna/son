"""Offline tests for ClickUp sync planning (no network)."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import clickup_sync as cs  # noqa: E402


def test_signals_are_planned_once(tmp_path, monkeypatch):
    monkeypatch.setattr(cs, "QUEUE", tmp_path / "queue.jsonl")
    monkeypatch.setattr(cs, "SENT", tmp_path / "sent.json")
    row = {"source": "tabc_pending", "record_id": "1", "change": "new", "run_date": "2026-09-27", "name": "Test Bar",
           "address": "1 Main St", "city": "Austin", "hub": None, "subsection": None, "cluster": "South Austin",
           "distance_mi": 0.8, "home_1mi": True, "detail": ""}
    cs.QUEUE.write_text(json.dumps(row) + "\n")
    plans = cs.plan_signals()
    assert len(plans) == 1 and plans[0]["name"].startswith("Act: Test Bar (0.8 mi)")
    cs.SENT.write_text(json.dumps([plans[0]["key"]]))
    assert cs.plan_signals() == []


def test_dropdown_fields_use_option_ids():
    f = cs.field("Venue status", "Open")
    assert f["id"] == cs.FIELDS["fields"]["Venue status"]["id"]
    assert f["value"] == cs.FIELDS["fields"]["Venue status"]["options"]["Open"]
    assert cs.field("Distance (mi)", None) is None
