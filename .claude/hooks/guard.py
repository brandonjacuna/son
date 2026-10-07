#!/usr/bin/env python3
"""PreToolUse guard for Sŏn build-out work.

Works in two layouts:
  - standalone son-build repo: PHASE.yaml at the repo root
  - unified son repo: PHASE.yaml under company/workstreams/build-out/ (or $SON_BUILD_DIR)
`.claude/` always sits at the repo root.

Rules:
1. Blocks writes into build-out phase folders that PHASE.yaml has not unlocked.
2. Blocks edits to PHASE.yaml, the phase script, hooks, settings, and hook state
   unless Brandon typed an unlock phrase in the last 10 minutes (see prompt_hook.py).
3. ClickUp: denies deletes and merges everywhere. Allows task creation on capture
   lists in clickup/allowlist.yaml. Asks Brandon before any other ClickUp write only
   during build-out work (decision M1, 2026-10-07): the session has read or written
   build-out files, or its cwd is inside the build-out root, or the call names a
   guarded build-out ID from clickup/allowlist.yaml. Elsewhere, normal permissions apply.
4. Settings: edits to .claude/settings.json that change the hooks block need an unlock
   phrase; other settings edits ask Brandon (decision M4, 2026-10-07).

Exit code 2 = block (stderr goes back to Claude). JSON on stdout = permission decision.
"""
import json, os, re, sys, time
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", Path(__file__).resolve().parents[2]))
UNLOCK = ROOT / ".claude/state/phase_unlock"
UNLOCK_TTL = 600  # seconds

def find_build_root():
    cands = []
    if os.environ.get("SON_BUILD_DIR"):
        cands.append(ROOT / os.environ["SON_BUILD_DIR"])
    cands += [ROOT, ROOT / "company/workstreams/build-out"]
    for c in cands:
        if (c / "PHASE.yaml").exists():
            return c
    return None

BUILD = find_build_root()

def phase_state():
    txt = (BUILD / "PHASE.yaml").read_text()
    cur = re.search(r"^current_phase:\s*(\S+)", txt, re.M).group(1)
    order = re.findall(r"^\s*-\s*(P\d-[\w-]+)", txt, re.M)
    return cur, order

def unlocked():
    return UNLOCK.exists() and time.time() - UNLOCK.stat().st_mtime < UNLOCK_TTL

def block(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)

def decide(decision, reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason}}))
    sys.exit(0)

ROOT_PROTECTED = [".claude/hooks/", ".claude/state/"]
SETTINGS = ".claude/settings.json"
STATE = ROOT / ".claude/state"
BUILD_PROTECTED = ["PHASE.yaml", "scripts/advance_phase.py"]

def rel_to(base, p):
    try:
        return str(Path(p).resolve().relative_to(base.resolve()))
    except ValueError:
        return None

def mark_buildout(session_id):
    if session_id:
        try:
            STATE.mkdir(parents=True, exist_ok=True)
            (STATE / f"buildout_session_{re.sub(r'[^A-Za-z0-9_-]', '', session_id)}").touch()
        except OSError:
            pass

def in_buildout_session(session_id):
    return bool(session_id) and (STATE / f"buildout_session_{re.sub(r'[^A-Za-z0-9_-]', '', session_id)}").exists()

def hooks_block(text):
    try:
        return json.loads(text).get("hooks")
    except (ValueError, AttributeError):
        return "unparseable"

def check_settings(tool, ti):
    path = ROOT / SETTINGS
    cur = path.read_text() if path.exists() else "{}"
    if tool == "Write":
        new = ti.get("content", "")
    else:
        new = cur
        edits = ti.get("edits") or [ti]
        for e in edits:
            old, rep = e.get("old_string", ""), e.get("new_string", "")
            new = new.replace(old, rep) if e.get("replace_all") else new.replace(old, rep, 1)
    if hooks_block(new) != hooks_block(cur) and not unlocked():
        block("That edit changes the hooks block in .claude/settings.json, which enforces the phase lock. It needs Brandon's unlock phrase.")
    decide("ask", "Settings change outside the hooks block. Confirm with Brandon.")

def check_path(p, tool="", ti=None, session_id=""):
    rel_root = rel_to(ROOT, p)
    if rel_root is None:
        return  # outside the repo
    if BUILD is not None and rel_to(BUILD, p) is not None:
        mark_buildout(session_id)
    if tool == "Read":
        return
    if rel_root == SETTINGS:
        check_settings(tool, ti or {})
    if any(rel_root == x or rel_root.startswith(x) for x in ROOT_PROTECTED) and not unlocked():
        block(f"{rel_root} is protected. Hook and phase controls change only after Brandon types an unlock phrase.")
    if BUILD is None:
        return
    rel = rel_to(BUILD, p)
    if rel is None:
        return  # not build-out work
    if rel in BUILD_PROTECTED and not unlocked():
        block(f"{rel} is protected. Phase changes happen only through Brandon's /lease-signed or /gate flow.")
    cur, order = phase_state()
    m = re.match(r"phases/(P\d-[\w-]+)/", rel + "/")
    if m and m.group(1) in order and cur in order and order.index(m.group(1)) > order.index(cur):
        block(f"{m.group(1)} is locked. Current build-out phase is {cur}. Write this under phases/{cur}/ instead.")

def check_bash(cmd):
    readonly = re.match(r"\s*(ls|cat|head|tail|grep|rg|find|git (log|diff|status|show)|wc|stat)\b", cmd)
    touches_protected = any(x in cmd for x in ["PHASE.yaml", ".claude/state", ".claude/hooks", "advance_phase"])
    if touches_protected and not readonly and not unlocked():
        block("That command touches phase or hook controls. Only Brandon's /lease-signed or /gate flow can do this.")
    if BUILD is None:
        return
    cur, order = phase_state()
    for ph in order:
        if f"phases/{ph}" in cmd and order.index(ph) > order.index(cur) and not readonly:
            block(f"{ph} is locked (current build-out phase {cur}).")

def check_clickup(tool, tinput, session_id="", cwd=""):
    name = tool.lower()
    if not re.search(r"(create|update|delete|move|merge|add|remove|attach|send|start|stop|execute)", name):
        return  # reads are fine
    if "delete" in name or "merge" in name:
        block("ClickUp deletes and merges are never done by Claude. Hand this to Brandon.")
    allow_file = (BUILD / "clickup/allowlist.yaml") if BUILD else None
    allow = allow_file.read_text() if allow_file and allow_file.exists() else ""
    capture_ids = set(re.findall(r"list_id:\s*\"?(\d+)", allow))
    guarded_ids = set(re.findall(r"^\s*-\s*\"?(\d+)\"?\s*(?:#.*)?$", allow.split("guarded_ids:", 1)[1], re.M)) if "guarded_ids:" in allow else set()
    list_id = str(tinput.get("list_id", ""))
    if "create_task" in name and list_id in capture_ids:
        decide("allow", "Capture list write, allowed in every phase.")
    blob = json.dumps(tinput)
    buildout = (in_buildout_session(session_id)
                or (BUILD is not None and cwd and rel_to(BUILD, cwd) is not None)
                or any(i in blob for i in guarded_ids))
    if buildout:
        decide("ask", f"ClickUp write ({tool}) during build-out work, outside a capture list. Confirm this is a real, committed task.")
    return  # not build-out work: normal permissions apply

def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name", "")
    ti = data.get("tool_input", {}) or {}
    sid = data.get("session_id", "")
    cwd = data.get("cwd", "")
    if tool in ("Read", "Write", "Edit", "MultiEdit", "NotebookEdit"):
        check_path(ti.get("file_path") or ti.get("notebook_path") or "", tool, ti, sid)
    elif tool == "Bash":
        check_bash(ti.get("command", ""))
    elif re.search(r"click_?up", tool, re.I):
        check_clickup(tool, ti, sid, cwd)
    sys.exit(0)

if __name__ == "__main__":
    main()
