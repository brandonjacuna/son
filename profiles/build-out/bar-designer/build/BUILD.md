# Build: bar-designer
mode: new | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: build-out | old: none (Tobin Ellis kb in company/workstreams/build-out/kb/bar/tobin-ellis/)

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract Tobin Ellis kb (01-03) | sonnet (profile-extractor) | 29,151 | 3 cards, 8.7 KB (book dimensions blank in kb; checklist all derived) |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 25,379 shared (~5k per seat) | tests/T*-base.md |
| 1 | scout, targets 1-5 in one agent | sonnet (general-purpose) | 81,854 | 01-sources.md |
| 3 | drafter | opus | 78,195 | agent.md 9,977 B; reference 5.6 KB; provenance 9.8 KB (35 sourced, 23 inferred, 9 project) |
| 5 | T2 replaced once (baseline also passed the mirror test) | n/a | n/a | tests.md |
| 2 | extract TAS (05) | see worker | 20,760 | |
| 2 | extract food code (04), with trim | see worker | 36,254 | |
| 2 | extract bev and glass (06), with trim | see worker | 26,871 | |
| 4 | critic grounding | see worker | 32,576 | |
| 4 | critic spec+rules+seams | see worker | 42,736 | |
| 4 | merger, 6 seats | see worker | 71,092 shared | |
| 4 | Fable judge, 6 seats + seams (rerun after restart) | see worker | 157,169 shared | |
| 4 | apply judgment edits (3 seats) | see worker | 111,042 shared | |
| 5 | with-runs T1-T3 (2 seats, sonnet) | see worker | 34,948 shared | |
| 5 | blind with-runs T1-T3 | see worker | 21,266 | |
| 5 | grader | see worker | 58,864 shared | |
| 5 | reruns after fixes + new bar T2 (with and base) | see worker | 41,200 shared | |
| 5 | grader, reruns | see worker | 23,255 shared | |
| 5 | haiku tier check T1, T3 | see worker | 33,090 shared | |
| 5 | grader, tier checks | see worker | 30,291 shared | |

## Closing (2026-10-09)
- Mode: new (Tobin Ellis kb + Austin, Texas, TAS, sake, glass wash research). Models: frame and judge fable; scouts, extract, critics, merger, runners, grader sonnet; drafter opus; edits applied by sonnet.
- Flags: 12 accepted. Cross-seat seams: profiles/_builds/batch3-seams-judgment.md.
- Tests: T1-T3 pass (see tests.md).
- Model line: sonnet: haiku missed the health-code call and the station method.
- Open: Station count now runs on the pro forma method (book note); T2 replaced once; working intent is a radius shotgun and peninsula hybrid (not final). Approval by Brandon pending; next-session check (stage 6 step 7) pending.
