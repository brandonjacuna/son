---
name: intake
description: Use whenever Brandon drops in a photo, sketch, marked-up photo or drawing, spec sheet, contract, or a rough idea he wants designed. Triage first, then clarify, then file. Never start modeling from raw intake.
---
# Intake

## Steps
1. **Collect.** Files attached in chat, anything in `intake/inbox/`, or items Brandon names in Box `…/04. Property and Build-Out/_Intake`.
2. **Triage.** Delegate to the `intake-triage` subagent (Haiku). It returns one card per file. Do not read large images yourself if the subagent can.
3. **Clarify.** Run the `interview` skill on each card with unresolved items. One question at a time.
4. **File.** Save the confirmed card to `intake/processed/YYYY-MM-DD-<slug>.md`, move the original out of `inbox/` into `intake/processed/originals/` (LFS), and link it from the right place:
   - equipment spec → `equipment-record` skill
   - design markup → the matching `phases/P0-concept/<area>/` folder
   - contract or quote → Box, with a pointer line in `decisions/open.md` if it raises a question
5. **Close.** One-line summary per item: what it was, where it went, what is still open.

## Card format
```
# <slug>
type: site-photo | markup-photo | hand-sketch | markup-design | spec-sheet | contract | idea
area: bar | kitchen | live-fire | mep | lighting | av-network | storage | water | other
phase: P0-concept
source: <chat attachment | inbox path | Box id>
dimensions:
  - {what: "...", value: "...", status: measured | read-from-drawing | estimated | unknown}
annotations: ["verbatim text from the markup"]
brandon_intent: <filled in by interview, in his words>
open_questions: []
```
