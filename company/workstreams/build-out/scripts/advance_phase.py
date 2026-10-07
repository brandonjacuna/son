#!/usr/bin/env python3
"""Advance PHASE.yaml by exactly one phase. Only works inside the 10-minute unlock
window that opens when Brandon types a confirmation phrase.

Works standalone (this script at <repo>/scripts/) or in the unified son repo
(this script at <repo>/company/workstreams/build-out/scripts/). The unlock file always lives
at <repo root>/.claude/state/phase_unlock.

Usage:
  python3 scripts/advance_phase.py --to P1-design --evidence "Box file 123456 (executed lease)" --note "Lease signed 2026-11-02"
"""
import argparse, os, re, subprocess, sys, time, datetime
from pathlib import Path

BUILD = Path(__file__).resolve().parents[1]

def repo_root():
    if os.environ.get("CLAUDE_PROJECT_DIR"):
        return Path(os.environ["CLAUDE_PROJECT_DIR"])
    r = subprocess.run(["git", "-C", str(BUILD), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip() else BUILD

UNLOCK = repo_root() / ".claude/state/phase_unlock"

ap = argparse.ArgumentParser()
ap.add_argument("--to", required=True)
ap.add_argument("--evidence", required=True, help="Box file ID or document proving the gate")
ap.add_argument("--note", required=True)
a = ap.parse_args()

if not (UNLOCK.exists() and time.time() - UNLOCK.stat().st_mtime < 600):
    sys.exit("Refused: no confirmation phrase from Brandon in the last 10 minutes.")

p = BUILD / "PHASE.yaml"
txt = p.read_text()
cur = re.search(r"^current_phase:\s*(\S+)", txt, re.M).group(1)
order = re.findall(r"^\s*-\s*(P\d-[\w-]+)", txt, re.M)
if a.to not in order or order.index(a.to) != order.index(cur) + 1:
    nxt = order[order.index(cur) + 1] if order.index(cur) + 1 < len(order) else "none"
    sys.exit(f"Refused: can only advance one step, from {cur} to {nxt}.")

today = datetime.date.today().isoformat()
txt = re.sub(r"^current_phase:.*$", f"current_phase: {a.to}", txt, flags=re.M)
if a.to == "P1-design":
    txt = re.sub(r"^lease_signed:.*$", "lease_signed: true", txt, flags=re.M)
entry = f'  - {{date: "{today}", from: {cur}, to: {a.to}, evidence: "{a.evidence}", note: "{a.note}"}}'
txt = txt.replace("gate_log: []", "gate_log:\n" + entry) if "gate_log: []" in txt \
      else txt.rstrip() + "\n" + entry + "\n"
p.write_text(txt)
UNLOCK.unlink(missing_ok=True)
subprocess.run(["git", "-C", str(BUILD), "add", str(p)], check=False)
subprocess.run(["git", "-C", str(BUILD), "commit", "-m", f"Build-out phase gate: {cur} -> {a.to}. {a.note} [{a.evidence}]"], check=False)
print(f"Advanced {cur} -> {a.to}. Unlock window closed.")
