# Build: environmental-signage-specialist
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: build-out | old: 06_Environmental_Signage_Specialist_Profile.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile (01) | sonnet (profile-extractor) | 28,990 | 4 cards (ADA dims and LRV figures marked no source) |
| 3 | drafter | opus | 76,493 | agent.md 9,463 B; reference 4.6 KB; provenance 5.0 KB (36 sourced old, 2 inferred, 7 project) |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 25,379 shared (~5k per seat) | tests/T*-base.md |
| 4 | critic grounding | see worker | 26,465 | |
| 4 | critic spec+rules+seams | see worker | 31,046 | |
| 4 | merger, 6 seats | see worker | 71,092 shared | |
| 4 | Fable judge, 6 seats + seams (rerun after restart) | see worker | 157,169 shared | |
| 4 | apply judgment edits (3 seats) | see worker | 111,042 shared | |
| 5 | with-runs T1-T3 (2 seats, sonnet) | see worker | 34,948 shared | |
| 5 | blind with-runs T1-T3 | see worker | 17,372 | |
| 5 | grader | see worker | 58,864 shared | |
| 5 | haiku tier check T1, T3 | see worker | 33,090 shared | |
| 5 | grader, tier checks | see worker | 30,291 shared | |

## Closing (2026-10-09)
- Mode: revise; moved to build-out. Models: frame and judge fable; scouts, extract, critics, merger, runners, grader sonnet; drafter opus; edits applied by sonnet.
- Flags: 12 accepted. Cross-seat seams: profiles/_builds/batch3-seams-judgment.md.
- Tests: T1-T3 pass (see tests.md).
- Model line: sonnet by stakes (haiku held T1 and T3).
- Open: Cue ids kept after cuts so references hold; code items log to codes/register.yaml as unverified. Approval by Brandon pending; next-session check (stage 6 step 7) pending.
