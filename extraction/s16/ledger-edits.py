PAGEID=open('page-id.txt').read().strip()
src=open('tracker-before.md',encoding='utf-8').read()
out=src.replace('**Reconciled 2026-09-11 against** **`CLAUDE.md`****, which','**Reconciled 2026-09-11 against `CLAUDE.md`, which',1)
def amend(key, addition):
    global out
    assert out.count(key)==1, key
    i=out.index(key); end=out.index('\n',i); start=out.rindex('\n',0,i)+1
    assert out[start:end].startswith('*   '), out[start:start+60]
    out=out[:end]+' '+addition+out[end:]

i=out.index('## First action'); j=out.index('* * *',i)
out=out[:i]+'''## First action

Every extraction session is complete. Session 16 closed on 2026-09-25 and its page is in the Operating System doc. Session 17, assembly and the company wiki (`86ajgmk27`), is the only session left, and it is gated on the document methodology (`86ajgn2z5`). Do not start Session 17 until that task lands. When it has landed, run Session 17 in a new chat:

> Sŏn. Scaling People, session 17. ClickUp task `86ajgmk27`. Begin.

Session 17 reads the ledger below before anything else, then every carryover linked to its task. Its inbound work from Session 16: rows 201 to 213 into the assembled test; the founder load ledger, the seat's load line, and the read on the center as the wiki's center page beside the cadence page; twelve findings into the conflicts list; the vocabulary line ("the center," "a load," "the read on the center"); the working-with-me spine's additions carried into `86akh2r2x`; and the audit that no wiki page names the nature of a founder's external load, lists a founder as a holder in service outside the ledger, or records any founder's interiority as a position.

'''+out[j:]

i=out.index('**Last session completed:** Session 15'); j=out.index('**Decisions binding a future session:**')
out=out[:i]+f'''**Last session completed:** Session 16, 2026-09-25. The Conclusion, "You": her return to self-awareness and resilience, manage your time and energy, foster relationships, consider your career, and her closing on fundamentals. The workbook has no Conclusion exercise; the Chapter 1 exercises it points back to were Session 1's.

**State:** S16 refused "founder operating discipline" as the name, because the record places stability in the system and a founder protected by their own will is a founder the house depends on. It split the chapter into the organizational, which the team designed as recommended positions, and the personal, which it proposed and marked founder-gated. Brandon ruled two things for the session: a founder's commitments outside the house are a generic load, named on no surface; and the team proposes to the ceiling, with every proposal about his time, energy, relationships, and career founder-gated. The founder load ledger tables forty-two loads that Sessions 2 to 16 placed on the founders' seats, each with its seat, source, mark, hand-over date or closing condition, and the reset read that sees it. A by-default load past its date is node overload at the center. The center is read by three readers, all in writing and none above: each partner on the other's domain page at the monthly domain read, writing the seat's load line; the leads' read on the center on their own pages; and the reset. The read concludes a load and a carrier and never a person. The house protects dinner, the founders' bandwidth by the record's sizing and by dates, the hand-overs, the partners' relationship as mechanisms, and the leads' pairing. It does not protect and does not need a founder's hours, floor presence, memory, mid-service approval, impression, first-quarter eye, judgment of another founder, or discipline. The founders have no review and none is built under another name, and there is no absorber above the founders by design. A founder's departure is a Class A event under the operating agreement, and the house's part is continuity. The partners sit outside the pool on the team's reading, founder-gated with counsel. A founder on the floor is bound by the two-kinds and live-speech rules more tightly than a lead. The page closes Session 1's loop principle by principle and adds to the working-with-me spine without writing any founder's answers. Fifty-seven positions: forty-two recommended, twelve founder-gated, two chef-gated, one team-filled. Readiness rows 201 to 213, so the test stands at two hundred thirteen. Twenty-two instrument specifications, twelve used and ten refused. Twelve findings inside the record, numbered 15.1 to 15.12; three would surface from a narrow read of the white paper's founder pages and nine would not. Six counsel questions added, 26 to 31. Page `{PAGEID}`.

'''+out[j:]

hdr='**Decisions binding a future session:**\n\n'
dec='''*   **A founder's commitments outside the house are a generic load, named on no surface. Binds S17.** Brandon's ruling on 2026-09-25. Every page, work item, carryover, comment, ledger line, and wiki page refers to them only as "a founder's external load" or "commitments outside the house," and never names, describes, or hints at their nature, for any founder. Each founder states presence by service period and by week in prompt C of their working-with-me document; the house reads it as availability and never as a commitment, no mechanism depends on presence outside the statement, and the read on the center reads only the consequences on records. S16 P17, A33.
*   **The founder load ledger, with dated hand-overs. Binds S17.** Every load on a founder's seat is a row on the partners' page with its seat, source, mark, hand-over date or closing condition, and reset read; every by-default row carries a date or a held decision; a by-default load past its date with no node-overload line on the partners' page is itself a line for the reset. The ledger reads loads on seats and nothing about any founder. S16 P6, section 2.
*   **The read on the center: three readers in writing, none above. Binds S17.** Each partner writes the seat's load line on the other partner's domain page at the monthly domain read, from counts on records, in the evidence line's form with the founding seat as its object; the leads write their read on the center on their own pages, aggregated by mechanism at the partners' review; the reset reads the ledger and the year's load lines as its second read after the Maitre d's seat. No meeting is added. The read may never become a rating, a case file, a read of a founder's feelings or outside commitments, a room, a trigger for the operating agreement, or a lead's impression. S16 P9 to P11.
*   **A founder on the floor holds no range there. Binds S17.** A founder on the floor is bound by the two-kinds rule and the live-speech rule more tightly than a lead: no floor range unless named at the brief for a designation, a live call only inside a range they hold, no correction of anyone and no message about a person, any hypothesis carried to the person's check-in holder, and a call deferred to a founder is a node-overload entry on the founder's seat. S16 P16, answering S12 P15.
*   **The founders have no review, no absorber stands above them, and a founder's departure is continuity. Binds S17.** No founder review is built under any name; a founder's domain is read by the domain read and the load line, and conduct by the flag and the range breach as a question on the partners' page. A founder's failure is absorbed by Principle 4 run on the founders' own mechanisms at the partners' review, with an evidence line written by the other partner naming no person, and never by a lead, the team, the public, or a person above. A founder's departure is a Class A event under the operating agreement's process, and the house's part is the three-pass departure read with the founding seat as the node, a structure change entry, and the seat's rows moved to the other partner as a node-overload line with a closing condition. S16 P33, P36, P37. The flag path with a founder as subject is founder-gated (P35).
*   **The partners' place in the pool is the team's reading, held. Binds S17.** The partners are outside the pool and paid under the operating agreement, under branch A the chef partner with them; founder-gated with counsel (question 28). The partners' pay is never a position, and the parameters register gains one unset row, "the partners' place in the pool." S16 P39.
*   **The readiness test stands at two hundred thirteen rows. Binds S17.** Rows 201 to 213 from S16. Every founder row is checked by the other partner or the leads, never by the founder it reads. Row 209 holds on the toxicity and exploitation definitions and the hierarchy ruling; row 210 on the pool ruling with counsel; row 213 reads not yet until the first reset. S16 section 13.
*   **Vocabulary: "the center," "a load," and "the read on the center." Binds S17.** These are the house's words for the founders' seats as nodes, for what a seat carries, and for the mechanism that reads it. The refused carriers extend to a chief of staff, an assistant to a founder, a founders' office, and a second holder of a domain. S16 A32, A33.
'''
assert out.count(hdr)==1; out=out.replace(hdr,hdr+dec)

oq='**Open questions a future session must close:**\n\n'
q='''*   **Brandon's protection order and presence.** The page proposes a protection order for his seat and asks him to confirm, reorder, or rewrite it, and to state presence by period and by week in prompt C. Brandon, before the first cohort start date is committed. S16 P18, P19.
*   **Dominic's protection order, presence, and path.** On the same frame, written by Dominic and by no one else. S16 P20, P32.
*   **The chef partner's protection order and ledger column.** Under branch A, when seated. Chef-gated. S16 P8, P21.
*   **How each partner's working style changes the partners' review's conduct.** Set at the first gate review from the working-with-me documents, without changing the agenda. Founders. S16 P24, `86akh6813`.
*   **The founders' review form, and the flag path with a founder as subject.** Founders, with counsel and canon's owner for the flag path. S16 P34, P35, counsel question 27.
*   **The operating agreement's departure, incapacity, and removal provisions.** The founders read and report them; the program never reads or writes the agreement. S16 P38, `86akh3t62`, counsel question 29.
*   **Where each founder's path leads beyond the hand-overs.** Each founder's own writing. S16 P32.
*   **The seat for the acoustic consultation, and canon's specialist seats.** The record names an acoustic consultation with an unnamed founder and specialist seats with no line. Brandon with Dominic. S16 findings 15.10, 15.11.
*   **Whether the assembled test carries a row that reads the company as well as the building.** "The operating system is running" reads the building, and a founder at zero bandwidth can stop a reserved class invisibly. S17. S16 finding 15.1, carryover B2.
*   **Counsel questions 26 to 31.** Added to the register by S16 in its urgency order. Founders, engaging counsel. S16 section 16.
'''
assert out.count(oq)==1; out=out.replace(oq,oq+q)

amend("**The interim holder of an open lead seat's domain.**","Read by S16 as a row on the founder load ledger with its closing condition (S16 section 2).")
amend("**The partners' place in the pool, and a departure's final pay.**","S16 narrows the pool half to the team's reading (outside the pool, paid under the operating agreement) with an unset register row, founder-gated with counsel (S16 P39).")
amend("**The founders' own bandwidth and path, as the founder side's missing conditions.**","S16 closes the bandwidth half as a mechanism, the read on the center (P9 to P11); the path is defined structurally, and where each founder's path leads is founder-gated (P32).")
amend("**The founders' own bandwidth read, and who sets a founder's learning tempo.**","Closed by S16 as a mechanism: three readers in writing and none above, and the learning tempo read at the reset (S16 P9 to P12); each founder's prompt H signals remain founder-gated (P13).")

k="and blame absorption names no absorber for a lead's failure."
assert out.count(k)==1
out=out.replace(k,k+" Session 16 found twelve, three of which would have surfaced from a narrow read of the white paper's founder pages and nine of which would not. Among them: the house runs without its founders but the company cannot, since every reserved class needs them; the record's web draws no founder node; upward feedback stops at the leads; and canon bars the founder hero narrative the brand engine runs on.",1)

i=out.index('| 16 | `86ajgmjz6` |'); e=out.index('\n',i)
row=out[i:e]
assert 'Complete' not in row
open('tracker-after.md','w',encoding='utf-8').write(out)
print(len(src.encode()),len(out.encode()))
