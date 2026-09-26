# Adapter: SCORM (tracked rich interactions)

SCORM is how a rich interaction runs inside Trainual and still reports completion. Trainual accepts SCORM 1.2 and 2004 zips (verified 2026-09-26). Any tool that exports SCORM, or this repo itself, can produce one. That keeps the studio free of any single authoring tool.

## Route 1: the repo's scenario player (built in, no extra tool)

`python scripts/build_scorm.py modules/<domain>/<module>` reads the module's `scenarios.md`, converts it to data, wraps it in a self-contained HTML player, and writes a SCORM 1.2 zip to `exports/<ID>/scorm/`.

What it reports to the LMS: `completed` when the learner reaches any end node, a score from 0 to 100 based on the end reached (strong 100, recoverable 70, failure 0), and `passed` or `failed` against the mastery score in `module.md` (default 70). Whether Trainual displays the score as well as completion is a question for the capability tour; completion is confirmed.

What it supports now: branching choices, consequence and feedback screens, the expert rationale reveal, optional image or video URL per node (for Synthesia clips or real footage), and a restart. Built to extend: add a node type in `scorm/player/player.js` and the parser in `scripts/build_scorm.py`.

Test any build before upload with a free SCORM test harness (for example SCORM Cloud's free tier), then in the Trainual sandbox.

## Route 2: H5P via Lumi (free, open source, wide variety)

H5P is an open-source library of interaction types: interactive video, branching scenario, drag and drop, drag the words, image hotspots, find the hotspot, image juxtaposition, dialog cards, flashcards, sort the paragraphs, timelines, course presentations, and more. Lumi is a free desktop editor for H5P that exports a SCORM package, a single HTML file, or an `.h5p` file.

- For **tracked** use: export SCORM from Lumi, upload to Trainual.
- For **untracked** practice: export HTML, host it, embed with an iframe.
- Store the `.h5p` source file in the module folder under `media/` so it stays editable. The SCORM export goes to `exports/`, not git.

Not every H5P type behaves perfectly inside every SCORM wrapper. Test each type in the sandbox once and note results in `adapters/trainual-tour-log.md`.

## Route 3: commercial authoring tools

Articulate Rise and Storyline, iSpring, Colossyan, Genially (paid tiers), and similar tools export SCORM. None is needed today. If one is adopted later, it becomes another adapter here, and the module source package stays the source of truth.

## Choosing a route

| Need | Route |
|---|---|
| Branching judgment scenario, tracked | 1 (repo player) |
| Drag and drop, hotspot, sort, flashcards, interactive video with questions | 2 (H5P via Lumi) |
| Polished course with custom layout, and budget for a tool | 3 |
| Quick practice, no record needed | 2 as HTML embed |
