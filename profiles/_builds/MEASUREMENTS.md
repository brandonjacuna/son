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
