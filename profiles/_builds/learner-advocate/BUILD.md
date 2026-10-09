# Build: learner-advocate
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 2)
cluster: learning-and-development | old: Learner Advocate.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 146,414 shared (~24k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile | sonnet (profile-extractor) | 32,159 | cards |
| 5 | baselines T1-T3 | haiku (profile-runner) | 13,328 | tests/T*-base.md |
| 3 | drafter | opus | 79,445 | agent.md 9,137 B; reference 2.7 KB; provenance 6.1 KB (24 sourced, 7 project, 1 project+inferred; R11 escalation inferred) |
| 4 | critic grounding | sonnet (profile-critic) | 26,477 | 04-critic-*.md |
| 4 | critic spec+rules (2 seats) | sonnet (profile-critic) | 30,434 shared | 04-critic-*.md |
| 4 | critic seams (2 seats) | sonnet (profile-critic) | 65,039 shared | 04-critic-*.md |
| 4 | merger, 6 seats in one agent | sonnet (profile-critic) | 54,671 shared (~9k per seat) | 04-flags.md 2383 B |
| 4 | Fable judge, 6 seats + seams in one agent | fable | 160,426 shared (~27k per seat) | 04-judgment.md |
