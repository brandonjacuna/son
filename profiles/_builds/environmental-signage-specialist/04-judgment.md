# Stage 4 judgment: environmental-signage-specialist
Read: 00-frame.md (Brandon's answers 2026-10-09), 04-flags.md, agent.md (9,394 bytes), batch3-seams.md, decisions 2026-10-09 (build-out), `company/workstreams/build-out/CLAUDE.md`, `.claude/hooks/guard.py` (write rules), `codes/register.yaml` (exists).
Size: room; G4 and G12 cut, G5, G6, G11 add.

## Flags
| id | ruling | edit |
|---|---|---|
| G1 | accept | R5 add: "The code text is read at opus (build-out CLAUDE.md s.4): either this seat runs at opus, set by the stage 5 tests, or the caller runs the read through an opus subagent and hands the finding here to file." The `model:` line stays for stage 5. |
| G2 | accept the fallback; the premise is wrong | Verified: `guard.py` blocks only locked `phases/` folders and the protected phase controls; `codes/register.yaml` exists and is writable in P0 (build-out CLAUDE.md s.2 names it). R5: "append each finding to the existing `codes/register.yaml` (Edit, never a new file); if the write is refused, log it to `research/raw/YYYY-MM-DD-<topic>.md` for `/consolidate`". |
| G3 | accept | Output, first line add: "Every output is labeled CONCEPT / NOT FOR CONSTRUCTION." |
| G4 | accept | Cut C7, C8, C10, C11, C14 (11 cues remain). Move C7 (viewing angle) and C10 (drawdown samples) to `reference/models.md`; C14 (schedule version) becomes a line in the pre-fabrication checklist there. Renumber. |
| G5 | accept, with S14 | Add seams row: "architect, MEP engineer (people) | sign power and illumination circuits, facade structure and loads, any facade change | this seat states intent and marks power and load `unverified`; they engineer it". Keep the fabricator row for shop drawings. |
| G6 | accept, with S14 | R5 add: "The required-postings and life-safety list is never declared complete here; a missing category is flagged `unverified`, and the legally required list comes from counsel through hr-systems-designer." |
| G7 | accept | R1: "because legibility and glare are proven only on the wall". A4: "raking" becomes "directional". provenance.md: C1, R1, A3, C9 `inferred (old)`. |
| G8 | accept | C8 is cut (G4); fold into C9 "do": "; finish (matte, satin) is `unverified` until a sample is viewed in site light". R5: "(TAS, the state's accessibility rules, enforced by TDLR; unverified until read)". C12 already carries `unverified`. |
| G9 | accept | A6: "Retired brand pages and V7 treated as canon: reference only, never a source." R7: "no pattern, cultural tie-in, or experiential material from retired pages" stays (it names no page). |
| G10 | accept | Scope add: "Writes: Edit only on `codes/register.yaml` and `research/raw/`; nothing else." |
| G11 | accept, with S13 | Scope, Surfaces: "Not menus, print, packaging, uniforms, or the bar top. Wall-mounted menu boards and back-bar graphics are mine; `bar-designer` owns their geometry." Output add: "A specification is marked "not cleared for release" until the pre-fabrication review passes; Brandon releases." |
| G12 | accept | Delete A1 and A2. R8 moves to Output as the critique shape ("sharpest finding first, each rated foundational, structural, or surface, the single most important fix first, no redesign"). R9 folds into Output: "findings that need investigation are listed as open, never dismissed". |

Counts: accept 12, reject 0, ask 0.

## Seams touching this seat (ruled in batch3-seams-judgment.md)
- S13: this seat owns back-bar graphics and wall-mounted menu boards; bar top is Brandon's until assigned (G11 edit, plus the bar-designer side).
- S14: architect and MEP own power, structure, and facade changes; counsel through hr-systems-designer owns the required-postings list (G5, G6 edits).

## Does it do the frame's job?
Yes. It judges a sign on the wall at real distance and light, maps every decision to material and mounting, holds the arrival intent as a P0 constraint, and files code findings as unverified at the right model; with G4 and G12 the distinctive rules are no longer buried in generic signage hygiene.
