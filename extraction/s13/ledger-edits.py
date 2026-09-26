import sys
PAGEID = sys.argv[1] if len(sys.argv) > 1 else 'PAGEID'
src = open('extraction/s13/tracker-before.md', encoding='utf-8').read()
out = src

def amend(key, addition):
    """Append a sentence to the end of the single bullet line containing key."""
    global out
    assert out.count(key) == 1, key
    i = out.index(key)
    end = out.index('\n', i)
    start = out.rindex('\n', 0, i) + 1
    assert out[start:end].startswith('*   '), out[start:start + 60]
    out = out[:end] + ' ' + addition + out[end:]

# 0. first-action block
i = out.index('## First action')
j = out.index('* * *', i)
first = '''## First action

Run Session 14. New chat:

> Sŏn. Scaling People, session 14. ClickUp task `86ajgmjk1`. Begin.

Session 13 is complete and its page is in the Operating System doc. Session 14 reads the ledger below before anything else. It is Chapter 5, high, middle, and low performers, owned by the People Systems Designer with the Hospitality Operations Realist. Its inbound constraints from Sessions 12 and 13: no review output and no feedback act reaches pay, and the point system reads four inputs on records and nothing a person judges, so no performance tier adds a pay line, a marker, a weight, or a withheld anything; the review has no rating and is never a managing-out file; no coaching record exists to cite; and the top of book p.419 (the end of "managing disappointment" and the closing paragraph on the formal review) was answered by Session 13, so Session 14's material begins at "Managing high performers."

'''
out = out[:i] + first + out[j:]

# 1. last session + state
i = out.index('**Last session completed:** Session 12')
j = out.index('**Decisions binding a future session:**')
state = f'''**Last session completed:** Session 13, 2026-09-24. Chapter 5, the formal review process (minimum viable people processes, performance feedback with peer reviews, self-assessment, and manager review, the sidebar on delivering reviews, calibration and its roles) and compensation (compensation conversations, comparisons, and managing disappointment, running onto the top of p.419), with the workbook's Performance Review Template and Compensation Conversations Preparation and Guide.

**State:** S13 designed the review and the compensation architecture with no figure anywhere. A person is reviewed every six months on their own clock, the first time six months after their first paid hour, in a paid thirty-minute block the stack places, held by the lead who holds their check-in, in their chosen language, with no one else present; there is no review season, and the interval is a reset parameter with the record's three-month floor. The review opens on the person page whole, is assembled by the stack, reads the four Session 6 dimensions as states from records the person can already read and never as marks, writes one record in two halves (the stack's states with citation dates and the person's own words), and the lead writes nothing in their own voice. "No surprises" is a mechanism: a lead holding something not on a record says nothing of it at the review and asks for a placed check-in, and the review ends with one question whose "something new" answer is a candor line on the lead's entry. Her self-assessment survives as the person's half; peer reviews, the manager narrative, rating designations, and calibration are refused, each with the mechanism that does its work. Pay is two layers on one pay date: base pay per seat, which the record never describes, and the pool, one per calendar day for the whole house, a defined proportion of a defined base computed by the stack at every close and shown on the person's pay page by the next morning. Points are set by four inputs on records (the seat's published weight at the horizon held, moved by a recorded unlock; the cross-strand, cross-period, and teaching markers while current; days worked, a calendar day counted once; the salaried every-open-day rule) and never by a review, a check-in, a designation, a recognition, or any judgment of a person. Review and pay are separated by design; the unlock, the markers, the pool's weighting, and the days carry her "pay for performance." Every value sits on a parameters register with its owner and is unset, because financials are not a context source for this program. The session task's text and two carryovers carried a percentage the record calls "still being finalized" and named an excluded source; neither was used, and the page records the disagreement as a finding without the figure. Fifty positions: forty recommended, six founder-gated, three chef-gated, one team-filled. Readiness rows 155 to 168, so the test stands at one hundred sixty-eight. Twenty-two instrument specifications, eleven used and eleven refused. Thirteen findings inside the record, four of which would surface from a narrow read of the white paper's review paragraph and pay section and nine of which would not. Page `{PAGEID}`.

'''
out = out[:i] + state + out[j:]

# 2. decisions
dec_hdr = '**Decisions binding a future session:**\n\n'
s13dec = '''*   **No review output and no feedback act reaches pay, and the point system reads four inputs on records and nothing a person judges. Binds S14, S15, S16, S17.** A person's points on a day are the seat's published weight at the horizon held (moved by a recorded unlock on its date), the cross-strand, cross-period, and teaching markers while current, the days worked, and the salaried every-open-day rule; never a review, a check-in, a rating, a designation, a recognition, a lagging indicator, a customer's rating, a sales attribution, hours, tenure, or a negotiation. A later session may design what S14 does with a person whose work is not holding, what S15 does with a lead's review and a departure's final pay, and what the reset does with the interval and the parameters; it may not add a pay tier, a rating, a review field a pay mechanism reads, or a person's judgment as an input to anyone's points. S13 names this as the one thing on its page a later session cannot revise at ordinary cost. S13 P23, P36, P37.
*   **The review has no rating and reads only what the person can read. Binds S14, S15, S17.** Six months on the person's own clock, placed by the stack, a paid thirty-minute block held by the check-in's holder in the person's language with no one else present; it opens on the person page whole, reads the four dimensions as states and never as marks, writes the stack's states and the person's own words, and ends with the "something new" question as a candor line on the lead's entry. It reaches no one beyond the person and their lead and may never become a verdict, a rating, a rank, a nomination, a managing-out file, a read of Nunchi or Jeong, or a room. S13 P3, P4, P6, P7, P9 to P11, P17.
*   **A day is a calendar day counted once, and there is one pool per day for the whole house. Binds S17.** A day is any calendar day with a scheduled shift, counted once whatever the periods worked; the pool is computed at every close across every open period. One pool per day is the team's reading of the record's dinner-shaped sentence, marked so. S13 P22, P24.
*   **Salaried seats hold a salary as base pay and pool points on the every-open-day rule. Binds S15, S16.** The salaried list and a lead's entry point are founder-gated; a lead's entry point is named without altitude. The partners' own place in the pool is S16's. S13 P28, P31.
*   **Pay parameters are named on a register and set by no session. Binds every session.** The percentage, the pool's base, the seat weights, the marker values, the wages and salaries, the payment rhythm, the generosity range's value and the financial recovery threshold, and the benefits gate are rows on the parameters register on the partners' page with their owners, unset in this program. S13 P26, P35.
*   **Vocabulary: "review" unqualified is the person's; "points" is the pay system's word. Binds S17.** The record's leads', house, partners', and gate reviews are always qualified. A recognition is never a point. S13 section 5, S11 P13.
*   **The readiness test stands at one hundred sixty-eight rows. Binds every session from here.** Rows 155 to 168 from S13; rows from S14 start at 169. Rows 160, 161, 163, 166, and 168 carry a founder-gated hold inside them and are read as failed until it closes; rows 157, 162, and 165 are read at the first reset as well as the gate. S13 section 17.
'''
assert out.count(dec_hdr) == 1
out = out.replace(dec_hdr, dec_hdr + s13dec)

# 3. open questions
oq_hdr = '**Open questions a future session must close:**\n\n'
s13oq = '''*   **The parameters register's rows an offer needs.** The percentage, the pool's base, the seat weights for the two lead seats, their salaries, and the payment rhythm, set by the founders with Dominic's domain and counsel, before the leads' offers, because item 6 gates every offer. Financials are not a context source for this program. Urgent. S13 P26, P31, `86akh9tb0`.
*   **Whether the pool's total is on the pay page, and whether the percentage's value is on item 6.** The pay page's legibility and the record's "nothing withheld" meet the transparency line at exactly one figure: the daily arithmetic discloses revenue. Founders, with `86akh5uby`, before the first pay page. S13 P40, finding 19.5.
*   **Setting or changing an architecture parameter as a reserved class.** S3's list does not include pay parameters; S13 recommends adding them under the interim two-partner rule. S13 P45, `86akh5u8m`, `86akh5u77`.
*   **The pay parity read's data, with counsel.** The three rates, the tags, and whether the data may be held at all. S13 P40, `86akh9tbd`.
*   **The benefits gate.** The record promises a fast path to full benefits "as the business supports them"; S13 recommends stating benefits at hire as facts and the path as a gate with conditions and no date, on the partners' page. Founders, before the first offer. S13 P25, finding 19.11.
*   **A lead's review holder.** Waits on `86akhb2jg`; the team's reading is whoever holds the lead's check-in, on the same form. S13 P20, routed to S15.
*   **What exploitation is.** Canon's non-negotiable "no exploitation ever" is defined in neither artifact, and pay is where it is tested. Canon's owner with the founders, beside the hierarchy ruling and the toxicity definition, before the first parameter that could be read as lean is set. S13 finding 19.12.
*   **The partners' place in the pool, and a departure's final pay.** Routed to S16 and S15 (with counsel). S13 B2, B3.
*   **The overnight cleaning crew outside the pool.** The record calls the whole team one team and the close depends on contracted labor outside the web. With S8 finding 21.10, `86akhcz6k`. S13 finding 19.13.
'''
assert out.count(oq_hdr) == 1
out = out.replace(oq_hdr, oq_hdr + s13oq)

# 4. narrow existing entries
amend('**Compensation splits. Binds S5, S6, and S13.**',
      'Answered by S13 as a mechanism with no figure: the architecture is designed and every value is a founder-gated row on the parameters register (S13 P22 to P26, P35).')
amend('**What training pay is.**',
      'Designed by S13: training pays base plus the seat\'s entry weight from the first paid hour; the value is on the parameters register, founder-gated (S13 P33, P34).')
amend('**Which seats are salaried.**',
      'Priced by S13 as a mechanism: a salaried seat holds a salary as base pay and pool points on the every-open-day rule; the list and values stay founder-gated (S13 P28, P31).')
amend('**What a lead enters at.**',
      'S13 names the entry point as the lead seat\'s entry horizon and its weight, without altitude; ratification and value founder-gated (S13 P28, P31).')
amend('**Whether a first interview may run while the compensation mechanics read "being finalized."**',
      'Narrowed by S13: item 6 can be stated as a mechanism with unset values; whether a first interview runs on it is founder-gated (S13 P39, P40).')
amend('**Whether the compensation architecture is ratified ahead of Session 13, or dinner\'s gate slides.**',
      'S13 has now designed the architecture; what remains is ratification and the register\'s rows an offer needs, ahead of the leads\' offers (S13 section 21).')
amend('**The unit of a departure\'s "calculable" cost.**',
      'S13 adds a departure\'s final pay as a pay question routed to S15 with counsel.')

# 5. reading note
key = 'the record gives what is observed about a person no destination but the capture.'
assert out.count(key) == 1
out = out.replace(key, key + ' Session 13 found thirteen, four of which would have surfaced from a narrow read of the white paper\'s review paragraph (WP p.19) and pay section (WP p.20) and nine of which would not; among them, base pay is never described though every paid act assumes it, the pay page\'s daily arithmetic discloses revenue against the transparency line, and "no exploitation ever" is defined in neither canon artifact. The session task\'s own text carried a figure the record calls unfinalized, which is why the reading rule applies to briefs and task text as well as to the record.')

open('extraction/s13/tracker-after.md', 'w', encoding='utf-8').write(out)
print(len(src.encode()), '->', len(out.encode()))

# 6. clean the escaped-asterisk artifact in the protocol header (one deliberate edit, per S12's note)
import re
out2, n = re.subn(r'\*\*Reconciled 2026-09-11 against\*\* \*\*`CLAUDE\.md`\*\*\*\*(?:\\\*)+, which is the governing document for this program\.\*\*',
                  '**Reconciled 2026-09-11 against `CLAUDE.md`, which is the governing document for this program.**', out)
assert n == 1, n
out = out2
open('extraction/s13/tracker-after.md', 'w', encoding='utf-8').write(out)
print('cleaned header;', len(out.encode()))
