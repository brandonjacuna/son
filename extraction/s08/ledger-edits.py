import re, sys
PAGEID = sys.argv[1] if len(sys.argv) > 1 else 'PAGEID'
src = open('extraction/s08/tracker-before.md').read()
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

# 1. last session + state
i = out.index('**Last session completed:** Session 7')
j = out.index('**Decisions binding a future session:**')
state = f'''**Last session completed:** Session 8, 2026-09-13. Chapter 4, Team structures.

**State:** S8 drew Sŏn's structure from the record's web and the two-lead management layer, under one founder ruling Brandon gave in the session: the floor manager and the Maitre d are one seat, the Maitre d as master of the house holding both roles rather than two leaders on the floor (`86akh5u9g`). The room's owner in every earlier decision-rights entry now names that seat, and S8 completed the server's escalation destination, the transition trigger, emergency authority, and the live cross-domain call where the record allows, marking the team-supplied parts. It routed the canon change to `86akh3tjb` rather than writing canon. It tested the seat's load and did not reverse the ruling: the room, the door, and the floor side of the pass are carried on services the holder does not work by per-service designations named at the brief, the record's own device, and a stack outage mid-service by a printed degraded-mode procedure, never by a second seat. It settled that Sŏn has one team in her sense, the house, and that the service periods are one team met at different hours for any ratified set, with the charter's dependent interfaces as the test; a period adds seats, designations, interfaces, and a register block, and no leadership line unless the variety pass at its gate requires one. It produced the leadership-line list (Operations Lead, Maitre d, the chef seat, Head of Beverage, and the Station Leads, chef-gated) with the count a stated gap, and ran the pre-opening requisite-variety pass: two partial holes, three parts resolving to a founder, and four classes converging on the Maitre d's seat. It made the Maitre d the domain lead for both floor strands, runners and hosts included, read the Lead Host as a designation, read the Head of Beverage as a seat, reconciled the three seat lists into inventory rows with kitchen rows chef-gated, and refused levels, ladders, dotted lines, business units, layers, and Code Yellows for their forms. It defined cross-strand fluency so it can be demonstrated, placed cross-period fluency, split advancement into three seats, placed the cross-domain signer, and held fourteen kitchen items for the chef's onboarding packet above an eleven-item shared spine. Fifty-six positions: forty-four recommended, seven founder-gated, four chef-gated, one team-filled. Readiness rows 93 to 106, so the test stands at one hundred six. Twenty-one instrument specifications, eleven used and ten refused. Eleven findings inside the record, five of which would surface from a narrow read and six of which would not. Page `2ky45bmy-{PAGEID}`.

'''
out = out[:i] + state + out[j:]

# 2. decisions: S8 block at top
dec_hdr = '**Decisions binding a future session:**\n\n'
s8dec = '''*   **The floor manager and the Maitre d are one seat, by Brandon's ruling of 2026-09-13, and the room is never held by a second seat. Binds every session from here.** The Maitre d holds the room and the floor team. On services the seat's holder does not work, the room's live functions are held by a room designation named at the brief, and the threshold and the floor side of the pass by the door and sequence designations; each lasts one service. A load finding on the seat is carried by a designation, the stack, or a procedure, never by reinstating a floor manager under another name. Canon still names a floor manager until its owner versions it (`86akh3tjb`). S8 names this as the one thing on its page a later session cannot revise at ordinary cost. S8 section 2, P4, P25.
*   **The floor is one domain with two strands, and the Maitre d is its lead for both. Binds S9, S12, S14, S15.** The Maitre d holds the check-ins of servers, hosts, and runners, opens their seats, and decides their hires; the Operations Lead reads the inward strand's outputs as a record and holds no floor check-in. The Lead Host is a designation, not a seat. S8 P21, P24.
*   **Sŏn has one team in her sense, the house. Binds S9, S10, S11, S17.** Her "team" is translated as the house for the collective, the domain for a manager's reports, and the service roster for who is on tonight. A domain, a strand, and a service period are not teams. S8 P6.
*   **The service periods are one team met at different hours, for any ratified set. Binds S17 and every gate review.** A period is a period of one restaurant when its charter's dependent interfaces are non-empty; a charter that fails the test is not opened. A period adds seats, a designation set, interfaces, a register block, and a period plan, and adds no leadership line unless the requisite-variety pass at its gate requires one, argued and ratified before it opens. No period has a lead, a team, or a roster of its own. S8 P7, P8, P19.
*   **Sŏn has no levels and no ladders; a lead enters at the lead seat's entry horizon. Binds S13 and S15.** The functions a ladder carries are carried by the seat sheet's horizons, connections on the person page, unlock-tied progression, one-service designations, and outward movement. What a lead enters at is read as two webs, founder-gated. The salaried test is structural: ownership of a domain or program across every open period. S13 prices; neither is a rank. S8 P30, P31, P33.
*   **Cross-strand and cross-period fluency are demonstrated, not asserted. Binds S13.** Cross-strand: two readiness forms, one per strand in one domain, each scored by that strand's assessor in a real service, plus a seat held on each strand inside a stated window, recorded as connections. Cross-period: a period-plan readiness form and a seat held in each period. Never a dimension, a rank, or a placement tool. S8 P35, P36.
*   **Advancement has three seats. Binds S12, S13, S14.** The stack schedules on the sheet's unlock period; an assessor from the pool scores, never the mentor and never the decider; the domain lead records the form at the check-in and may not override it either way. For a second domain, the receiving domain's assessors score and its lead records. Which of the record's two wordings stands is founder-gated. S8 P37, P38, P39.
*   **Code Yellows are refused; a live risk is a line on the partners' page. Binds S11 and S16.** From the existential-risk register, with a founder owner, a closing condition, and a daily written state, and no special powers. S8 P42.
*   **A structure change is a versioned inventory entry, and it reaches the team without an announcement. Binds S11 and S15.** Proposed through the leads' review, versioned by the partners' review, with its reason first; it reaches the team by the affected person's check-in, the sheet's version, the brief, and the team home, in that order. S8 P49.
*   **Work style demand by period is answered by the charter and the schedule, never by a profile. Binds S10.** S8 P40.
*   **The readiness test stands at one hundred six rows. Binds every session from here.** Rows 93 to 106 from S8; rows from S9 start at 107. Row 101 holds on the chef ruling and row 105's second half on a second charter existing. S8 section 19.
'''
assert out.count(dec_hdr) == 1
out = out.replace(dec_hdr, dec_hdr + s8dec)

# 3. open questions: S8 block at top
oq_hdr = '**Open questions a future session must close:**\n\n'
s8oq = '''*   **The room designation, and the door as the threshold's holder.** Every brief from the first training service names who holds the room on services the Maitre d does not work; canon's Maître d' at the porch steps is read as a register set by whoever holds the door, not a fixed post, which routes to canon's owner. Urgent. S8 P25, P5.
*   **The team-supplied parts of the ruling's decision-rights entries.** The transition's trigger destinations, emergency authority's range and triggers, and the live cross-domain call's range and triggers are the team's, not the record's; the chef seat ratifies the kitchen's half. S8 P2, P52.
*   **Whether the Head of Beverage is a seat and a leadership line.** The record carries it as a designation, a program owner, and a collapsed seat. The team reads a seat, its check-in held by the Maitre d. S8 P9, finding 21.3.
*   **Which of the record's two advancement wordings stands.** The structure runs on the three-seat reading until ratified. S8 P38, extending `86akhb2ja`.
*   **Who holds an event in the room.** The record removes the events team and commits events; nothing holds one. S8 finding 21.9.
*   **The overnight cleaning crew's place in the structure.** The close depends on contracted labor outside the web. S8 finding 21.10.
*   **The leadership-line count.** Four named lines plus the Station Leads; the total is a gap until the chef fills the Station Leads. The check-in load beneath the Maitre d's seat is read first at the mechanism reset. S8 P12, P14.
'''
assert out.count(oq_hdr) == 1
out = out.replace(oq_hdr, oq_hdr + s8oq)

# 4. amend questions S8 closes or moves
bullet('**Who signs a competency held across two domains.**',
 '**Who signs a competency held across two domains.** Placed by S8: the receiving domain\'s assessors score on the receiving seat\'s rows and the receiving domain\'s lead records the form, the kitchen chef-gated. The founders\' ratification remains open. P40, S8 P39, `86akhb2ja`.')
bullet('**Which seats are salaried.**',
 '**Which seats are salaried.** Structural half closed by S8: a seat is salaried when it owns a domain or program across every open period, which the Operations Lead, the Maitre d, the chef seat, and the Head of Beverage meet, with the Station Leads chef-gated. The founders ratify the list and S13 prices it. Finding 18.7, S8 P33, P34, `86akh9tbw`.')
bullet('**What a lead enters at, when the record says',
 '**What a lead enters at.** Structural half closed by S8 as two webs: a lead holds a center seat in the house\'s web and enters their own inverted web at its center like every person, at the lead seat\'s entry horizon, never a rank. Founder ratification open; S13 names the entry point. Finding 18.3, S8 P31, P32, `86akh9tbz`.')
bullet('**Whether the Lead Host seat exists at all.**',
 '**Whether the Lead Host seat exists at all.** Closed by S8 for the structure: the Lead Host is a per-service designation held by a host seat; the uniform tables are canon\'s owner\'s. Finding 18.9, S8 P24.')
bullet('**Who signs off a competency held across two domains.**',
 '**Who signs off a competency held across two domains.** Merged with the entry above by S8. Finding 18.8.')
bullet('**The owner of the seat inventory.**',
 '**The owner of the seat inventory.** S8 holds the inventory\'s structure and reconciled the three seat lists into rows, with kitchen rows chef-gated, the Lead Host a designation mark, and events and the overnight crew recorded as gaps. The owner stays founder-gated: the team recommends the partners\' review on the partners\' page, the Operations Lead holding the record. Row 36 and row 93 fail until it closes. `86akh7qq4`, S8 P27, P28.')
bullet('**The domain lead for the inward-facing floor strand, and for hosts.**',
 '**The domain lead for the inward-facing floor strand, and for hosts.** Closed by S8 for the structure under Brandon\'s ruling: the Maitre d, for both floor strands, runners and hosts included; runner and host seats can open. The founders ratify P21. `86akh7r10`, S8 P21.')
bullet('**Whether the floor manager and the Maitre d are one role or two, and which owns the room.**',
 '**Whether the floor manager and the Maitre d are one role or two, and which owns the room.** Closed by Brandon\'s ruling, 2026-09-13: one seat, the Maitre d, as master of the house. Canon\'s wording routed to `86akh3tjb`. `86akh5u9g`, `86akh5utd`, `86akh2r3e`; S8 section 2.')
bullet('**The seat that starts service and turns the room to late night.**',
 '**The seat that starts service and turns the room to late night.** Owner named by S8 under the ruling: the Maitre d as the room\'s owner for the service, or the room designation on services the Maitre d does not work. Trigger destinations are the team\'s and open with the ruling\'s entries above. `86akh5u94`, S8 2.3.')
bullet('**The owners the record leaves unnamed in the decision-rights register.**',
 '**The owners the record leaves unnamed in the decision-rights register.** Management sign-off at the sonic system\'s second tier, now a canon question under the ruling (`86akh3tjb`); leadership review for content; the owner of the David flag. S8 named the person who triggers the pre-service scene and the late-night transition and the holder of emergency authority during a service: the Maitre d for the room. `86akh5u94`.')

# 5. reading note
key = 'and one sets a bought tool against canon.'
assert out.count(key) == 1
out = out.replace(key, key + ' Session 8 found eleven, five of which would have surfaced from a narrow read of the structure pages (WP pp. 9 to 11, 14, 22) and six of which would not; two turn on canon\'s two versions against the white paper\'s management layer, and one found a committed activity, events, that the leadership delta removed and nothing holds.')

open('extraction/s08/tracker-after.md', 'w').write(out)
print(len(src.encode()), '->', len(out.encode()))
led_b=src[src.index('### Context ledger'):src.index('### Archive')]
led_a=out[out.index('### Context ledger'):out.index('### Archive')]
for bad in ['\u2014','Good Energy','Dosi','Luxx',' guest']:
    assert led_a.count(bad)==led_b.count(bad),(bad,led_b.count(bad),led_a.count(bad))
print('lint ok')
