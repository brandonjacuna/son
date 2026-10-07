# State (in flight)

Rewrite freely. One line per item: what | owner | next step. Plan and phase briefs: `memory/plan.md`, `memory/briefs/`.

## Now
- Phase 3 session B: test rebuild of the Practice and Simulation Designer with the new builder | next Code session (Opus orchestrator) | start a fresh session, then `/profile-build practice-simulation-designer rebuild`; record results in `profiles/_builds/MEASUREMENTS.md`; Brandon gives final builder approval after seeing them
- Phase 3 session C: red-team skill (`.claude/skills/red-team/`, three intensities) | Fable session | until it exists, profile-build stage 4 runs its interim critics
- Phase 2 done-when still open: real-session tests of `thread` (first tangent) and `chat-handoff` (first real package) | any session | record results in `memory/audits/2026-10-07-phase2-skill-tests.md`
- Account-synced skills cost about 3,300 tokens a turn of listing; unused ones (browser, computer-use, morning, google-workspace, import-memory, mcp-builder) can be turned off on claude.ai | Brandon, optional | see `memory/audits/2026-10-07-skill-doctor-baseline.md`
- Old `son-build` name in the root guard script docstring (line 5) | Brandon | needs the unlock phrase; one-word comment fix, then drop its allowlist entry
- Cloud environment for `son` | Brandon | paste `scripts/setup_cloud.sh` into the environment setup; check ClickUp and Box connectors
- Five data API keys (FRED, BLS, Socrata, Census, EIA) | Brandon | before nerve switches on in phase 5
- Archive the old GitHub repos (son-learning-studio, son-operational-buildout, son-nerve; make agenticproject private and archive) | Brandon to confirm | everything from them is in `son`
- Delete `~/Desktop/son-imports/_transfer` and the zips on the Desktop | Brandon, any time | originals are in the repo

## Done 2026-10-07
- Phase 3 session A: `profile-build` skill designed (7 stages, Sonnet workers hand back paths, draft once then edit, provenance outside the loaded text, agent core 12 KB cap, interim blind red team plus Fable judge, lint/ship/measure scripts); blind Fable review approved it for a test rebuild after fixes; baseline in `profiles/_builds/MEASUREMENTS.md`; `profile-forge` retired (M3)
- Phase 2 pull request merged (#4); profile-build pull request merged (#5)
- Phase 2 Session basics built (PR open): skills `session-close` (with verify-first, refused rationalizations, context-rot cue), `thread`, `chat-handoff` (dry-run tested, nine gaps fixed); `.claude/skills/REGISTRY.md` with the vetting gate; skill-scanner vendored; `/skill-doctor` and scanner baseline; CLAUDE.md names session-close as the only way to end a session; close-reminder hook parked
- Phase 1 Cleanup complete. Brand canon line applied: ClickUp Brand Guidelines doc 2ky45bmy-15773 (13 pages, log `memory/audits/session-b/brand-applied-clickup.md`) and the design system (log `memory/audits/session-b/brand-applied-repo.md`)
- Brandon deleted the four by-hand items (task 17tn048wdwr closed)
- Phase 1 session B: Box batches applied (experiential PDF to Reference (not canon), exhibit files to Pitch Materials / Investment, Start Here.md fixed); ClickUp inventory (`memory/audits/session-b/`); Jun removed from four Home Base pages and the website Team copy; Master Pointer Index registry copied to kb/tools; V7 citations rewritten as background; brand canon line marked
- Phase 1 session A: repo sweep (5 Sonnet agents, about 200 rewrites); raw exports deleted (clickup-system/exports, operations/archive, uncited extraction); cited extraction kept in operations/sources/extraction; old learning-studio clones deleted after salvaging their tooling to learning-studio/_salvage (inert); stale routing rewritten in operations, learning-studio, nerve, build-out, clickup-system; raise working files marked superseded; allowlist built
- Pull request #1 merged (Brandon): build-out workspace, phase lock hooks, skills, commands, and workflows are live on `main`; guard self-test 22/22
- Profile baseline imported from Box zip: 52 profiles in `profiles/_source/` and `founders/profiles/_source/`, 7 investment working files in `founders/capital-raise/working-files/` (phase 3 step 2 done)
- Community skills research done; approved list and install schedule in `memory/skills-plan.md`
- Rebuild intake; repo `son` created and pushed with history from every source (learning-studio from unmerged branch claude/blissful-einstein; nerve from unmerged PR branch claude/bold-goldberg; operations; design-system; local profile builds; ClickUp system; Espresso Chiller; Claude Science matcha and cryo espresso; construction workspace on PR #1)
- Build-out migration decisions M1, M2, M4 applied on PR #1
- Founder-only manual chunks and the old OA brief moved to `founders/`; Home Base facts ported to `founders/context.md` and `memory/context.md`
- Account memory cleaned and Project instructions replaced (Brandon)
- Workstream readiness audit: `memory/audits/2026-10-07-readiness.md`

## Open sandboxes
- None

## Live automation outside the repo
- Wednesday restaurant tech digest (scheduled task trig_01EUH167wrsReHWDvt5Sv7vG; prompt in `prompts/scheduled/weekly-tech-digest.md`)
- ClickUp Meetings Agent v3: Monday 7 AM roll-forward, day-before reminders, close-out; checkpoints Oct 8, 12, 13 (`company/workstreams/clickup-system/STATE.md`)

## Open questions for Brandon
- Resolved 2026-10-07 (Brandon): brand canon line marked; see `memory/decisions.md` (`brand`)
- Resolved 2026-10-07 (Brandon): V7 Business Strategies Notebook (ClickUp 2ky45bmy-11873) is kept as background only, not canon; the white paper is canon.
- Operational figures (pars, labor targets, pay, schedules, counts) have no source since Airtable retired; learning-studio marks them unbound (phase 5)
- build-out/HANDOFF.md: delete now that the migration is done? (phase 5)
- Build-out migration still open: M5 command names (phase 4), M6 build-out kb location (phase 5). M3 resolved 2026-10-07
- Founder-only seats: where their agents live once built (root `.claude/agents/` or a founders-only location for the repo split); `ship.py` refuses founder seats until decided (phase 3 step 5)
- Red-team lens source "notmanas questioning-frameworks" was not found on GitHub; Brandon to supply the URL if it matters (session C)
