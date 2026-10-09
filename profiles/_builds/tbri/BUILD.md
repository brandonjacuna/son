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
