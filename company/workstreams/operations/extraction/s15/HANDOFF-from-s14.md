> **Provenance.** Written by the Session 14 controller at close, 2026-09-24. It is a handoff to verify, not authority. Session 15 reads the ledger (tracker page `2ky45bmy-30353`), its carryovers, the profiles, and Sŏn's record for itself. Where this note and the ledger disagree, the ledger wins.

# Session 15 handoff: Chapter 5, managing managers and managing out (Book pp. 449 to 483)

## The prompt

```
Sŏn. Scaling People, session 15. ClickUp task 86ajgmjpw. Begin.
```

## Before starting

Session 14 closed complete (`output/s14/RESUME-HERE.md`). Its entire close-out ran on ClickUp's REST API with Brandon's token (`~/.clickup_token`, helper `extraction/s13/cu.py`), and no MCP connector calls were used for bulk work.

## What Session 15 is

Book pp. 449 to 483. **The top of p.449 is Session 14's material**: two paragraphs that finish "Potential outcome 2: Move roles or teams" are quoted in the bracketed context line at `extraction/s14/book-419-448.md` line 471 and answered on the S14 page. Session 15's material begins at the head "Managing managers" (p.449, y 475.8). Footnote 76 falls on p.450. The book's outcome 3, where the person leaves, is deferred to its managing out, firing, and layoffs section, which is in Session 15's range. Chapter 5's font scale matches the one S13 and S14 recorded (see `extraction/s14/extraction-notes.md`); run the census anyway. Workbook: the Managing Out Checklist (p.124) is Session 15's. The PIP template (pp. 118 to 123) was answered by S14. Profile: Designer, and the Realist if the session has a floor-execution surface; the profile override applies, and at least one profile embeds a compensation percentage that must not be reproduced.

## What Session 14 settled that Session 15 runs into

- **The horizon window never concludes departure** (S14 P16, P21). Session 15 gets only the stack-assembled hand-off package: the window block whole, the pool and inventory read, and, for a non-negotiable line, the line, the flag record, and the person's words. It may cite nothing outside the package and may never reach back into a window.
- **A decision about staying is a reserved class at the partners' review, with counsel** (S14 P26). S14 recommended adding it to S3's list (`86akh5u8m`, `86akh5u77`). Session 15 designs the mechanism that receives the package: the departure decision, its conversation, final pay with counsel, and the checklist.
- **The flag read and the line** (S14 P24, P25). The line's lifetime and whether one line is itself the decision are founder-gated (P27), held on the toxicity and exploitation definitions and the hierarchy ruling.
- **A lead's own window, flag read as subject, and departure** are held for S15 and the founders on `86akhb2jg` (S14 P36).
- **No HR seat exists** (S14 finding 19.1, P34). S14 split her HR functions between the flag read's second reader, the Operations Lead's employment record, and counsel.
- **From Session 13:** a departure's final pay (with counsel); a lead's review holder; managing out against a pay system with no lever.

## Carryovers linked to `86ajgmjpw`

Read the task's linked tasks rather than trusting a count from this note. Session 14's is `17tn048qfp2`; Session 13's is `17tn048qepa`.

## Prior pages, by index rather than whole

- S14: `extraction/s15/s14-page-index.md`. Sections 5 (the horizon window, esp. the seam with S15), 6 (the non-negotiable breach), 8 (moves), 9 (what performance management may never become), 10 (a lead's own performance), 13 (rows 169 to 182).
- S13: `extraction/s14/s13-page-index.md`. Sections 8.5 (a lead's review) and 14 (the compensation conversation, and pay as never a lever).
- S12: `extraction/s13/s12-page-index.md`. Sections 11 (the non-negotiable breach) and 15 (who holds a lead's check-in).

## Operating lessons carried forward

1. Run the whole close-out on the REST API through `extraction/s13/cu.py`, which avoids the connector's daily cap. S14's scripts (`build-plan.py`, `file.py`, `ledger-edits.py`) in `extraction/s14/` can be adapted by changing the session numbers. Never print the token.
2. A create call can return a 500 and still create the task. `file.py` checks for the task by exact name before it retries.
3. Upload the page in chunks of about 24 KB and the ledger in chunks of about 12 KB, and diff the live copy word for word afterward. S14 had zero differences on both.
4. The Fable brief should tell it to end every work item with its priority word as the last sentence, and to put no provenance line in descriptions.
5. S14's page numbers its findings 19.1 to 19.13 under section 15, not 15.x. Cite them as S14 findings 19.x. In the brief, ask Fable to number findings under the section's own number.
6. A carryover answered by a session gets a comment, not a status change. The session list's closed status is `done`.
