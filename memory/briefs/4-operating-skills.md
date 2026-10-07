# Phase 4: Operating skills

## Goal
The repeatable procedures Brandon relies on exist as skills, so every session does them the same way.

## Work
1. **`task-tree`.** Builds ClickUp work in Brandon's shape: parent = the outcome; second level = phases (A, B, C...); third level = every action item, numbered (A1, A2...) and prefixed by kind (FRAME, DECIDE, CONFIRM, FLAG, ACTION, GENERATE, SIGN). Reference example: [Finalize Founders Operating Agreement](https://app.clickup.com/t/86aknm6zc). Uses the shared ClickUp knowledge base and helper in `company/workstreams/clickup-system/`.
2. **`kb-refresh` plus a weekly scheduled task.** Scans `kb/` and workstream knowledge files for `review_every` / `last_verified` frontmatter; checks changelogs and primary sources for anything overdue; opens a pull request Brandon approves from his phone. Cadences: tools (ClickUp, Claude products, Box, Trainual) weekly; law and compliance monthly; pedagogy quarterly. Covers knowledge of Claude itself (Code, Design, Science, chat), ClickUp, Box.
3. **`decide` (walk mode).** Standard for decision pop-ups: one decision per question, full context to answer cold, options that include what Brandon does not want, recommended option first, and a read-back before recording.
4. **`scheduled-sync`.** Keeps `prompts/scheduled/*.md` and the live scheduled tasks identical; flags drift (model versions, UTC versus Central time shifts at daylight saving changes).
5. **ClickUp knowledge base merge.** Done in phase 1 (2026-10-07): the build-out copy held nothing unique and was deleted; `kb/cu.py` deleted, `scripts/cu.py` kept.
6. **Build-out open decision M5.** Resolve any command and skill name collisions.

## Done when
Skills exist and are each used once in a real session; the weekly knowledge refresh task is live and its prompt is in `prompts/scheduled/`.

## Red team
Standard.
