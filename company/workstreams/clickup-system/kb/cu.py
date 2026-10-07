"""Tiny ClickUp REST helper. Token is never printed or written to disk.

Token source, in order:
  1. CLICKUP_API_TOKEN environment variable (cloud sessions, injected at runtime)
  2. macOS Keychain item "clickup-api-token" (Brandon's Mac)
The token is read on first use, so importing this file never fails.
"""
import json, os, subprocess, urllib.request, urllib.error, time
WID = "90131574430"
_T = None

def _token():
    global _T
    if _T:
        return _T
    _T = os.environ.get("CLICKUP_API_TOKEN", "").strip()
    if not _T:
        _T = subprocess.run(["security", "find-generic-password", "-s", "clickup-api-token", "-w"],
                            capture_output=True, text=True, check=True).stdout.strip()
    return _T

def req(method, path, body=None, v=2):
    base = f"https://api.clickup.com/api/v{v}/"
    for _ in range(5):
        r = urllib.request.Request(base + path, method=method,
            headers={"Authorization": _token(), "Content-Type": "application/json"},
            data=json.dumps(body).encode() if body is not None else None)
        try:
            with urllib.request.urlopen(r, timeout=60) as resp:
                txt = resp.read(); return json.loads(txt) if txt else {}
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(15); continue
            raise RuntimeError(f"{method} {path} -> {e.code} {e.read()[:300]!r}")

def tasks(list_id, closed=True):
    out, p = [], 0
    while True:
        d = req("GET", f"list/{list_id}/task?include_closed={'true' if closed else 'false'}&subtasks=true&page={p}")
        out += d.get("tasks", [])
        if d.get("last_page", True) or not d.get("tasks"): return out
        p += 1
