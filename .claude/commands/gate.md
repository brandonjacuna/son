---
description: Run a phase gate review (P1 to P2, P2 to P3, P3 to P4). Brandon only.
disable-model-invocation: true
model: opus
argument-hint: <target phase, e.g. P2-permitting>
---
Gate review toward $ARGUMENTS.

1. Read PHASE.yaml and the entry criteria in `decisions/0001-architecture.md` (Phase table).
2. Check each criterion against evidence in the repo and Box. Write `decisions/gate-$ARGUMENTS.md` with a pass/fail table and the evidence for each row.
3. If anything fails, stop and list what is missing. Nothing changes.
4. If all pass, tell Brandon: "To advance, type exactly: GATE CONFIRMED". After he types it, run `python3 scripts/advance_phase.py --to $ARGUMENTS --evidence "<key evidence>" --note "<summary>"`.
5. List any ClickUp tasks the new phase requires and ask before creating them.
