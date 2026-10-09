# Provenance: Hospitality Operations Realist

Build-time record. Never loaded at runtime. One row per row id in `agent.md` and each reference file. Card ids refer to `profiles/_builds/hospitality-operations-realist/extract/`. Every source row is carried from the old profile and not re-verified against its original sources this build.

| id | tag | grounding |
|---|---|---|
| C1 | sourced (old) | 01r.1; 01s.1 ("A design is not what it specifies.") |
| C2 | sourced (old) | 01c.1 ("a station that survives only on a calm night has not passed") |
| C3 | sourced (old) | 01c.2 |
| C4 | sourced (old) | 01c.3 |
| C5 | sourced (old) | 01c.4 |
| C6 | sourced (old) | 01c.5; 01s.3 |
| C7 | sourced (old) | old cue 8 core via 01c "Not usable" note; Airtable clause replaced by the workbook rule (frame, Sŏn rules) |
| C8 | sourced (old) | 01c.6; 01s.4 |
| C9 | sourced (old) | old cue 7 core via 01c "Not usable" note; 01-examples Ex. 4; 120 seats and Airtable removed |
| C10 | sourced (old) | 01c.7 |
| C11 | inferred | 01c.8 and 01r.5 (old: inferred); `tool.*` binding is project (frame, Sŏn rules) |
| C12 | sourced (old) | 01c.9; 01s.10 |
| C13 | sourced (old) | 01c.10 |
| C14 | sourced (old) | 01c.11; 01c.12; 01r.6 |
| R1 | sourced (old) | 01r.2 ("find yourself spinning in place and calling for backup") |
| R2 | sourced (old) | 01r.3 ("can no longer keep track of where each dish is") |
| R3 | sourced (old) | 01r.4 |
| R4 | inferred | from the 01c tension (cue 4 vs cue 5), C6, C10 |
| R5 | sourced (old) | 01s.13; 01-examples Ex. 6 |
| R6 | sourced (old) | 01-examples Ex. 1; structure held as proposal, not landed (frame: nothing landed unless decisions.md records it) |
| R7 | sourced (old) | 01-examples Ex. 3; 01s.10 |
| R8 | project | decision 2026-10-07 (pay in menu price is a project not yet begun; frame, Sŏn rules); tempo consequence from 01-examples Ex. 5 with the stated percentage removed |
| R9 | sourced (old) | 01-examples Ex. 7 |
| R10 | project | 01r.7; 01s.5; frame decision 7 |
| R11 | sourced (old) | 01s.15 ("calling a design un-survivable when it is only untested") |
| A1 | sourced (old) | 01r.9 |
| A2 | sourced (old) | 01r.10 |
| A3 | sourced (old) | 01r.11 ("Optimism is a reasonable quality in a person. At the pass, it is a liability.") |
| A4 | sourced (old) | 01r.12 |
| A5 | sourced (old) | 01r.13 (old: sourced/inferred) |
| A6 | inferred | 01r.14 (old: inferred) |
| A7 | project | 01s.11; 01s.14; frame decision 7 |
| M1 | sourced (old) | 01r.15 (quote) |
| M2 | sourced (old) | 01r.16 (quote) |
| M3 | sourced (old) | 01r.17 ("mindless, unvarying repetition"); 01-examples Ex. 3 |
| M4 | sourced (old) | 01r.18; 01s.2 |
| M5 | sourced (old) | 01r.3 (quote) |
| M6 | sourced (old) | 01c.15 (diagnostic procedure) |
| E1 | sourced (old) | 01-examples Ex. 1, scrubbed: V7-as-landed removed, structure marked founder-gated |
| E2 | sourced (old) | 01-examples Ex. 2, scrubbed: V7, David protocol, cooling system, Airtable removed |
| E3 | sourced (old) | 01-examples Ex. 4, scrubbed: four dayparts, 120 seats, Airtable removed; menu chef-gated |
| E4 | sourced (old) | 01-examples Ex. 6, verbatim judgment, trimmed |

Unnumbered material: scope and seams from 01s.5 to 01s.11 and the frame seam table (project); personnel actions recommend-only from Brandon's answer 2026-10-09 (project); output marks from 01s.12 (project); workbook, `tool.*`, `brand.*`/`team.*` bindings and the people-practices pointer from the frame's Sŏn rules and Brandon's answers 2026-10-09 (project); diagnostic sequence and translation note in `models.md` from 01c.15, 01c.13, 01s.16.

Dropped: old Ex. 5 (stated comp percentage; its tempo consequence survives as R8), old Ex. 7 (kept as R9 only), lineage rule 01r.8 (dropped per review), page 08 Service Choreography (reference only; recovery sequences are bindings), Meyer ABCD model (Culture's), V7-as-landed claims throughout.

## Tensions kept open
- Weeds response vs minimum staffing: old cue 4 redeploys spare hands; old cue 5 says a minimum-staffed model has none. Held by R4 (check slack first, fall back to pacing).
- Reliability over brilliance (01r.17, Bourdain) vs the brand's warmth and attunement ambitions. Unreconciled; named in "When to distrust my read".
- Transfer: anchors are elite fine dining and one brasserie memoir; transfer to Sŏn's room is reasoned, not proven.
- Shared sources with Culture Implementer (Meyer, Guidara): the boundary is drawn by object, not by source.
- "Do not own the fix" vs fix-shaped requirements (cross-domain call rule, tempo component in assessment). Held by feeding back one requirement and routing its design to the owner.

## Sources
| card | citation | verified this build |
|---|---|---|
| 01-old-cues | `profiles/_source/scaling-people/Hospitality Operations Realist.md`, cue_table and diagnostic_procedure | read at source; original citations not re-verified |
| 01-old-rules | same file, decision_rules, anti_patterns, mental_models, uncertainty | read at source; original citations not re-verified |
| 01-old-scope | same file, role_anchor, scope, interfaces, outputs, uncertainty | read at source |
| 01-examples | same file, worked_examples 1 to 7 | read at source; scrubbed |
