# Build: materials-author-editor
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 2)
cluster: learning-and-development | old: Educational Materials Author and Editor.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 146,414 shared (~24k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile (incl. voice card) | sonnet (profile-extractor) | 34,146 | cards |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 23,366 shared (~4.7k per seat) | tests/T*-base.md |
| 3 | drafter | opus | 81,245 | agent.md 9,674 B; skill/SKILL.md 5,404 B; reference 4.2 KB; provenance 9.7 KB (56 sourced, 3 inferred, 3 project+inferred, 12 project) |
| 4 | critic grounding | sonnet (profile-critic) | 31,097 | 04-critic-*.md |
| 4 | critic spec+rules (2 seats) | sonnet (profile-critic) | 35,552 shared | 04-critic-*.md |
| 4 | critic seams (2 seats) | sonnet (profile-critic) | 65,039 shared | 04-critic-*.md |
| 4 | merger, 6 seats in one agent | sonnet (profile-critic) | 54,671 shared (~9k per seat) | 04-flags.md 2657 B |
| 4 | Fable judge, 6 seats + seams in one agent | fable | 160,426 shared (~27k per seat) | 04-judgment.md |
| 4 | apply judgment edits, 3 seats | sonnet (general-purpose) | 96,127 shared | agent.md, provenance, reference |
