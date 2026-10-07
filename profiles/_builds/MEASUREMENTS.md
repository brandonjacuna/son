# Profile build measurements

One row per build. Bytes are measured by `.claude/skills/profile-build/scripts/measure.py`; tokens are bytes / 4 unless marked "usage" (summed from worker usage lines in the build's `BUILD.md`). The per-call load is what a seat costs every time it is used: the agent core, plus the skill if it is a mode.

## Baseline (old seven-stage builder, measured 2026-10-07)
| Seat | Stage files written | Full profile rewrites | Per-call load | Inline tags in load | Plumbing in load | Orchestrator context | Worker tokens | Validation |
|---|---|---|---|---|---|---|---|---|
| Hospitality Craft Educator | 445 KB | 3 (draft 81, tagged 95, revised 95 KB) | 95.0 KB (~23,750 tok) | 16.0 KB (17%) | 6.4 KB (7%) | maxed out (Brandon) | not recorded | stage 6 skipped; stage 7 on the build model |
| Practice and Simulation Designer | 199 KB | 3 (draft 40, tagged 53, revised 53 KB) | 53.0 KB (~13,260 tok) | 9.7 KB (18%) | 5.1 KB (10%) | maxed out (Brandon) | not recorded | stages 6 and 7 skipped |

Measured facts behind the redesign: the tagged and revised files kept 99% of the draft's lines (tagging only appended tags and a tag audit; revision changed about 1% of lines), so two of the three full writes carried no new judgment. In the finished PSD profile, the every-call judgment (role, scope, cues, rules, anti-patterns, outputs) is 23.6 KB with tags, about 19 KB without.

## Caps of the new builder (`.claude/skills/profile-build/`)
Build folder about 75 KB or less (frame 6, sources 6, cards 40, flags 4, tests and BUILD.md about 20). Per-call load 12 KB cap (about 3,000 tokens), 10 KB target. Reference 30 KB, loaded on demand. Orchestrator under 60k tokens for the whole build. These are caps, not results: session B measures the first real build against them.

## Builds
| Date | Seat | Build folder | Cards | Per-call load | Reference | Worker tokens (usage) | Orchestrator context | Tests |
|---|---|---|---|---|---|---|---|---|
| 2026-10-07 | practice-simulation-designer (rebuild, test build) | 93.8 KB (56 KB of it test outputs) | 22.2 KB (+4.7 KB examples) | 11.7 KB (~3,000 tok) | 5.8 KB | 2.21M across 36 workers (frame 157k, extract 520k, draft 90k, red team 545k, test 894k) | not measured; never opened a source or card; session also carried session A | 5/5 on Sonnet (one after a fix); Haiku failed T3 |

## Result of the test build (Practice and Simulation Designer, 2026-10-07)
| Measure | Old builder | New builder | Change |
|---|---|---|---|
| Per-call load (every use of the seat) | 53.0 KB, ~13,260 tok | 11.7 KB, ~3,000 tok | -78% |
| Stage files written | 199 KB, profile written 3 times | 94 KB, profile drafted once (38 KB without test outputs) | -53% |
| Orchestrator context | maxed out | sources and cards never opened; reads were frame, source list, core, flags, verdict tables | the stated pain point removed |
| Worker tokens | not recorded (one context) | 2.21M across 36 subagents | new cost, now visible |
| Validation | stages 6 and 7 skipped | 5 blind critics, Fable judge (15 flags accepted, incl. 3 critical on employee records and consent), 5 tests vs baseline | lever restored |
| Grounding re-checked | none | 4 sources re-read; 2 old citations corrected; 2 overclaims cut | |

Worker cost driver: each subagent carries about 50k tokens of fixed overhead (system prompt, CLAUDE.md, tools), so 36 agents is most of the 2.21M. Batching small jobs (finding F7 in the build's BUILD.md) should cut it by roughly a third without losing blindness where it matters.
