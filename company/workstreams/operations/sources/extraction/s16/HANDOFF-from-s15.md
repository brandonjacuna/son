> **Provenance.** Written by the Session 15 controller at close, 2026-09-24. It is a handoff to verify, not authority. Session 16 reads the ledger (tracker page `2ky45bmy-30353`), its carryovers, the profiles, and Sŏn's record for itself. Where this note and the ledger disagree, the ledger wins.

# Session 16 handoff: the Conclusion and "You" (Book pp. 484 to 503)

## The prompt

```
Sŏn. Scaling People, session 16. ClickUp task 86ajgmjz6. Begin.
```

## Before starting

Session 15 closed complete (`output/s15/RESUME-HERE.md`). Its entire close-out ran on ClickUp's REST API (`extraction/s13/cu.py`, Brandon's token at `~/.clickup_token`, never printed). No MCP connector calls were used for bulk work.

## What Session 16 is

Book pp. 484 to 503. S15's extraction found that the Chapter 5 notes end on p.483, so p.484 should open the Conclusion; confirm this with a census. The workbook has no pages after Chapter 5: its last exercise is the Managing Out Checklist on p.124, and p.125 is the publisher's back page. Check the workbook's front matter or Chapter 1 for any "You" exercise before concluding there is none. Profile: Designer. **This session's material is about the founder as a person.** Brandon's values, interiority, working style, strengths, failure modes, and pay are never recorded as positions. The team may propose them, and every such proposal is founder-gated until Brandon confirms it. At least one profile embeds a compensation percentage that must not be reproduced.

## What Session 15 settled that Session 16 runs into

- **The partners are the leads' check-in holders on the team's reading** (S15 P6 to P8, founder-gated on `86akhb2jg`). This is a founder load, and it bears on "You."
- **The center absorbs a lead's failure** at the partners' review (S15 P11). Who absorbs the founders' failure is Session 16's question (B1).
- **A person's staying is decided only by the partners, with counsel** (S15 P22). A founder as a flag's subject, a founder's departure, and the operating agreement's rule beneath every reserved class are Session 16's.
- **The interim holder of an open lead seat's domain is the pairing partner**, carried as a node-overload line. This is a founder load.
- **From earlier sessions:** the partners' own place in the pool (S13); whether a founder on the floor is bound by the live-speech rule (S12 P15); a founder's impression is never a trigger (S14 B2).

## Carryovers linked to `86ajgmjz6`

Read the task's linked tasks rather than trusting a count from this note. Session 15's is `17tn048qg2h` and Session 14's is `17tn048qfp3`.

## Prior pages, by index rather than whole

- S15: `extraction/s16/s15-page-index.md`. Read sections 2 (leading the leads, especially 2.3 and 2.6), 3 (a lead's window, and the interim holder), 4.2 (the decision about staying), 13 (findings 13.7 and 13.13), and 14 (counsel's questions).
- S14: `extraction/s15/s14-page-index.md`. Read section 10.
- S13: `extraction/s14/s13-page-index.md`. Read the partners' salaried rule and their place in the pool (P28, P31).

## Operating lessons carried forward

1. Run the whole close-out on REST. S15's scripts in `extraction/s15/` can be adapted by changing the session numbers: `upload-page.py`, `verify-page.py`, `build-plan.py` (its Section C parser handles quoted comments and "Comment for each"), `file.py`, `verify-filed.py`, `comment.py`, `ledger-edits.py`, and `upload-ledger.py`.
2. A create call can return a 500 and still create the task. `file.py` checks for the task by exact name before it retries.
3. Upload the page in chunks of about 24 KB and the ledger in chunks of about 12 KB. S15 had zero differences on both.
4. The Fable brief should require the priority word as each work item's last sentence and no provenance line in any description. S15's brief (`extraction/s15/fable-brief.md`) is the current form.
5. A carryover answered by a session gets a comment, not a status change. The session list's closed status is `done`.
