# Workstream readiness audit, 2026-10-07 (read-only; evidence from branch import/build-out)

Evidence base: branch `import/build-out` (dc484d9) at /home/claude/son. Counts are matching lines from grep.

## Facts that cut across everything
- **Almost nothing in `.claude/` or `.github/` exists on `main`.** `main` has only `.claude/agents/.gitkeep` and `.claude/skills/.gitkeep`. The hooks, `settings.json`, 6 skills, 6 commands, 2 agents and both workflows exist only on unmerged `import/build-out`. On `main` the build-out phase lock is not enforced. The daily watch cron cannot run until the branch merges, because scheduled workflows run only from the default branch.
- **Learning-studio lost its dot-folders in transit.** The cloud branch began with commit 1a0feed ("Add files via upload"), which has 0 files under `.claude`, `.mcp.json` or `.github`. Its README warns that drag-and-drop upload drops those folders. The 13 studio skills, `.mcp.json` and `lint.yml` survive only in `imports/profile-builds-local/*`.
- **Account scheduled tasks** (checked with list_triggers):
  - Only one live recurring task exists: "Weekly restaurant tech intelligence digest", `trig_01EUH167wrsReHWDvt5Sv7vG`, Wednesdays 12:00 UTC. It last fired 2026-10-07 and succeeded; next run is 2026-10-14. It matches `prompts/scheduled/weekly-tech-digest.md`.
  - A "Weekly Motorsport Brief" task exists but is disabled.
  - No task matches nerve's R1, R2 or R3 routines. These might be stored on a surface list_triggers does not show.
- **Missing skills the root CLAUDE.md names.** It references a `red-team` skill and a `session-close` procedure. `.claude/skills/` has only book-ingest, consolidate, equipment-record, intake, interview and profile-forge. `memory/state.md` lists red-team and session-close as P5, not built.
- **Scope and boundary leaks under `company/`:**
  - `clickup-system/exports/2026-09-16-baseline/docs/` holds 17 raw ClickUp exports. These include `Operating_Agreement_Founder_Pre-Counsel_Brief.md` (556 lines, founder-only governance material under `company/`), `Claude_Project_Review.md` (contains the "Event Co" section), and Pointer Index and Operating System exports. They account for most of that workstream's Josephine, Jun, Airtable and experiential hits.
  - The operations manual (comp 5.5, firing 5.10, founder self-awareness 1.1 to 1.4, career 6.3) sits under `company/`. The root CLAUDE.md puts comp under `founders/`. This is a boundary question for Brandon.

## 1. build-out (`company/workstreams/build-out`)
- **What it is:** Construction-mode workspace for equipment, bar and kitchen design, MEP and codes. A phase lock (P0 concept until the lease is signed) is enforced by root hooks.
- **State: [ready-to-build].** HANDOFF.md says "no record that it was published to GitHub or that KICKOFF.md was run. Treat it as never run." There are 0 equipment records, 0 models and 0 book notes. Only `kb/bar/tobin-ellis/` is populated. `PHASE.yaml` has `lease_signed: false`. `validate_equipment.py` exits 0.
- **Steps to work-ready:**
  1. Merge PR `import/build-out`, so the hooks, skills, commands and workflows exist on `main`.
  2. Run KICKOFF steps 1 and 2 (hook health check and guard test). The hooks were only fed sample events and are untested in a live session.
  3. Fix the stale pointer in `clickup/space-blueprint.md` ("Follow `knowledge-base.md`"). The file now lives at `clickup-system/kb/clickup-knowledge-base.md`.
  4. Get the geometry stack (build123d, ifcopenshell, ezdxf) installed. It is not installed here. Use the cloud setup script and merge its package list into the repo environment.
  5. Add the Product and Technology capture list IDs to `clickup/allowlist.yaml` (open item 7). Only Property Capture 901327291277 is allowlisted.
  6. Run KICKOFF steps 4 to 6 (import the 9 ClickUp guides without figures, create the Box folders after asking Brandon, start the bar sandbox interview).
- **Profile rewrite dependency:** Not for steps 1 to 6. `bar-designer` is referenced by the Tobin Ellis kb but not built (16 of 18 planned profiles are unbuilt). It depends on open decision M3 (profile-forge versus the P4 pipeline).
- **Stale references:** Almost clean.
  - `son-build`: 12 lines in 5 files (HANDOFF 5, README 4, `scripts/watch.py` 1).
  - Keychain: 1 (blueprint research note).
  - experiential: 2 (`toc.yaml`, CLAUDE.md).
  - All other terms: 0.
  - Top files: HANDOFF.md, README.md (still describes the standalone setup), `scripts/watch.py`.
- **Commands and skills:** All referenced ones exist on the branch: capture, deep, gate, lease-signed, promote and sandbox as commands; intake, interview, equipment-record, consolidate, profile-forge and book-ingest as skills. HANDOFF lists `/digest`, `/export-handoff` and `/code-check` as planned and not built.
- **External dependencies:**
  - ClickUp and Box connectors (Box folder 420132927884).
  - Git LFS.
  - GitHub Actions with a `watch` issue label.
  - Local Mac GUI tools (Blender with Bonsai, FreeCAD) over MCP.
  - Optional `CLICKUP_API_TOKEN`.
- **Recurring jobs not running:**
  - `build-out-watch.yml`, a daily cron, is not on `main`.
  - It pushes directly to the default branch. That will fail if the branch protection HANDOFF recommends is enabled.
  - HANDOFF §8 also plans a weekly code-change Routine, an innovation feed Routine and a monthly equipment merge. None exist.
  - 4 of 10 watched sites returned 403 to scripted requests.

## 2. learning-studio
- **What it is:** Studio for designing tool-neutral training modules, bound to tools later. Source is the cloud branch (52 commits, up to D65).
- **State: [mid-build].** `framework/system-design.md` holds decisions D1 to D65. `research/position-paths/` specifies about 253 modules in prose. `catalog/catalog.yaml` has only 6 unconfirmed seed modules, and `modules/` has only `_example`. The Module Review pass was paused and resumed on 2026-10-02 (a claude.ai artifact page). `lint.py` reports 0 errors and `status.py` runs.
- **Steps to work-ready:**
  1. Restore the 13 skills from `imports/profile-builds-local/hospitality-craft-educator/.claude/skills/` into the repo (either learning-studio-scoped or root `.claude/skills`). Also restore `.github/workflows/lint.yml` (the repo has no learning-studio lint) and a trimmed `.mcp.json` with Airtable removed.
  2. Rewrite `/sync-profiles` and the profile pointers once the profile system decision lands (**profile rewrite**).
  3. Rewrite CLAUDE.md and `canon/pointers.md`: drop Airtable, the Replacement Queue and the Master Pointer Index; point brand to the cleaned canon and figures to the Investor Review workbook.
  4. Reconcile the catalog with the position-path modules. Brandon finishes the Module Review pass; its decisions live in an artifact store, not the repo, so export them.
  5. Sync the parked Module Catalog ClickUp list (1400400000001424) via `/status`.
  6. Run the Trainual capability tour before any render (still undone per the README).
- **Depends on profile rewrite:** Steps 1 (sync-profiles), 2 and 3 do. The manifest lists 29 profiles by Box ID (all "live", 0 local files).
- **Stale references:**
  - Airtable 52 lines in 26 files.
  - Replacement Queue 12 in 7.
  - sync-profiles 9 in 6.
  - Master Pointer Index 5 in 3.
  - 2ky45bmy-16833: 3 in 3.
  - son-learning-studio 3 in 3.
  - experiential 30 in 21.
  - Business Strategies Notebook and 2ky45bmy-11873: 5 each (in profile-build files).
  - Josephine, Pullman and Jun: 0.
  - Top files: CLAUDE.md, `canon/pointers.md`, `profiles/manifest.yaml` (plus `README.md`, `profile-builds/RUNBOOK.md`).
- **Missing commands/skills (all 13):** `/sync-profiles`, `/identify`, `/ideate`, `/design-module`, `/draft-module`, `/review-module`, `/park-module`, `/bind`, `/render`, `/status`, `/refresh-capabilities`, `/build-profile`, `/validate-profile`. None are in learning-studio or root `.claude`; older versions exist only in the imports folders.
- **External dependencies:**
  - Box (profiles, brand PDF 2281626080747, white paper 2466517057642).
  - ClickUp.
  - Trainual and Synthesia.
  - Python with pyyaml.
  - The Module Review artifact (QRu1evLAawnFdqaBh6XxdQ).
- **Recurring jobs:** None expected.

## 3. operations (Scaling People build-out)
- **What it is:** The book converted to a manual of 33 chunks, mirrored by 764 tasks in ClickUp under parent 86akh1hdg.
- **State: [work-ready].** README: "Done 2026-09-27", with all 33 chunks marked "Ready". All 33 `decisions.md` files are seeded and open, apart from one recorded ruling in 2.2. A working session can start today; sources, including the white paper PDF, are in the repo.
- **Steps (sandbox and polish):**
  1. Open a session on chunk 2.1 using the README opening prompt.
  2. Update CLAUDE.md for the unified repo. `son-operational-buildout` is cited in 2 lines, and Box/Mac assumptions need rewording ("Claude's memory files live only on Brandon's Mac").
  3. Fix `.gitignore`. It ignores `profiles/people-and-culture/` and `profiles/founder-development/`, which are absent from the repo. Chunks 1.1 to 1.4 and 6.1 to 6.3 are meant to use the founder-development profiles (**profile rewrite**).
  4. Decide the founders/ boundary for comp, firing and founder-reflection chunks.
  5. Add the clickup connector note; the REST token `~/.clickup_token` is Mac-only.
- **Profile rewrite dependency:** Partial. The manual does not reference `profiles/` anywhere (0 files). Profiles are optional lenses.
- **Stale references (whole workstream, mostly archive/extraction):**
  - Airtable 229 lines in 108 files (live docs only: 56 lines, in the 8 profiles, CLAUDE.md 2, `reference/standing-rules.md` 3, and 1 manual line in 5.4 tasks).
  - `.clickup_token` 10 in 8 (CLAUDE.md 1).
  - `son-operational-buildout` 4 in 4.
  - experiential 92 in 81 (live docs: 15).
  - Business Strategies Notebook and 2ky45bmy-11873: 12 each in 11 files (live: CLAUDE.md, `reference/standing-rules.md`, profiles).
  - Pullman 2 (extraction only).
  - Replacement Queue, sync-profiles, Keychain, Josephine and Jun: 0.
  - Top files: CLAUDE.md, `reference/standing-rules.md`, `profiles/hospitality-operations-realist.md`.
- **Commands and skills:** None referenced.
- **External dependencies:** ClickUp connector (parent 86akh1hdg, list 901323485125), PyMuPDF.
- **Recurring jobs:** None.

## 4. nerve
- **What it is:** Weekly Austin hospitality digest pipeline with 3 routines: R1 daily ingest, R2 Sunday releases, R3 Monday digest to ClickUp and Box.
- **State: [built-not-switched-on].** Code and tests exist: 13 scripts and 6 test files. There is one DRAFT digest (2026-09-28) and data last pulled 2026-09-26. CLAUDE.md says routines are "live from 2026-09-26" and run on `main`. But the source repo's `main` held only BRIEF.md (the code was on an unmerged PR branch). `memory/state.md` says "Monday Industry Digest has no scheduled task yet", and no matching scheduled task appears in list_triggers. So it is not running.
- **Steps to work-ready:**
  1. Install deps (`duckdb`, `pyarrow`, `pandas`, `shapely` are missing here) and run `pytest -q` (offline).
  2. Fill `.env` keys: FRED, BLS, SOCRATA, CENSUS, EIA.
  3. Run R1 and R2 by hand to confirm the ingest works from the unified repo.
  4. Fix routine docs and paths. CLAUDE.md names a `son-nerve` repo, and routine commit targets must point at `son` and the nerve subfolder.
  5. Create the three scheduled tasks with a custom network allowlist and ClickUp and Box connectors on R3.
  6. Review and publish the draft digest.
- **Profile rewrite dependency:** None.
- **Stale references:** Clean.
  - Airtable 2 (the "No Airtable" rule).
  - `son-nerve` 3.
  - Josephine 10, Jun 10, experiential 2. These are data and month-name noise, such as inspection records, "Jun to Aug" and licence names.
  - Other terms 0.
  - Top files: `scripts/common.py` (user agent), CLAUDE.md, BRIEF.md.
- **Commands and skills:** None.
- **External dependencies:** API keys above, ClickUp (space 90136733098, doc 2ky45bmy-20073, lists 1400400000001380 and 1400400000001381), Box (folder 393201935562), cloud routines with network allowlist, `CLICKUP_API_TOKEN` for R1 signals.
- **Recurring jobs not running:** R1 (daily 6:07 CT), R2 (Sun 8:07 pm CT), R3 (Mon 7:07 CT).

## 5. clickup-system
- **What it is:** ClickUp knowledge base, runbooks, exports, Meetings Agent v3 plans and the CU REST helper. The workstream has no CLAUDE.md.
- **State: [work-ready].** `STATE.md` (2026-10-04) says the meetings system, agenda flow, Meetings Agent v3, Investor CRM and workspace are "Live and working". Open items are checkpoints, not setup: Oct 8 standup, Oct 12 roll-forward, Oct 13 meeting.
- **Steps to work-ready (hardening):**
  1. Add a workstream CLAUDE.md pointing at `STATE.md`, `DECISIONS.md` and the kb.
  2. Merge `kb/from-build-out-2026-09-28.md` into `clickup-knowledge-base.md`, then delete it. It is flagged "Merge ... then delete".
  3. Remove the duplicate `cu.py` (`scripts/cu.py` and `kb/cu.py` are identical).
  4. Move or scrub `exports/`: the Operating Agreement brief, Josephine and Jun content, and the Pointer Index exports. Decide the archive location.
  5. Run the Oct 8, 12 and 13 checkpoints.
- **Profile rewrite dependency:** None.
- **Stale references (whole workstream):**
  - Airtable 176 lines in 27 files (non-export: 10).
  - Josephine 65 in 18 (non-export 17, in research, audit, DECISIONS, blueprint and the you-checklist).
  - Pullman 19 in 9 (non-export 1, `audit/events.md`).
  - Jun 43 in 7 (all in exports, including founding-punch-list.json, Claude_Project_Review and 2ky45bmy-16873).
  - experiential 54 in 9 (exports).
  - Keychain 14 in 11 (non-export 13: kb, `scripts/cu.py`, runbooks, blueprint).
  - Replacement Queue 8, Master Pointer Index 23, 2ky45bmy-16833 14, Business Strategies Notebook 8, 2ky45bmy-11873 6 (all in exports).
  - Top files: `exports/2026-09-16-baseline/docs/Claude_Project_Review.md`, `Sŏn_Master_Pointer_Index_Inventory.md`, `exports/.../tasks/founding-punch-list.json`.
- **Commands and skills:** None referenced. The v3 agent skills (`templates/meetings-agent-v3-skills.md`) are ClickUp agent skills and were never built.
- **External dependencies:**
  - ClickUp Super Agent and Automations (credits).
  - Google Calendar and Meet.
  - Wispr Flow MCP.
  - `CLICKUP_API_TOKEN` or the macOS Keychain item `clickup-api-token`.
- **Recurring jobs:** Meetings Agent v3 (roll-forward Mondays 7 AM, day-before reminders, close-out) runs inside ClickUp, not in the repo. This is unverifiable from here.

## 6. science
- **What it is:** Beverage R&D: matcha sonication, cryo espresso and an espresso chiller. It is modelling only; the README says "no bench measurements yet".
- **State: [reference/paused].** The handoff says "Status of everything in this package: modelling and design work. No bench measurements have been made." There is no CLAUDE.md. Known issues:
  - Citation provenance is unconfirmed.
  - `vessel_ledger.csv` and `assay_panel.csv` have inconsistencies.
  - `build_scene.py` "has never been executed".
  - The chiller Fabrication Handoff (Rev C) describes an Eversys Enigma E'4s with two coils, while `model/README.md` models a La Marzocco Strada X with three coils.
- **Steps to sandbox-ready:**
  1. Reconcile the espresso-chiller Rev C against the three-group model.
  2. Dedupe `cryo-espresso/05_equipment_design` against `espresso-chiller` (the coil-sizing CSV is identical; `Design Package.md` differs).
  3. Fix the Mac absolute path in `model/README.md`.
  4. Add a CLAUDE.md with the "no bench data" caveat.
  5. Fix `HANDOFF-claude-science-2026-10-07.md` folder names. It says `01_matcha_sonication` and `02_cryo_espresso`, but the actual folders are `matcha-sonication` and `cryo-espresso`.
  6. Fix `cryo-espresso/05_equipment_design/claude_code_prompt.md`, which names `blender_handoff_brief.md` (not in the folder).
- **Profile rewrite dependency:** None.
- **Stale references:** 0 across all 19 terms.
- **Commands and skills:** None.
- **External dependencies:** Python with numpy and matplotlib for `chiller_model.py`; Blender 4.x for `build_scene.py`.
- **Recurring jobs:** None.

## 7. brand/design-system
- **What it is:** Sŏn design system, 63 commits (July 2026): tokens, React components, a scroll-driven `track/` site, a frozen `site/` v3 fallback, UI kits and a guidelines deck.
- **State: [built-not-switched-on].** `docs/handoff.md` (2026-07-23) lists tasks "owed by name": a Dominic task to provision the POST endpoint, deduplicate by email, run external regeneration (the compiler is not in this repo) and deploy to Vercel, plus Brandon's verify-pending copy facts and portraits. Nothing has been deployed. It also conflicts with current canon.
- **Steps to work-ready:**
  1. Decide per canon cleanup which content stays. The readme's three "Tier-1" cultural frameworks (Jaeyeonmi, Ma, Mahk) and the Korean tie-ins conflict with the decision to remove cultural tie-ins. Show the extraction first, as `state.md` says.
  2. Run the codename copy pass. "Good Energy" appears in 61 lines (18 files), "Dosi" in 109 (32), "Luxx" in 12 (5), "Future Nostalgia" in 9 (8), and daypart in 220 lines. The readme still cites ClickUp canon 2ky45bmy-15773.
  3. Run `npm install && npm run lint` (Node v22 is present; `node_modules` is not).
  4. Dominic does the endpoint, dedupe, regeneration and Vercel deploy. Brandon provides the verify-pending facts.
  5. Move `SKILL.md` (`son-design`) into `.claude/skills/` if you want it registered; it is currently inert.
  6. Consider moving `refs/` out (126 MB tracked, 972 files; repo pack is 96 MiB). The licensed GT fonts in `assets/fonts` are also in the repo.
- **Profile rewrite dependency:** None.
- **Stale references:** Airtable 1 (AUDIT.md), experiential 15 in 9 (guidelines deck HTML 3 each, the uploads brand guidelines v1 2), Josephine, Pullman and Jun 0, other terms 0. Top files: `readme.md`, `docs/handoff.md`, `uploads/Son Brand Guidelines v1 (1).md`.
- **Commands and skills:** `SKILL.md` declares `son-design` but is not registered. No commands.
- **External dependencies:** npm (eslint, stylelint, playwright, lenis), Vercel (Dominic), licensed fonts, the endpoint.
- **Recurring jobs:** None.

## 8. imports/profile-builds-local (two branches) versus learning-studio/profile-builds
- **What they are:** Older clones of the learning studio, one per profile build: `hospitality-craft-educator` (8 commits) and `practice-simulation-designer` (5 commits to stage 05). Each has its own `.claude` (13 skills, settings), `.mcp.json` and `.github/workflows/lint.yml`.
- **State: [reference/paused].** `learning-studio/profile-builds/` is a superset.
  - The HCE stage files are byte-identical everywhere.
  - The PSD stage files 00 to 05 match, except the PSD `00-frame.md` in the HCE clone, which differs (an earlier frame).
  - Learning-studio additionally has `06-revised.md` and `06-validation.md` for PSD.
  - Per the README, both profiles are "live in Box" (2491194239261 and 2491190356107) with Stage 6 skipped for HCE and stages 6 and 7 skipped for PSD by founder decision.
  - So the imports hold nothing unique except the dot-folders.
- **Steps to retire safely:**
  1. Move the 13 skills, `settings.json` (permissions for `profile-builds/**`) and `lint.yml` into learning-studio or root. Drop Airtable from `.mcp.json`.
  2. Delete the imports folder (all 4 `README.md`/`manifest.yaml`/stage differences are older versions).
  3. Decide whether to run `/validate-profile` later (**profile rewrite**). It depends on the Box Replacement Queue.
- **Stale references:** Airtable 48 in 30, Replacement Queue 18 in 12, sync-profiles 18 in 14, Master Pointer Index 10 in 6, 2ky45bmy-16833: 8 in 8, son-learning-studio 4 in 4, Business Strategies Notebook 12 and 2ky45bmy-11873 14 (in 12 to 14 files).

## Profiles in the repo
- `operations/profiles/` has 8 files (about 320 KB): hospitality-operations-realist, organizational-systems-architect, people-systems-designer, and in `learning-and-development/` educational-materials-author-and-editor, highscope, instructional-designer, learner-advocate and tbri.
- `learning-studio/profiles/` has no profile files, only a manifest of 29 Box-referenced slugs (9 learning-development, 8 people-culture, 3 scaling-people, 9 design-translating).
- The 2 built profiles live as stage files in `learning-studio/profile-builds/` (final text is `06-revised.md`). They are triplicated: learning-studio plus both imports for HCE, and learning-studio plus one import for PSD.
- Duplicate names between operations files and the manifest: instructional-designer, highscope, tbri, learner-advocate, materials-author-editor, hospitality-operations-realist, organizational-systems-architect and people-systems-designer.
- `build-out/.claude/agents` (really root `.claude/agents`): 2 lean agents (equipment-librarian, intake-triage).
- Empty: root `profiles/` (only `.gitkeep`) and `build-out/tests/profiles/`.
- Not copied: operations' people-and-culture and founder-development folders.

## Nested `.claude` / `.mcp.json`
- Only in `imports/profile-builds-local/hospitality-craft-educator/` and `.../practice-simulation-designer/`: `.claude/` (13 skills plus `settings.json`) and `.mcp.json` (Box, ClickUp and Airtable servers).
- No other nested `.claude` or `.mcp.json` outside root.
- Learning-studio, operations and nerve have none, and never did in source history.

## Nested `.github/workflows` (will not run)
- `imports/profile-builds-local/hospitality-craft-educator/.github/workflows/lint.yml`
- `imports/profile-builds-local/practice-simulation-designer/.github/workflows/lint.yml`
- Root `.github/workflows/` (on the branch only): `build-out-validate.yml` and `build-out-watch.yml`.
- Nothing for learning-studio, operations or nerve.
