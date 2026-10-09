# Build: assessment-competency-designer
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 2)
cluster: learning-and-development | old: Assessment & Competency Designer.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 146,414 shared (~24k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile | sonnet (profile-extractor) | 35,192 | cards |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 23,366 shared (~4.7k per seat) | tests/T*-base.md |
| 3 | drafter | opus | 79,790 | agent.md 11,466 B; reference 5.1 KB; provenance 8.5 KB (43 sourced, 2 inferred, 13 project) |
| 4 | critic employee-harm b | sonnet (profile-critic) | 23,617 | 04-critic-*.md |
| 4 | critic spec+rules a | sonnet (profile-critic) | 22,530 | 04-critic-*.md |
| 4 | critic grounding a | sonnet (profile-critic) | 29,694 | 04-critic-*.md |
| 4 | critic grounding b | sonnet (profile-critic) | 29,699 | 04-critic-*.md |
| 4 | critic employee-harm a | sonnet (profile-critic) | 25,576 | 04-critic-*.md |
| 4 | critic spec+rules b | sonnet (profile-critic) | 26,842 | 04-critic-*.md |
| 4 | critic seams b | sonnet (profile-critic) | 52,189 | 04-critic-*.md |
| 4 | critic seams a | sonnet (profile-critic) | 60,796 | 04-critic-*.md |
| 4 | merger, 6 seats in one agent | sonnet (profile-critic) | 54,671 shared (~9k per seat) | 04-flags.md 4945 B |
| 4 | Fable judge, 6 seats + seams in one agent | fable | 160,426 shared (~27k per seat) | 04-judgment.md |
| 4 | apply judgment edits + 5 neighbor masters | sonnet (general-purpose) | 106,362 | agent.md 12,274 B (7 cues, 5 rejects moved to reference) |
| 5 | with-runs T1-T3 | sonnet (profile-runner) | 17,693 | tests/T*-with.md |
| 5 | grader, 6 seats in one agent | sonnet (profile-grader) | 49,555 shared (~8k per seat) | verdicts: T1-T3 pass |
| 5 | haiku tier check T2, T3 | haiku (profile-runner) | 19,754 | tests/T*-haiku.md |
| 5 | grader, haiku tier check (5 seats in one agent) | sonnet (profile-grader) | 37,318 shared | verdicts |

## Closing (2026-10-09)
- Mode: revise, harsh (every lens twice + employee-harm). Models: frame and judge fable; extract, critics, merger, runners, grader sonnet (haiku for tier checks); drafter opus; edits applied by sonnet.
- Flags: 15 accepted (2 critical), 0 rejected, 1 to Brandon (retry cap: none; escalate by count). Cross-seat seams: profiles/_builds/batch2-seams-judgment.md.
- Tests: T1-T3 pass (see tests.md).
- Model line: sonnet: haiku passed T2 and T3 but hedged on record wording; kept by stakes.
- Open: Core 12.0 KB, near cap: 7 cues and 5 rejects moved to reference/models.md. 01-old-cues card 1% over, accepted. Approval by Brandon pending; next-session check (stage 6 step 7) pending.
