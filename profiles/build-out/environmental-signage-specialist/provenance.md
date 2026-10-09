# Provenance: Environmental Signage Specialist

Build-time record. Never loaded at runtime. One row per row id in `agent.md` and each reference file. Card ids refer to `profiles/_builds/environmental-signage-specialist/extract/`. Every `sourced (old)` row is carried from the old profile; its original sources (the design-translator corpus, Last 10 Percent Checklists s.8) were not re-read this build.

| id | tag | grounding |
|---|---|---|
| C1 | sourced (old) | 01.c1, 01.r1 |
| C2 | sourced (old) | 01.c2, 01.r2 |
| C3 | sourced (old) | 01.c3 |
| C4 | sourced (old) | 01.c4; the 70 percent figure dropped from the core (no primary source), kept in M4 as `unverified`; LRV definition from frame decision 3 |
| C5 | sourced (old) | 01.c5; ratio demoted to `unverified` (no independent source) |
| C6 | sourced (old) | 01.c6 |
| C7 | sourced (old) | 01.c7 |
| C8 | sourced (old) | 01.c11 |
| C9 | sourced (old) | 01.c12, 01.m2 |
| C10 | sourced (old) | 01.c13 |
| C11 | sourced (old) | 01.c8; 40/60 ratio moved to M4 as `unverified` |
| C12 | sourced (old) | 01.c9; current editions not checked |
| C13 | sourced (old) | 01.c14, 01.a3 |
| C14 | sourced (old) | 01.c15 |
| C15 | sourced (old) | 01.c16; project: brand source is `company/brand/design-system` (frame Sŏn rules) |
| C16 | project | build-out CLAUDE.md s.3 (dimensions trace to a source); frame "What NOT" (no invented specs); 01.s5 marked no source |
| R1 | sourced (old) | 01.r1, 01.a1 |
| R2 | sourced (old) | 01.r2, 01.m1 |
| R3 | sourced (old) | 01.r3; journey list from frame decision 2 |
| R4 | project | Brandon's answers 2026-10-09 (arrival sequence is standing intent, P0 constraint, not the page 06 nine-beat); behavior from 01.s6 and 01.examples ex. 2 |
| R5 | project | Brandon's answers 2026-10-09 (codes); frame decision 5; 01.c10, 01.r4 for the audit items; no dimension source exists (01.c10) |
| R6 | project | frame decision 6; 01.s5 (square footage, no source); build-out phase lock |
| R7 | project | frame decision 7; brand decision 2026-10-07 (`memory/decisions.md`); build-out CLAUDE.md s.6; 01.s3, 01.s7 |
| R8 | sourced (old) | 01.r5 |
| R9 | sourced (old) | 01.r6 |
| R10 | sourced (old) | 01.d1, 01.s4; frame Sŏn rules (no AI imagery on a public surface) |
| A1 | sourced (old) | 01.a1 |
| A2 | sourced (old) | 01.a2 |
| A3 | sourced (old) | 01.a3 |
| A4 | sourced (old) | 01.a5 |
| A5 | inferred | from 01.a4, retargeted from "Sŏn spatial sequence" to Brandon's arrival intent (R4) |
| A6 | project | Brandon's answers 2026-10-09 (no reviving references); brand decision 2026-10-07 |
| M1 | sourced (old) | 01.m1 |
| M2 | sourced (old) | 01.m2, 01.c12 |
| M3 | sourced (old) | 01.m3 |
| M4 | inferred | from 01.c4, 01.c5, 01.c6, 01.c8; figures carried as `unverified` (no source) |
| P1 | sourced (old) | 01.r7, 01.c5 to 01.c8 |
| P2 | sourced (old) | 01.r7, 01.m1, 01.a5, 01.c13 |
| P3 | sourced (old) | 01.r8 |
| P4 | sourced (old) | 01.r9 |
| P5 | project | R5 grounding; 01.c10 |
| P6 | sourced (old) | 01.r7, 01.c15 |
| E1 | sourced (old) | 01.examples ex. 1, near verbatim |
| E2 | sourced (old) | 01.examples ex. 2; "patio is the primary brand surface" and "deferred to canon" rewritten to hypothesis and Brandon's intent (R4, R6) |
| E3 | sourced (old) | 01.examples ex. 3; retired tool names and design-team seat removed per orchestrator note |

Tags: `sourced` (an extraction row with a quote), `sourced (old)` (carried from a prior profile, not re-verified), `inferred` (reasoned from named rows), `project` (a Sŏn fact or rule, with its location).

## Tensions kept open
- Old profile vs. Brandon's answers on the arrival: 01.s6 calls it a locked nine-beat sequence from brand canon; Brandon keeps only the maitre d at the porch steps and a one-sign building as standing intent. The seat holds the intent (R4) and drops the sequence (A6).
- Patio as primary brand surface: 01.s5 states it with square footage and no source; the frame makes it a hypothesis. The seat lists it for the site walk (R6, E2).
- Legibility figures: the old profile tags them sourced to Checklist s.8, the card marks them secondhand with no primary source. The seat computes legibility (C4, C5) but holds every number `unverified` (M4).
- Codes: the old profile audits ADA at schedule level with no dimensions; Brandon now asks the seat to read TAS and the Austin sign code itself. The seat reads and logs as `unverified`, but nothing has yet been read (distrust line 2).

## Sources
| card | citation | verified this build |
|---|---|---|
| 01-old-scope | profiles/_source/design-translating-team/06_Environmental_Signage_Specialist_Profile.md (role_anchor, scope, interfaces, project_block) | yes (read at source) |
| 01-old-rules | same file (decision_rules, anti_patterns, mental_models, procedures) | yes |
| 01-old-cues | same file (cue_table, critique Pass 2) | yes; underlying checklist corpus not read |
| 01-examples | same file (worked_examples 1 to 3) | yes, verbatim |
