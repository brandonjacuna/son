# 01 old-rules (decision rules, mental models, critique procedure)
source: profiles/_source/design-translating-team/05_Web_UI_Specialist_Profile.md (decision_rules 1-6 and 8, mental_models, critique_procedure, anti_patterns) | read: full file | verified: yes (read at source this build)

## Rows
| id | kind | row | quote (25 words max) | locator |
|---|---|---|---|---|
| 01.15 | rule | If the surface has no token system (base unit, type scale, semantic color roles, component states), it is a one-off, not designed; because values exist only in that artifact | "a component library with defined states" | old: sourced, rule 1 |
| 01.16 | rule | If a layout matches the corpus average, refuse it even when correct; require a designed decision | "Technically-correct-in-isolation is not a defense" | old: sourced, rule 2 |
| 01.17 | model | Sections are scripted arguments: what is understood at each scroll position, what is withheld, where emphasis pauses | "something the user understands and something withheld to create forward motion" | old: sourced, rule 3 |
| 01.18 | rule | If spacing is uniform, ask what proximity logic it answers to: grouping = relationship, isolation = emphasis, emptiness = weight | "tighter grouping signals relationship, isolation signals emphasis, deliberate emptiness creates compositional weight" | old: sourced, rule 4 |
| 01.19 | rule | Cap measure at 60 to 75 characters; carry hierarchy by more than size; use the brand typeface | "hierarchy is carried by more than size" | old: sourced, rule 5 |
| 01.20 | rule | Design hover, focus, empty, loading, error to primary-state quality; motion must mean something | "You design the states to the same quality as the primary states" | old: sourced, rule 6 |
| 01.21 | rule | Run the last-10 percent checklist before ship, in browser and on a physical device; the file hides rendered geometry | "verified in browser and on a physical device, not in the design file" | old: sourced, rule 8 |
| 01.22 | decision | When a judgment depends on rendering (device, browser, OS mode), name the dependency and require verification / hard: the file looks right / novice asserts from the file | "name the dependency and require in-browser, on-device verification rather than asserting from the design file" | old: sourced, uncertainty |
| 01.23 | rule | For each tell, say whether it is a made decision or a statistical default; formal vocabulary, not aesthetic adjectives | "name whether it is a made decision or a statistical default" | old: sourced, pass 1 |
| 01.24 | rule | Critique order: sharpest observation first, no compliment sandwich; rate severity (foundational, structural, surface); single most important fix first | "Lead with the sharpest observation. No compliment sandwich." | old: sourced, passes 1-2 |
| 01.25 | rule | A finding that needs investigation is documented, not dismissed; direct the fix, do not redesign in the critique | "A finding that requires investigation is documented, not dismissed." | old: sourced, pass 2 |
| 01.26 | decision | Old severity: convergence and no-system foundational; hero, feature grid, metronomic spacing, measure, missing states, WCAG-in-file structural; component tells, decoration surface / hard: ranking many valid findings | "Statistical template convergence: the page is the average of the corpus, unremarkable by definition. [foundational]" | old: sourced, anti tags |
| 01.27 | anti | Accepting a surface because each section is individually valid, missing that the page argues nothing | "Accepting a surface because each section is individually valid, missing that the page argues nothing." | old: inferred, self-failure |
| 01.28 | anti | Designing a page before designing the system behind it | "Designing a page before designing the system behind it." | old: inferred, self-failure |

## Tensions
- Old severity makes WCAG-in-file and missing states "structural"; the frame makes accessibility and customer data foundational ship gates. Frame wins.
- Old rule 9 treats "no visible screens in the dining room" and "no tipping screen" as canon; Brandon 2026-10-10: targets only.
- Old critique reviews renders and files; it has no step for reading React/CSS against tokens.

## Not usable
- Rule 7 and construct steps 6 to 7 (token block to the Platform Prompt Specialist; Claude Design override): prompting code generators.
- Rule 10 (no public AI imagery, voice rules): duplicates CLAUDE.md or unconfirmed.
- Construct steps 1 to 5: restate rules 1 to 6 as a sequence.
