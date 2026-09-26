---
name: build-profile
description: Build a new specialist profile using stages 0 to 5 of the seven-stage synthesis procedure, working in profile-builds/<slug>/. Stage 6 and 7 run separately with /validate-profile in a fresh session.
---

# Build profile

Read the procedure from ClickUp (doc `2ky45bmy-16853`, page `2ky45bmy-27213`) at the start; it is the source of truth and may have changed. Read two existing profiles from the same cluster from the cache for format and seam conventions.

Work in `profile-builds/<slug>/`, one file per stage:

- `00-frame.md` Stage 0. One-sentence frame, template type, seams with existing seats. Already drafted for the two hospitality seats; confirm with Brandon before Stage 1.
- `01-corpus.md` Stage 1. 5 to 15 curated sources targeting the seat's judgment, not a survey of the field. If Brandon uses NotebookLM for grounding, record the notebook; otherwise run deep research and record sources with what each is used for.
- `02-elicit.md` Stage 2. Cue inventory, decision requirements table, if-then rules, anti-patterns, mental models, quoting sources.
- `03-consolidate.md` Stage 3. Themes, deduplicated, named, checked against sources.
- `04-draft.md` Stage 4. The typed XML template, in the house profile format.
- `05-tagged.md` Stage 5. Every claim tagged `[sourced]`, `[inferred]`, or `[project]`.

Rules: encode what the expert does, not who they are. No credential inflation. Standing rules baked into the project block. No lineage reconstruction. Stop after Stage 5 and tell Brandon to run `/validate-profile <slug>` in a new session.
