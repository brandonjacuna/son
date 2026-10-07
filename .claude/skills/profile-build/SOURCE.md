# Source and design record: profile-build

Written 2026-10-07 (phase 3, session A). Our own skill; nothing vendored. Ideas mined from the sources below (approved in `memory/skills-plan.md`); no files copied.

## What it replaces
| Old | Kept | Changed |
|---|---|---|
| Learning studio `build-profile` and `validate-profile` (salvaged copies in `company/workstreams/learning-studio/_salvage/skills/`), `profile-builds/RUNBOOK.md` | The seven-stage synthesis (ClickUp 2ky45bmy-16853, page 2ky45bmy-27213): frame, 5 to 15 curated sources, cue inventory and decision requirements, consolidation without smoothing tensions, the typed template's judgment sections, the confabulation firewall, independent adversarial validation, behavioral tests that check diagnostic moves, not tone. "Encode what the expert does, not who they are." | Stages 2 and 3 run in Sonnet workers, not the main context. Draft once; tag and revise as edits. Tags move to `provenance.md`. Output split into agent core, reference, and skill. Shared plumbing dropped (CLAUDE.md carries it). Validation runs inside the same build as blind subagents plus a Fable judge, instead of a second session. |
| Build-out `profile-forge` (four stages, never run) | Hard budgets per stage, research for judgment not survey, a 120-line agent core, long reference out of the agent, three test scenarios with an expected catch, cheapest model that passes. | Becomes stages 0, 1, 5, and 6 of this skill. Retires once Brandon closes build-out decision M3. |
| `/sync-profiles` and the Box cache | | Not needed once the repo is master (phase 3 step 6). |

## Why each change (measured 2026-10-07; numbers in `profiles/_builds/MEASUREMENTS.md`)
- Full rewrites: PSD's tagged and revised files kept 99% of the draft's lines. Two of three full writes added no judgment. Now: one draft, then Edits.
- Inline tags: 18% of every loaded PSD profile. Now: zero at runtime, kept in `provenance.md`.
- Plumbing (project_block, interaction_guide, reanchor): 7 to 10% of each load, paraphrased differently in every profile. Subagents load CLAUDE.md by default, so the standing rules reach them without restating.
- Reference material (mental models, worked examples, source manifest, tag audit): 29 to 35% of each load. Now on demand.
- One context holding corpus, elicitation, three drafts, and critique: the reason context windows maxed out. Now the orchestrator never opens a source or a card; workers hand back paths.

## Mined sources
| Source | License | Idea used |
|---|---|---|
| muratcankoylan/Agent-Skills-for-Context-Engineering | MIT | Pass file paths, not contents; one file per worker; deterministic validation before LLM judgment; fewest agents, 3 to 5 per supervisor; sub-agents isolate context. |
| mattpocock/skills, writing-for-agents | MIT | Single source of truth (skill points to agent, never repeats it); cut identity sentences; split only when some branches never need the material (the reference rule). |
| obra/superpowers, writing-skills | not confirmed in fetch | Tests written before drafting; a baseline run without the seat; a refused-rationalization table. |
| wshobson/agents | MIT | Model field from one rule (cheapest tier that passes), with the reason recorded. |
| aaddrick/contrarian | Unlicense | Severity (critical, major, minor) with a verified failure path; a clean result is normal; agent and skill generated from one source with a drift check (`scripts/ship.py`). |
| alirezarezvani/claude-skills, executive-mentor | not confirmed | Held for the red-team skill's harsh level (session C). |
| notmanas questioning-frameworks | | Not found; Brandon to supply a URL if it matters. |
| Claude Code docs (sub-agents, skills) | | Agent descriptions load every session (keep them short); `skills:` preloads in full (do not preload into seats); SKILL.md body loads on trigger, references on demand. |

## Known limits
- Caps are design targets until session B rebuilds the Practice and Simulation Designer and measures.
- Stage 4 runs an interim red team until `.claude/skills/red-team/` exists (session C).
- Orchestrator context is measured with `/context` in an interactive session; headless runs record "not measured".
