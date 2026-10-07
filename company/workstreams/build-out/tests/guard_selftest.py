#!/usr/bin/env python3
"""Read-only self-test of the build-out guard hook. Feeds sample tool calls to
.claude/hooks/guard.py and checks each decision. Writes nothing.

Run from anywhere inside the repo:  python3 <build-out root>/tests/guard_selftest.py
Requires: no unlock window open (do not run right after typing an unlock phrase).
"""
import json, os, subprocess, sys
from pathlib import Path

BUILD = Path(__file__).resolve().parents[1]
r = subprocess.run(["git", "-C", str(BUILD), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or (r.stdout.strip() if r.returncode == 0 else BUILD))
GUARD = ROOT / ".claude/hooks/guard.py"
env = dict(os.environ, CLAUDE_PROJECT_DIR=str(ROOT))

def run(event):
    p = subprocess.run([sys.executable, str(GUARD)], input=json.dumps(event), capture_output=True, text=True, env=env)
    if p.returncode == 2:
        return "block"
    if p.stdout.strip():
        return json.loads(p.stdout)["hookSpecificOutput"]["permissionDecision"]
    return "allow"

def w(path):  # write event for a path under the build-out root
    return {"tool_name": "Write", "tool_input": {"file_path": str(BUILD / path)}}

cases = [
    ("write P0 concept file", w("phases/P0-concept/bar/x.md"), "allow"),
    ("write kb file", w("kb/bar/x.md"), "allow"),
    ("write locked P1 folder", w("phases/P1-design/x.md"), "block"),
    ("write locked P3 folder", w("phases/P3-construction/x.md"), "block"),
    ("edit PHASE.yaml", {"tool_name": "Edit", "tool_input": {"file_path": str(BUILD / "PHASE.yaml")}}, "block"),
    ("edit advance script", w("scripts/advance_phase.py"), "block"),
    ("edit hook", {"tool_name": "Edit", "tool_input": {"file_path": str(ROOT / ".claude/hooks/guard.py")}}, "block"),
    ("edit settings.json", {"tool_name": "Edit", "tool_input": {"file_path": str(ROOT / ".claude/settings.json")}}, "block"),
    ("bash run advance script", {"tool_name": "Bash", "tool_input": {"command": "python3 scripts/advance_phase.py --to P1-design --evidence x --note y"}}, "block"),
    ("bash read PHASE.yaml", {"tool_name": "Bash", "tool_input": {"command": "cat PHASE.yaml"}}, "allow"),
    ("bash touch P2 folder", {"tool_name": "Bash", "tool_input": {"command": "touch phases/P2-permitting/x"}}, "block"),
    ("clickup read", {"tool_name": "mcp__ClickUp__clickup_get_task", "tool_input": {}}, "allow"),
    ("clickup create on capture list", {"tool_name": "mcp__ClickUp__clickup_create_task", "tool_input": {"list_id": "901327291277"}}, "allow"),
    ("clickup create elsewhere", {"tool_name": "mcp__ClickUp__clickup_create_task", "tool_input": {"list_id": "123"}}, "ask"),
    ("clickup create doc", {"tool_name": "mcp__ClickUp__clickup_create_document", "tool_input": {}}, "ask"),
    ("clickup delete", {"tool_name": "mcp__ClickUp__clickup_delete_task", "tool_input": {}}, "block"),
    ("clickup merge", {"tool_name": "mcp__ClickUp__clickup_merge_tasks", "tool_input": {}}, "block"),
]
fails = 0
for name, ev, want in cases:
    got = run(ev)
    ok = got == want
    fails += not ok
    print(f"{'ok  ' if ok else 'FAIL'} {name}: got {got}, want {want}")
print(f"\nbuild-out root: {BUILD}\nrepo root: {ROOT}\n{len(cases)-fails}/{len(cases)} passed")
sys.exit(1 if fails else 0)
