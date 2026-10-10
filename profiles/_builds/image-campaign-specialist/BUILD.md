# Build: image-campaign-specialist
mode: revise | started: 2026-10-10 | orchestrator: Opus 5.5 (batch 4)
cluster: design | old: design-translating-team 07

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 5 seats (one agent) | fable | 180,151 shared (~36k per seat) | 00-frame.md, 00-tests.md; 15 pop-ups answered 2026-10-10 |
| 1 | scout (3 outside targets, one agent) | sonnet | 157,198 shared | 01-sources.md rows; Brandon approved the list 2026-10-10 |
| 2 | extractors (14 across the batch) | sonnet (profile-extractor) | not recorded (worker restart lost the usage lines) | extract/*.md |
| 2 | extractors: print production 22,207; likeness 22,197; ownership and time 19,922 | sonnet (profile-extractor) | 64,326 | 3 cards |
| 5 | baselines T1-T5, all 5 seats in one runner | sonnet (profile-runner) | 35,786 shared (~7k per seat) | tests/T*-base.md |
| 3 | drafter | opus | 88,573 | agent.md 10.1 KB; reference 8.8 KB; provenance 10.2 KB (50 sourced, 9 inferred, 9 project); description trimmed by the orchestrator |
| 4 | note | | | harsh seams/vagueness critic b read part of 00-frame.md while grepping; cited nothing from it (logged as a minor blindness breach) |
| 4 | 16 critics across the batch (3 standard shared by 3 seats; 13 harsh for web-ui and image) | sonnet (red-team-critic, custom) | 848,980 batch total (20k to 134k each; see red-team SOURCE.md) | 04-critic-*.md |
| 4 | merger, both harsh seats | sonnet (red-team-merger) | 52,360 shared | 04-flags.md |
| 4 | Fable judge, 5 seats + cross-seat seams (one agent) | fable (red-team-judge) | 107,801 shared | 04-judgment.md; batch4-seams-judgment.md |
| 4 | apply judged edits, 5 seats + registry (one agent) | sonnet | 159,067 shared | edits to masters and REGISTRY.md; lint 0 errors |
| 5 | with-runs T1-T5, 3 seats in one runner | sonnet (profile-runner) | 60,208 shared (~20k per seat) | tests/T*-with.md |
| 5 | grader, 3 seats | sonnet (profile-grader) | 43,177 shared | 14 of 15 pass; editorial T2 replaced (stage 0 alignment miss) |

## Closing (2026-10-10)
- Shipped to `.claude/agents/image-campaign-specialist.md`. Mode revise (07). Agent, sonnet. Red team harsh: 3 criticals and 10 majors merged; 13 accepted, 1 rejected, 1 critical ask answered by Brandon (the frontline-advocate check runs before any staff shoot is planned). Tests 5/5 on sonnet (T3 thin: no image attached). Model line: sonnet by stakes (harsh people seat), no haiku check. Comparison single review added portfolio and AI-training terms to R7.
- Approval by Brandon pending; next-session check (stage 6 step 7) pending.
