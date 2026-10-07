# Stage 4: Red team, then Fable judgment

1. If `.claude/skills/red-team/` exists, run it on the master at the frame's intensity, with these lenses added. If it does not exist yet, run the interim procedure below.
2. Interim procedure: spawn these critics in one message, all `model: sonnet`, each with the brief "Read `.claude/skills/profile-build/workers/critic.md` and follow it. Build: <folder>. Master: <path>. Lens: <lens>." Light intensity runs lenses 1 and 2 only.
   1. `grounding`: every `sourced` row in provenance is supported by the cited card row; every `inferred` row follows from what it names.
   2. `specificity`: rules and cues a generalist would give anyway; credential or identity inflation; survey material in the core.
   3. `seams`: overlaps and gaps with each neighbor named in the frame (reads the neighbors' `agent.md` or old profile scope sections only).
   4. `rules`: standing rules (CLAUDE.md), scope exclusions, lineage reconstruction, retired tools, figures written as fact.
   Harsh intensity: add lens 5 `employee-harm` (anything that could reach an employee as an unfair gate, a discipline trigger, or a legal exposure) and run every lens twice, blind to each other; keep a flag only if both runs raise it or one run shows a verified failure path.
3. Each critic writes `04-critic-<lens>.md` and returns one line. One Sonnet merger reads them and writes `04-flags.md` (4 KB cap, deduplicated): `id | severity (critical, major, minor) | lens | flag | evidence | proposed edit`. You read only `04-flags.md`.
4. Final judgment: spawn one Fable subagent (`model: fable`) with only `00-frame.md`, `04-flags.md`, `agent.md`, and `skill/SKILL.md` if any. Brief: "For each flag: accept (with the exact edit), reject (one reason), or ask Brandon (one question). Then one line: does this seat do the frame's job? Return the decisions table only."
5. Apply accepted edits yourself as Edits to the named rows; update provenance rows the edits touch. Ask Brandon the "ask" items by pop-up. A clean result is a normal outcome; do not invent flags.
6. Log tokens in `BUILD.md`.
