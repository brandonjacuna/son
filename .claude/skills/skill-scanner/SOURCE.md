# Source

- Repo: https://github.com/getsentry/skills (path `skills/skill-scanner`)
- Commit: d18b7aa8ba878354e5c348310230e652f7690f9c
- Vendored: 2026-10-07 (phase 2)
- License: Apache 2.0 (`LICENSE`, copied from the repo root)
- Scanner verdict on itself: 35 findings (23 critical, 11 high, 1 medium), all in the pattern tables of `scripts/scan_skill.py` and the example blocks in `references/`. Expected for a scanner: it documents attacks, it does not perform them. Manual read: `scan_skill.py` imports only base64, json, re, sys, pathlib, yaml; no network, subprocess, or file writes; prints JSON to stdout.
- Hooks: none. MCP servers: none. Writes outside its folder: none.
- Run without `uv`: `python3 -I .claude/skills/skill-scanner/scripts/scan_skill.py <skill-dir>` (needs pyyaml, already installed).

## Local edits
- `SKILL.md` line 109: rewrote the literal bang-backtick example as words, so the example cannot be read as a load-time command when the skill is invoked.
