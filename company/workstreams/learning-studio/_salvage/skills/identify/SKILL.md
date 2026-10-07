---
name: identify
description: Intake a training need, run the front-end check (is instruction even the lever), and add it to the catalog. Also used to confirm or reject the seed rows in the catalog.
---

# Identify

Load: Instructional Designer, Hospitality Operations Realist, Frontline Advocate (from `profiles/cache/`; run `/sync-profiles` if missing).

1. Ask Brandon for the observed gap in behavior, not a topic. If he gives a topic, ask what people are doing or not doing on the floor.
2. Pull what the white paper (canon) and the Brand Guidelines already hold; V7 Part II (ClickUp `2ky45bmy-11873`, page `2ky45bmy-30273`) may be read as background only, not canon on this, so the need is not re-derived from scratch.
3. Run the front-end check in the Instructional Designer's voice: knowledge or skill gap, or tools, conditions, tempo, motivation? Run the Operations Realist's tempo read. Get the Frontline Advocate's read on how the team experiences the gap.
4. Fill `templates/00-intake.md` into `catalog/intake/<ID>-<slug>.md`.
5. If the verdict is instruction: add a catalog row with `status: identified`, `confirmed: true`. If routed out: add the row as `routed-out` with where it went.
6. For seed rows: ask Brandon to confirm, edit, or reject each. Set `confirmed: true` or delete the row.

Commit: `ID identified: <need>`.
