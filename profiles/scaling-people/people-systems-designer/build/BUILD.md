# Build: people-systems-designer
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: scaling-people | old: People Systems Designer.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile (01) | sonnet (profile-extractor) | 40,796 | 4 cards (examples 2, 5, 6 not copied: cap) |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 25,379 shared (~5k per seat) | tests/T*-base.md |
| 3 | drafter | opus | 80,107 | agent.md 11,043 B; reference, provenance |
| 4 | critic employee-harm a (3 seats) | see worker | 33,815 shared | |
| 4 | critic seams a (3 seats) | see worker | 43,856 shared | |
| 4 | critic employee-harm b (3 seats) | see worker | 39,223 shared | |
| 4 | critic seams b (3 seats) | see worker | 38,516 shared | |
| 4 | critic spec+rules a (3 seats) | see worker | 49,625 shared | |
| 4 | critic spec+rules b (3 seats) | see worker | 56,053 shared | |
| 4 | critic grounding b (3 seats) | see worker | 88,941 shared | |
| 4 | critic grounding a (3 seats) | see worker | 89,544 shared | |
| 4 | merger, 6 seats | see worker | 71,092 shared | |
| 4 | Fable judge, 6 seats + seams (rerun after restart) | see worker | 157,169 shared | |
| 4 | apply judgment edits (3 seats + neighbor) | see worker | 121,983 shared | |
| 5 | with-runs (discarded: brief let runner see catches) | see worker | 18,450 | |
| 5 | blind with-runs T1-T3 | see worker | 18,751 | |
| 5 | grader | see worker | 58,864 shared | |
| 5 | reruns after fixes + new bar T2 (with and base) | see worker | 41,200 shared | |
| 5 | grader, reruns | see worker | 23,255 shared | |

## Closing (2026-10-09)
- Mode: revise; harsh. Models: frame and judge fable; scouts, extract, critics, merger, runners, grader sonnet; drafter opus; edits applied by sonnet.
- Flags: 14 accepted. Cross-seat seams: profiles/_builds/batch3-seams-judgment.md.
- Tests: T1-T3 pass (see tests.md).
- Model line: sonnet by stakes.
- Open: T2 and T3 passed after A3 and C10 fixes; core at 12.2 KB, near cap; M1 card wording (P14) left as an open item. Approval by Brandon pending; next-session check (stage 6 step 7) pending.
