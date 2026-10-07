import sys
PAGEID = sys.argv[1] if len(sys.argv) > 1 else 'PAGEID'
src = open('extraction/s10/tracker-before.md', encoding='utf-8').read()
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

Run Session 11. New chat:

> Sŏn. Scaling People, session 11. ClickUp task `86ajgmj7c`. Begin.

Session 10 is complete and its page is in the Operating System doc. Session 11 reads the ledger below before anything else. It is Chapter 4, team-building complexities, inclusion, and communication, owned by the People Systems Designer. Its inbound constraints from Session 10: the environment names no person in a room, every speech act has a named destination on a record, and the brief's team slot and the gathering's half are communication surfaces with fixed lists and refusals.

'''
out = out[:i] + first + out[j:]

# 1. last session + state
i = out.index('**Last session completed:** Session 9')
j = out.index('**Decisions binding a future session:**')
state = f'''**Last session completed:** Session 10, 2026-09-14. Chapter 4, Creating the team environment: offsites, meetings, and leadership team meetings, and the workbook's offsite and leadership snippet pages.

**State:** S10 answered the session task's question, whether the Playground Philosophy is mechanisms or a slogan, for the employee side. Canon's test ("does this build or foreclose conditions for agency?") is run on a mechanism as six questions, with canon v3.0's two failure directions as the tight and loose edges. "Conditions for agency" decomposes into ten conditions, each tested against a mechanism: four are mechanisms (legible rules, a stated range, safety to err, a path), five are partial (judgment beyond procedure, safety to speak, being known, time not taken, a say in the rules), and one is a slogan today (a place of their own: the employee area and lockers, promised and placed on no drawing). Two further slogans sit outside the ten: belonging among the team in the steady state, whose one direct carrier is the founder-gated gathering, and the founders' own bandwidth, which the record reads nowhere. Her environment-by-convening is replaced by environment-by-structure: no offsite for the house or the leads, the partners' reset and principles revision held as one annual closed-hour block; her meeting roles, norms, openers and closers, icebreakers, parking lot, decision frameworks, decision logs, personality exercise, and supplemental leadership team refused or absorbed into the mechanism map, the register, and the change record. Psychological safety's environment half is blame the process, the capture, private post-mortems, the check-in's refusals, and every topic having a named destination. The brief's team slot carries one item from a fixed list and records only which item ran. The work style grid has no team use beyond a lead's working-with-me. Every designation carries a rotation floor. Bandwidth is the environment's primary read through cooling failure's line. The staff meal is the one team mechanism the record and canon are silent on, filed founder-gated. Forty-five positions: thirty-four recommended, six founder-gated, three chef-gated, two team-filled. Readiness rows 119 to 129, so the test stands at one hundred twenty-nine. Twenty instrument specifications, seven used and thirteen refused or replaced. Twelve findings inside the record, four of which would surface from a narrow read of canon's Playground page and the white paper's people sections and eight of which would not. Page `2ky45bmy-{PAGEID}`.

'''
out = out[:i] + state + out[j:]

# 2. decisions: S10 block at top
dec_hdr = '**Decisions binding a future session:**\n\n'
s10dec = '''*   **The environment names no person in a room. Binds S11, S12, S14, S15, S17.** No opener asks how anyone is; no brief, close, review, or gathering carries a read or a correction of a person; the work style grid appears on no record about a person; every speech act's destination is a record and not a room. Bad behavior in a meeting-shaped mechanism is corrected by the spine and the chair's clock, the private correction is the check-in's and S12's. S10 names this as the one thing on its page a later session cannot revise at ordinary cost: a later session may add to the slot's list, change the rotation floor, define the score, and design what S12 does with a correction, and may not put a person's state, work style, or failure into any room the roster or the house is in. S10 P14, P15, P20, P30.
*   **The playground test runs as six questions on every mechanism. Binds every session that proposes a mechanism, and S17.** The condition, the legible rule, the open-ended result, the tight edge, the loose edge, and the documented reason with the read that would notice the condition's absence; run on every mechanism on the map at the reset and on any proposed mechanism at entry, beside the four-part test. The ten employee conditions are the answer set to its first question, each with a verdict of mechanism, partial, or slogan. S10 P3, P4, P6.
*   **Every topic has a named destination. Binds S11, S12, S15.** A question goes to the mentor, the check-in, or the channel; a dissent to the hold or the upward question; a failure to the capture; vulnerability is refused as a mechanism. The one undiscussable topic left is a concern about a lead that the lead holds, until `86akhb2jg` closes. S10 P14, P15.
*   **Sŏn holds no offsite for the house or the leads. Binds S11, S16, S17.** The partners' mechanism reset and principles revision are one closed-hour block per year, at no cost to service and with no diagnostic role. The cohort's orientation block is the one existing gathering that does her forming work. S10 P17.
*   **The brief's team slot carries one item from a fixed list and records only which item ran. Binds S11, S17.** In priority: the designations' one line each, what the system learned from the last close as process, a principle against a moment at most weekly, a thread added as a fact. It refuses anything about a person beyond a page fact, a script, a survey, an opener, a personal share, a lagging figure, an announced change, and a build item; ends at the scene trigger; is held by the owner of the room or the room designation. Its five-minute ceiling on a full window, zero on a compressed one, is a reset parameter. If the gathering is approved, its team-making half is as S10 P21 specifies. S10 P20, P21, P24.
*   **The work style grid has no team use beyond a lead's working-with-me document. Binds S12, S13, S15, S16.** Its one team-facing use is upward: a lead's domain may use the lead's own self-placement about the lead. It never names a designation's need and never enters a room as a read of anyone. S10 P30.
*   **Every designation carries a rotation floor, and a designation is never a status. Binds S12, S13, S14, S15.** No eligible person holds it on every service they work in a quarter while another eligible person held it on none, read by the stack's count at the reset and never as the holder's performance. No pay line, page mark, title, reward, or sanction. S10 P33.
*   **Bandwidth is the environment's primary read, through cooling failure's line and the bandwidth ledger and no new read. Binds S14, S17.** `86akh5uw3` and S9 P13 are one rule. Two sources join the line as counts of services: briefs with the slot dropped, and closes with the capture or the note displaced. A culture mechanism met at a bandwidth cost is cooling failure on the mechanism. S10 P34.
*   **Her meeting decision methods are replaced by the register. Binds S11, S15, S16.** The owner decides inside a range; Class B is consultative by rule; Class A is both or neither with the status quo as default under `86akh5u77`. Disagree and commit survives with the disagreement written as a hold and the commitment replaced by the read-back; the senior person speaks last survives for a founder in any room. S10 P26.
*   **After the ninety-day plan the house records only the mentor relationship's shape the person stated, and takes no further act. Binds S12, S13.** The mentor never becomes a sponsor, a coach, or a channel for the lead; the relationship reproduces through the pool. S10 P32.
*   **The readiness test stands at one hundred twenty-nine rows. Binds every session from here.** Rows 119 to 129 from S10; rows from S11 start at 130. Row 125's kitchen half holds on the chef ruling, row 126 on the gathering decision, row 127 on the employee area, and rows 128 and 129 are read at the first house review and the first reset. S10 section 18.
'''
assert out.count(dec_hdr) == 1
out = out.replace(dec_hdr, dec_hdr + s10dec)

# 3. open questions: S10 block at top
oq_hdr = '**Open questions a future session must close:**\n\n'
s10oq = '''*   **Whether the pre-service window carries a staff meal, and its kitchen cost.** Absent from the record and both canon artifacts, and the one team mechanism on her list that passes the entry test on its face. The team recommends nothing from scratch. Founders, with the chef for the kitchen's half. S10 P12, P13, finding 20.9.
*   **The pre-service window's length.** Canon gives the pre-service scene a length; the record gives the window none, and the check-in, the brief's slot, and a meal would all spend its minutes. With S4's close-window question. S10 finding 20.8.
*   **Who holds the room's "emotional standard" as a versioned document.** The record gives it to the Maitre d's seat and no versioned document holds it, which is the tight edge's likeliest drift into a lead's personal rule. Canon's owner, `86akh3t3y`. S10 finding 20.11.
*   **Whether a peer's recognition is a brand surface under canon's lexicon.** Canon's forbidden lexicon applies in all contexts; the recognition platform is written by the team in the moment and read aloud at the brief. S10 reads the language constant as applying and the lexicon as not, held. Canon's owner, with S11. S10 finding 20.10.
*   **Whether staying is a condition or an output.** Canon's playground is "open enough to stay"; the record places retention third, produced by bandwidth and joy. S10 reads it as an output. Founders, with `86akh3t00`. S10 finding 20.2.
*   **Where a non-negotiable breach by a person goes.** Blame absorption runs one way, and the one act canon treats as a person's has no path in the record. Founders, with S12, S14, S15. S10 finding 20.5.
*   **The founders' own bandwidth and path, as the founder side's missing conditions.** S16, `86akh2qzy`. S10 P37.
'''
assert out.count(oq_hdr) == 1
out = out.replace(oq_hdr, oq_hdr + s10oq)

# 4. amend questions S10 narrows
bullet("**Who holds a lead's check-in.**",
 "**Who holds a lead's check-in.** The record runs feedback both directions and names no one for the leads. Urgent since S9: the diagnosis of a lead's own node is half-blind until it closes, the lead's career conversation and the seat holder's line in the reset's first read wait on it, and row 118 fails. S10 adds the environment's reason: a concern about a lead is the one topic with no destination the lead does not hold, so safety to speak stays partial, and every range breach on a lead's environment entry has no destination. The team recommends closing it before the leads are in the building six weeks ahead of dinner's gate. Finding 19.7, P21, S9 P35, S10 P15, `86akhb2jg`.")
bullet("**Where the employee area and the lockers are.**",
 "**Where the employee area and the lockers are.** Promised by the record and absent from canon's spatial sequence; a first-shift walk depends on it. S10 reads it as the one employee condition for agency that is a slogan today, a place of their own, and row 127 fails until it exists as a zone. Finding 19.11, `86akhb2kb`, S10 section 3.")

# 5. reading note
key = "including canon reserving the word \"diagnostic\" against the reference's own name for itself."
assert out.count(key) == 1, key
out = out.replace(key, key + " Session 10 found twelve, four of which would have surfaced from a narrow read of canon's Playground page and the white paper's people sections and eight of which would not; one found canon stating the philosophy's obligation for three parties and specifying it for one, and one found the staff meal absent from the record and both canon artifacts.")

open('extraction/s10/tracker-after.md', 'w', encoding='utf-8').write(out)
print(len(src.encode()), '->', len(out.encode()))
