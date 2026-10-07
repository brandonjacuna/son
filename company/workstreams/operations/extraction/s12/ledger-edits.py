import sys
PAGEID = sys.argv[1] if len(sys.argv) > 1 else 'PAGEID'
src = open('extraction/s12/tracker-before.md', encoding='utf-8').read()
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

# 0. first-action block
i = out.index('## First action')
j = out.index('* * *', i)
first = '''## First action

Run Session 13. New chat:

> Sŏn. Scaling People, session 13. ClickUp task `86ajgmjey`. Begin.

Session 12 is complete and its page is in the Operating System doc. Session 13 reads the ledger below before anything else. It is Chapter 5, the formal review process and compensation, owned by the People Systems Designer with the Hospitality Operations Realist. Its inbound constraints from Sessions 11 and 12: the hypothesis has no page and no coaching record exists to cite, so the review opens on the person's own lines; the four scorecard dimensions bind and nothing is added at review that was not read at hiring; feedback never touches pay; and compensation's architecture, held since Session 2, is this session's.

'''
out = out[:i] + first + out[j:]

# 1. last session + state
i = out.index('**Last session completed:** Session 11')
j = out.index('**Decisions binding a future session:**')
state = f'''**Last session completed:** Session 12, 2026-09-24. Chapter 5, the chapter opener and its untitled introduction, hypothesis-based coaching, giving hard feedback, and creating a culture of informal feedback, with the workbook's Performance Improvement Documentation Templates read for the written recap.

**State:** S12 wrote the coaching model and the feedback culture. A hypothesis about a person is one shape, a behavior in a service and its impact on the work, formed only from records the person can already read and the lead's unwritten observation, and it has no page. It is tested once at the check-in, after the person's own account, as her open-ended question and then an observation owned as the lead's perception, in the person's chosen language; the one line is the person's only and is the only residue of coaching; no written recap exists. Her conversation (explorer, not lecturer) is kept as a way of talking and placed at the check-in. The session task's "direct transfer" premise is answered as two transfers: during a live service an operating instruction (the object of the work as subject, a present act as verb, complete when done) transfers whole to the range's holder, and feedback about a person is never said on the floor, at the pass, or in any room and waits for a check-in, which the lead may ask the stack to place ahead of the interval once per interval. Failure is typed at the capture review on the process update, never on a person; an intelligent failure is never corrected. Candor moves in every direction and lands on a record every time; corrective feedback between peers has no surface and no record. A non-negotiable breach is never a check-in item or a hypothesis. The Maitre d's coaching load is read as three counts at the reset. The kitchen's version is chef-gated with the floor's rules recommended unchanged. Forty-nine positions: forty-two recommended, four founder-gated, two chef-gated, one team-filled. Readiness rows 142 to 154, so the test stands at one hundred fifty-four. Twenty-two instrument specifications, nine used and thirteen refused, routed, or answered by reference. Twelve findings inside the record, two of which would surface from a narrow read of the white paper's performance management section and canon's voice section and ten of which would not. Page `{PAGEID}`.

'''
out = out[:i] + state + out[j:]

# 2. decisions
dec_hdr = '**Decisions binding a future session:**\n\n'
s12dec = '''*   **The hypothesis has no page, and the correction is the check-in's. Binds S13, S14, S15, S17.** A lead's reading of a person is said at the check-in, once, as an observation of behavior and impact, and is written nowhere; the only record of coaching is the person's own line, which may never hold the lead's hypothesis, observation, summary, or a verdict; no written recap of a hard-feedback conversation exists. No coaching record exists to cite in a review, a plan, or a decision about staying. S12 names this as the one thing on its page a later session cannot revise at ordinary cost. S12 P5, P10, P13, P14, P48.
*   **Two kinds of live speech. Binds S13 to S17.** During a live service an operating instruction (the object of the work as subject, a present act as verb, complete when done) is the range's holder's to say to anyone doing that work; feedback about a person is never said on the floor, at the pass, or in any room the roster is in. A live call repeated at the same person on the same object in one service is a sequence or readiness question captured as process. Whether a founder on the floor is bound by the rule is routed to S16. S12 P15.
*   **The placed check-in is a second trigger, ratified beside S4 P15. Binds S13, S15, S17.** A lead may ask the stack to place a check-in ahead of the interval once per interval, on the person's next shift the lead also works, in the pre-service window, paid, with no reason written; the interval resets from it. The count of placed, extended, and moved check-ins per lead per month is a load reading at the leads' review and the reset, never review context or a read of the person. S12 P16, P37.
*   **Failure is typed on the process update, never on a person. Binds S14, S17.** Basic, complex, or intelligent, typed at the capture review by the reviewing lead; a basic failure reaches a person only as a hypothesis after recurrence on the same seat with the placement already fixed; an intelligent failure is never corrected; the count by type is read per period and never per person; a non-negotiable breach is not typed. S12 P28.
*   **The not-yet form and the tension-slack hand-off are read in their own words. Binds S14.** A not-yet readiness form is read row by row in the assessor's words with nothing added by the lead; the tension-slack hand-off works only from the domain's dated fixes and the person's own lines; "disengaged" is never said and the motivation questions are never asked. The workbook's initial documentation template is refused and its three follow-on letters are routed to S14 under the constraint that every check-in writes only the person's words. S12 P14, P21, P24.
*   **A non-negotiable breach is never coaching. Binds S14, S15.** Never a check-in item, a hypothesis, a typed failure, a placed check-in's reason, or a lead's line on the person page; the flag goes to both leads the same day and what follows is not coaching. S12 P36.
*   **The readiness test stands at one hundred fifty-four rows. Binds every session from here.** Rows 142 to 154 from S12; rows from S13 start at 155. Row 143 reads against P16's ratification, row 151 fails until the interpreter ruling, and row 154 reads not yet until principles version one exists. S12 section 16.
'''
assert out.count(dec_hdr) == 1
out = out.replace(dec_hdr, dec_hdr + s12dec)

# 3. open questions
oq_hdr = '**Open questions a future session must close:**\n\n'
s12oq = '''*   **The narrowing of S4 P18.** S4 P18 lets a lead say anything between check-ins in person and write it at the next; S10 P15 makes the private correction the check-in's. S12 recommends narrowing S4 P18 to the live call and the placed line, with the correction itself the check-in's, and states the alternative. Founders ratify beside S4 P15, P18, and S10 P15, before the first training service. S12 P19.
*   **The placed check-in's reset parameters.** The ceiling on placed check-ins per lead per month and the fit count are set at the first reset from the team-filled coaching load baseline written at the first house review. S12 P16, P37, P49.
*   **What toxicity is.** Canon names toxicity as a non-negotiable and defines it in neither artifact, so the line between hard feedback and the thing the non-negotiable forbids is undrawn. Founders with canon's owner, beside the hierarchy ruling (`86akh3rx4`), before the first non-negotiable flag. S12 finding 18.9.
'''
assert out.count(oq_hdr) == 1
out = out.replace(oq_hdr, oq_hdr + s12oq)

# 4. amend questions S12 narrows
bullet("**Where a non-negotiable breach by a person goes.**",
 "**Where a non-negotiable breach by a person goes.** Blame absorption runs one way, and the one act canon treats as a person's has no path in the record. Founders, with S12, S14, S15. S10 finding 20.5. Narrowed by S12: the breach is never a check-in item, a hypothesis, a typed failure, a placed check-in's reason, or a lead's line on the person page, and the flag goes to both leads the same day (S12 P36). Open: the destination after the flag, who writes the non-negotiable line on the person page and in what form (S8 P25's eligibility rule reads it), a breach by a lead, and the definition of toxicity. `86akht39y`.")
bullet("**Who holds a lead's check-in.**",
 "**Who holds a lead's check-in.** The record runs feedback both directions and names no one for the leads. Urgent since S9: the diagnosis of a lead's own node is half-blind until it closes, the lead's career conversation and the seat holder's line in the reset's first read wait on it, and row 118 fails. S10 adds the environment's reason: a concern about a lead is the one topic with no destination the lead does not hold, so safety to speak stays partial, and every range breach on a lead's environment entry has no destination. S12 adds that every coaching trigger for the Maitre d's own work has no destination, the Maitre d's re-training trigger has no reader, and blame absorption stops one seat short (S12 finding 18.5). The team recommends closing it before the leads are in the building six weeks ahead of dinner's gate. Finding 19.7, P21, S9 P35, S10 P15, S12 section 15, `86akhb2jg`.")

# 5. reading note
key = "Session 11 found twelve"
assert out.count(key) == 1, key
i = out.index(key); end = out.index('\n', i)
out = out[:end] + " Session 12 found twelve, two of which would have surfaced from a narrow read of the white paper's performance management section and canon's voice section and ten of which would not; among them, the record's one form of hard feedback is addressed to a customer, and canon builds an observation post on the floor while the record gives what is observed about a person no destination but the capture." + out[end:]

open('extraction/s12/tracker-after.md', 'w', encoding='utf-8').write(out)
print(len(src.encode()), '->', len(out.encode()))
