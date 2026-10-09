# Build: hospitality-operations-realist
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 1; session also carried earlier phase 3 work)
cluster: scaling-people | old: Hospitality Operations Realist.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 2 | extract old profile | sonnet (profile-extractor) | 39,661 | 4 cards |
| 0 | frames (all six, one agent) | fable | 151,260 shared | 00-frame.md, 00-tests.md |
| 5 | baselines T1-T3 | sonnet (profile-runner) | 10,442 | tests/T*-base.md |
| 3 | drafter | opus | 80,820 | agent.md 9,985 B; reference 5.5 KB; provenance 5.2 KB (36 sourced old, 3 inferred, 3 project) |
| 4 | critics (grounding, spec+rules, seams) | sonnet (profile-critic) | 28,395 + 26,988 + 35,567 | 0 critical, 6 major, 18 minor |
