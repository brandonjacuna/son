# Source and design record: red-team

Written 2026-10-09 (phase 3, session C, Fable). Our own skill; nothing vendored. Ideas mined from the sources below, approved in `memory/skills-plan.md` (A tier, "Mine"); no files copied.

## What it replaces
| Old | Kept | Changed |
|---|---|---|
| profile-build stage 4 interim procedure and the `profile-critic` worker (ran batches 1 to 3, 2026-10-09) | Blind critics with assigned lenses; one lens per critic; 2 KB critic files; a merger at harsh with the "both runs or a verified path" rule; a Fable judge; accept, reject, ask per flag; "a clean result is normal" | Lenses became files any target can use, each with a "for a seat" paragraph, so profile-build no longer carries its own lens text. `profile-critic` retired; `red-team-critic` reads the lens file instead of carrying all lenses. Judge model scales with intensity (session, opus, fable). Added `who-pays` and `loop`. Standard runs skip the merger (the judge reads three critic files directly). |
| Ad hoc red-team passes in workstream notes (for example `company/workstreams/clickup-system/blueprint/06-redteam.md`, 2026-09-16) | Severity ranked, each finding with location, issue, fix, status; clear-cut fixes applied, judgment calls left open for Brandon | Those passes were written by the same session that wrote the plan. Now the critics are blind subagents and the session only orchestrates. |

## Design choices and why
- Three intensities with a floor (CLAUDE.md "Working with Brandon"): light for ideation, standard by default, harsh for legal, compliance, money, employees. The floor can be overruled only by Brandon, explicitly, and the report logs it.
- The session never critiques its own target. It wrote or carried it; blindness is the whole mechanism.
- Harsh adds the `loop` lens, which reads only a session brief the orchestrator writes, because the risk at harsh is not only the target but the session agreeing with itself (framing adopted, recommendation drift, source selection, missing "not wanted").
- Report leads with at most three concerns ranked by reversibility, because Brandon reads on a walk and reasons from exclusions. Fewer than three is normal: a forced three invites padding.
- Workers are custom agents (measured 2026-10-07: 11k to 25k tokens each against 53k to 66k for general-purpose). Judge is `opus` by default and `fable` at harsh, by the model policy (judgment on design; Fable only where stakes earn it).

## Mined sources
| Source | License | Idea used | Not used |
|---|---|---|---|
| aaddrick/contrarian | Unlicense | Intensity scales with stakes and reversibility; method order (steel-man, assumptions, pre-mortem, inversion, second-order); three severities with a verified failure path before critical or major; anti-invention rules; verdicts `sound with caveats` only when nothing critical or major remains, `needs rework`, `investigate first` | |
| alirezarezvani/claude-skills, executive-mentor | MIT | Three concerns, each framed as a failure already happened, with the earliest warning sign and the cheapest hedge; confidence times impact decides which assumptions count; reversibility read | "Always exactly three, never a clean approval": forces padding, contradicts the clean-result rule |
| notmanas questioning-frameworks | | Not found on GitHub or the web (searched 2026-10-07 and 2026-10-09). The question set in `lenses/failure-path.md` and `lenses/loop.md` is our own | |

## Measured
- 2026-10-09 self-test (standard on this skill, light on profile-build stage 4, plus one loop critic on a session brief): see the "Self-test" section below once filled.

## Known limits
- New worker agents are callable by `subagent_type` only after a session restart; the self-test ran them as general-purpose agents reading the worker files (costlier). Batch 4 of profile-build is the first run with the custom workers; log its tokens here.
- The `loop` lens depends on an honest session brief written by the session it audits. It catches what the brief shows and nothing the brief hides; a dishonest brief is a limit, not a bug the lens can fix.
- Harsh on a target with no neighbors or no provenance runs `grounding` and `seams` against the text alone; expect them to come back clean and say so.
