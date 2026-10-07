import re, sys
PAGEID = sys.argv[1] if len(sys.argv) > 1 else 'PAGEID'
src = open('extraction/s09/tracker-before.md').read()
out = src

def bullet(key, new):
    global out
    assert out.count(key) == 1, key
    i = out.index(key)
    start = out.rindex('\n', 0, i) + 1
    end = out.index('\n', i)
    line = out[start:end]
    assert line.startswith('*   '), line[:60]
    out = out[:start] + '*   ' + new + out[end:]

# 0. housekeeping: line 5's escape run (nested bold around a code span re-escapes on every save)
lines = out.split('\n')
assert lines[4].startswith('**Reconciled 2026-09-11 against**'), lines[4][:40]
tail = lines[4].split(', which is the governing document for this program.**', 1)[1]
lines[4] = '**Reconciled 2026-09-11 against `CLAUDE.md`, which is the governing document for this program.**' + tail
out = '\n'.join(lines)

# 0b. stale first-action block
i = out.index('## First action')
j = out.index('* * *', i)
first = '''## First action

Run Session 10. New chat:

> Sŏn. Scaling People, session 10. ClickUp task `86ajgmj2u`. Begin.

Session 9 is complete and its page is in the Operating System doc. Session 10 reads the ledger below before anything else. It is Chapter 4, team environment, owned by the People Systems Designer with the Realist at the table. Its inbound constraints from Session 9: team state is read by the diagnostic and never by a survey, and the offsite has no diagnostic role.

'''
out = out[:i] + first + out[j:]

# 1. last session + state
i = out.index('**Last session completed:** Session 8')
j = out.index('**Decisions binding a future session:**')
state = f'''**Last session completed:** Session 9, 2026-09-14. Chapter 4, Diagnosing team state, team changes and restructuring, (re)building the team, and the workbook's career conversations.

**State:** S9 built the instrument and not the diagnosis, as the session task directed: Sŏn has no team to diagnose, so the page specifies the team-state diagnostic and runs no read. The diagnostic is the record's failure mode reference (WP p.14) assembled into one instrument from what Sessions 3 to 8 built around it, and her chapter is consumed by it rather than replacing it. Every read names one of five objects (the house, the domain, the service roster, the seat, the service period; the last two are not teams), then a mode from a source on a record, then the mechanism the record's fix touches, and reaches a person only for tension slack, last, by one path that hands to S12 and through it to S14 and never to S15. Its unit is a seven-field evidence line (mode, object, source, count, compensation, fix and mechanism, state) that names no person and carries no figure, fed weekly at the leads' review, read quarterly at the house review, corrected at the mechanism reset, and checked at each gate, adding no meeting. Recurrence thresholds are counts of reviews and services. A diagnosis becomes care (logged) or correction (versioned) by four paths, with the line as the change's reason verbatim and a read-back by the source that raised it. Inside dinner's first-quarter freeze the diagnostic reads everything and changes nothing on the room's map; a pre-opening first run records what it can and cannot read. The reset's first read is the Maitre d's seat, its load carried by a designation, the stack, or a procedure, with the refused carriers listed under Brandon's ruling. Her reorganizations, DRIs, delegation framework, skill-will matrix, survey, and Lencioni frame are refused or absorbed; delegation lands on the decision-rights register; a departure is read in three passes and the brief carries coverage only. The career conversation is placed once, after the plan closes and before the first review. Fifty-one positions: forty-four recommended, two founder-gated, two chef-gated, three team-filled. Readiness rows 107 to 118, so the test stands at one hundred eighteen. Eighteen instrument specifications, nine used and nine refused. Thirteen findings inside the record, three of which would surface from a narrow read of WP pp. 13 to 14 and ten of which would not. Page `2ky45bmy-{PAGEID}`.

'''
out = out[:i] + state + out[j:]

# 2. decisions: S9 block at top
dec_hdr = '**Decisions binding a future session:**\n\n'
s9dec = '''*   **The diagnostic is the failure mode reference, and the mode is named before any person is read. Binds S12, S13, S14, S15, S17.** Every read names its object (house, domain, service roster, seat, service period), then the mode from a source on a record, then the mechanism the record's fix touches. The order is enforced by the evidence line's form, which names no person, carries no verdict, no dimension, and no figure, and adds nothing to the four scorecard dimensions. S9 names this as the one thing on its page a later session cannot revise at ordinary cost: a later session may add sources, change thresholds, and design what S12 to S15 do with a hand-off, and may not let a read open at a person, write a person's name on a line, or add a dimension by way of the diagnostic. S9 P1, P3, P4, P8, P42.
*   **The evidence line is the reason field of every change, verbatim, and every change is read back. Binds every session that proposes a change, S11, and S17.** A diagnosis produces care (a process update from a capture, logged) or correction (a mechanism, a designation's rule, a seat, a line, or a period, versioned) by four paths: a mechanism through the leads' review and the reset; a designation's rule through a structure change entry; a seat through S8's path whole; a line or a period through the variety pass at a gate. A change with no line or with a person as its reason is refused; the next scorecard reads it back as cleared, not cleared, or cannot read. S9 P24, P25, P26.
*   **The diagnostic runs on four rhythms that exist and adds no meeting. Binds S10, S11, S17.** The leads' review's items 2 and 6 are the weekly feeders, the house review's scorecard section is the quarterly read, the mechanism reset is the correction, and the gate review's failed rows are the gate's line. S9 P20.
*   **Recurrence thresholds are counts of reviews and services, never money. Binds S12 to S15 and S17.** Three consecutive leads' reviews on the same object go to the partners' review; two consecutive quarterly lines after a fix go to the reset; a designation held by one person every service for a quarter is a question at the reset about the Maitre d's seat's hours and the designation's rule, never a second seat and never a read of the holder. A domain that repeats is read in three questions (count, sheet, lead's load) before any hiring question. The thresholds are reset parameters. S9 P17, P18, P19, P32.
*   **A diagnostic read reaches a person by one path, for tension slack only. Binds S12, S14, S15.** The seat and adjacent seats named, the domain fix made and read back, the person's own check-in line as the only person-side source, one permitted dated statement after recurrence, then S12, only through S12 to S14, and never to S15. No evidence line, scorecard, or reset record may be cited in a managing-out decision. The skill-will matrix is refused as a read of anyone. S9 P40, P41, P42.
*   **Inside dinner's first-quarter freeze the diagnostic reads everything and changes nothing on the room's mechanism map. Binds S10 and S17.** Lines that would change a frozen mechanism are held on the partners' page for the first reset with their dates. S9 P21.
*   **The reset's first read is the Maitre d's seat, and its carriers are listed. Binds S15, S16, S17.** From nine inputs on the stack and the records. A load finding is carried by a designation, the stack, or a procedure; a second floor seat, a floor manager under any name, an assistant of any title, a permanent room holder, and a service manager are refused carriers. S9 P36, under Brandon's ruling of 2026-09-13.
*   **A departure is read in three passes, and the brief carries coverage only. Binds S11 and S15.** The tension-loss row, the leads' review line, the pool, and the adjacent seats' lines; then whether what the node held was in the system; then the read-back at re-fill. The floor hears which seat is open and who holds its functions this service, and nothing about the person; this reads S3 P11.6, S7 P47, and S8 P49 as one rule, the practice S11's. A lead seat's departure adds a structure change entry with the departure's line as reason. S9 P30.
*   **Delegation lands on the decision-rights register, and DRIs are refused. Binds S12 and S14.** The job is carried by the seat sheet and range card, a one-off by a process change with an owner or a designation, and no task is handed down at a check-in or a brief. S9 P38, P39.
*   **The career conversation is held once, and adds nothing the person has not heard. Binds S10, S12, S13.** In the month after the ninety-day plan closes and before the first review, placed by the stack, paid as shift, between the person and the domain lead, opening on the person page's path line, the sheet's horizons, the tracks, and the fluency record. It writes one track and what the building must supply in the person's words, and refuses levels, titles, ranks, seat promises, pay, the person's history before the house, and any use in placement or delegation. Its length, thirty minutes, is a reset parameter. A lead's waits on `86akhb2jg`; the kitchen's is chef-gated. S9 P43, P44, P45.
*   **The readiness test stands at one hundred eighteen rows. Binds every session from here.** Rows 107 to 118 from S9; rows from S10 start at 119. Rows 111 and 112 are read at the first-reset review, and row 118 fails until `86akhb2jg` closes. S9 section 17.
'''
assert out.count(dec_hdr) == 1
out = out.replace(dec_hdr, dec_hdr + s9dec)

# 3. open questions: S9 block at top
oq_hdr = '**Open questions a future session must close:**\n\n'
s9oq = '''*   **Which changes need a version.** The record updates a process nightly from a capture with no version step (WP p.13) and the deck allows change only by versioned decision (Deck 3.0); S9 reads the first as care and the second as correction. The versioning authority ratifies. S9 finding 19.8, extending `86akh3t3y`.
*   **The unit of a departure's "calculable" cost.** The record calls the loss of a person bounded and calculable; financials are not a context source, so S9 bounds it as which mechanism now has to be maintained. S9 finding 19.5.
*   **Whether a server's book of regulars is recorded on the tension-loss row.** S9 finding 19.6.
*   **"Diagnostic" reserved for the instrument.** Canon says Nunchi is "not diagnostic inquiry" and the record calls its reference "a diagnostic"; the reconciliation should keep the word for the instrument and off the floor. S9 finding 19.11, extending `86akh3tjb`, with S11.
*   **Who holds a lead's career conversation.** Waits on `86akhb2jg`. S9 P43.
*   **The career conversation's length.** Set at thirty minutes as a reset parameter; a duration, flagged for the founders in case it should stay unset. S9 P43, extending `86akh7rrb`.
'''
assert out.count(oq_hdr) == 1
out = out.replace(oq_hdr, oq_hdr + s9oq)

# 4. amend questions S9 narrows
bullet("**The leadership-line count.**",
 "**The leadership-line count.** Four named lines plus the Station Leads; the total is a gap until the chef fills the Station Leads. The check-in load beneath the Maitre d's seat is read first at the mechanism reset; S9 specified that read (nine inputs, one line per mode, the carriers and refused carriers), and the count stays the chef's. S8 P12, P14, S9 P36.")
bullet("**Who holds a lead's check-in.**",
 "**Who holds a lead's check-in.** The record runs feedback both directions and names no one for the leads. Urgent since S9: the diagnosis of a lead's own node is half-blind until it closes, the lead's career conversation and the seat holder's line in the reset's first read wait on it, and row 118 fails. The team recommends closing it before the leads are in the building six weeks ahead of dinner's gate. Finding 19.7, P21, S9 P35, `86akhb2jg`.")

# 5. reading note
key = 'and one found a committed activity, events, that the leadership delta removed and nothing holds.'
assert out.count(key) == 1
out = out.replace(key, key + ' Session 9 found thirteen, three of which would have surfaced from a narrow read of the failure mode reference (WP pp. 13 to 14) and ten of which would not; three set canon against the white paper, including canon reserving the word "diagnostic" against the reference\'s own name for itself.')

open('extraction/s09/tracker-after.md', 'w').write(out)
print(len(src.encode()), '->', len(out.encode()))
