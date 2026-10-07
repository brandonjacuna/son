---
description: Advance from P0 concept to P1 design after the lease is signed. Brandon only.
disable-model-invocation: true
model: opus
---
Brandon says the lease is signed. Run this gate carefully. Never skip a step.

1. Use AskUserQuestion, one question at a time:
   - "Is the lease fully executed by both parties?" options: "Yes, fully executed" / "Signed by us only" / "Not yet".
   - "Is the executed lease uploaded to Box?" options: "Yes, I have the file ID" / "Not yet".
   Stop if any answer is not the first option. Nothing changes.
2. Ask Brandon for the Box file ID of the executed lease. Confirm it with the Box connector if available (file exists, name looks like a lease).
3. Tell Brandon: "To unlock the phase change, type exactly: LEASE SIGNED CONFIRMED". Wait for his next message.
4. After he types it, run: `python3 scripts/advance_phase.py --to P1-design --evidence "Box <id> executed lease" --note "<his words>"`.
5. Then, in order, and asking before each:
   a. Run `/gate` style review of P0: list which concept designs are ready to promote into `phases/P1-design/`, which are superseded, and what open decisions carry forward.
   b. Snapshot `kb/` into `phases/P1-design/kb-baseline/` for the architect and MEP engineer.
   c. Propose the ClickUp construction space from `clickup/space-blueprint.md` as a preview file, get sign-off, build it using the rules in `company/workstreams/clickup-system/kb/clickup-knowledge-base.md` (shared ClickUp knowledge base), then read everything back to verify.
6. Summarize what changed in five lines or fewer.
