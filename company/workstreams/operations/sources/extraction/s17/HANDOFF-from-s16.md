> **Provenance.** Written by the Session 16 controller at close, 2026-09-25. This is a handoff to verify, not an authority. Session 17 reads the ledger (tracker page `2ky45bmy-30353`) and its linked carryovers for itself. Where this note and the ledger disagree, the ledger wins.

# Session 17 handoff: assembly and the company wiki

## Gate

Session 17 does not start until the document methodology (`86ajgn2z5`) lands. That task is not reachable with the REST token (it returned "Team not authorized"), so confirm its state in ClickUp directly.

## The prompt

```
Sŏn. Scaling People, session 17. ClickUp task 86ajgmk27. Begin.
```

## State at hand-off

- Sixteen session pages sit in the Operating System doc. S16's page is `2ky45bmy-33293`.
- The readiness test stands at 213 rows. The counsel questions register holds 31 questions. The punch list parent `86akh1hdg` holds 400 subtasks. The Carryover Register holds 147 items.
- Every carryover routed to S1 through S16 was answered by comment and left open for founder ratification. S17's task (from its description) closes, parks, or escalates every one.

## Binding on S17 from S16

- **Ruling 1 (Brandon, 2026-09-25):** a founder's outside commitments are "a founder's external load" on every surface, and their nature is never named. S17's audit covers every wiki page.
- No founder's interiority, values, working style, or pay is recorded as a position anywhere in the wiki.
- S16 carryovers: `17tn048qr4m` (rows 201 to 213, the center's page, extensions, findings, vocabulary, the interiority audit) and `17tn048qr4n` (a row that reads the company as well as the building).

## Operating lessons carried forward

1. Run close-out on REST. The script set in `extraction/s16/` is current: `gather.py`, `upload-page.py`, `verify-page.py`, `build-plan.py`, `file.py`, `verify-filed.py`, `comment.py`, `ledger-edits.py`, `upload-ledger.py`.
2. ClickUp renumbers a markdown ordered list from 1. Use bold numbers for any list that continues an earlier numbering.
3. S17 will be the largest read-in of the program: sixteen pages totalling about 3 MB. Use the page indexes (`extraction/*/s*-page-index.md`, `extraction/s05/positions-index.md`) and split assembly into passes with clean seams rather than one Fable read of everything.
