# Phase 3: Profiles

Design runs on Fable. Extraction and mechanical work run on Sonnet subagents; drafting and migration on Opus.

## Goal
One profile system for all of Sŏn: profiles live in the repo as master, run as subagents, cost little context, stay aligned with each other, and are built by one token-lean pipeline. Box becomes a read-only mirror and the Replacement Queue retires.

## What exists today
- **Box master:** 64 profiles in 8 clusters under Sŏn / 10. AI Projects / Profiles (393577233571): Voice (4), Investment (11 plus 7 working files that do not belong there), Design Translating Team (10), Founder Development Plan (6), Learning & Development (9), People & Culture (8), Scaling People (3), Narrative and Structure (1). 20 to 95 KB each. All share a `project_block` that hardcodes stale facts (a nonexistent profile path, Airtable figures, The Josephine). Three naming conventions.
- **Repo copies:** `company/workstreams/operations/profiles/` (8 verbatim), `company/workstreams/learning-studio/profiles/manifest.yaml` (29 seats by Box ID), `learning-studio/profile-builds/` (2 profiles built through the seven-stage procedure), `.claude/agents/` (2 build-out agents).
- **Planned, unbuilt:** 16 build-out specialists (bar-designer first; roster in `company/workstreams/build-out/research/raw/2026-09-28-construction-mode-blueprint.md` section 5).
- **Three overlapping build pipelines:** the seven-stage synthesis (ClickUp Research Capture 2ky45bmy-16853, Actionable Distillation page), build-out `profile-forge` skill, learning-studio `/build-profile` and `/validate-profile` (definitions survive only in `imports/profile-builds-local/*/.claude/skills/`).
- **Brandon's observation:** one profile takes 2 to 3 hours and maxes out context windows. Time is fine; token use is not. Cause: one context holds raw sources, extractions, drafts, and critiques together.

## Work
0. **Intake.** Unzip Brandon's Box Profiles download into `profiles/_source/<cluster>/`, untouched, with `profiles/_source/manifest.csv` (name, Box ID, cluster, size, modified date). Box stays master until step 7.
1. **Seat inventory (Sonnet).** For each workstream, list the seats it needs, what each seat decides, and which existing profile (if any) covers it. Output `profiles/roster-needs.md`. Include seats no workstream needs (retirement candidates).
2. **Efficacy and alignment review (Sonnet per cluster, Fable synthesizes).** Rubric: overlap and conflict between profiles; stale or out-of-scope content; size versus value; whether each encodes judgment (decision rules, cue tables, failure modes) or survey; consistency of standing rules. Output `profiles/review.md` with a recommendation per profile: keep, merge, rebuild, retire.
3. **System design (Fable).** Schema: a lean core loaded as the agent definition, and reference material loaded on demand. Shared rules move to CLAUDE.md once, out of every profile. Agent frontmatter (model, tools). Naming. Folder layout. How workstreams call seats (by agent name). How the Voice system, the Design Translator auto-trigger, and the Founder Development profiles (founder-only, so `founders/`) fit. Output `profiles/SYSTEM.md`.
4. **Build pipeline (Fable designs).** Merge the three pipelines. Sonnet subagents read sources and write quoted extractions to files; Opus drafts from extraction files only, never raw sources; a fresh agent red-teams the draft blind; another runs behavioral tests (3 to 5 tasks per profile). Fable only at Frame and final judgment. Set token budgets per stage. Output `.claude/skills/profile-build/`.
5. **Red-team skill (Fable designs).** Three intensities: light (concept ideation: push back a little, constructively), standard (default), harsh (legal, compliance, anything touching employees: multiple blind agents with assigned bias-hunting lenses, and a feedback-loop check across the session). Output `.claude/skills/red-team/`. The profile pipeline uses it.
6. **Migration (Opus and Sonnet).** Apply the review decisions: rewrite, merge, retire. Generate `.claude/agents/*.md`. Point learning-studio, operations, and build-out at the new agents; retire `/sync-profiles`.
7. **Flip the master.** Repo becomes master. Automate a read-only mirror to Box (renamed consistently). Retire the Replacement Queue (ClickUp Master Pointer Index page 2ky45bmy-27093) and the seven-stage page, pointing both to the repo.

## Decisions for Brandon (pop-ups, with context)
- Per cluster: the keep / merge / rebuild / retire recommendations.
- Whether the Design Translator auto-trigger stays, now that he prefers designing in code.
- Build-out open decision M3 (profile-forge versus this pipeline).
- Which build-out specialists to build first (bar-designer is referenced by the Tobin Ellis knowledge base).

## Done when
- Every seat in `roster-needs.md` is resolved (agent built, mapped, or deliberately deferred).
- Agents load and pass their behavioral tests.
- One profile built end to end through the new pipeline, with token use recorded against the old process.
- Box mirror updated; Replacement Queue retired.

## Session split
A: intake and seat inventory. B: review. C: system design and pipeline (Fable). D: red-team skill (Fable). E and on: migration in batches. F: flip.
