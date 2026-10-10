# Source and design record: red-team

Written 2026-10-09 (phase 3, session C, Fable). Our own skill; nothing vendored. Ideas mined from the sources below, approved in `memory/skills-plan.md` (A tier, "Mine"); no files copied.

## What it replaces
| Old | Kept | Changed |
|---|---|---|
| profile-build stage 4 interim procedure and the `profile-critic` worker (ran batches 1 to 3, 2026-10-09) | Blind critics with assigned lenses; one lens per critic; 2 KB critic files; a merger at harsh with the "both runs or a verified path" rule; a Fable judge; accept, reject, ask per flag; "a clean result is normal" | Lenses became files any target can use, each with a "for a seat" paragraph, so profile-build no longer carries its own lens text. `profile-critic` retired; `red-team-critic` reads the lens file instead of carrying all lenses. Judge model scales with intensity (session, opus, fable). Added `who-pays` and `loop`. Standard runs skip the merger (the judge reads three critic files directly). |
| Ad hoc red-team passes in workstream notes (for example `company/workstreams/clickup-system/blueprint/06-redteam.md`, 2026-09-16) | Severity ranked, each finding with location, issue, fix, status; clear-cut fixes applied, judgment calls left open for Brandon | Those passes were written by the same session that wrote the plan. Now the critics are blind subagents and the session only orchestrates. |

## Design choices and why
- CLAUDE.md ("Working with Brandon") sets three intensities: light for concept ideation, standard by default, harsh for legal, compliance, and anything touching employees. This skill adds the floor rule, money, safety, external-facing, and hard-to-undo as harsh triggers, the judge-model ladder, the three-pop-up cap, the agent-count announcement at harsh, and the three-concern report (all confirmed by Brandon 2026-10-09, `memory/decisions.md`, `system`). The floor can be overruled only by Brandon, explicitly, and the report logs it.
- The session never critiques its own target. It wrote or carried it; blindness is the whole mechanism.
- Harsh adds the `loop` lens, which reads only a session brief the orchestrator writes, because the risk at harsh is not only the target but the session agreeing with itself (framing adopted, recommendation drift, source selection, missing "not wanted").
- Report leads with at most three concerns ranked by reversibility, because Brandon reads on a walk and reasons from exclusions. Fewer than three is normal: a forced three invites padding.
- Workers are custom agents (measured 2026-10-07: 11k to 25k tokens each against 53k to 66k for general-purpose). Judge is `opus` by default and `fable` at harsh; a caller may raise it (profile-build runs one Fable judge per batch).

## Mined sources
| Source | License | Idea used | Not used |
|---|---|---|---|
| aaddrick/contrarian | Unlicense | Intensity scales with stakes and reversibility; method order (steel-man, assumptions, pre-mortem, inversion, second-order); three severities with a verified failure path before critical or major; anti-invention rules; verdicts `sound with caveats` only when nothing critical or major remains, `needs rework`, `investigate first` | |
| alirezarezvani/claude-skills, executive-mentor | MIT | Three concerns, each framed as a failure already happened, with the earliest warning sign and the cheapest hedge; confidence times impact decides which assumptions count; reversibility read | "Always exactly three, never a clean approval": forces padding, contradicts the clean-result rule |
| notmanas questioning-frameworks | | Not found on GitHub or the web (searched 2026-10-07 and 2026-10-09). The question set in `lenses/failure-path.md` and `lenses/loop.md` is our own | |

## Measured
2026-10-09 self-test, folder `memory/audits/red-team/2026-10-09-red-team-skill/`: standard on this skill (three critics, two lenses each), one `loop` critic on a session brief, light on profile-build stage 4 (one critic), one judge.
| Worker | Model and type | Tokens |
|---|---|---|
| critic failure-path + who-pays | sonnet, general-purpose reading the worker file | 70,932 |
| critic grounding + rules | same | 82,659 |
| critic seams + vagueness | same | 99,796 |
| critic loop | same | 66,139 |
| light critic (stage 4) | same | 67,811 |
| judge | opus, `red-team-judge` custom worker | 41,442 |
| source mining (Sonnet, before the build) | general-purpose | 63,849 |
Total about 493k worker tokens. Flags: skill 3 critic files plus loop raised 0 critical, 8 major (before merging duplicates), 13 minor; judge: 14 accept, 3 reject, 2 ask; verdict "investigate first" pending Brandon's answers. Light on stage 4: 0 critical, 2 major, 4 minor, all six accepted by the session. The custom critic and merger were not exercised (the critics ran before the agent types registered); batch 4 of profile-build measures them.

### Batch 4 of profile-build (2026-10-10): first run with the custom workers
Five design seats: three at standard (one critic per lens pair shared by all three seats), two at harsh (13 critics), one merger, one Fable judge.
| Worker | Count | Tokens each | Total |
|---|---|---|---|
| `red-team-critic`, single seat, one lens (employee harm, loop) | 5 | 20k to 26k | 111k |
| `red-team-critic`, two lenses, two seats | 6 | 42k to 70k | 341k |
| `red-team-critic`, grounding and rules, one seat (opens cards) | 4 | 55k to 70k | 242k |
| `red-team-critic`, two lenses, three seats (standard) | 3 | 50k to 134k | 269k (the grounding critic alone 134k) |
| `red-team-merger`, two seats | 1 | 52k | 52k |
| `red-team-judge` on fable, five seats plus cross-seat seams | 1 | 108k | 108k |
Red team total about 1.12M for five seats (about 225k per seat), against 1.12M to 1.20M for six seats in batches 2 and 3 with general-purpose critics. The custom critic's fixed cost is about 20k, against 66k to 100k for a general-purpose critic in the self-test; the variable cost is what the critic opens (grounding opens cards).

Comparison (state.md asked for it): one Opus general-purpose agent did a single careful review of the image seat's pre-red-team draft, all lenses at once, 82k tokens. Against the harsh panel's merged flags for the same draft:
- Both caught: team members flagged but not held; no penalty-free refusal and no takedown on departure; casting by look or ethnicity; no hold verdict; generative fill passing as retouch; captions unowned; the likeness statute misapplied to living people; HR seats that do not own likeness. The single review rated the casting risk critical where the panel rated it major.
- Only the panel caught: the advocate gate was the drafter's rule and Brandon never saw it (the loop lens; the single review had no session brief); per-person release status readable by coworkers in the brief; the person's right to preview and strike their frame; type-zone and crop ownership across three seats; the signature call duplicating the creative director.
- Only the single review caught: maker terms silent on portfolio use and AI-training use of a person's likeness (applied to R7 after the judge). One single-review flag was an artifact of the comparison setup (reference files not exported).
- Reading: one careful reviewer finds most of the content at about a third of the per-seat cost; the blind panel's margin is the session check, neighbor seams, and second-order privacy items. Keep the panel at harsh; consider one careful reviewer plus the loop and seams lenses for standard seats (Brandon's call; not changed here).

## Known limits
- Worker agents created this session became callable in the same session once their files existed, with no restart. The self-test's critics had already run as general-purpose agents (about 66k to 100k each, against about 12k to 25k measured for custom workers). Log batch 4's custom-worker tokens here.
- Blind subagent critics have not been compared against one careful single review on the same target. Batches 1 to 3 of profile-build (96, 59, and 82 merged flags, nearly all accepted) are the evidence so far; a comparison on one batch 4 seat would settle it.
- The `loop` lens depends on an honest session brief written by the session it audits. It catches what the brief shows and nothing the brief hides; a dishonest brief is a limit, not a bug the lens can fix.
- Harsh on a target with no neighbors or no provenance runs `grounding` and `seams` against the text alone; expect them to come back clean and say so.
