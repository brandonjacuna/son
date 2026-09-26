# S8 filing manifest (exact titles)

Filed 2026-09-13 from `output/s08/work-items-and-carryovers.md`, sections A and B only (section C, comments on existing tasks, is filed separately). Format matches Session 7: description is the item's paragraph after its bold title, with the provenance line as its own closing paragraph; no tags, no custom field, list default status (`identified` for work items, `to do` for carryovers). Carryover descriptions open with a **Routed to:** line, and the inline routing arrow and priority word are carried by that line and the priority field, as Session 7 did. The priority word in each paragraph sets the priority field.

Subtasks under `86akh1hdg`: **165 before, 190 after** (25 added, no duplicate names). Counted from the parent's subtask list (every entry's parent is `86akh1hdg`); list `901323485125` was also paged in full with closed tasks and subtasks (416 tasks, five pages), but filter_tasks returns no parent field, so the parent's subtask list is the count of record.

Carryover Register list `901327884538`: **101 before, 110 after** (9 added).

A4 and A5 are not filed: Session 6 already holds both decisions as `86akh9tbw` and `86akh9tbz`, extended by comment under section C.

## Work items: subtasks of `86akh1hdg`, list `901323485125`

| ID | Title | Task | Priority |
|---|---|---|---|
| A1 | Founder decision: Name the room designation, and read the door as the threshold's holder | `86akhcz1h` | urgent |
| A2 | Founder decision: Fill the team-supplied parts of the ruling's decision-rights entries | `86akhcz1m` | high |
| A3 | Founder decision: Rule the Head of Beverage as a seat and a leadership line | `86akhcz1u` | high |
| A6 | Founder decision: Rule which of the record's two advancement accounts stands in wording | `86akhcz22` | normal |
| A7 | Founder decision: Rule who holds an event in the room | `86akhcz26` | normal |
| A8 | Founder decision: Fill the incomplete structure decision-rights entries | `86akhcz2e` | normal |
| A9 | Document: Write the chef onboarding packet's structure section | `86akhcz2m` | normal |
| A10 | Process: Name the designations at the brief: the room, the door, the sequence, and the pass | `86akhcz2y` | high |
| A11 | Process: Run the degraded-mode service once in a training service | `86akhcz34` | high |
| A12 | Process: Design how a structure change is made and reaches the team | `86akhcz3c` | normal |
| A13 | Process: Design the live-risk line, in place of a Code Yellow | `86akhcz3g` | normal |
| A14 | Process: Run advancement as three seats: the stack schedules, the assessor scores, the lead records | `86akhcz3n` | high |
| A15 | Process: Run the requisite-variety pass at every gate | `86akhcz3x` | high |
| A16 | Instrument: Build the seat inventory's structure fields (gated on `86ajgn2z5`) | `86akhcz45` | high |
| A17 | Instrument: Build the leadership-line list and the requisite-variety test record (gated on `86ajgn2z5`) | `86akhcz49` | high |
| A18 | Instrument: Build the designation block of the shift brief (gated on `86ajgn2z5`) | `86akhcz4d` | high |
| A19 | Instrument: Build the room designation's card (gated on `86ajgn2z5`) | `86akhcz4g` | normal |
| A20 | Instrument: Build the structure change entry (gated on `86ajgn2z5`) | `86akhcz4n` | normal |
| A21 | Instrument: Build the web render's structural content (gated on `86ajgn2z5`) | `86akhcz5j` | normal |
| A22 | Instrument: Build the fluency record on the person page (gated on `86ajgn2z5`) | `86akhcz5y` | normal |
| A23 | Instrument: Build the degraded-mode service's printed set (gated on `86ajgn2z5`) | `86akhcz66` | high |
| A24 | Instrument: Build the interface read's structure line (gated on `86ajgn2z5`) | `86akhcz68` | normal |
| A25 | Instrument: Build the live-risk line's form (gated on `86ajgn2z5`) | `86akhcz6d` | normal |
| A26 | Structure: Reconcile the inventory's rows from the three seat lists | `86akhcz6h` | high |
| A27 | Structure: Place the overnight cleaning crew in the structure | `86akhcz6k` | normal |

Every item in the spec states a priority, so no default was applied.

## Carryovers: list `901327884538`, each linked to its target session task

| ID | Title | Task | Linked targets | Priority |
|---|---|---|---|---|
| B1 | "Team" translated three ways, and what a diagnosis reads | `86akhcz6u` | S9 `86ajgmj07` | normal |
| B2 | The house as the one team, designations as rotation, and the grid as team language only | `86akhcz6v` | S10 `86ajgmj2u` | normal |
| B3 | Communication in crisis, the unblocking practice, how a structure change is told, and events | `86akhcz6y` | S11 `86ajgmj7c` | high |
| B4 | Feedback to a designation's holder, and a designation as never a rating | `86akhcz71` | S12 `86ajgmjba` | normal |
| B5 | The two fluency markers defined, the salaried test, what a lead enters at, and the advancement account's review relation | `86akhcz76` | S13 `86ajgmjey` | high |
| B6 | Retiring a seat is never a departure, and a designation is not performance | `86akhcz7b` | S14 `86ajgmjk1` | normal |
| B7 | The Maitre d's load findings, node overload at the reset, and lead succession from the pool | `86akhcz7f` | S15 `86ajgmjpw` | high |
| B8 | The founders as post-service destinations only, and the live-risk line's load on a founder's seat | `86akhcz7m` | S16 `86ajgmjz6` | normal |
| B9 | The chef packet's fourteen structure items, rows 93 to 106, the team vocabulary rule, and the line count gap | `86akhcz7t` | S17 `86ajgmk27` | high |

All nine links returned success, and each carryover's `linked_tasks` on re-read contains its target.

## Verification

- Every task ID above was re-read with get_task: all 34 exist, with the title, priority, status, and list shown here, no tags, and the provenance paragraph closing the description.
- All 25 work items carry parent `86akh1hdg`; no duplicate names under the parent after filing.
- Local register `reference/carryover-register.md` is not updated by this filing.
