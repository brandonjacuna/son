# Provenance: Design Brief Translator

Build-time record. Never loaded at runtime. One row per row id in `skill/SKILL.md` and each reference file. The tag is the row's primary grounding; secondary grounding follows in the same cell. Card ids: `01c` cues, `01p` protocol, `01r` rules, `01s` scope, `01ex` examples (all from the old 01 profile), `02` old Platform Prompt Specialist, `03` old Design Director, `04` the Sŏn design system (live source), `05` old Brand Identity rows. Frame = `profiles/_builds/design-brief-translator/00-frame.md`.

## skill/SKILL.md
| id | tag | grounding |
|---|---|---|
| G1 | project | frame decision 1; auto-trigger scope decision 2026-10-07 (as cited in the frame); cases from 01c.2, 01c.9; "new surface" definition: Fable judge 2026-10-10, V1 |
| G2 | project | frame decision 1; Brandon 2026-10-10 (not wanted: fire on edits); frame seam `artifact-design` (internal tracker or dashboard never triggers); brief amendment line: Fable judge 2026-10-10, S5 (X3); learning-studio and operations pages added to "not needed": Fable judge 2026-10-10, S1 (X7) |
| G3 | project | frame decision 2 and founder-seat seam; Brandon 2026-10-10 (not wanted: touch investor or founder material); frame seam `intake`; sourced (old) 03.10 for the pure-content return; "any figure from the Investor Review workbook": Fable judge 2026-10-10, FP2 |
| R1 | sourced (old) | 01r.1, 01r.2, 01p.1, 01r.12, 01r.13; frame decision 3 |
| R2 | sourced (old) + project | 01r.7, 01c.4, 01s.5, 01s.7, 03.8, 01r.16; sourced 04.11 (open decisions stay gaps); frame decision 2; "prices" added: Fable judge 2026-10-10, FP2; brand copy gaps "owner: Brandon": Brandon 2026-10-10 (X5) |
| R3 | sourced (old) | 01r.3, 01r.4, 01s.6, 01s.9; sourced 04.3 (no ninth color); frame decision 4 (eight-color system) |
| R4 | sourced (old) | 01r.5, 01r.6, 01c.3, 01c.8; sourced 04.4 (theme via `data-theme`, system never selects); frame decision 5 |
| R5 | project | frame decision 8; Brandon 2026-10-10 (son-design guide reference only, never triggers); sourced (old) 01r.9, 01s.4, 01c.10, 01r.17, 02.12; card 04 tension (company name, daypart code names); "holds the brand's rules..." wording: Fable judge 2026-10-10, G2; company-name flag and daypart-only-where-customer-facing (moved to `reference/makers.md` M12): Fable judge 2026-10-10, G1 |
| R6 | project | Korean canon line, `memory/decisions.md` 2026-10-07 `brand`, as stated in frame decision 8; card 04 tension (Card.prompt sample term); operative test wording: Fable judge 2026-10-10, V4 and RU1 |
| R7 | sourced (old) | 03.1, 03.2, 03.3, 03.4, 03.6, 01c.7; frame decision 6 |
| R8 | sourced (old) | 01r.8, 01c.9, 03.5, 03.7; frame decision 6 |
| R9 | sourced | 04.2, 04.9; sourced (old) 02.7; frame decision 7 (paths, never an invented value); paths checked to exist this build; words-by-token-role for makers that cannot read the repo: Fable judge 2026-10-10, FP3; immersive-retired sentence moved to `reference/makers.md` M13 for the size cap |
| R10 | sourced (old) | 02.4, 02.5 (first clause only); frame decision 7 |
| R11 | project | Brandon 2026-10-10 (no AI imagery anywhere, mood by real photographs and words); sourced 04.10 (no images shipped, AI and stock banned); no-real-source gap clause: Fable judge 2026-10-10, WP3 |
| R12 | sourced (old) | 05.1, 05.2, 05.3, 05.4; Brandon 2026-10-10 moves the row here |
| R13 | sourced + project | 04.12; project: CLAUDE.md phase lock (P0 until the lease is signed); card 04 tension; lease recorded in `memory/decisions.md` or confirmed by Brandon, drop "check live": Fable judge 2026-10-10, FP1; rule binds every external surface until the lease is signed: Brandon 2026-10-10 (G3) |
| R14 | sourced (old) | 01s.11 |
| R15 | project | Brandon 2026-10-10 (drop every tool prompt except Claude Code; grammar to `kb/tools/`); against sourced (old) 01s.2, see tensions; "not yet written; list it as a gap": Fable judge 2026-10-10, G4 |
| A1 | project | frame decision 1 (novice error) |
| A2 | sourced (old) | 01r.3, 01r.10; sourced 04.3 |
| A3 | sourced (old) | 02.2, 02.3; frame decision 7 (novice error) |
| A4 | sourced (old) | 01r.8; frame decision 6 (novice error) |
| A5 | sourced (old) | 01r.14, 01r.15, 01s.1, 01p.15 |
| A6 | project | frame seam `creative-director`; sourced (old) 02.11 |

Unnumbered parts of SKILL.md: procedure step 2 from 01c.6 and 01p.2; step 4 "take any creative-director reason on file" project (Fable judge 2026-10-10, S5, X3); step 7 from 01p.4 and 04.8, with "names the observation and the routed seat" project (Fable judge 2026-10-10, V3); step 8 from Brandon 2026-10-10 (ask only when the answer changes the brief) and 01c.11, 01s.10, with the ask test project (Fable judge 2026-10-10, V2); output block from 01s.12 and 01s.13, with the Gaps owner/proceeds-waits clause project (Fable judge 2026-10-10, WP1) and the Sequence line project (Fable judge 2026-10-10, S3, X2); the audit check from 01p.14 and 01p.15.

## reference/extraction.md
| id | tag | grounding |
|---|---|---|
| X1 | sourced (old) | 01r.11, 01c.2 |
| X2 | sourced (old) | 01c.5 |
| X3 | sourced (old) | 01p.6 |
| X4 | sourced (old) | 01p.9 |
| X5 | sourced (old) | 01p.7; 01ex example 2 (accent under 10 percent); "colors from the eight" inferred from 04.3 |
| X6 | sourced (old) | 01p.8; "faces from `tokens/`" inferred from 04.2 |
| X7 | sourced (old) | 01p.12 |
| X8 | inferred | from 01r.3, card 01p tension and not-usable note (layers 5 and 6), 04.3, and the Korean canon line (frame decision 8); no source says which layers to drop |
| X9 | sourced (old) | 01p.13, 01r.4, 01s.12 |
| X10 | sourced (old) | 01s.9, 01r.15, 01r.10 |
| X11 | sourced (old) | 01r.6, 01p.12 |
| X12 | inferred | premium row from 01ex example 3 and 01r.5; clean, modern, and warm rows reasoned from 01r.5 (space ratio, palette discipline, type register) and X3 to X6; no source maps them |
| X13 | sourced | 04.4; project: code names not written (frame decision 8, card 04 tension) |

## reference/makers.md
| id | tag | grounding |
|---|---|---|
| M1 | project | frame seam table and decision 6 (five owners, `artifact-design`, `materials-author-editor`, signage scope, founder seats); sourced (old) 03.2 (medium map); "fabricator" as signage maker inferred; menus row and signage menu-board clause (Brandon 2026-10-10: menus wait for a dedicated seat) and Fable judge 2026-10-10, S1 (X1); long-form reading pages on screen row: Fable judge 2026-10-10, X6; learning-studio and operations row replaces the `materials-author-editor` row: Fable judge 2026-10-10, S2, FP4 (X7) |
| M2 | inferred | from card 03 tension (identity work has no owner in the new route list) and card 01s tension (Brand Identity retires); the frame does not assign it |
| M3 | sourced (old) | 03.5, 03.4 |
| M4 | sourced (old) | 03.6 (tagged inferred in the old profile) |
| M5 | sourced | 04.1, 04.4, 04.5, 04.6, 04.7, 04.8, 04.10 |
| M6 | sourced (old) | 02.8, 02.9; token names in place of values from frame decision 7 and 04.2 |
| M7 | sourced (old) | 02.3, 02.1 |
| M8 | inferred | from 02.6 and 02.4; card 02 tension: the source is silent on Sŏn's register passing as on-brand; acceptance check reasoned from 04.3 |
| M9 | sourced (old) | 05.1, 05.2, 05.3, 05.4, 05.5, 05.6; Brandon 2026-10-10; "named gap if the system lacks Pantone" inferred from R2 |
| M10 | project | Brandon 2026-10-10 (tool prompts; no AI imagery); sourced (old) 02.10 |
| M11 | sourced (old) | 03.9, 03.13, 03.11, 01s.3 |
| M12 | project | R5 canon-conflict sentence moved here for the size cap; company-name flag and daypart-only-where-customer-facing: Fable judge 2026-10-10, G1 |
| M13 | project | R9 immersive-retired sentence moved here for the size cap; sourced 04 (card 04 tension: index lists retired immersive components) |

## reference/examples.md
| id | tag | grounding |
|---|---|---|
| E1 | sourced (old) | 01ex example 2, adapted per the card note: route to `editorial-layout-specialist`, color and type layers reduced to coverage and mechanism, materiality and era layers dropped |
| E2 | sourced (old) | 01ex example 3; function-line and placement exclusion added from the frame's signage seam |
| E3 | sourced (old) | 02.13, adapted: values replaced by token paths (frame decision 7), propose-three dropped (frame: bloat), M8 check added |
| E4 | sourced (old) | 03.6, 03.7 (old example 2, a case the card describes); real photographer and no generated frame from Brandon 2026-10-10 |

Counts: 54 ids. sourced 37 (4 from the live design system card, 33 sourced (old)), inferred 4, project 13 (counts before the 2026-10-10 judge edits, plus M12 and M13).

## Not used
- 05.7, 05.8, 05.9 (force convergence on a spread, refuse round five): the point of view and what dies belong to `creative-director`; this seat never selects. 05.8's "round five" reading was inferred on its card.
- 02.5 second clause (propose several directions first): the three-variant rule is bloat per the frame.
- 01c.1 as applied to investor decks; 01ex example 1 (investor material, shape only).

## Tensions kept open
- Trigger gate vs old practice: the old profile briefed every input; the gate rests only on the 2026-10-07 decision and Brandon's 2026-10-10 answer, with no card evidence. Held by G1 and G2; tests should probe the edge (a new state added to an existing component).
- Name the gap vs ask Brandon (01c.11, 01s.10 vs Brandon 2026-10-10): held by step 8, ask only when the answer changes the brief, otherwise state assumptions.
- Seven layers vs a closed design system (card 01p tension): the old source does not say which layers to drop. Held by X3 to X8, which are inferred cuts.
- Success criteria judged by eye (card 01p) vs a coding maker that needs checkable criteria: held by step 7 and 04.8; no source gives a test a coding maker can run.
- Paste the token block (02.7) vs hand files by path (frame decision 7): path wins for Sŏn.
- "You do not write the prompt" (01s.2) vs Brandon 2026-10-10 Claude Code exception: Brandon's answer wins; R15.
- Claude's house style reads right for hospitality (02.6), so a default can pass as on-brand: the source is silent for Sŏn; M8 is inferred.
- AI imagery: the old Design Director allowed internal comps (card 03 tension); Brandon 2026-10-10 bans it everywhere. R11.
- Identity work has no owner after the brand identity seat retires (card 03 tension): M2 asks Brandon rather than assigning. Open for the frame or roster.
- Canon source moved from the ClickUp Brand Guidelines to `company/brand/design-system` (cards 01c, 03): path only.
- The design system's company name differs from CLAUDE.md, and two daypart code names sit in `data-theme` tokens (card 04): flagged in one line, never repeated (R5, X13).
- Pre-lease no-address rule (dated, written for the investor site) vs carrying the address verbatim (card 04): resolved by Brandon 2026-10-10 (G3): the rule binds every external surface until the lease is signed; R13 holds the address as a named gap until then.
- Card.prompt sample uses a Korean term that is internal under the canon line (card 04): R6.
- The design system index still lists retired immersive components (card 04): R9 points at `track/`.
- Old rule 10 duplicated standing rules (card 01r): not restated.

## Sources
| card | citation | verified this build |
|---|---|---|
| 01-examples | `profiles/_source/design-translating-team/01_Design_Brief_Translator_Profile.md`, worked examples | yes (read at source by extractor) |
| 01-old-cues | same, cue table | yes |
| 01-old-protocol | same, construct and critique procedures, seven-layer protocol | yes |
| 01-old-rules | same, decision rules, mental models, anti-patterns | yes |
| 01-old-scope | same, scope, interfaces, uncertainty, outputs | yes |
| 02-old-prompt | `profiles/_source/design-translating-team/02_Platform_Prompt_Specialist_Profile.md` | yes |
| 03-old-routing | `profiles/_source/design-translating-team/08_Design_Director_Profile.md` | yes |
| 04-design-system | `company/brand/design-system`: `readme.md`, `docs/codified-patterns.md`, `docs/content-architecture.md`, Button, Card, Input, Wordmark, Chapter, ImageSlot `.prompt.md` | yes; drafter confirmed `styles.css`, `tokens/`, `tokens/fonts.css`, `track/`, `components/immersive/` exist |
| 05-old-03-rows | `profiles/_source/design-translating-team/03_Brand_Identity_Specialist_Profile.md`, partial read | yes |
