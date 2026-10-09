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
