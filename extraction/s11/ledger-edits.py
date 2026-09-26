import sys
PAGEID = sys.argv[1] if len(sys.argv) > 1 else 'PAGEID'
src = open('extraction/s11/tracker-before.md', encoding='utf-8').read()
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

Run Session 12. New chat:

> Sŏn. Scaling People, session 12. ClickUp task `86ajgmjba`. Begin.

Session 11 is complete and its page is in the Operating System doc. Session 12 reads the ledger below before anything else. It is Chapter 5, hypothesis-based coaching, giving hard feedback, and a culture of informal feedback, owned by the People Systems Designer. Its inbound constraints from Sessions 10 and 11: the environment names no person in a room, nothing reaches the house that is not on a record first, upward feedback runs on the channel and the check-in's fourth question, and a concern about a lead still has no destination until `86akhb2jg` closes.

'''
out = out[:i] + first + out[j:]

# 1. last session + state
i = out.index('**Last session completed:** Session 10')
j = out.index('**Decisions binding a future session:**')
state = f'''**Last session completed:** Session 11, 2026-09-24. Chapter 4, team-building complexities, diversity and inclusion, team communication, the remainder of Stripe's leadership cadence on p.331, and the Chapter 4 exercises appendix and notes.

**State:** S11 wrote the team communication architecture and Sŏn's position on team composition. The architecture is one account: every speech act inside the house has one destination and it is a record (the book, the capture, the versioned entry, the person page, the platform, the channel, the partners' page, the team home); nothing reaches the house that is not on a record first; the brief and the slot read records aloud and originate nothing but the designations' lines. A change reaches the house by three channels proven on a change-reach record the stack writes (the affected check-in first, then the sheet, then every open period's brief in one sentence under the change line, then the team home), and has reached the house only when every open period's brief marks it and the team home shows it in every language on the house's versioned language list. Every house-written surface exists in every listed language under one version number before it publishes; translation is paid work by a holder of the language, approved twice; a person's own words are never translated for the house. Canon governs every house-written word inward in a register the team reads and canon's owner must rule; a person's own words carry the customer word and the language constant and nothing else of canon's. Her remote, distributed, and global material is refused (the house has no remote team in her sense; its non-co-presence is by hour); her inclusive meeting practices are absorbed by construction. The four bought tools named by the session task are placed: Google Workspace as the interim carrier of the written surfaces, never the hub; Nectar as the inferred carrier of peer recognition with points, rankings, per-person counts, surveys, and prompts disabled; Canny as the inferred carrier of the structured feedback channel, with the loop window regardless of votes and no person as a subject; Slang AI only where a call becomes a note on the book, the readiness block, or the capture, and held against canon where it speaks, the second bought tool the program holds against canon. The composition position is a conduct statement entailed by the record's own rules and recommended: four reads and nothing about who a person is, every stage in the chosen language, nothing about who a person is on any record, the house reads its own reach and widens it and moves no bar, and no composition target. Whether the house says anything about who it hopes its team will be, and whether it asks candidates for self-identification, are founder-gated with counsel, recommended against for now. Forty-six positions: thirty-eight recommended, six founder-gated, one chef-gated, one team-filled. Readiness rows 130 to 141, so the test stands at one hundred forty-one. Twenty-five instrument specifications, eleven used and fourteen refused, absorbed, or answered by reference. Twelve findings inside the record, two of which would surface from a narrow read of the white paper's people and brand sections and ten of which would not. Page `{PAGEID}`.

'''
out = out[:i] + state + out[j:]

# 2. decisions: S11 block at top
dec_hdr = '**Decisions binding a future session:**\n\n'
s11dec = '''*   **Nothing reaches the house that is not on a record first. Binds S12, S14, S15, S17.** Every speech act's destination is a record; the brief and the slot read records and originate nothing but the designations' lines; a change has reached the house only when the change-reach record shows every open period's brief and every language version; a person's own words are theirs and the house speaks none on their behalf. S11 names this as the one thing on its page a later session cannot revise at ordinary cost. S11 P10, P15, P17, P46.
*   **Three channels are proven by the change-reach record, and the order is produced by the schedule. Binds S15, S17.** The stack places the affected person's check-in before the version publishes and the entry waits for it; a version that cannot wait is a load on the clock and never a reason to skip the person. A departure's brief carries coverage once and then as the designations' line while the seat is open. S11 P15, P16, P25.
*   **The house's language list is a versioned entry, and every house-written surface exists in every listed language before it publishes. Binds every session that writes a page, and S17.** The list is field 14 across every open seat sheet plus every language a person on the roster chose at hiring; a language never leaves it while a person who chose it is in the house. The brief runs in the roster's languages by the block on the surface, the owner's languages, and an interpreter designation on the clock. Translation is paid work by a holder of the language, priced by S13. S11 P17 to P19.
*   **Canon's internal register is the team's reading, held for canon's owner. Binds S12, S13, S17.** House-written internal pages read as correspondence's cousin under the six tests; a person's own words on any surface (a recognition, a check-in line, a capture's free field, a channel item) carry the language constant and the customer word and nothing else of canon's lexicon, exclamation, or emoji rules. Canon's Korean terms stand untranslated in every language version. One ruling with the candidate-facing question (`86akh7r2t`). S11 P23, P24.
*   **The composition statement is conduct, and the reach read acts on reach only. Binds S13, S14, S17.** Four reads and nothing about who a person is; every stage in the chosen language; nothing about who a person is on any record beyond the seat's language field; the house widens its reach when it narrows and moves no bar; no target. The source-dominance and stage-rate read changes the sheet's sourcing mix and triggers the calibration read's existing acts, never a scorecard, a decision, a candidate, or a bar, and is never a performance input. S11 P35, P36, P39.
*   **Nectar, Canny, and Slang AI carry their functions only inside their refusals. Binds S12, S13, S14, S17.** Recognition is a peer's words about an act, read verbatim at the brief, never a rank, reward, point, per-person count, or review input, and is read only as a count per period. The channel is a named item with an owner and the loop window, never a survey, never a person as its subject, never anonymous by default. Neither carries the pulse or reads how the team is doing. Slang AI presents to no customer as a person until canon's owner rules on the synthesized voice. S11 P11, P13, P14, P30, P31.
*   **The transparency line's closed half. Binds S13, S17.** Everything that is not an operating figure, review content beyond the person and their lead, or the financial model is shared at the moment it is versioned, to every open period at once, on the team home, in every house language; the slot's and the gathering's "learned" items are inside it. The rest stays founder-gated (`86akh5uby`). S11 P32, P33.
*   **The unblocking practice runs on the joint half-page, never up a line. Binds S12, S15.** Either party writes; the range's owner decides inside a domain, as Class B across domains, as Class C between the leads, within the loop window; a unilateral case is refused until the absent party has been asked to write. A disagreement about a person is S12's; a lead who repeatedly hears one side is S15's. S11 P29.
*   **The readiness test stands at one hundred forty-one rows. Binds every session from here.** Rows 130 to 141 from S11; rows from S12 start at 142. Row 136's voice half holds on canon's synthesized-voice ruling, row 139's second half on the self-identification ruling, and row 141 reads as not yet until a live risk or a public statement exists. S11 section 18.
'''
assert out.count(dec_hdr) == 1
out = out.replace(dec_hdr, dec_hdr + s11dec)

# 3. open questions: S11 block at top
oq_hdr = '**Open questions a future session must close:**\n\n'
s11oq = '''*   **Whether a synthesized voice on the house's phone is inside canon's concealment prohibition.** Canon prohibits AI-generated imagery and Jaeyeonmi's concealment; it says nothing of a voice, and the record puts "the phone in software." Until canon's owner rules with the founders, the software says what it is in its first line and presents as no person. Urgent, before the first reservation is taken. S11 P14, finding 20.5.
*   **The internal register, ruled as one question with the candidate-facing register.** Canon names no employee-facing or candidate-facing surface; S11's reading is held. With the two canon versions' different Korean term lists (S11 finding 20.12). Canon's owner, `86akh7r2t`, `86akh3tjb`.
*   **The check-in through an interpreter, and the lead seat's languages.** Where a person and their lead share no language the check-in runs with an interpreter designation present who writes nothing; it changes what a check-in is, so the founders ratify it. With the first interview and the why block in a language no founder holds (`86akh9tar`). S11 P20.
*   **Whether the house states anything about who it hopes its team will be, and whether it asks candidates for self-identification.** Values statements, founder-gated with counsel; the team argues both to the ceiling and recommends against for now. S11 P37, P38, `86akh7r8z`, `86akh9tbd`.
*   **The dominance count as a reset parameter.** The number of consecutive reviews a source must dominate before the sheet's sourcing mix changes. S11 P36.
*   **The exit interview's owner and consent, and post-departure communication.** The record measures people growing beyond the building and runs an exit interview; no surface, owner, or consent exists for either. S11 finding 20.11, with S15.
*   **The house language list's pre-opening fill.** The seat sheets' field 14 and the founders' own languages; the founders are the first translators. S11 P21.
'''
assert out.count(oq_hdr) == 1
out = out.replace(oq_hdr, oq_hdr + s11oq)

# 4. amend questions S11 closes or narrows
bullet("**Whether a peer's recognition is a brand surface under canon's lexicon.**",
 "**Whether a peer's recognition is a brand surface under canon's lexicon.** Canon's forbidden lexicon applies in all contexts; the recognition platform is written by the team in the moment and read aloud at the brief. S10 reads the language constant as applying and the lexicon as not, held. S11 extends the same reading to every person's own words on a house surface (a check-in line, a capture's free field, a channel item) and files it with the internal register as one ruling for canon's owner (S11 P24). S10 finding 20.10.")
bullet("**\"Diagnostic\" reserved for the instrument.**",
 "**\"Diagnostic\" reserved for the instrument.** Canon says Nunchi is \"not diagnostic inquiry\" and the record calls its reference \"a diagnostic\"; the reconciliation should keep the word for the instrument and off the floor. S11 placed the rule: the word and the modes' names stay on the leads' review record, the house memo, the reset's record, and the team home's diagnostic page, and never in a spoken item at the brief or on a recognition, checked at row 137 (S11 P27). The word in canon remains the reconciliation's. S9 finding 19.11, extending `86akh3tjb`.")
bullet("**Bias measurement's data.**",
 "**Bias measurement's data.** Closed by S11 except self-identification: the source tag, the pool tag, the chosen language and format, the stage outcomes and on-sheet decline reasons, the interviewer, and the dates, per seat and stage, read weekly, monthly, at ninety days, and at the reset, with no target, figure, name, inference, or act on a candidate (S11 P39). Whether candidates are asked to self-identify is founder-gated with counsel (S11 P37). P47, with `86akh7r8z`, `86akh9tbd`.")
bullet("**Whether the house states a position on the composition of its team.**",
 "**Whether the house states a position on the composition of its team.** Narrowed by S11: the conduct statement is entailed by the record's rules and recommended (S11 P35), and the reach read acts on reach once it exists (P36). What remains is the values statement, whether the house says anything about who it hopes its team will be, founder-gated with counsel and recommended against for now (P38). `86akh7r8z`.")
bullet("**The transparency line: what is shared, when, and with whom.**",
 "**The transparency line: what is shared, when, and with whom.** Half closed by S11: everything that is not an operating figure, review content beyond the person and their lead, or the financial model is shared when versioned, to every open period at once, on the team home, in every house language (S11 P32). The rest, including the third seat's access, is founder-gated (S11 P33, `86akh5ucu`). `86akh5uby`.")

# 5. reading note
key = "one found the staff meal absent from the record and both canon artifacts."
assert out.count(key) == 1, key
out = out.replace(key, key + " Session 11 found twelve, two of which would have surfaced from a narrow read of the white paper's people and brand sections and ten of which would not; one set a second bought tool against canon (a synthesized voice on the phone), one found the two canon versions listing different Korean terms, and one found the phone ranked with the plate in the record and given no register in canon.")

open('extraction/s11/tracker-after.md', 'w', encoding='utf-8').write(out)
print(len(src.encode()), '->', len(out.encode()))
