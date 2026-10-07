---
name: render
description: Render a bound module through an adapter (trainual, synthesia, scorm, live, print) into exports/, with a guided publish checklist.
---

# Render

Usage: `/render MOD-ID <adapter>`

1. Confirm the module is `bound`. Refuse otherwise, unless Brandon asks for a draft render for the capability tour.
2. Run `/refresh-capabilities <platform>` if the adapter's `verified` dates are older than 60 days.
3. Follow the adapter file in `adapters/`:
   - `trainual`: write `exports/ID/trainual/publish-guide.md` (subject, documents, pages to paste, test items formatted per question type with settings, checklist items, embeds to place, SCORM zips to upload, e-signature items) in the order they are entered.
   - `scorm`: `python scripts/build_scorm.py <folder>`.
   - `synthesia`: one scene list per video; visual direction goes through the Design Translating Team first (load 01, 02, and 03 from the cache).
   - `live` or `print`: per `adapters/live-and-print.md`; print layout through 04 Editorial & Layout Specialist.
4. Any prompt for an AI design or video tool runs through the Design Translating Team before it is used. No exceptions.
5. Set status `rendered`. After Brandon publishes, record the link in `module.md`, export a frozen snapshot to Box, and set `published`.

Commit: `ID rendered: <adapter>`.
