---
description: Promote a sandbox design to canonical (main) through a pull request.
argument-hint: <optional summary>
model: sonnet
---
1. Confirm the current branch starts with `sandbox/`. If not, stop.
2. Regenerate exports from `models/src/` and run `python3 scripts/validate_equipment.py`. Fix failures before continuing.
3. Summarize what changed versus main: layout moves, equipment added or removed, utility impacts (power, water, drain, gas, exhaust). Flag any clash.
4. Ask Brandon with AskUserQuestion: "Promote this to canonical?" options: "Promote" / "Keep iterating" / "Archive this sandbox".
5. On Promote: push and open a PR to main with the summary. On Archive: add a line to `decisions/open.md` noting what was learned, then leave the branch.
