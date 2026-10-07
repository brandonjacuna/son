#!/usr/bin/env python3
"""UserPromptSubmit hook.
- Injects a one-line build-out phase banner so every turn knows the phase.
- If Brandon's own prompt contains an unlock phrase, opens a 10-minute window
  for phase-control edits. Claude cannot trigger this: only a typed prompt can.
Works standalone (PHASE.yaml at repo root) or in the unified son repo
(PHASE.yaml under company/workstreams/build-out/ or $SON_BUILD_DIR).
"""
import json, os, re, sys, time
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", Path(__file__).resolve().parents[2]))
PHRASES = ("LEASE SIGNED CONFIRMED", "GATE CONFIRMED", "PHASE CONTROLS UNLOCK")

def find_build_root():
    cands = [ROOT / os.environ["SON_BUILD_DIR"]] if os.environ.get("SON_BUILD_DIR") else []
    cands += [ROOT, ROOT / "company/workstreams/build-out"]
    return next((c for c in cands if (c / "PHASE.yaml").exists()), None)

data = json.load(sys.stdin)
prompt = data.get("prompt", "")

if any(p in prompt for p in PHRASES):
    state = ROOT / ".claude/state"
    state.mkdir(parents=True, exist_ok=True)
    (state / "phase_unlock").write_text(str(time.time()))
    print("[phase controls unlocked for 10 minutes by Brandon's confirmation phrase]")

build = find_build_root()
if build:
    txt = (build / "PHASE.yaml").read_text()
    cur = re.search(r"^current_phase:\s*(\S+)", txt, re.M).group(1)
    lease = re.search(r"^lease_signed:\s*(\S+)", txt, re.M).group(1)
    print(f"[build-out phase: {cur} | lease_signed: {lease}]")
