src=open('extraction/s07/tracker-before.md').read()
out=src

def rep(old,new,count=1):
    global out
    assert out.count(old)==count,(old[:80],out.count(old))
    out=out.replace(old,new)

# 1. last session + state
i=out.index('**Last session completed:** Session 6')
j=out.index('**Decisions binding a future session:**')
state='''**Last session completed:** Session 7, 2026-09-12. Chapter 3, Onboarding, Hiring mistakes, and the Chapter 3 exercises.

**State:** S7 built what happens to a person between accepting a seat and their ninety-day plan closing, for the hourly edge seat first, the kitchen seat under the chef ruling, and the lead as the variant. It held the record's onboarding and training paragraphs as decided and built the mechanism under them, into the bought stack (Trainual, Loom, Rippling, Greenhouse, Google Workspace), stating for every placement whether it is configuration, a build, or to confirm. It held one bought tool rather than building into it: no synthesized presenter in any module until canon rules on whether internal training sits inside its prohibition on AI-generated imagery. It wrote the period count as a parameter, dinner first, a new period adding a module set and a register block. It recorded that the record's own "why before how" commitment is unmet, because the charter is unratified, and left the why block's mission and principles empty rather than filling them with brand language. It defined service-ready once, gated the first solo on a readiness form using the same rows as S6's paid practical, scored by an assessor who is not the mentor, and wrote the ninety-day plan as a plan block on the person page carried by the six check-ins, one read per check-in, with no dimension mark, rating, free text, or probation label. It put felt knowledge on a sequence off the chef chain's menu link, with tastings before anyone serves alone, and left the count chef-gated rather than inventing an interval. It named a mentor pool beneath S5 P16, paid mentoring as shift, and routed training, authorship, and mentoring pay to S13 with three constraints. It made readiness row 4 an onboarding output through five moments. It answered her hiring mistakes as a state the house reads and fixes in the building first, and routed managing out to S14 and S15. It kept working-with-me off hourly seats, stood the chef's exchange as S1 decided, and wrote one for every lead inside the lead's plan. Sixty-one positions: fifty-three recommended, five founder-gated, two chef-gated, one team-filled. Readiness rows 75 to 92, so the test stands at ninety-two. Thirty instrument specifications, seventeen used and thirteen refused. Twelve findings inside the record, five of which would surface from a narrow read and seven of which would not. Page `2ky45bmy-PAGEID`.

'''
out=out[:i]+state+out[j:]

# 2. decisions: insert S7 block at top
dec_hdr='**Decisions binding a future session:**\n\n'
s7dec='''*   **Service-ready is defined once, and the readiness form reads the practical's rows. Binds S8, S13, S14, and S17 above everything else on the S7 page.** A person is service-ready when a readiness form reads ready at the seat sheet's field 6 entry horizon, per seat and per period, and nothing beyond it. The form (I7) uses the same rows as S6's paid practical (I4) plus language, range, and felt-knowledge rows, is scored by an assessor who is not the mentor, is a milestone and never a scorecard, and travels to no review. A candidate and a new hire are read against one list. S7 names this, with the next entry, as the two things on its page a later session cannot revise at ordinary cost. S7 P23, P24, I7.
*   **Nothing is written on a person page during the ninety-day plan but states and the person's own words. Binds S12, S13, S14, S15.** The plan block (I2) holds one goal as a state, milestones as states with dates, the baseline the candidate gave at the first interview, and the six check-in dates, one read per check-in. It refuses dimension marks, ratings, free text about the person, and any probation label. The plan's close is a state, not a review or a verdict. The plan extends once, for a building fix, and never for a person's not holding; a plan not held after one extension is handed to S14 with its record. S7 sections 7.1 to 7.6, P25 to P29.
*   **Nothing is required of a person before their first paid hour. Binds every session.** No module assigned or due before the start date, no pre-arrival reading required; information delivered before arrival is available, not owed. The first shift is a paid orientation block with no table and no station. S7 P15, row 87.
*   **The why block is empty until the charter is ratified. Binds S17 and the founders.** Onboarding delivers mission, principles, and behavioral standard before operational training, in that order, drawn from the charter. The charter is unratified, so the record's own onboarding commitment is unmet and the charter is the blocking dependency. The team recommends charter ratification as a condition of every cohort start date, surfaced as an extension to S5 12.6 and not made. S7 P12, P16.
*   **Operational onboarding runs on S6's training sequence. Binds S12 and S13.** Modules read, live session, observed service, paired services, readiness read, then solo, all on scheduled shift, with two stated differences from S6 P38. No cohort member's first solo is dinner's first service. S7 P10, P18, P23.
*   **The mentor is paid as shift, never scores, never writes on the person page, and comes from a pool. Binds S8, S10, S13.** The pool's five conditions sit beneath S5 P16 as the source of the name recruiting writes. The first wave's mentors are the leads, with provisional marks converted at the mechanism reset. Mentoring, module authorship, and completion pay are S13's, with three constraints. S7 P8, P41, P42, P35.
*   **No synthesized presenter in any module until canon rules. Binds S11 and S17.** Carryover `86ajgmm86` says build into the bought stack; S7 holds Synthesia against canon's prohibition on AI-generated imagery and says so as the one place it does not follow the carryover. S7 P32, finding 19.12.
*   **Cross-domain assessment waits until the person's own plan closes; the own-seat unlock is never held by the plan. Binds S8 and S13.** Tracks are visible from day one. Who signs a cross-domain competency is founder-gated, the receiving lead recommended. S7 P39, P40.
*   **Working-with-me exists for every lead, written between the fourth and sixth check-ins, and never for an hourly seat. Binds S15 and S16.** The chef partner's exchange stands as S1 decided, before the chef signs. S7 P49, P53; the work style grid lives only inside the working-with-me document, and team use is S10's.
*   **A change of domain lead is carried by the person page, not a transition meeting. Binds S15.** S7 P51.
*   **A new period is a module set and a register block, not a second ninety-day plan. Binds S8.** A person already in the house who takes a seat in a new period runs the shorter period plan. S7 P3, P30.
*   **The readiness test stands at ninety-two rows. Binds every session from here.** Rows 75 to 92 from S7. Rows 76, 81, 82, 86, and 88 carry a hold written inside the row and are read as failed at the gate review until it closes. S7 section 17.
'''
rep(dec_hdr, dec_hdr+s7dec)

# 3. open questions: insert S7 block at top; close the chef working-with-me question
oq_hdr='**Open questions a future session must close:**\n\n'
s7oq='''*   **Whether charter ratification is a condition of every cohort start date.** The why block cannot be delivered until the mission and principles land. The team recommends yes. P12, P16, extending `86akh3tdr` and `86akh3tg0`.
*   **The cohort in two waves, decided with the pre-opening hiring burst.** The first wave's mentors are the leads, and the first wave's count is what the leads can carry. P8, with `86akh7qnb`.
*   **Who holds a lead's check-in.** The record runs feedback both directions and names no one for the leads. Finding 19.7, P21.
*   **Whether a coach is engaged for a lead's first months.** A spend; the team recommends none. P22.
*   **Who signs a competency held across two domains.** Now met by two sessions. P40, S6 finding 18.8, to S8 with the chef.
*   **The two canon uniform tables, reconciled before the first fitting.** Finding 19.4, extending `86akh3tjb`.
*   **Whether internal training sits inside canon's prohibition on AI-generated imagery.** Gates any Synthesia module. Finding 19.12, P32.
*   **Whether a training module may explain a Korean term.** Canon says terminology stands without explanation in all brand contexts. Finding 19.6, with `86akh7r2t`.
*   **Where the employee area and the lockers are.** Promised by the record and absent from canon's spatial sequence; a first-shift walk depends on it. Finding 19.11.
*   **What training pay is.** The transparency sheet carries "the training plan with pay dates" and the record does not define training pay. Financials are not a context source; routed to S13. Finding 19.5.
*   **One reading of "no one touches a table until they are actually ready," ratified with S5 P41.** Read literally it contradicts the paid practical. Finding 19.3.
*   **Who approves a module, and what "qualified" means for authorship.** S7 recommends the module standard; the record names no approver and no test. Finding 19.1, P33.
*   **The incomplete onboarding decision-rights entries.** P56.
'''
rep(oq_hdr, oq_hdr+s7oq)

old_wwm='*   **When the working-with-me document is exchanged with the chef partner.** S7, carryover `86ajgnj8t`.\n'
new_wwm='*   **When the working-with-me document is exchanged with the chef partner.** Closed by S7: it stands as S1 decided, exchanged before the chef signs, and nothing in her Chapter 3 material changes it. S7 P49. Carryover `86ajgnj8t` stays open in the register for provenance.\n'
rep(old_wwm,new_wwm)

# 4. reading note
old_note='Read the record in full, including both canon artifacts.'
new_note=old_note+' Session 7 found twelve, five of which would have surfaced from a narrow read of the onboarding pages (WP pp.17 to 21) and seven of which would not; two turn on the canon artifacts disagreeing with each other, and one sets a bought tool against canon.'
rep(old_note,new_note)

open('extraction/s07/tracker-after.md','w').write(out)
print(len(src.encode()),len(out.encode()))
