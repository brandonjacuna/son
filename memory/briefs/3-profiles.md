# Phase 3: Profiles

Order set by Brandon 2026-10-07: fix the builder first (token use is the priority, efficacy second), then use the new builder to revise, improve, or generate profiles. Design runs on Fable; extraction and mechanical work on Sonnet subagents; drafting and migration on Opus.

## Goal
One profile system for all of Sŏn: profiles live in the repo as master, run as subagents, cost little context, stay aligned with each other, and are built by one token-lean builder. Box becomes a read-only mirror and the Replacement Queue retires.

## Step 1: Rebuild the profile builder (first, before touching any profile)

**Status 2026-10-07:** session A done. Builder at `.claude/skills/profile-build/` (design record in its `SOURCE.md`), baseline in `profiles/_builds/MEASUREMENTS.md`, profile-forge retired (M3). Session B done the same day: test rebuild measured (`profiles/_builds/MEASUREMENTS.md`), builder approved with fixes (applied). Next: smoke test, then steps 3 and 4.

**The builder to start from** is the one Brandon developed: the learning studio's `build-profile` and `validate-profile` skills (only copies: `imports/profile-builds-local/hospitality-craft-educator/.claude/skills/`), its runbook `company/workstreams/learning-studio/profile-builds/RUNBOOK.md`, and the seven-stage synthesis it implements (ClickUp Research Capture doc 2ky45bmy-16853, Actionable Distillation page). Also read build-out's `profile-forge` skill (`.claude/skills/profile-forge/`, four stages with token budgets, never run) and treat it as a source of ideas, not a competitor (build-out open decision M3).

**Measured baseline** (stage files in `company/workstreams/learning-studio/profile-builds/`):
- Hospitality Craft Educator: about 445 KB of stage files. Corpus 81 KB, elicitation 49 KB, then the full profile written three times: draft 81 KB, tagged 95 KB, revised 95 KB. The finished profile is 95 KB, about 24,000 tokens loaded every time the seat is used.
- Practice and Simulation Designer: about 199 KB of stage files; finished profile 53 KB.
- Brandon's experience: 2 to 3 hours per profile (time is fine) and context windows maxed out (not fine).

**Visible token sinks to test first:**
- Whole-profile rewrites at each stage (draft, then tagged, then revised). Tag and revise as edits or annotations, not full rewrites.
- One context holding the corpus, extractions, drafts, and critiques together. Use Sonnet subagents that read sources and write short quoted extraction files; the drafter reads only extraction files; the red-team agent reads only the draft.
- Finished profiles that are too large to load per call. Split into a lean core (the agent definition, a hard size cap) and reference files loaded on demand.
- Repeated shared rules (the `project_block` in every profile). Move them to CLAUDE.md once.
- Fable used for stages that do not need it. Fable only at Frame and final judgment.

**Format decision, per profile (the core design question):** today profiles are long markdown files attached whole into a chat. In Claude Code each one splits into the right container:
- judgment and identity (role, scope, decision rules, cue table, failure modes, output contract) become a **subagent** in `.claude/agents/`: its own context, its own model, returns only its conclusion, can run in parallel and blind;
- procedures (generate, critique, diagnose) and reference knowledge (mental models detail, worked examples, platform grammars, sources) become **skills** with reference files, loaded only when triggered;
- shared plumbing (`project_block`, interaction guide, standing rules) moves to CLAUDE.md once; `reanchor` sections mostly fall away because a subagent starts with a fresh context.
Some profiles are seats (subagent), some are modes of the main conversation (skill, for example the House voice), some are both (Design Translator: a translation skill plus a reviewing subagent). The builder outputs this split directly.

**Output:** `.claude/skills/profile-build/` (one builder, replacing the three), with a token budget per stage, and a measurement log. **Test:** rebuild one existing profile (Practice and Simulation Designer is the smaller one) and record tokens and quality against the baseline. Brandon approves the builder before step 2.

The red-team skill is designed alongside, because the builder's validation stage uses it: three intensities, light (concept ideation, constructive push back), standard (default), harsh (legal, compliance, anything touching employees: multiple blind agents with assigned bias-hunting lenses and a check for feedback loops in the session). Output `.claude/skills/red-team/`.

**Approved inputs for the builder (see `memory/skills-plan.md`):** Context Engineering patterns (filesystem context, compression, evaluation), writing-for-agents (for the agent and skill split), the superpowers writing-skills test method (for behavioral tests), model tiering conventions (per-agent model and tool limits), and the red-team lenses (questioning frameworks, stakes calibration, three-concerns output). Note: a skill preloaded into a subagent loads in full, so keep agent cores short and let agents read reference files on demand.

## Step 2: Bring the profiles into the repo (DONE 2026-10-07)
Done: see `profiles/_source/README.md` and `manifest.csv`. 52 profiles plus 7 investment working files (the earlier count of 64 was wrong). Original instructions kept below for reference.

Brandon downloads Sŏn / 10. AI Projects / Profiles from Box as a zip to the Mac Desktop. Unzip into `profiles/_source/<cluster>/`, untouched, with `profiles/_source/manifest.csv` (name, Box ID, cluster, size, modified date). Box stays master until step 6. (Today only 8 profiles are in the repo, copied earlier by the operations workstream, plus the 2 learning studio builds.)

## Step 3: Seat inventory
For each workstream, list the seats it needs, what each seat decides, and which existing profile covers it (Sonnet). Output `profiles/roster-needs.md`, including retirement candidates no workstream needs. Inputs: learning-studio `profiles/manifest.yaml` (29 seats), build-out roster (18 planned, 2 built as agents; blueprint section 5 in `company/workstreams/build-out/research/raw/2026-09-28-construction-mode-blueprint.md`), operations' use of profiles as lenses, the Voice and Investment clusters, Design Translating Team, Founder Development (founder-only, so `founders/`).

## Step 4: Review
Per cluster (Sonnet, Fable synthesizes): overlap and conflict between profiles, stale or out-of-scope content, size versus value, judgment (decision rules, cue tables, failure modes) versus survey, consistency of standing rules. Output `profiles/review.md` with a recommendation per profile: keep and slim, revise, merge, rebuild with the new builder, retire, or generate new.

## Step 5: Run the builder across the roster
In batches, in the order Brandon sets: revise, merge, rebuild, or generate. Generate `.claude/agents/*.md`. Point learning-studio, operations, and build-out at the new agents; retire `/sync-profiles`. Bar-designer is the first new build-out seat (the Tobin Ellis knowledge base references it).

## Step 6: Flip the master
Repo becomes master. Automate a read-only mirror to Box with consistent names. Retire the Replacement Queue (ClickUp Master Pointer Index page 2ky45bmy-27093) and the seven-stage page, pointing both to the repo.

## Decisions for Brandon (pop-ups, with context)
- Approve the new builder after the test rebuild.
- Per cluster: the review recommendations.
- Whether the Design Translator auto-trigger stays, now that he prefers designing in code.
- Build order for new build-out specialists.

## Done when
- The builder is approved, with measured token use well below the baseline.
- Every seat in `roster-needs.md` is resolved (built, mapped, or deliberately deferred); agents pass their behavioral tests.
- Box mirror updated; Replacement Queue retired.

## Session split
A: builder analysis and redesign (Fable). B: test rebuild and measurement. C: red-team skill (Fable). D: profile intake, seat inventory, review. E and on: builder runs in batches. Last: flip.
