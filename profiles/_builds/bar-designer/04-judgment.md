# Stage 4 judgment: bar-designer
Read: 00-frame.md (Brandon's answers 2026-10-09), 04-flags.md, agent.md (9,977 bytes), batch3-seams.md, decisions 2026-10-09 (build-out), `company/workstreams/build-out/CLAUDE.md`, `kb/bar/tobin-ellis/book-notes/how-many-stations.md` (now present, read 2026-10-09).
Size: about 2,000 bytes of room; no cuts needed.

## Lifted since the flags (not a flag; apply with the edits)
- R3 replace with: "R3. Station count uses Ellis's pro forma method (`kb/bar/tobin-ellis/book-notes/how-many-stations.md`, Brandon's choice 2026-10-09): the workbook's budgeted beverage revenue down to revenue per operating hour and drinks per hour, then the bartenders it takes for Sŏn's service model, checked against the seat count and the test fit of the footprint; one bartender per station; the count is `estimated` with every input cited to the workbook or the note, never to his worked example."
- C10 "do": "Pull beverage revenue, operating hours, and the seat count from the Investor Review workbook and run R3; if the workbook is unreachable, say so and leave the count `unknown`".
- Output, Unknowns: delete "(station count always listed until ingested)".
- When to distrust my read, third bullet: "Only "How Many Stations?" is ingested; the other book dimensions (bar top height, station width, aisle, knee space, die wall, floor sink placement) are blank."

## Flags
| id | ruling | edit |
|---|---|---|
| B1 | accept | R5: "it carries its own dump sink, trash, tool rinse (dipper well), and chilled garnish, juice, and vermouth (the kb's inference from Perlick training); the hand sink is shared, and whether Austin Public Health wants one per well is a code item, unverified". provenance.md R5: `inferred (03.7, 02.5)`; 04.1 sourced for the APH check only. |
| B2 | accept | R8 replace with: "R8. If any bar seat is a dining surface, the customer-side counter carries an accessible section (TAS 904.4, unverified for the site); whether the bartender side carries any TAS geometry is unverified; put the accessible section in the concept, not after the footrail, and log both to `codes/register.yaml`." |
| B3 | accept | Scope: "seated, about 8 seats at most (Brandon's design intent, 2026-10-09; a constraint, not a workbook figure)". A7: "Writing a seat count, cover count, or revenue figure as a sizing input: those come only from the Investor Review workbook; Brandon's stated bar-seat intent is cited as intent." |
| B4 | accept | Add C16: cue "Dining-room tickets and bar customers share a bartender, and no print point or server collection edge is drawn"; means "The cross-serve fork is open and the cockpit does not show it"; do "Draw each option (a true service well, a split menu, another arrangement) with its print point and server pickup edge; Brandon picks". C13 "do" add: "; chilled small-pour service (soju, makgeolli) sits inside the cockpit, not in a back-bar walk". |
| B5 | accept, with S12 | C7 cue: "Server pickup crosses a bartender's working zone at the bar's edge". C7 "do": "Move the pickup to the bar-side edge; the server path beyond it (station, POS, runner route) belongs to no seat yet: list it as a fork for Brandon". |
| B6 | accept, with S13 | Seams row environmental-signage-specialist "they own": "graphics on the back bar and wall-mounted menu boards". Scope "Does not decide": "signage and graphics on the back bar and wall boards (`environmental-signage-specialist`); the bar-top brand surface, which no seat owns: Brandon's until he names one". |
| B7 | accept | C14 "do": "Glasswasher at the bar; the bar-to-kitchen path is listed as a fork until kitchen-layout exists". R10: replace "(ask APH)" with "(an open code item; no seat asks APH yet, so it goes to Unknowns)". Output, Unknowns add: "questions with no asker or no seat (APH, kitchen-layout) listed as forks for Brandon; the caller logs code items to `codes/register.yaml`". |
| B8 | accept | C13 "means": "Spoilage risk: unpasteurised sake and makgeolli want cold and dark (sourced); soju and cheongju storage is unknown". |
| B9 | accept | C5 cue: drop "or a deep rail". R6: "a book figure is cited first once ingested; the conflict stays shown". R3 is replaced above. |
| B10 | accept | Output add: "Define TAS, APH, NSF, MEP, and every bar term (cockpit, scupper, speed rail, die wall, floor sink) at first use (build-out CLAUDE.md s.3)." R11: "Texas Food Establishment Rules (25 TAC 228, adopting the FDA Food Code; unverified for the site)". |
| B11 | accept the caveat; rejects stay | Intro add: "The kb is a paraphrase of Ellis plus Perlick training, ingested chapter by chapter through `book-ingest`; I cite the note, not the book." A1 to A7 stay as the frame's novice list. C9 to C12 stay: each is tied to the barback path, the workbook, the `needs-book` tag, or frame decision 8. |
| B12 | accept | Add seams row: "licensed architect and MEP engineer (people) | stamped drawings and the engineered MEP plan | the station layout sets floor sinks, drains, and power as design intent; they engineer it". hospitality-operations-realist row "hand off when": "a station count or well arrangement is proposed; their tempo read is data". |

Counts: accept 12, reject 0, ask 0.

## Seams touching this seat (ruled in batch3-seams-judgment.md)
- S12: dining-room floor layout unowned; the bar seat stops at the bar-side edge and lists the rest as a fork (B5 edit).
- S13: signage owns back bar and wall boards; bar top is Brandon's until assigned (B6 edit, plus the signage side).

## Does it do the frame's job?
Yes. It reviews inside out, sets MEP from stations, sizes by the pro forma method Brandon chose against the workbook, keeps every dimension and code item traced or unknown, and now draws the two-well cross-serve fork instead of passing a generic bar.
