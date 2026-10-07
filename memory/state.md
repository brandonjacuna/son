# State (in flight)

Rewrite freely. One line per item: what | owner | next step. Plan and phase briefs: `memory/plan.md`, `memory/briefs/`.

## Now
- Phase 1 Cleanup, session B | next Code session (Opus) | `memory/briefs/1-cleanup.md` steps 4 to 6 and 8: Box batches, ClickUp delete list, brand canon extraction as pop-ups, V7 question. Session A is done (reports: `memory/audits/cleanup-sweep/`; allowlist: `memory/audits/cleanup-allowlist.md`)
- Old `son-build` name in the root guard script docstring (line 5) | Brandon | needs the unlock phrase; one-word comment fix, then drop its allowlist entry
- Cloud environment for `son` | Brandon | paste `scripts/setup_cloud.sh` into the environment setup; check ClickUp and Box connectors
- Five data API keys (FRED, BLS, Socrata, Census, EIA) | Brandon | before nerve switches on in phase 5
- Archive the old GitHub repos (son-learning-studio, son-operational-buildout, son-nerve; make agenticproject private and archive) | Brandon to confirm | everything from them is in `son`
- Delete `~/Desktop/son-imports/_transfer` and the zips on the Desktop | Brandon, any time | originals are in the repo

## Done 2026-10-07
- Phase 1 session A: repo sweep (5 Sonnet agents, about 200 rewrites); raw exports deleted (clickup-system/exports, operations/archive, uncited extraction); cited extraction kept in operations/sources/extraction; old learning-studio clones deleted after salvaging their tooling to learning-studio/_salvage (inert); stale routing rewritten in operations, learning-studio, nerve, build-out, clickup-system; raise working files marked superseded; allowlist built
- Pull request #1 merged (Brandon): build-out workspace, phase lock hooks, skills, commands, and workflows are live on `main`; guard self-test 22/22
- Profile baseline imported from Box zip: 52 profiles in `profiles/_source/` and `founders/profiles/_source/`, 7 investment working files in `founders/capital-raise/working-files/` (phase 3 step 2 done)
- Community skills research done; approved list and install schedule in `memory/skills-plan.md`
- Rebuild intake; repo `son` created and pushed with history from every source (learning-studio from unmerged branch claude/blissful-einstein; nerve from unmerged PR branch claude/bold-goldberg; operations; design-system; local profile builds; ClickUp system; Espresso Chiller; Claude Science matcha and cryo espresso; construction workspace on PR #1)
- Build-out migration decisions M1, M2, M4 applied on PR #1
- Founder-only manual chunks and the old OA brief moved to `founders/`; Home Base facts ported to `founders/context.md` and `memory/context.md`
- Account memory cleaned and Project instructions replaced (Brandon)
- Workstream readiness audit: `memory/audits/2026-10-07-readiness.md`

## Live automation outside the repo
- Wednesday restaurant tech digest (scheduled task trig_01EUH167wrsReHWDvt5Sv7vG; prompt in `prompts/scheduled/weekly-tech-digest.md`)
- ClickUp Meetings Agent v3: Monday 7 AM roll-forward, day-before reminders, close-out; checkpoints Oct 8, 12, 13 (`company/workstreams/clickup-system/STATE.md`)

## Open questions for Brandon
- Brand canon line: which Korean cultural tie-ins go (phase 1, shown section by section first)
- Is the V7 Business Strategies Notebook (ClickUp 2ky45bmy-11873) still canon? (phase 1)
- Operational figures (pars, labor targets, pay, schedules, counts) have no source since Airtable retired; learning-studio marks them unbound (phase 5)
- build-out/HANDOFF.md: delete now that the migration is done? (phase 5)
- Build-out migration still open: M3 profile pipeline (phase 3), M5 command names (phase 4), M6 build-out kb location (phase 5)
