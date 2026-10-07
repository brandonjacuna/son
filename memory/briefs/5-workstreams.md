# Phase 5: Workstream builds

## Goal
Every workstream is work-ready (real work can start today) or at least sandbox-ready (Brandon can play on a `sandbox/<name>` branch, including revising the workstream's own system). Each has a CLAUDE.md, a start-here, passing checks, and its scheduled jobs live.

Evidence and step lists for each: `memory/audits/2026-10-07-readiness.md`.

## Order
1. **Operations (Scaling People): work-ready now.** Polish: update its CLAUDE.md for the unified repo (repo name, Mac-only token note, profile paths after phase 3); fix `.gitignore` entries for profile folders that are not in the repo; note that founder-only chunks now live in `founders/operations-manual/`.
2. **ClickUp system: live.** Add a CLAUDE.md pointing to STATE, DECISIONS, kb; confirm the Meetings Agent v3 checkpoints (Oct 8 standup, Oct 12 roll-forward, Oct 13 meeting) passed.
3. **Nerve: built, never switched on.** Install deps and run tests; Brandon's five API keys into the environment; run R1 and R2 by hand; fix routine paths for the `son` repo; create the three scheduled tasks (R1 daily, R2 Sunday, R3 Monday digest to ClickUp and Box); publish the draft digest; save the prompts in `prompts/scheduled/`.
4. **Science: reference, paused.** Add a CLAUDE.md with the "no bench data yet" caveat; reconcile the chiller fabrication handoff (Eversys Enigma, two coils) with the model (La Marzocco Strada X, three coils); dedupe `cryo-espresso/05_equipment_design` against `espresso-chiller`; fix folder names and the Mac path. Next real step is a bench test plan (`cryo-espresso/06_test_program`).
5. **Design system: built, never deployed.** Apply the brand canon line from phase 1; codename copy pass (Good Energy, Dosi, Luxx are internal only); `npm install && npm run lint`; register its `SKILL.md` if wanted; consider moving the 126 MB `refs/` to Box. Deployment items owed to Dominic (endpoint, regeneration, Vercel).
6. **Learning studio: mid-build.** Restore its 13 skills, lint workflow, and a trimmed `.mcp.json` (no Airtable) from `imports/profile-builds-local/`; bind it to the phase 3 agents; export the Module Review decisions from the artifact into the repo; reconcile the catalog with the position-path modules; then delete `imports/profile-builds-local/`.
7. **Build-out: ready to build.** Run its KICKOFF.md: live hook test, capture list IDs, import the nine ClickUp build-out guides without figures, Box subfolders (ask first), bar sandbox interview; build bar-designer and the first specialists from phase 3; resolve open decision M6 (knowledge base location).

## Approved external skills to use here
See `memory/skills-plan.md`: build123d-mcp (build-out), id-skills-for-claude and education rubrics (learning studio), cowork-sop-writer and knowledge-ops (operations), Anthropic Operations, HR, Legal, Design tested ad hoc. Vet each before install.

## Done when
Each workstream passes its own done line above, and `memory/state.md` lists each as work-ready or sandbox-ready.

## Red team
Standard; harsh for anything compliance, code, or employee-facing (codes register in build-out, training content touching policy).
