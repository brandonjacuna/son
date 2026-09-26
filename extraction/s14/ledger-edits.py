import sys
PAGEID='2ky45bmy-33253'
src=open('extraction/s14/tracker-before.md',encoding='utf-8').read()
out=src.replace('**Reconciled 2026-09-11 against** **`CLAUDE.md`****, which','**Reconciled 2026-09-11 against `CLAUDE.md`, which',1)
def amend(key, addition):
    global out
    assert out.count(key)==1, key
    i=out.index(key); end=out.index('\n',i); start=out.rindex('\n',0,i)+1
    assert out[start:end].startswith('*   '), out[start:start+60]
    out=out[:end]+' '+addition+out[end:]

i=out.index('## First action'); j=out.index('* * *',i)
out=out[:i]+'''## First action

Run Session 15. New chat:

> Sŏn. Scaling People, session 15. ClickUp task `86ajgmjpw`. Begin.

Session 14 is complete and its page is in the Operating System doc. Session 15 reads the ledger below before anything else. It is Chapter 5, managing managers and managing out (Book pp. 449 to 483), owned by the People Systems Designer. Its inbound constraints from Sessions 12 to 14: the horizon window never concludes departure and hands Session 15 a package assembled by the stack and nothing else, and Session 15 may cite nothing outside the package and may never reach back into a window; a decision about a person's staying is a reserved class at the partners' review; no review output, feedback act, or performance situation reaches pay; no coaching record exists to cite. The two paragraphs at the top of book p.449 (the end of "move roles or teams") were answered by Session 14, so Session 15's material begins at "Managing managers."

'''+out[j:]

i=out.index('**Last session completed:** Session 13'); j=out.index('**Decisions binding a future session:**')
out=out[:i]+f'''**Last session completed:** Session 14, 2026-09-24. Chapter 5, managing high performers (pushers and pullers, boredom, opportunity, letting go, potential over experience, pre-exit interviews and retrospectives, retaining top talent, telling a high performer they will not be promoted), the steady middle, and managing low performers (edge cases, the role of HR, the phases, delivering and documenting feedback, the performance improvement plan, and moving roles or teams, running onto the top of p.449), with the workbook's three follow-on documentation letters and the Performance Improvement Plan Template.

**State:** S14 refused "three tiers" as tiers and kept three situations read from records, with no field, list, count, or room that sorts a person into one: a person moving past a horizon, carried by mechanisms already built (the advocate, the markers, teaching, the career conversation, the pool, succession) and nothing a lead does; a person holding a horizon, the state of every seat between unlocks and nearly everyone on nearly every service, owed the horizon's weight, the pool, bandwidth, the schedule, the same check-in, and rotation, and asked for nothing; and a seat whose horizon is in question. The steady middle carries the page's weight, argued from the record, and her proportions are recorded as a fact about her industry. The one mechanism added is the horizon window: opened by the stack and never by a lead, on five triggers read from records the person has already read and only after the building's fixes are made and read back, a bounded count of services with a check-in at two weeks and the person's words as its only record, closed by an assessor from the pool reading the readiness form at the horizon held in a real service, ending as held, not held with the rows, a move the person chooses, or a package the stack assembles for the partners' review. It never concludes departure, a label, a pay change, or anything about a person's will or life. Her PIP, the three follow-on letters, and the sample plan conversation are refused as instruments, with the mechanism that does each one's work. After a non-negotiable flag, the destination is the flag read: both leads, on the clock, before the person's next service, writing one of three states on the flag's record; a non-negotiable line on the person page is written jointly in a closed form, and a decision about staying after one is a reserved class at the partners' review with counsel. A hire that does not hold is read at the hiring system by the calibration read on a first-year window, closing finding 18.6 as a mechanism. Forty-five positions: thirty-six recommended, five founder-gated, three chef-gated, one team-filled. Readiness rows 169 to 182, so the test stands at one hundred eighty-two. Twenty-four instrument specifications, eleven used and thirteen refused. Thirteen findings inside the record, numbered 19.1 to 19.13 under the page's section 15, six of which would surface from a narrow read of the white paper's people pages and seven of which would not. Page `{PAGEID}`.

'''+out[j:]

hdr='**Decisions binding a future session:**\n\n'
dec='''*   **No record, list, count, or room sorts a person into a performance situation. Binds S15, S16, S17.** The three situations (moving past a horizon, holding one, a seat whose horizon is in question) are seat states on records and never properties of a person; no tier, label, list, ranking, per-person count, playbook per person, or pay lever exists, and her three playbooks are three pages on the team home, the same for everyone. Performance management may never become a coaching record, a review or check-in by another name, a room, a read of Nunchi or Jeong, a case file in a lead's voice, a probation state, a hypothesis on the outcome, or a lead's decision that a person leaves. S14 names this as the one thing on its page a later session cannot revise at ordinary cost. S14 P2, P33.
*   **The horizon window opens only by the stack, after the building's fixes, and never concludes departure. Binds S15, S17.** Five triggers read from records the person has already read (the hypothesis count, the tension-slack statement, a basic failure recurring after the fix, a plan not held after one extension for a fix that was made, and missed services after the building's questions). It closes by an assessor's readiness form at the horizon held and ends as held, not held with the rows, a move the person chooses, or no move open. Session 15 receives only the stack-assembled package, may cite nothing outside it, and may never reach back into a window. The review's assembly refuses the window block as a source, extending S13 P6 by one refused record. S14 P16, P21.
*   **After a non-negotiable flag, the flag read; the line's closed form; staying as a reserved class. Binds S15, S16.** Both leads read the flag's record together on the clock before the person's next service and write one of three states; the person hears it from their check-in's holder with the other lead present, before anything is written. The line on the person page is written jointly as a state with a citation, in a closed form, read by the eligibility rule, dimension 3 as a fact, the pools, and Session 15's mechanism only. A decision about staying after a line is a reserved class at the partners' review, with counsel, never a lead's and never at the flag read. S14 P24 to P26.
*   **A hire that does not hold is read at the hiring system. Binds S17.** A window opened inside a person's first year triggers the calibration read on that packet at the leads' review, writing to the calibration record and versioned changes to the sheet, rows, kit, or training record, never to a page about the person; first-year windows per seat class are a hiring-system leading indicator. S14 P29, extending S6 P41.
*   **The readiness test stands at one hundred eighty-two rows. Binds every session from here.** Rows 169 to 182 from S14; rows from S15 start at 183. Rows 177, 178, and 180 carry a founder-gated hold; row 175 reads not yet until the performance page exists in every language; rows 181 and 182 are read at the first reset as well as the gate. S14 section 13.
'''
assert out.count(hdr)==1; out=out.replace(hdr,hdr+dec)

oq='**Open questions a future session must close:**\n\n'
q='''*   **The decision about a person's staying as a reserved class.** Under the interim two-partner rule, before the first not-held close or the first non-negotiable line, because the hand-off package has nowhere lawful to go until it exists; with counsel on what the flag's record, the line, and the package may hold. Founders. S14 P26, `86akh5u8m`, `86akh5u77`. Session 15 designs the mechanism that receives the package.
*   **The horizon window's parameters as counts.** The thresholds it reads, the missed-services count, the window's length, the moves' count, the seat-repeat count, and the resumed-trigger count; starting values recommended in the record's own units, set at or before the first reset against the first year's counts (P45). S14 P22.
*   **The non-negotiable line's lifetime, and whether one line is itself the decision about staying.** Held on the definitions of toxicity and exploitation (canon's owner, before the first flag read) and the hierarchy ruling. S14 P27, finding 19.10, `86akht39y`, `86akh3rx4`.
*   **The return to an earlier horizon as a move the person chooses, with the weight moving on the form's date.** S13's architecture did not anticipate a downward move. Founders. S14 P32, extending S13 P23 and P29.
*   **Who lawfully holds the employment record with no HR seat.** The record removed the back-office administrator into software; her HR's functions are split between the flag read's second reader, the Operations Lead's employment record, and counsel. S14 finding 19.1, P34.
*   **Time in a seat against canon's Jeong and Nunchi, and canon's care-and-correction reading for a seat.** Canon's owner, beside the advancement wording. S14 findings 19.4 and 19.12, `86akhcz22`.
'''
assert out.count(oq)==1; out=out.replace(oq,oq+q)

amend('**Where a hire that does not hold is read, and what in the hiring system','Closed by S14 as a mechanism: a horizon window opened inside the first year triggers the calibration read on the packet, written to the hiring system and never to the person (S14 P29, `86akh9t9q`).')
amend('**Where a non-negotiable breach by a person goes.**',"Narrowed by S14: the destination after the flag is the flag read, the line is written jointly by both leads in a closed form, and a decision about staying is a reserved class at the partners' review (S14 P24 to P26). Open: the line's lifetime and whether one line is the decision (P27), a breach by a lead (S15), and the definitions of toxicity and exploitation (canon's owner).")
amend('**Who holds a lead\'s check-in.**','S14 adds that a lead\'s own horizon window, flag read as subject, and departure wait on it; the team\'s reading is held for S15 and the founders (S14 P36).')

k='The session task\'s own text carried a figure the record calls unfinalized, which is why the reading rule applies to briefs and task text as well as to the record.'
assert out.count(k)==1
out=out.replace(k,k+' Session 14 found thirteen, six of which would have surfaced from a narrow read of the white paper\'s people pages and seven of which would not; among them, the record has no HR seat and no owner for employment law, the record never describes the house ending anyone\'s employment, and time in a seat is worth nothing in the record and everything in canon\'s Jeong and Nunchi.')
open('extraction/s14/tracker-after.md','w',encoding='utf-8').write(out)
print(len(src.encode()),len(out.encode()))
