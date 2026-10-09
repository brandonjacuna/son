# Build: tbri
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 2)
cluster: learning-and-development | old: TBRI.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 146,414 shared (~24k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile | sonnet (profile-extractor) | 32,439 | cards |
| 3 | drafter | opus | 74,377 | agent.md 10,069 B; reference 5.4 KB; provenance 6.5 KB (41 sourced, 1 inferred, 8 project) |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 23,366 shared (~4.7k per seat) | tests/T*-base.md |
| 4 | critic spec+rules | sonnet (profile-critic) | 20,249 | 04-critic-*.md |
| 4 | critic employee-harm | sonnet (profile-critic) | 22,875 | 04-critic-*.md |
| 4 | critic grounding | sonnet (profile-critic) | 28,065 | 04-critic-*.md |
| 4 | critic seams | sonnet (profile-critic) | 48,936 | 04-critic-*.md |
| 4 | merger, 6 seats in one agent | sonnet (profile-critic) | 54,671 shared (~9k per seat) | 04-flags.md 3101 B |
| 4 | Fable judge, 6 seats + seams in one agent | fable | 160,426 shared (~27k per seat) | 04-judgment.md |
| 4 | apply judgment edits, 3 seats | sonnet (general-purpose) | 96,127 shared | agent.md, provenance, reference |
| 5 | with-runs T1-T3 | sonnet (profile-runner) | 17,883 | tests/T*-with.md |
| 5 | grader, 6 seats in one agent | sonnet (profile-grader) | 49,555 shared (~8k per seat) | verdicts: T1-T3 pass |
| 5 | haiku tier check T1, T3 | haiku (profile-runner) | 19,992 | tests/T*-haiku.md |
| 5 | grader, haiku tier check (5 seats in one agent) | sonnet (profile-grader) | 37,318 shared | verdicts |

## Closing (2026-10-09)
- Mode: revise + employee-harm lens. Models: frame and judge fable; extract, critics, merger, runners, grader sonnet (haiku for tier checks); drafter opus; edits applied by sonnet.
- Flags: 9 accepted (1 critical: disclosure routing without consent), 0 rejected. Cross-seat seams: profiles/_builds/batch2-seams-judgment.md.
- Tests: T1-T3 pass (see tests.md).
- Model line: sonnet: haiku T1 allowed a consented record of a disclosure.
- Open: none Approval by Brandon pending; next-session check (stage 6 step 7) pending.
