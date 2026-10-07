> **Provenance.** Written by the Session 13 controller at close, 2026-09-24. It is a handoff to verify, not authority. Session 14 reads the ledger (tracker page `2ky45bmy-30353`), its carryovers, the profiles, and Sŏn's record for itself. Where this note and the ledger disagree, the ledger wins.

# Session 14 handoff: Chapter 5, high, middle, and low performers (Book pp. 419 to 448)

## The prompt

```
Sŏn. Scaling People, session 14. ClickUp task 86ajgmjk1. Begin.
```

## Before starting

Session 13 closed complete (`output/s13/RESUME-HERE.md`). Its close-out hit the ClickUp connector's daily cap and finished on the REST API with Brandon's token (`~/.clickup_token`, helper `extraction/s13/cu.py`).

## What Session 14 is

Book pp. 419 to 448. **The top of p.419 is Session 13's material**: the end of "managing disappointment" and a closing paragraph on the formal review, quoted in the bracketed context line at `extraction/s13/book-399-418.md` line 297 and answered on the S13 page. Session 14's material begins at the head "Managing high performers" (p.419, y 413.4). Chapter 5's font scale matches Chapter 4's (see `extraction/s13/extraction-notes.md`). Workbook: the Performance Improvement Documentation Templates and PIP (pp. 113 to 117, extracted by S12 at `extraction/s12/workbook-ch5.md`); confirm any further exercise against the census there. Profiles: Designer and Realist; the profile override applies, and at least one profile embeds a compensation percentage that must not be reproduced.

## What Session 13 settled that Session 14 runs into

- **No review output and no feedback act reaches pay** (S13 P23, P36, P37). No performance tier may add a pay line, a marker, a weight, or a withheld anything; "pay for performance" is carried by the unlock, the markers, the pool's weighting, and the days.
- **The review has no rating and is never a managing-out file** (S13 P7, P17). Her high, middle, and low labels have no field to live in.
- **A person who holds a seat's horizon and never unlocks** earns the horizon's weight and the pool's growth and is not "partially meets" (S13 B1).
- **From Session 12:** no coaching record exists to cite; the not-yet form and the tension-slack hand-off are read in their own words; a non-negotiable breach is never coaching; failure is typed on the process update, never on a person.

## Carryovers linked to `86ajgmjk1`

Read the task's linked tasks, not a count from this note. Session 13's is `17tn048qep8`; Session 12's is `17tn048qcjt`.

## Prior pages, by index rather than whole

- S13: `extraction/s14/s13-page-index.md`. Sections 3 (what the review reads), 7 (what it may never become), 9 and 12 (the point system's inputs and the separation of review from pay), 17 (rows 155 to 168).
- S12: `extraction/s13/s12-page-index.md`. Sections 3.5 (the self-awareness gap as a count), 7.1 (the not-yet form), 7.4 (the tension-slack hand-off), 8 (failure by type), 11 (the non-negotiable breach).

## Operating lessons carried forward

1. The ClickUp tools are `mcp__daa70cda-fb71-479a-9e27-a042277a02d7__*`; the "clickup needs auth" notice is a different, unused server. Put that in every subagent prompt.
2. **ClickUp's MCP connector has a daily cap of 1,000 calls per workspace.** Session 13 hit it during close-out. For bulk work (page chunks, filing, comments, verification, the ledger) use the REST API through `extraction/s13/cu.py`, which reads Brandon's token from `~/.clickup_token`. It has no daily cap, and a script passes files directly, so nothing gets retyped. Never print the token.
3. Uploads go through a subagent passing chunk files verbatim; diff the live page after. Ledger chunks at about 12 KB.
4. End every work item with its priority word as the paragraph's last sentence.
5. Filing agents retype descriptions; verify by a separate agent that saves the fetched descriptions and compares by script.
6. Carryovers answered by a session get a comment, not a status change. The session list's closed status is `done`.
