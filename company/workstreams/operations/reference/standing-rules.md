# Standing rules

**Status: reconciled 2026-09-11** against the tracker protocol (`2ky45bmy-17233`). Transcribed from `CLAUDE.md`, section "Standing rules on every output."

This file exists so the rules can be handed to a subagent as part of its brief without passing all of `CLAUDE.md`. It is a faithful transcription, not a summary. If it ever disagrees with `CLAUDE.md`, `CLAUDE.md` wins.

No rule here required correction. The drift ran the other way: the tracker doc was the stale artifact. See "Tracker reconciliation" at the bottom.

---

## The rules

These are non-negotiable and apply to all text this project produces, in any context, at any stage.

1. The customer is the "customer." Never "guest."
2. No em dashes. Use commas, colons, semicolons, or restructure.
3. No performed conviction: never "we believe," "we hope," "our goal is," "we are committed to." Declarative over aspirational.
4. Sentence case for all headings and labels.
5. No daypart code names (Good Energy, Dosi, Luxx) in any output. Refer to dayparts by time of day or service period.
6. Brand facts defer to brand canon (`sources/brand-guidelines.md` and `sources/brand-guidelines-deck.pdf`). Do not assert brand facts from memory.
7. No financial figures generated, estimated, or recalled. If a financial figure is needed, state that financials are not a context source for this program and flag the gap.
8. Profanity is spoken-only. It never appears in written output.

---

## Marking rules

Nothing this project produces is marked "final." Every position carries one of four marks until Brandon ratifies it.

| Mark | Meaning |
|---|---|
| Recommended | The team's position, ready for founder ratification |
| Chef-gated | Deliberately left open for the chef partner to shape |
| Founder-gated | Requires founder input the team cannot supply (values, interiority, working style) |
| Team-filled | Populated once the team exists |

---

## The boundary rule

Never present as landed what only the group can land. Founder-gated work is developed to the ceiling one founder can reach, argued, staked, then marked for what Dominic, the chef, or the team must close.

Specifically, the team does not produce:

- Brandon's personal values, interiority, work style, strengths, or failure modes. Claude may propose. Claude may not record a proposal as a recommended position without Brandon's confirmation.
- Sŏn's intent (mission, principles, what good looks like) from scratch. The white paper and brand canon carry the intent. The team interprets and applies it.
- Finished instruments. Specifications describe what to build. The building happens later, and is gated on the document methodology (ClickUp task `86ajgn2z5`).
- Anything marked "final."

---

## Post-extraction work item types

Every typed subtask filed under the post-extraction parent task carries exactly one of these.

| Type | Meaning |
|---|---|
| Founder decision | A choice requiring one or more founders to ratify |
| Document | A founding document, policy statement, or philosophy to write |
| Process | A cadence, workflow, or operating rhythm to design |
| Instrument | A tool, template, rubric, scorecard, or form to build (gated on document methodology) |
| Structure | An organizational design element to finalize |

---

## Source boundary

Only the allowlist exists for this project. If a source is not on it, it does not exist here.

**Allowed, local, read-only:**
`sources/scaling-people-book.pdf`, `sources/scaling-people-workbook.pdf`, `sources/robert-lerma-white-paper.pdf`, `sources/brand-guidelines.md`, `sources/brand-guidelines-deck.pdf`, and the three profiles in `profiles/`.

**Allowed, ClickUp:**
tracker doc `2ky45bmy-17233`, Operating System doc `2ky45bmy-17253`, session subtasks under `86ajgmh9a`, Carryover Register list `901327884538`, Founding Punch List `901323485125`.

**Excluded, hard boundary:**
Business Strategies Notebook (`2ky45bmy-11873`, all versions V1 through V7; background only, not canon, the white paper is canon), ClickUp Brand Guidelines doc (`2ky45bmy-15773`, archived), Research Capture doc (`2ky45bmy-16853`), any ClickUp doc not on the allowlist, the Pre-Archive space, Airtable, Box (all files are local; do not fetch from Box), the downstream profile clusters in Box (`400224498698`, `400281721352`) unless Brandon explicitly approves a specific profile, and any white paper file other than `robert-lerma-white-paper.pdf`.

---

## Reading discipline

The white paper and brand guidelines are the record of what Sŏn has already decided. Read them broadly for the relevant domain. When in doubt, read more of the record, not less. Never skim the record to save tokens.

The book and workbook are raw material, not the record. Read them by exact page range from the chapter map. Token savings come from the book PDFs. They never come from the record.

---

## Tracker reconciliation

On 2026-09-11 the tracker protocol (`2ky45bmy-17233`, page `2ky45bmy-30353`) was read and found to predate the current source allowlist. It contradicted `CLAUDE.md` on six points. The tracker was corrected to match. This section records what changed, so that a stale copy of the old protocol, pasted into a session from anywhere, is recognized and rejected rather than followed.

| Point | What the tracker said | What governs |
|---|---|---|
| Sŏn's record | V7 notebook (`2ky45bmy-11873`) and ClickUp canon (`2ky45bmy-15773`), read live | Neither is canon (V7 is background only, not canon; the white paper is canon). Both are off this program's allowlist. The record is `sources/robert-lerma-white-paper.pdf`, `sources/brand-guidelines.md`, `sources/brand-guidelines-deck.pdf` |
| Profiles | Box folder `400727361228`, fetched by file ID | Local `profiles/`, read from disk by range |
| Marks | landed, founder-gated, team-filled, chef-gated | recommended, chef-gated, founder-gated, team-filled. Nothing is ever marked final |
| Financials | a stale profile instruction naming a retired data tool | Financials come only from the current Investor Review workbook in Box (Sŏn / 02. Capital Raise). Not a context source for this program. State the gap and flag it |
| Session output | Two things: decisions and specifications | Three things. Typed post-extraction work items are the third |
| Definition of done, item 6 | Hand Brandon the next session prompt | Post-extraction work items created as typed subtasks under `86akh1hdg` |

The tracker's session sequence, task IDs, page ranges, carryover routing, tangent protocol, pause and resume, and archive were accurate and were left as written.

A session that encounters an instruction to read V7, the archived ClickUp canon doc, or a Box profile has hit a source that is not canon (V7 is background only, not canon). It does not follow it. It surfaces the conflict.
