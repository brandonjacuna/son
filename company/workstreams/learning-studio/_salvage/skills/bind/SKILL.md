---
name: bind
description: Fill bindings once a tool, workflow, menu, role, or founder decision is set. Takes a module ID or a binding key or prefix (for example tool.pos) and fills every module that depends on it.
---

# Bind

1. Run `python scripts/status.py bindings` and read `bindings/registry.md`.
2. Scope: a module ID fills that module's bindings; a key or prefix fills that key across every module.
3. For each binding, get the value from its proper source only:
   - `fact.*` financial figures from the current Investor Review workbook in Box (Sŏn / 02. Capital Raise); operational figures stay unbound until a source is chosen. Never estimate.
   - `brand.*` from the Brand Guidelines.
   - `chef.*` from the chef, confirmed in writing.
   - `founder.*` and `people.*` from Brandon.
   - `tool.*` and `workflow.*` from the owner of that tool or SOP.
4. Write `value`, `source`, `status: filled` in each `bindings.yaml`.
5. Re-read each affected module: does the filled value change any durable content (for example, the tool makes a step easier and the job aid should shrink)? If so, that module goes back to `designed` for a quick pass.
6. Modules with no open bindings move to `bound`.

Commit: `bind <key or ID>: <n> modules`.
