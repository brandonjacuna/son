#!/usr/bin/env python3
"""Validate equipment/*.yaml against equipment/schema.json plus Sŏn rules.
Usage: python3 scripts/validate_equipment.py [files...]   (default: all records)
"""
import json, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / "equipment/schema.json").read_text())
V = Draft202012Validator(schema)
files = [Path(f) for f in sys.argv[1:]] or sorted(p for p in (ROOT / "equipment").glob("*.yaml") if not p.name.startswith("_"))
bad = 0
for f in files:
    rec = yaml.safe_load(f.read_text())
    errs = [e.message for e in V.iter_errors(rec)]
    d = rec.get("dimensions", {}) or {}
    srcs = rec.get("sources", []) or []
    if d.get("status") == "verified":
        if not any(s.get("type") == "spec-sheet" and s.get("url") for s in srcs):
            errs.append("dimensions marked verified but no spec-sheet source with a URL")
        if None in (d.get("w_in"), d.get("d_in"), d.get("h_in")):
            errs.append("dimensions marked verified but a W/D/H value is missing")
    if rec.get("id") and rec["id"] != f.stem:
        errs.append(f"id '{rec['id']}' does not match filename '{f.stem}'")
    if errs:
        bad += 1
        print(f"FAIL {f.name}"); [print(f"   - {e}") for e in errs]
    else:
        print(f"ok   {f.name}")
sys.exit(1 if bad else 0)
