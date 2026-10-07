# Cross-chunk changes

Produced from the task index, the phase-inversion list, the leftovers list, the multi-row list, and the handoff notes. Nothing here decides anything for Brandon; it restructures the work list so each question is asked once, in one chunk, in the phase the phase rule puts it in.

Numbers refer to the task numbers as they stand today. The apply step renumbers each chunk at the end and rewrites every reference.

## Verbs used in the change list

- `REMOVE n. Keeper: m.` Delete task n. Every task that lists n in "Depends on" lists m instead (or drops n where m is already listed). n's "Replaces old items" move to m. n's row in `mapping.md` points at m.
- `NARROW n.` Task n stays, with the new title, done-when, and dependencies given. Nothing else about it changes.
- `APPEND n: ...` Add the clause to the end of n's done-when. Nothing else changes.
- `PHASE n: A -> B.` Change n's phase.
- `DEPS n: drop ... / add ... / replace X with Y.` Edit n's "Depends on" only. A dropped dependency that is still worth reading is listed as "reads" at the end of the done-when, in the words given.
- `SPLIT n into ...` n keeps its number with the first half; the second half is a new task placed directly after n.
- `ADD <chunk>: ...` A new task in tasks.md format, placed where stated.
- `MERGE a, b, c into a.` a stays with the new title and done-when; b and c are deleted; dependencies, dependents, and old items are the union.
- `KIT n: ...` Change n's "Repeatable" line (who produces their own, and which kit).
- `MAPPING <chunk>: add row / change row / remove row.` Edit that chunk's `mapping.md`.

## 1. Summary

| Change type | Count |
|---|---|
| Remove (duplicate) | 12 |
| Narrow (duplicate kept for its own angle, or a task retitled) | 12 |
| Append (keeper's done-when takes the loser's angle) | 9 |
| Merge (deliverables always built together) | 8 merges removing 11 tasks |
| Add (gaps) | 4 |
| Split (one task carrying two phases) | 2 |
| Phase move | 47 |
| Dependency edits | 126 bullets (covers all 319 inversions) |
| Kit pointer changes | 2 |
| Mapping rows added or changed | 37 |

Task count: **781 before, 764 after** (781 minus 12 removed, minus 11 merged away, plus 4 added, plus 2 from splits).

Leftover old items: 29 placed. Served by an existing task 22; new task 1; dropped 6 (brand-dependent 3, machinery 3).

Phase inversions: 319 covered. By pattern: the largest group is loose dependencies dropped from "Read what the upstream chunks settle" tasks and from decisions that name a later mechanism by kind; the next largest is cleared by 47 phase moves (a task moved to the phase the phase rule puts it in); the rest by removals and merges. Some inversions are cleared by more than one change; every line in `phase-inversions.md` is covered by at least one bullet below.

## 2. Changes by chunk

### 0 Management basics checklist

- `ADD 0: new task, placed after 0.3.`

  ```
  ### 0.4 Open the counsel questions register
  - Type: Deliverable
  - Phase: Before the first hire
  - Book: pp. 23 to 24 (the legal responsibilities of an employer and a manager are the floor beneath every people system; know them before the first hire)
  - Default assumption: None; the white paper does not describe how the founders work with counsel
  - Depends on: 0.1
  - Done when: one register exists, outside this repo, holding every open question for counsel from any chunk, each with the chunk and task that asked it, the step waiting on it, its urgency tier (before the first paid shift; before the first flag read; before the first slow-season cut; before the wider opening gate), its date, and its status; only counsel writes an answer into it and it never states a legal conclusion in the house's voice; this repo holds the question list only. Every later task that asks counsel something (3.1.37, 3.4.4, 4.3.14, 4.4.6, 4.7.5, 5.2.4, 5.5.29, 5.8.2, 5.10.2, 6.3.7) adds its rows here rather than opening a register of its own
  - Replaces old items: 17tn048qg2b (the register half, received from 5.5), 17tn048qg2j (the counsel register as a standing page in counsel's words only)
  ```
- `MAPPING 0: add row | 17tn048qg2j | Rows 183 to 200, the departure page, fifteen instrument extensions, the counsel questions register as a standing wiki page | Served | 5.10.20 (the departure page) and 0.4 (the counsel register) | The page is 5.10.20's; the counsel register in counsel's words only is 0.4's; the row counts, instrument extensions, and routed findings are assembly machinery and are not carried |`
- `MAPPING 0: add row | 86ajgmxnp | The workbook is free and official: both PDFs load every session | Dropped (machinery) | none | A working rule of the extraction program. CLAUDE.md's sources table now holds the workbook and how it is read |`
- `MAPPING 0: add row | 86ajgn3ep | Specifications, not instruments: no SOPs until the document methodology exists | Dropped (machinery) | none | The extraction program's gate on producing instruments. The reconsideration builds deliverables and kits directly; 1.1.11 records that the document-methodology gate is dropped |`

### 1.1 Build self-awareness to build mutual awareness

- `PHASE 1.1.13: "Before the first hire (moves to hiring and training if 1.1.9 chooses the onboarding timing)" -> Before the first hire. Reason: ClickUp needs one tag; the conditional stays in the done-when as "if 1.1.9 chooses the onboarding timing, retag to hiring and training".`

### 2.1 Founding documents

- `MAPPING 2.1: add row | 86akh2qht | Founder decision: Set the founder decision-rights rule | Served | 2.1.13 | How the partners make joint decisions and break deadlocks is 2.1.13; the rule beneath the partner level and the cross-domain case are 2.2.2 and 2.2.3 |`
- `MAPPING 2.1: add row | 86akh2qrp | Founder decision: Reconcile the two accounts of the chef seat | Served | 2.1.10 | Who holds culinary direction overall and the chef seat's standing is 2.1.10. The second account rests on the brand canon, which is not a source here; only the white paper's account is carried |`
- `MAPPING 2.1: add row | 86akh2r4k | Structure: Reconcile the three profiles to the current source allowlist | Dropped (machinery) | none | Profiles are reasoning lenses, never authorities (CLAUDE.md); the overrides the item asked for are now CLAUDE.md's rules, and the marks it names are retired |`
- `MAPPING 2.1: add row | 86akh3rx4 | Founder decision: Rule on the six-tier authority hierarchy and the placement of the company non-negotiables | Dropped (brand-dependent) | none | Both hierarchies are brand canon, excluded. The one non-brand question inside it, what standing the principles have among the founding documents and who may change them, is 2.1.18's |`
- `MAPPING 2.1: add row | 86akh3t00 | Founder decision: Adopt or decline "the order is the decision" as an operating tiebreaker | Served | 2.1.4 | The same decision, framed from the white paper (WP p. 17) rather than the deck |`
- `MAPPING 2.1: add row | 86akh3t27 | Founder decision: Settle ownership of the OS surface between the two seated founders | Served | 2.1.7 | The same decision; the two options (specification and build split, or one seat outright) are in 2.1's considerations |`
- `MAPPING 2.1: add row | 86akh3tg0 | Founder decision: Select and word the long-term commitments and the principles | Served | 2.1.5 (with 2.1.3) | The sorting of candidates into long-term goals, principles, and operating rules is 2.1.3 and 2.1.5; the canon voice tests it named are brand material and are not carried |`
- `MAPPING 2.1: add row | 86akh3tjb | Document: Reconcile the two canon artifacts into one version of record | Dropped (brand-dependent) | none | Both artifacts are excluded brand guidelines |`
- `MAPPING 2.1: add row | 86akh3tp5 | Document: Relocate or re-point the Surface-and-Zone Baseline Document and the canon's record-of-truth reference | Dropped (brand-dependent) | none | The baseline document and the canon footer are brand material. Its one operating point, that no founding document names a tool as the data hub before the hub is confirmed, is 2.2.24's |`

### 2.2 The operating system

- `PHASE 2.2.7: Hiring and training -> Before the first hire. Reason: who holds emergency authority during a service and who may close a period or the building is in each lead's seat description and decision-rights entry, which a lead candidate reads at the first interview. Clears the inversions on 3.4.3, 5.10.7, 5.9.7, 6.1.11.`
- `PHASE 2.2.14: Hiring and training -> Before the first hire. Reason: the ninety-day plan (3.3.10) and the lead onboarding plan (3.3.45), both before the first hire, are built on how development goals are set. Clears 3.3.10, 5.4.1, 5.7.1, 5.7.3, 6.2.5.`
- `PHASE 2.2.24: Before opening -> Before the first hire. Reason: the applicant system (3.1.35, before the first hire) cannot be configured before the data hub of record is confirmed. Clears 3.1.35, 3.3.32, 4.1.26.`
- `PHASE 2.2.29: Before opening -> Before the first hire. Reason: 2.3 decides the individual rhythms (2.3.4 to 2.3.13) before the first hire, and the set they belong to cannot be decided later than its members. Clears 4.2.1, 4.5.1, 4.5.5, 4.5.15.`
- `DEPS 2.2.29: drop 2.2.22 (loose: the set of mechanisms does not wait on every metric having an owner; reads "2.2.22 confirms each mechanism's metric owners once assigned").`
- `PHASE 2.2.31: Before opening -> Hiring and training. Reason: naming per-service ownership in the brief needs the designations (4.1.20) and the shift brief's fixed content (2.3.7); both exist by hiring and training, and 4.4.7 and 4.5.13 (hiring and training) depend on it. Clears 4.4.7, 4.5.13.`
- `NARROW 2.2.32. New title: Specify the metrics and alerts the shift brief and shift close carry. New done-when: the operating-system fields of both structures exist as a list (which metrics the brief opens on, which alerts the close records, and what each refuses to carry); the kitchen's fields are held for the chef partner; the realist's test has been run against a full night and any field that cannot be read at tempo has been cut or moved; 2.3.20 builds the running checklists around these fields. Depends on: 2.2.31, 2.2.25. Reason: the brief's and close's fixed content and order are 2.3.7 and 2.3.8; the checklists are 2.3.20; 2.2 keeps only the operating-system contents.`
- `REMOVE 2.2.33. Keeper: 2.3.19. Repoint dependents (3.3.28, 4.7.16, 4.8.6, 4.8.7, 5.6.17, 5.8.27) to 2.3.19. Move old item 86akh5ume to 2.3.19. Reason: one leads' review agenda; the book's operating cadence section (2.3) holds the meetings. The weekly note travels to 2.3.19 (see 2.3).`
- `REMOVE 2.2.34. Keeper: 2.3.23. Repoint dependents (2.2.40, 4.5.24, 4.7.9, 4.7.13) to 2.3.23. Move old item 86akh5ukw to 2.3.23. Reason: the house review's shape is 2.3.22 and its template 2.3.23; the gate review is 2.3.26.`
- `PHASE 2.2.37: Before opening -> Before the first hire. Reason: that a service period opens on a test, not a date, shapes the hiring calendar (3.2.34) and the start-date promise a candidate is given. Clears 3.2.34's inversion on 2.2.37.`
- `ADD 2.2: new task, placed after 2.2.38.`

  ```
  ### 2.2.38a Decide whether the readiness test reads the company's shape as well as the building
  - Type: Decision
  - Phase: Before opening
  - Book: pp. 104 to 106 (the operating system must show when the company, not only the day's work, is stuck)
  - Default assumption: (WP p. 06) "a company built to run without them" is stated of the operating system; the white paper says nothing about the reserved-class decisions that only the partners can take
  - Depends on: 2.2.37, 2.2.38, 2.3.4, 2.1.13
  - Done when: the founders have chosen one of: a row in the readiness test that reads whether any reserved-class decision (a service period built or removed, a principle changed, a version, a principal admitted or removed, a pay parameter set) has stood open past a stated count of partners' reviews, read from the partners' page with no person named and the count as a reset parameter; or a statement beside the test that it reads the building only and the partners' page reads the company; agreed by both seated founders
  - Replaces old items: 17tn048qr4n
  ```
- `REMOVE 2.2.41. Keeper: 2.3.24. Repoint dependents (4.7.18) to 2.3.24. Reason: one review kit for the house review memo and the lead's weekly note; 2.3.24 is before opening and does not wait for the first house review to run (the first build makes the kit; the first review revises it).`
- `MAPPING 2.2: add row | 86akh5uym | The team home is the wiki's staff-facing face, and the vocabulary line is an audit rule | Served | 2.2.15 | The team home is 2.2.15. The vocabulary line ("operating system" for the human system, "the stack" or "the OS surface" for the software) is decided in 1.4.1 and collected on the fixed-terms list in 4.5.19; the hub confirmation is 2.2.24 |`
- `MAPPING 2.2: add row | 17tn048qr4n | "The operating system is running" reads the building and not the company | New task | 2.2.38a | The decision it asks for, with both options and no recommendation |`

### 2.3 Operating cadence

- `DEPS 2.3.12: drop 2.1.15 (loose: the closed day and the reviews' placement are decided from the calendar's shape; reads "dinner's charter (2.1.15) may revise the seasonal shape once written").`
- `NARROW 2.3.14. New title: Place each lead's monthly conversation on the calendar. New type: Action. New done-when: each lead's monthly conversation (held by the partner 2.2.5 named, in the check-in's form, on the lead's own page) has a closed hour on the calendar at the interval 2.3.10 set; the hour is outside every service and every other standing rhythm. Depends on: 2.2.5, 2.3.10, 2.3.12. Move old item 86akh6742 (the pairing half) to 2.2.5. Reason: who holds each lead's check-in is 2.2.5; 2.3 keeps the placement.`
- `DEPS: every task that lists 2.3.14 and does not already list 2.2.5 adds 2.2.5 (from the index: 2.3.17, 3.3.22, 3.3.23, 3.3.45, 4.4.3, 4.4.11, 4.4.14, 4.4.21, 5.6.18, 5.9.3, 5.9.5, 6.1.10, 6.2.1, 6.2.9). Reason: they wanted the holder, which now lives in 2.2.5 alone.`
- `APPEND 2.2.5: the conversation is held in the check-in's form, on the lead's own page, at a closed hour (2.3.14 places it); the rule for who reads the other lead when a partner is the subject is 5.9.10's.`
- `NARROW 2.3.19. New title: Write the leads' review agenda, record form, and the lead's weekly note. New done-when: the agenda exists in fixed order with the source of each read and what it refuses (to open on a lagging figure, to run without a written record, to become the integration layer the stack should be); the record form exists (notes, action items with owners that are a lead, a domain, or a unit); the lead's weekly note has a structure and a page limit and is filed before every review; the one thing is written to the team's internal home before the first brief of the week; lagging indicators are stated as not on it; the review has run at least four consecutive weeks on the form before dinner's gate. Depends on: 2.3.13, 2.2.25, 2.2.29. Repeatable: yes. Each lead files the note before every leads' review; the chef partner files the kitchen's. Kit: 2.3.24. Old items: 86akh675n (the agenda half), 86akh6785 (the agenda third), 86akh5ume (from 2.2.33).`
- `DEPS 2.3.20: add 2.2.32 (the fields), 4.5.13 (the team-content slot).`
- `APPEND 2.3.23: the sections carry the statements that must be true after a house review, in Sŏn's terms, and what the review refuses (to review a period without a charter; to score a goal met at a bandwidth cost as a win; to exceed what the leads can prepare between services); the first instance's length is left to calibrate after it runs (from 2.2.34).`
- `NARROW 2.3.24. New title: Build the review kit: the lead's weekly note and the house review memo. New done-when: kits/review/ holds an intake (the questions a lead answers before writing the weekly note, and before writing a candid quarterly memo readable in the reading block), a guide (how to write skewed to lowlights without writing about a person; how the partners integrate the memos and chair the review, including the reading block, the top-of-mind round, and the reflection; how to keep lagging figures in the appendix), and templates for the note and the memo; a memo as the example only if its author consents; revised after the first house review runs. Depends on: 2.3.19, 2.3.23. Reason: absorbs 2.2.41.`
- `MAPPING 2.3: add row | 86akh681a | The mechanism map is the wiki's cadence page, and the marks travel with it | Served | 2.3.33 | The one-page cadence for the team's internal home is the mechanism map; the marks are retired and the cultural labor score's line is 2.2.20's |`

### 3.1 Recruiting

- `APPEND 3.1.3: whether a founder's "no" must name a read; the end condition for entry-level seats stated as one of a date, a headcount, a number of consecutive clean calibration reads, or never (from 3.2.6).`
- `NARROW 3.1.8. New title: Decide how seats are classed for hiring. New done-when: every seat in the inventory carries a hiring class (high-volume, physical-skill, leadership or salaried, with the chef partner handled by 3.1.21), a seat may carry more than one, and the class list carries the rule that no class decides on a single scorecard; 3.2.4 lists each class's stages and who runs each. Depends on: 4.1.9, 4.1.15. Reason: the stages per class were also 3.2.4's.`
- `REMOVE 3.1.15. Keeper: 3.2.13. Repoint dependents (3.1.33) to 3.2.13. Move old item 86akh9tar (the training half) to 3.2.13. Reason: interviewer training belongs with interviewing (3.2), where the modules (3.2.24) and the founders' completion (3.2.25) already sit.`
- `REMOVE 3.1.16. Keeper: 3.2.15. Repoint dependents (3.1.28, 6.2.11) to 3.2.15; drop 3.1.16 from 4.7.1, 4.8.1, 4.8.2 (they already list 3.2.15). Move old item 86akh9tar (the language half) to 3.2.15.`
- `DEPS 3.1.30: replace 5.5 with 3.2.18. Reason: the interim compensation line on the candidate sheet follows the order decision, not the finished architecture; 5.5.20 later tells 3.1.31 the final wording.`
- `DEPS 3.1.34: drop 2.2.8 (loose: the entries follow 2.2.4's form; the kit is built from them).`
- `PHASE 3.1.36: Hiring and training -> Before the first hire. Reason: the paid practical's pay and employment form is promised on every posting (3.1.28) and is legally sensitive; the phase rule puts a policy promised to candidates before the first hire even when the practice is later. Clears 5.5.6 and 5.5.15.`
- `PHASE 3.1.37: Hiring and training -> Before the first hire. Reason: as 3.1.36; it is the counsel half. Clears 5.5.6 and 5.5.15.`
- `DEPS 3.1.37: add 0.4.`
- `PHASE 3.1.40: Before opening -> Before the first hire. Reason: the pool-first check and the note an outside leadership hire requires are what the candidate sheet says about how far the path goes (5.6.3, before the first hire); the phase rule applies. Clears 4.3.8, 4.4.1, 5.10.14, 5.4.15, 5.6.1, 5.6.3, 5.6.8, 6.3.9.`
- `REMOVE 3.1.41. Keeper: 3.2.42. Move old item 86akh9tba to 3.2.42. Reason: the same question (what replaces the founders' read on entry-level packets once it retires).`
- `NARROW 3.1.42. New title: Revise the success profile after the first cohort. New done-when: at the first mechanism reset after dinner's first quarter, the profile from 3.1.6 is reread against the pipeline report (3.1.39) and the hiring-quality read (3.4.17), each read that predicted nothing is named, and a version two is written or the profile is confirmed; the anchors are 3.2.48's. Depends on: 3.1.6, 3.1.39, 3.4.18, 2.3.34. Old items: none. Reason: 86akh9tay (the anchor set's first revision at the mechanism reset) gets one home, 3.2.48.`
- `MAPPING 3.1: change row for 86akh9tay: fate "Routes to 3.2", goes to 3.2.48, reason "The anchor set's first revision is 3.2.48's; 3.1.42 keeps the success profile's revision only".`
- `MAPPING 3.1: add row | 86akh7rm1 | One account of each seat, read by three systems, and the readiness test now stands at fifty-nine rows | Served | 3.1.31 | The seat's account that opens it (the candidate sheet) is the one 3.3.36 (the onboarding plan), 4.1.15 (the inventory), and 2.2.15 (the team home) reference rather than copy; the readiness rows and the marks are machinery and are not carried |`

### 3.2 Hiring

- `NARROW 3.2.2. New title: Confirm the reads list as the interview's rubric, and mark which are scored on the candidate and which recorded about the building. New type: Action. New done-when: the list from 3.1.5 is confirmed or amended as the reads every stage draws from, each read carries its one-line definition, a note says which are scored on the candidate and which (if any) are recorded about the building, and the list is the one the scorecard (3.2.9), the kit (3.2.27), and the review process in 5.4 all use. Depends on: 3.1.5, 3.2.1. Old items unchanged. Reason: what every hire is read on is 3.1.5's decision; 3.2 confirms and allocates it.`
- `DEPS 3.2.4: replace "3.1 (whether the phone screen exists and what it may read)" with 3.1.8, 3.1.9.`
- `REMOVE 3.2.6. Keeper: 3.1.3. Repoint dependents (3.2.7, 3.2.42, 6.1.5) to 3.1.3. Reason: the same decision (the founders' stage in every hire before opening and when it ends); the earlier chunk keeps it.`
- `APPEND 3.2.15: the languages offered in hiring match the languages onboarding can deliver in (3.3), and the posting says which are offered (from 3.1.16).`
- `DEPS 3.2.18: replace 5.5 with 5.5.2, 5.5.3. Reason: the order decision needs the philosophy and the two layers, both before the first hire, not the finished architecture.`
- `MERGE 3.2.27, 3.2.30 into 3.2.27. New title: Write the interview kit and anchors, with the candidate stage notes and interviewer prep notes: the lead seats first, then each seat class before its first posting. New done-when: for each stage of each seat class there is a fixed question order with at least one situational, one behavioral, and (where the read allows) one competency question per read, scripted probes, an anchor per question at three evidence levels written for capacity that could show up in any kind of work, a scan confirming no anchor uses presence or fit language, a phone-screen script where 3.1.9 keeps the screen, the lead-seat block (holding a domain with no one above, reading a problem as a systems question, what they would refuse to do), and a version number, with the anchors marked provisional until 3.2.48; and for each stage a candidate note (what the stage is for, its length, who is present by seat, format and language confirmed, what they will be asked to do, what it does and does not read, what to wear, when and how they will hear, that they may ask questions) and an interviewer prep note (the seat description, the stage's kit and anchors, the reads it carries, the candidate's chosen language and format, what the candidate was already told, the interviewer's own training currency, and whether it includes any prior interviewer's read, per 3.2.9). Depends on: 3.2.2, 3.2.3, 3.2.4, 3.2.9, 3.2.12, 3.1.31. Repeatable: yes. Each domain lead writes and revises the kit and notes for their own seats; the chef partner writes the kitchen's. Kit: 3.2.31. Old items: 86akh9tcx, 86akh9te7. Repoint dependents of 3.2.30 (3.2.31) to 3.2.27.`
- `DEPS 3.2.34: drop 2.2.38, 2.3.31 (loose: the calendar's cohort gates are revised when the cadence calendar and the "dinner is steady" definition exist; reads "2.3.31 and 2.2.38 once they exist"). 2.2.37 stays (now before the first hire).`
- `DEPS 3.2.35: drop 2.2.8 (loose, as 3.1.34).`
- `DEPS 3.2.36: add 3.1.36, 3.1.37 (the practical's pay and employment form).`
- `PHASE 3.2.42: Before opening -> Hiring and training. Reason: the outside-domain check sits on entry-level packets, which are hired in hiring and training; 4.7.7 (hiring and training) depends on it. Clears 4.7.7 and 4.7.1.`
- `APPEND 3.2.42: the decision-rights entry in 3.1.34 is updated; the answer is reread at the first mechanism reset with 3.1.39's data in hand (from 3.1.41).`
- `DEPS 3.2.44: add 3.1.40.`
- `MAPPING 3.2: add row | 86akh9tay | The anchor set's first revision at the mechanism reset | Received from 3.1 | 3.2.48 | One home; 3.1.42 keeps the success profile's revision |`
- `MAPPING 3.2: add row | 86akh9tar | (from 3.1.15 and 3.1.16) | Received from 3.1 | 3.2.13 (the training half), 3.2.15 (the language half) | 3.1.15 and 3.1.16 removed as duplicates |`
- `MAPPING 3.2: add row | 86akh9tba | (from 3.1.41) | Received from 3.1 | 3.2.42 | 3.1.41 removed as a duplicate |`

### 3.3 Onboarding

- `DEPS 3.3.1: drop 3.1.38 (loose: the read takes what exists).`
- `DEPS 3.3.4: drop 2.2.27 (loose: the curriculum's order does not wait for the goal pages; reads "the why session (3.3.35) reads the first goal pages once written").`
- `DEPS 3.3.9: drop 3.2.37 (loose; reads "shares its separation of duties with 3.2.37").`
- `DEPS 3.3.12: drop 3.4.5 (it was a forward note, not a prerequisite; 3.4.5 depends on 3.3.12).`
- `PHASE 3.3.29: After opening -> Before opening. Reason: the shorter plan for a person changing domain is a policy 4.3.7, 5.7.6, and 5.8.14 read; only its templates (3.3.52) and the internal mobility survey (3.3.31) wait for opening. Clears 4.3.7, 5.7.6, 5.8.14.`
- `DEPS 3.3.39: add 5.10.17 (the arrival note carries what happens when a person stops showing up).`
- `DEPS 3.3.45: drop 2.3.17 (loose: the plan is written before the first check-in; reads "revised after the first check-ins (2.3.17)").`

### 3.4 Hiring mistakes

- `DEPS 3.4.4: add 0.4.`
- `DEPS 3.4.6: drop 3.3.28 (loose: the retrospective reads the training-infrastructure line once it exists).`
- `NARROW 3.4.8. New title: Decide whether candidates are surveyed on the hiring process, declined and hired, from which stage, and what is asked. New done-when: the answer is written (a survey from the first interview onward, from the practical onward, of hired people only at the thirty-day check-in, or none), for whom (declined candidates, hired people, both), the questions are fixed (a recommend question and two or three open ones at most), the sender and timing are named, the reader and rhythm are named, and it is stated that a response never changes that candidate's pool standing or a hired person's record. Depends on: 3.1.11, 3.1.12, 3.2.22. Reason: this is the optional candidate pulse (old S5 section 6.4); no separate task is needed.`
- `NARROW 3.4.13. New title: Write the candidate survey and add it to the applicant system. New done-when: the survey exists in the languages the applicant system offers, sends automatically at the stage 3.4.8 fixed (after the decline message, and to hired people if 3.4.8 included them), stores responses apart from the candidate's file and the person page, and its read is on a named rhythm. Depends on: 3.4.8, 3.1.35, 3.2.22.`
- `MAPPING 3.4: add row | 86akh9tau | The hiring system has no leading indicators | Served | 3.4.17 | The hiring-quality read is the leading indicator the item found missing; the pipeline report (3.1.39) and the reach read (4.7.6) feed it |`

### 4.1 Team structures

- `MERGE 4.1.18, 4.1.19 into 4.1.18. New title: Write the structure narrative and the structural content the web rendering carries. New done-when: one page, in plain words for a line cook or a server, says what the structure is, why there are two leads and no general manager, what a designation is and is not, how someone advances, what changes and how they will hear about it, and that the structure will change as periods open; it names no one; both founders have read it and the objections it surfaced are listed beneath it; beside it, a one-page content list drawn from the inventory that a designer could render without inventing structure, and the candidate sheet has an interim rendering (a list will do) until the designed one exists. Depends on: 4.1.2 to 4.1.12, 4.1.15. Old items: 86akh7ru5, 86akhcz5j (the structural content; the visual design stays outside). Repoint dependents of 4.1.19 (3.1.29) to 4.1.18.`
- `DEPS 4.1.12: drop 2.2.11 (loose: how a change is made is decided here; how it reaches people reads "through the channels 2.2.11 names once decided").`
- `PHASE 4.1.20: Hiring and training -> Before the first hire. Reason: whether a designation pays (5.5.14) is on the compensation mechanics page a candidate reads; the designation must be defined first. Clears 4.5.1, 5.5.1, 5.5.14, 5.7.1, 5.9.7.`
- `PHASE 4.1.29: Before opening -> Before the first hire. Reason: whether the overnight crew is in the pool (5.5.6, before the first hire) needs their place in the structure. Clears 5.5.1, 5.5.6.`
- `PHASE 4.1.30: Before opening -> Hiring and training. Reason: the forms of one-off work (4.4.7, 4.4.10) are decided when the leads arrive; nothing about temporary structures waits for opening. Clears 4.4.1, 4.4.7, 4.4.10, 5.6.8.`
- `PHASE 4.1.35: Before opening -> Hiring and training. Reason: the cross-domain hold's half-page is the instrument the unblocking path (4.5.10) and the unblocking note (4.5.18) point at, both hiring and training. Clears 4.5.10, 4.5.18.`
- `PHASE 4.1.37: After opening -> Before opening. Reason: the seat load reading is built before opening and run at the reset; 4.3.19 (before opening) builds on it. Clears 4.3.19, 4.2.1, 4.2.6, 4.2.12.`
- `PHASE 4.1.38: After opening -> Before opening. Reason: the floor and kitchen interface exists from dinner's first service; the read line is built for it and a later period's leads add theirs. Clears 4.6.10, 4.6.19.`
- `DEPS 4.1.38: drop "the second period's charter" (loose; reads "each later period's leads add their interface line before the period opens").`
- `MAPPING 4.1: add row | 86akhcz2m | Document: Write the chef onboarding packet's structure section | Served | 4.1.17 | The chef partner's open list is the fourteen items, each with its spine entry, the record's sentence, what the floor has written on its side of the seam, and the gate it must close before; filled by the chef partner once seated (4.1.25) |`
- `MAPPING 4.1: add row | 86akhcz7t | The chef packet's fourteen structure items, rows 93 to 106, the team vocabulary rule, and the line count gap | Served | 4.1.17 | The fourteen items and the leadership-line count as a stated gap are 4.1.17's; the team vocabulary rule ("team" is the house; "level" and "below" read as kind and edge) joins the fixed-terms list in 4.5.19; the readiness rows are machinery |`

### 4.2 Diagnosing team state

- `DEPS 4.2.1: drop 4.1.33, 4.1.36, 4.1.37, 2.3.22, 2.3.30 (loose: the read takes what exists).`
- `DEPS 4.2.4: drop 2.3.25 (loose; reads "if 2.3.25 holds a quarterly gathering, whether results are discussed there").`
- `DEPS 4.2.6: drop 2.2.21, 2.2.25, 4.1.37 (loose: the evidence is named by kind; reads "2.2.25's register confirms each named source once written").`
- `PHASE 4.2.9: Hiring and training -> Before opening. Reason: it places the diagnostic on rhythms (the house review 2.3.22, the gate 2.3.26, the reset 2.3.30) that are decided before opening.`
- `PHASE 4.2.10: Hiring and training -> Before opening. Reason: follows 4.2.9; the thresholds are reset parameters.`
- `PHASE 4.2.11: Hiring and training -> Before opening. Reason: follows 4.2.10; a diagnosis becomes a change through the structure change entry (4.1.34, before opening).`
- `PHASE 4.2.12: Hiring and training -> Before the first hire. Reason: whether the founders' own seats are read by the same diagnostic is what 5.9, 5.10.8, 6.1, 6.2, and 6.3 (all before the first hire) build on; it is a founders' decision, not a team one. Clears 5.9.1, 5.9.3, 5.10.8, 6.1.1, 6.1.4, 6.2.5, 6.3.1, 6.3.5.`
- `DEPS 4.2.12: drop 4.1.37, 4.2.6 (loose: the sources are named by kind; reads "4.2.6 confirms the sources once the evidence list exists").`
- `PHASE 4.2.13: Before opening -> After opening. Reason: a lead taking over a running domain is an after-opening event; 3.3.30 and 3.3.47 (after opening) are its inputs.`
- `MAPPING 4.2: add row | 86akhpvvq | Rows 107 to 118, the diagnostic's page for the wiki, nine instrument extensions, and thirteen findings routed | Served | 4.2.14 | The diagnostic's page for the team home; the recurrence thresholds as reset parameters are 4.2.10's; the rows, extensions, and findings are machinery |`

### 4.3 Team changes and restructuring

- `DEPS 4.3.5: drop 2.3.34 (loose: it decides what waits for the first reset; 2.3.30 is enough).`
- `DEPS 4.3.7: drop 3.3.30 (loose; reads "a change of domain lead (3.3.30) is handled by that rule once written").`
- `DEPS 4.3.8: add 4.3.14.`
- `DEPS 4.3.9: add 4.3.14.`
- `PHASE 4.3.14: Hiring and training -> Before the first hire. Reason: a counsel question, asked through 0.4; what may be said about a departure is legally required knowledge before anyone can leave. Clears 5.10.1, 5.10.2, 5.2.4.`
- `DEPS 4.3.14: drop 4.3.8, 4.3.9 (the counsel question is asked first; both read the answer); add 0.4.`

### 4.4 Rebuilding the team

- `PHASE 4.4.2: Hiring and training -> Before the first hire. Reason: what a lead may write about a person is a record policy the team relies on from the first check-in; 5.6.2, 5.8.9, and 5.2.8 (before the first hire) depend on it. Clears 5.6.2, 5.8.1, 5.8.9.`
- `DEPS 4.4.2: drop 4.2.5, 4.4.1 (loose; reads "4.2.5 says whether a will reading may be written").`
- `APPEND 4.4.3: whether the conversation is voluntary, whether it runs for leads only or for every person, and that it is held in the person's language (from 4.6.17).`
- `DEPS 4.4.4: add 4.4.6.`
- `APPEND 4.4.5: nothing from the conversation is written anywhere but where the person agrees; what the house does with the two or three development goals (2.2.14) is stated (from 4.6.17).`
- `PHASE 4.4.6: Hiring and training -> Before the first hire. Reason: a counsel question, asked through 0.4; 5.10.16 and 5.8.15 (before the first hire) need the answer. Clears 5.10.16.`
- `DEPS 4.4.6: drop 4.4.4 (the counsel question is asked first; 4.4.4 reads the answer); add 0.4.`
- `PHASE 4.4.8: Hiring and training -> Before the first hire. Reason: what a seat decides alone, what is a trapdoor, and what a founder keeps is in each lead's seat description and decision-rights entry, read at the first interview. Clears 5.9.1, 5.9.2, 6.1.6, 6.3.10.`
- `DEPS 4.4.8: drop 2.2.8, 4.4.7 (loose; reads "4.4.7 adds the one-off owner's case once decided").`
- `PHASE 4.4.9: Hiring and training -> Before the first hire. Reason: what the founders hand each lead on arrival, and by when, is told to the lead at hire (the lead onboarding plan 3.3.45 is before the first hire). Clears 5.9.1, 5.9.2, 5.9.5, 6.1.1, 6.1.7.`
- `APPEND 4.4.13: the guide exists in every house language; the invitation and what the person is told it is for and is not for are in it (from 4.6.22).`
- `KIT 4.4.13: Repeatable: yes. Every lead holds one with each person in their domain; each partner with their lead; the chef partner in the kitchen. Kit: 4.4.15 (the only career conversation kit).`

### 4.5 Creating the team environment

- `DEPS 4.5.1: drop 2.3.22, 2.3.25, 2.3.30, 3.3.14 (loose: the read takes what exists).`
- `DEPS 4.5.4: drop 2.3.30 (loose; reads "the block's date is placed by 2.3.30 once the reset is set").`
- `PHASE 4.5.11: Hiring and training -> Before the first hire. Reason: the destination for a report of a serious violation, a concern about one's own lead, and a concern about a founder is legally required and promised from the first hire; the phase rule applies. Clears 5.10.7, 5.10.8, 5.10.26, 5.2.2, 5.9.6, 5.9.8, 5.10.1.`
- `DEPS 4.5.11: drop 2.2.11, 2.3.15, 2.3.16, 4.5.10 (loose; reads "2.2.11's channels, 2.3.15's pulse, 2.3.16's loop window, and 4.5.10's unblocking path fill in their destinations once decided").`
- `DEPS 4.5.12: drop 2.3.29 (loose: a staff meal does not wait on the menu cadence).`
- `DEPS 4.5.13: drop 2.3.20 (reversed: 2.3.20 now depends on 4.5.13).`
- `ADD 4.5: new task, placed after 4.5.13.`

  ```
  ### 4.5.13a Decide the "not currently available" state: what a person may declare, what it protects, and what never reads it
  - Type: Decision
  - Phase: Hiring and training
  - Book: pp. 296 to 298 (the environment a person can count on includes being able to say no without explaining)
  - Default assumption: (WP pp. 16, 19) the white paper commits to bandwidth before results and to a team that is not disposable; it does not describe an availability state
  - Depends on: 2.3.11, 4.1.20, 5.8.6, 3.3.32
  - Done when: the founders have decided whether a person may declare themselves not currently available for a shift, a designation, or a stretch of the schedule with no reason required; who may see the state (the person, the scheduler, the lead) and who may not; that it is distinct from the paid hold (5.10.9), from a departure state (5.10.12), and from the attendance states (5.8.6); what it protects (rotation standing, the pool, the review, pay's days-worked count) and for how long; how it ends; and that performance, attendance, or rating data never sets or reads it; the build is 5.8.22's
  - Replaces old items: 17tn048qg2a (the availability state; the rotation floor is 4.1.20's)
  ```
- `MERGE 4.5.14, 4.5.15 into 4.5.15. New title: Write the meeting norms page and the meeting page for each standing meeting, the leads' review first. New done-when: one page holds the house's meeting norms, the three meeting roles, the rule for naming a decision method, the rule on correcting people, and the reconfigure date rule, reads in under five minutes, and lives in the team home (2.2.15); the leads' review has a one-page meeting page (purpose, standing agenda with limits, membership, who chairs, where the record lives, what pre-read is expected, the decision methods it uses, its next reconfigure date), and each other standing meeting gets one before its first run. Depends on: 4.5.9, 4.5.5, 2.2.29, 2.3.19. Repeatable: yes. Every owner of a standing meeting writes their own, and any new rhythm writes one before it passes the test in 2.3.3. Kit: 4.5.16. Old items: none. Repoint dependents of 4.5.14 (4.5.33) to 4.5.15.`
- `DEPS 4.5.15: drop 2.3.23 (loose: each meeting's page is written when that meeting's form exists; the leads' review first).`
- `DEPS 4.5.19: add 4.8.3, 4.8.3a (the own-words rule), 1.3.2, 1.4.1.`
- `APPEND 4.5.19: the card carries the house's fixed-terms list, version one: each term the chunks decide ("operating system" and "the stack" from 1.4.1; "lead" from 1.3.2; the departure words from 5.10.20; "the center", "a load", and "a founder's external load" from 6.1; "team", "the floor team", "the culinary team" from 4.1; "the review" and "points" from 5.4 and 5.5; "feedback" from 5.3), with the words each replaces, and the rule that every page on the team home is checked against the list before it is published and at each reset.`
- `PHASE 4.5.20: Hiring and training -> Before opening. Reason: it edits the brief checklist, which 2.3.20 writes before opening.`
- `PHASE 4.5.23: Before opening -> Hiring and training. Reason: the moments the house marks (a first solo, a departure, a birthday) start with the first cohort; 4.6.8, 4.8.9, 5.3.1, and 5.3.7 (hiring and training) depend on it. Clears 4.6.8, 4.8.9, 5.3.1, 5.3.7.`
- `DEPS 4.5.23: drop 2.3.25 (loose; reads "if 2.3.25 holds a quarterly gathering, which moments it carries").`
- `DEPS 4.5.22: drop 2.3.34 (loose; 2.3.30 is enough).`
- `DEPS 4.5.29: drop 2.3.34 (loose; 2.3.30 is enough).`
- `MAPPING 4.5: add row | 17tn048qg2a | Build a "not currently available" state and a fair-rotation rule | New task | 4.5.13a (the state); 4.1.20 (the rotation floor) | The person-declared availability state had no task; the rotation rule is 4.1.20's |`
- `MAPPING 4.5: add row | 86akht3fx | Rows 119 to 129, the conditions layer on the map, seven instrument extensions, two reset parameters, and twelve findings routed | Served | 4.5.30 | The ten conditions are what every person at Sŏn can count on, which is the environment checklist; the slot's ceiling and the rotation floor as reset parameters are 4.5.13's and 4.1.20's; the no-person-in-a-room rule is 5.3.9's; the rows, extensions, and findings are machinery |`
- `MAPPING 4.5: add row | 17tn048qg2f | Structure: Fix the vocabulary line: "lead," never "manager," for any seat, and the departure's words on every house surface | Served | 4.5.19 (the fixed-terms list) | Whether "manager" is a word the house uses is 1.3.2's decision and the departure's words are 5.10.20's; the list collects what those chunks decide. The item's rulings are options in those chunks, not rules here |`
- `MAPPING 4.5: add row | 17tn048qr4k | Structure: Fix the vocabulary line: "the center," "a load," and "the read on the center," and the rule that no house surface names the nature of any founder's commitments outside the house | Served | 4.5.19 (the fixed-terms list) | The terms are collected from 6.1; the rule that no surface names the nature of a founder's outside commitments is 6.1.9's decision |`

### 4.6 Team-building complexities

- `DEPS 4.6.1: drop 2.2.11, 4.1.31, 4.1.35, 4.3.9, 4.5.10, 4.5.18 (loose: the read takes what exists).`
- `DEPS 4.6.14: drop 4.3.7 (loose; reads "whether a move is a lever reads 4.3.7 once decided").`
- `REMOVE 4.6.17. Keeper: 4.4.3. Repoint dependents (4.6.22 removed; 5.4.1, 5.4.19, 5.6.1 already list 4.4.3: drop 4.6.17 from them). Reason: one career conversation decision; 4.4 holds the full set (what it asks, what it produces, counsel).`
- `REMOVE 4.6.22. Keeper: 4.4.13. Repoint dependents (4.6.23, 4.6.25: both removed).`
- `REMOVE 4.6.23. Keeper: 4.4.14.`
- `PHASE 4.6.24: Before opening -> Hiring and training. Reason: the working-block kit is built from the first leadership block (4.5.21, hiring and training); the first build makes the kit.`
- `DEPS 4.6.24: drop 4.6.7 (loose; reads "4.6.7's in-person cadence places later blocks").`
- `REMOVE 4.6.25. Keeper: 4.4.15. Reason: one kit per repeatable deliverable; kits/career-conversation/ is 4.4.15's.`

### 4.7 Diversity and inclusion

- `DEPS 4.7.1: drop 3.1.39, 3.2.41, 3.2.42, 3.3.27, 4.5.25, 4.5.6 (loose: the read takes what exists).`
- `DEPS 4.7.5: add 0.4.`
- `DEPS 4.7.10: drop 3.3.27 (loose: 3.3.11 is enough; reads "3.3.27's read may compute the answer later").`
- `DEPS 4.7.14: drop 2.2.15 (loose; reads "published to the team home once it exists").`

### 4.8 Team communication

- `DEPS 4.8.1: drop 2.2.11, 2.2.12, 2.2.13, 2.2.15, 2.3.15, 2.3.16, 2.3.33, 4.1.23, 4.1.31, 4.3.9, 4.5.13, 4.5.17, 4.5.19 (loose: the read takes what exists). 4.5.11 stays (now before the first hire).`
- `DEPS 4.8.3: drop 4.5.19 (reversed: 4.5.19 now depends on 4.8.3).`
- `ADD 4.8: new task, placed after 4.8.3.`

  ```
  ### 4.8.3a Decide the own-words rule: whether the house ever rewrites, summarizes, or translates what a person wrote in their own words
  - Type: Decision
  - Phase: Before the first hire
  - Book: pp. 330 to 332 (written communication carries the writer's meaning only if no one edits it on the way)
  - Default assumption: (WP p. 21) "employees are the users"; the white paper does not address who may edit a person's own record
  - Depends on: 4.8.2, 4.8.3, 2.3.11
  - Done when: the founders have decided, for a person's own words on the person page, in a check-in line, a review's self-assessment, a feedback item, a recognition, an exit conversation, and a candidate's scorecard note: whether anyone may rewrite or summarize them (never; only the person; a lead with the person's sign-off), whether they are ever translated (never, the original always stands and a translation is marked as one, or translated only at the person's request), what a translation of a personal record must carry (the original beside it, the translator, the date), and what a reader does with words they cannot read; the rule is stated on the internal writing reference card (4.5.19) and the language page (4.8.15)
  - Replaces old items: 17tn048qc3y (the own-words half, received from 5.3)
  ```
- `PHASE 4.8.8: Before the first hire -> Hiring and training. Reason: a chat tool and its off-shift rule concern the team, not a candidate; its inputs (2.2.13, 2.2.15) are hiring and training. Clears 4.8.8's two inversions.`
- `PHASE 4.8.13: Before opening -> Hiring and training. Reason: a departure can happen in the first cohort; 5.10.12 and 5.6.10 (hiring and training) depend on it. Clears 5.10.12, 5.6.10, 5.10.1.`
- `DEPS 4.8.13: replace 5.10 with nothing (reads "5.10.18 decides who reads the exit conversations").`
- `DEPS 4.8.15: drop 2.2.15 (loose; reads "published to the team home once it exists").`
- `MERGE 4.8.18, 4.8.19, 4.8.20, 4.8.22 into 4.8.18. New title: Write the communication tools specification: recognition, the feedback channel, phone handling, and the change-reach record, each with its manual fallback. New done-when: one specification, in sections, states for recognition what the tool must allow (a peer's words, a specific action, one service), what must be off (rankings, points, leaderboards, manager-authored praise shown as peer praise, surveys, off-shift prompts, any export to a review), and how a decline is handled; for the feedback channel the item's fields, the three closing states and their windows (2.3.16), the anonymity option and its behaviour, who sees what, the sync to the execution system, and the languages; for phone handling who or what answers, the disclosure sentence if any, the languages, the three record destinations and the no-relay rule, the routing of staff-directed calls on and off shift, and the gap flag for a message not in the record; for the change-reach record that, for each versioned change, the stack produces from existing data and not by hand whether it appeared in every open period's brief, exists in every listed language, and dates before each affected person's check-in, showing the process step that missed and never a name, on the leads' review agenda (2.3.19); and for each a paper or form fallback if the tool cannot be configured as specified; the build is Dominic's. Depends on: 4.8.9, 4.8.10, 4.8.11, 4.8.12, 4.8.14, 2.2.11, 2.2.24, 2.3.16, 4.1.12. Old items: 17tn048qc3n (the build half), 17tn048qc3q (the build half), 17tn048qc3r, 17tn048qc3m. Repoint dependents: 4.8.25 (drop 4.8.19, 4.8.20, 4.8.22; keep 4.8.18), 4.8.26 (replace 4.8.22 with 4.8.18).`
- `MAPPING 4.8: add row | 17tn048qc3y | Fix the rule that nothing reaches the wider team that was not a record first | Received from 5.3 (the own-words half) | 4.8.3a | The record-first half is 5.3.9's and the channels 2.2.11's; the rule that the house never rewrites or translates a person's own words is now a decision here |`
- `MAPPING 4.8: add row | 17tn048qc2j | Rows 130 to 141, the architecture page beside the destinations and cadence pages, the language list as a constraint on every wiki page, eleven instrument extensions, the vocabulary line as an audit rule, and twelve findings routed | Served | 4.8.17 | The communication page for the team home; the every-language constraint is 4.8.2's; the "diagnostic" vocabulary line joins the fixed-terms list in 4.5.19; the record-first rule is 4.8.5's; the rows, extensions, and findings are machinery |`
- `MAPPING 4.8: add row | 17tn048qck2 | Rows 142 to 154, the feedback culture page beside the destinations and communication pages, nine instrument extensions, twelve findings routed, "feedback" as a vocabulary line, and the no-page rule beside the other structural rules | Served | 4.8.17 | The feedback culture page (17tn048qck5) is already 4.8.17's; "feedback" as a term joins the fixed-terms list in 4.5.19; that a hypothesis has no page is 5.1.6's decision; "disengaged" as a word to remove is a candidate for the list; the rest is machinery |`

### 5.1 Hypothesis-based coaching

- `DEPS 5.1.3: drop 4.5.28 (loose; reads "a mentor relationship continuing after the pairing (4.5.28) is not a source").`
- `PHASE 5.1.9: Hiring and training -> Before the first hire. Reason: it holds the first trigger's policy for the performance track (5.8.5, before the first hire); a trigger is a policy the team relies on. Clears 5.8.5, 5.8.1.`
- `DEPS 5.1.9: drop 5.1.7 (loose: the policy names a repeated hypothesis by count; reads "5.1.7 sets how a hypothesis is tested").`
- `PHASE 5.1.12: Hiring and training -> Before the first hire. Reason: who coaches each founder is a founders' arrangement 6.2.10 (before the first hire) reads. Clears 6.2.10, 5.9.1.`
- `KIT 5.1.13: Kit: 2.3.18 (an insert to the check-in kit; no kit of its own).`

### 5.2 Giving hard feedback

- `DEPS 5.2.4: add 0.4.`
- `PHASE 5.2.8: Hiring and training -> Before the first hire. Reason: whether a hard conversation leaves a record and whose words it holds is a record policy counsel closes (5.2.4) and 5.8.9 and 5.10 (before the first hire) build on. Clears 5.8.9, 5.8.1, 5.4.1, 5.10.1.`
- `DEPS 5.2.8: drop 5.1.6, 5.2.5 (loose; reads "5.2.5 sets the conversation's form; 5.1.6 says where a hypothesis lives before it is tested").`

### 5.3 Creating a culture of informal feedback

- `PHASE 5.3.4: Hiring and training -> Before the first hire. Reason: where feedback about one's own lead goes when the check-in is not safe is a destination, decided with 4.5.11 before the first hire. Clears 5.9.6, 5.9.8, 6.2.9, 5.4.1.`
- `DEPS 5.3.4: drop 2.3.16, 5.3.2 (loose; reads "5.3.2 names the kinds; 2.3.16 sets the loop window").`
- `DEPS 5.3.9: drop 2.3.22 (loose; reads "the period's read is placed in the house review once 2.3.22 shapes it").`
- `PHASE 5.3.11: Hiring and training -> Before opening. Reason: how the feedback culture is read and when its baseline is set belongs with the other reads (4.5.25, 2.2.20), all before opening.`

### 5.4 The formal review process

- `DEPS 5.4.1: drop 4.4.3, 4.6.17, 5.1.6 (loose: the read takes what exists; 4.6.17 is removed).`
- `DEPS 5.4.13: drop 3.3.28 (loose; reads "the training-infrastructure line (3.3.28) receives the upward half's process items").`
- `DEPS 5.4.14: drop 4.7.9 (loose; reads "4.7.9's equity checks read the calibration record if one exists").`
- `DEPS 5.4.19: drop 4.6.17 (removed; 4.4.3 stays).`
- `DEPS 5.4.20: drop 4.1.36 (loose; reads "a holder's overload is a 4.1.36 case").`
- `MERGE 5.4.23, 5.4.24 into 5.4.23. New title: Build the review record on the person page and the review's placement trigger on the scheduling surface. New done-when: the record sits on the person page beside the check-in and plan records; the assembly pulls only from 5.4.8's source list and has no free-text field for the holder unless 5.4.11 allowed one; every entry carries the citation to the dated line it draws from; the record refuses a rating field and a pay field unless 5.4.4 or 5.4.5 kept one; visibility matches 5.4.18; a manual fallback (a printed assembly) exists for a review held with the stack off (4.1.26); the scheduling surface places each person's review on their clock (or on the season, if 5.4.6 chose one) in a window that meets 5.4.16, offers the holder a move but not a cancel, records held, moved, and extended, and reports the counts to the leads' review (5.4.20); the first cohort's reviews and the leads' reviews are on it before the first is due. Depends on: 5.4.6, 5.4.8, 5.4.16, 5.4.18, 5.4.19, 2.3.11, 3.3.32. Old items: 17tn048qeq2 (the build half), 17tn048qeu9 (the configuration half), 17tn048qeq3, 17tn048qepw (the placement half). Repoint dependents of 5.4.24 (5.4.28) to 5.4.23.`
- `MAPPING 5.4: add row | 17tn048qepg | Rows 155 to 168, the review page and the mechanics page beside the destinations and feedback pages, eleven instrument extensions, thirteen findings routed, "review" and "points" as vocabulary lines, and the no-pay-input rule beside the other structural rules | Served | 5.4.22 | The review page is 5.4.22's and the mechanics page 5.5.32's; the parameters register on the partners' page and never on the wiki is 5.5.31's; "the review" and "points" join the fixed-terms list in 4.5.19; that no review feeds pay is 5.4.5's decision; the rest is machinery |`

### 5.5 Compensation

- `DEPS 5.5.1: drop 3.3.18, 4.8.4 (loose: the read takes what exists).`
- `DEPS 5.5.14: drop 4.3.13 (loose; reads "a designation held every service (4.3.13) is read at the reset").`
- `DEPS 5.5.16: drop 3.3.14, 3.3.18 (loose: teaching is paid by kind; reads "3.3.18's module standard names who may author, and 3.3.14 what a mentor does").`
- `DEPS 5.5.17: drop 4.8.4 (loose: translation and interpreting are paid by kind; reads "4.8.4's interpreter designation once defined").`
- `DEPS 5.5.21: drop 3.3.32 (loose; reads "3.3.32 confirms the platform can show the benefits path").`
- `PHASE 5.5.25: Hiring and training -> Before opening. Reason: the pay parity read runs on the equity checks (4.7.9, before opening); it says itself when it can first run.`
- `NARROW 5.5.27. New title: List the parameter rows a lead's offer needs, and date them on the hiring calendar. New type: Action. New done-when: the rows an offer needs are listed by name from the parameters register, the date each must be set is on the hiring calendar (3.2.34) ahead of the leads' offers under the order 3.2.18 decided, and Dominic has confirmed the dates. Depends on: 5.5.3 to 5.5.18, 3.1.30, 3.2.18, 3.2.34. Old items unchanged. Reason: the order against the leads' interviews is 3.2.18's decision; 5.5 keeps the list of rows.`
- `SPLIT 5.5.28 into 5.5.28 (Before the first hire: "Dominic sets the values of the offer rows on the parameters register, with counsel where wage law applies"; done-when: every row 5.5.27 listed carries a value, set by Dominic, with counsel's answer where wage law applies, before the first lead's offer; no value is recorded in this repo) and a new task placed after it (Before opening: "Dominic sets every remaining value on the parameters register"; done-when: every row on the register 5.5.31 wrote carries a value or is marked unset with an owner and date, before the first training service; depends on 5.5.28, 5.5.31, 5.5.29, 5.5.30). Old item 17tn048qepf stays with 5.5.28.`
- `DEPS 5.5.29: add 0.4.`
- `NARROW 5.5.31. New title: Write the parameters register. New done-when: an internal register exists, outside this repo, with one row per value the architecture needs (the percentage; the revenue classes; each seat's point weight at each horizon; each marker's value; each salaried seat's salary and its day rule; each hourly seat's base wage; the payment cycle; the authorship, revision, translation, and any completion payment; the discretionary range's two values; the benefits gate's conditions; the closed-day rule; separation-related rows), each with its owner, what it is set against, whether it is set or unset, and a version; this repo holds the row names only and no value; the counsel questions this chunk raised are rows on 0.4's register. Depends on: 5.5.3 to 5.5.18, 5.5.21, 5.5.22, 5.5.26, 5.5.29, 0.4. Old items: 17tn048qept (the register half), 17tn048qeu4 (the register half). Reason: the counsel questions register is 0.4's.`
- `MERGE 5.5.33, 5.5.34 into 5.5.33. New title: Build the pay page, the daily calculation, and the pay correction path. New done-when: the calculation runs from the register's values and the scheduling and progression records with no hand entry per person; the page shows 5.5.19's fields with 5.5.19's visibility, beside the person page; a salaried seat's day rule and every marker are applied automatically; the fallback for a day with the stack off is written; a test day run against a training service reconciles to the rule by hand; a person can raise a correction from their own pay page, it reaches the owner 5.5.24 named with the windows running, the outcome and reason are written back to the person, a systemic cause opens a process item, the counts flow to the leads' review, and the destinations page (4.5.17) points to it. Depends on: 5.5.19, 5.5.24, 5.5.28, 5.5.30, 2.3.11, 2.3.16, 3.3.32, 4.5.17. Old items: 17tn048qeq5 (the build half), 17tn048qepx (the calculation and path halves), 17tn048qeu7 (the pay-entry half), 17tn048qepz (the automatic-move half), 17tn048qeu5 (the build half). Repoint dependents of 5.5.34 (5.5.39, 5.5.40) to 5.5.33.`
- `SPLIT 5.5.36 into 5.5.36 (Hiring and training: "Hold the first pay conversations at the offer: each partner with their lead"; done-when: each lead has heard the mechanics in 5.5.23's form at the offer, from the partner 3.2.20 named, with the written offer (3.2.32) beside it; what did not land is noted for 5.5.35) and a new task placed after it (After opening: "Hold the first pay conversations at the first pay move: each partner with their lead"; done-when: each lead has had the conversation at their first pay move in 5.5.23's form, and the guide is revised from both rounds; depends on 5.5.36, 5.5.35, 5.5.33). Repeatable and Kit lines stay with 5.5.36; 5.5.37 depends on both.`
- `MAPPING 5.5: change row for 17tn048qg2b: the register half goes to 0.4 (was 5.5.31); the counsel rows stay with 5.5.29; the card stays 5.10.26's.`

### 5.6 Managing high performers

- `DEPS 5.6.1: drop 4.4.3, 4.6.17, 5.1.10, 3.2.44, 4.3.13 (loose: the read takes what exists; 4.6.17 is removed).`
- `DEPS 5.6.6: drop 2.2.23, 4.3.13 (loose; reads "a goal met at a bandwidth cost (2.2.23) and a designation held every service (4.3.13) are the reset's reads of the same load").`
- `DEPS 5.6.8: drop 4.1.36, 4.3.6 (loose; reads "4.3.6 says whether the structure is ever changed for one person").`

### 5.7 The steady middle

- `DEPS 5.7.1: drop 4.8.9 (loose: the read takes what exists).`
- `DEPS 5.7.3: drop 4.4.3 (loose; reads "the career conversation (4.4.3), if held, is where the question would be asked").`
- `DEPS 5.7.4: drop 2.2.19, 2.2.20 (loose; reads "the charter metrics and the cultural labor score once defined").`
- `PHASE 5.7.7: Before opening -> Before the first hire. Reason: whose hours are reduced in a slow season is a policy promised to every hire; 5.10.3 and 5.10.14 (before the first hire) depend on it. Clears 5.10.3, 5.10.14, 5.10.1.`
- `DEPS 5.7.7: drop 4.1.20, 2.2.23, 5.6.6, 5.10 (loose; reads "the load rule (5.6.6) and the reduction boundary (5.10.14) read this rule").`

### 5.8 Managing low performers

- `DEPS 5.8.1: drop 3.4.5, 3.4.6, 4.2.5, 4.2.6, 4.2.10, 4.3.7, 4.3.12 (loose: the read takes what exists).`
- `DEPS 5.8.2: add 0.4.`
- `DEPS 5.8.4: drop 4.2.2, 4.2.6, 5.1.3, 5.2.9 (loose: the order of reads is named by kind; reads "4.2.2's diagnosis, 4.2.6's evidence, 5.1.3's sources, and 5.2.9's failure types fill in each read once decided").`
- `DEPS 5.8.5: drop 4.2.10 (loose: the recurrence thresholds are reset parameters; reads "4.2.10 sets the counts").`
- `DEPS 5.8.6: drop 3.4.5, 4.8.5 (loose; reads "3.4.5 handles a first-weeks pattern; 4.8.5 says where the record lives").`
- `PHASE 5.8.7: Hiring and training -> Before the first hire. Reason: the pauses (the organizational failures that stop the process) are part of the performance policy page (5.8.18, before the first hire) and the partners' review (5.10.10). Clears 5.10.10, 5.9.9.`
- `DEPS 5.8.7: drop 4.3.12 (loose; reads "the seat-repeat check reads 4.3.12's domain read once built").`
- `DEPS 5.8.14: drop 3.2.44, 3.3.29, 4.3.7 (loose: the outcomes are named by kind; reads "a move the person chooses runs through 3.2.44, 3.3.29, and 4.3.7 once decided").`
- `PHASE 5.8.15: Hiring and training -> Before the first hire. Reason: what a lead may ask about a hardship, what the house may adjust, and where a schedule request goes is a policy the team relies on and 5.10.16 (before the first hire) depends on. Clears 5.10.16, 5.10.1.`
- `DEPS 5.8.17: drop 3.4.10 (loose: 3.4.6 is enough; reads "3.4.10 joins the records later").`
- `MERGE 5.8.22, 5.8.23 into 5.8.22. New title: Build the attendance states, the "not currently available" state, the window block, and the trigger surfacing on the scheduling surface and the person page, or the manual fallback. New done-when: the scheduling surface records the attendance states per shift as 5.8.6 decided, counts over the window, shows the person their own states, surfaces the count to the check-in as a fact under the logistics questions, and refuses what 5.8.6 refused; it carries the "not currently available" state as 4.5.13a decided, set only by the person, with no reason field, visible only to whom 4.5.13a allowed, and read by nothing 4.5.13a excluded; the person page carries the block 5.8.11 shaped (its state with dates, the trigger's citations, the fixes owed and made, the check-in dates, the person's words, the close), written by whom 5.8.9 allowed and readable by whom 5.8.10 allowed; the triggers 5.8.5 chose are surfaced from the records that hold them, with the counts as reset parameters; aggregate counts flow to the leads' review; where the surface or the stack cannot do any of this, a manual record with the same rules is written and the partners' page records it as manual. Depends on: 5.8.5, 5.8.6, 5.8.9, 5.8.10, 5.8.11, 5.8.20, 4.5.13a, 3.3.41, 4.2.18, 2.3.7. Old items: 17tn048qfnx (the build half), 17tn048qfnj (the build half), 17tn048qfnk (the build half), 17tn048qfnc (the surfacing half). Repoint dependents of 5.8.23 (5.8.27, 5.9.15, 5.10.24) to 5.8.22.`
- `MAPPING 5.8: add row | 17tn048qfp4 | Rows 169 to 182, the performance page beside the destinations, feedback, review, and diagnostic pages, eleven instrument extensions, thirteen findings routed, the horizon vocabulary line, the two structural rules, and the first-year window count as the hiring system's leading indicator | Served | 5.8.18 | The performance page for the team home; the first-year window count is 5.8.17's and 3.4.17's; "the horizon" joins the fixed-terms list in 4.5.19; the rest is machinery |`

### 5.9 Managing managers

- `DEPS 5.9.1: drop 4.4.11, 4.7.12, 4.7.13, 5.4.12, 5.4.13 (loose: the read takes what exists).`
- `DEPS 5.9.3: drop 4.4.11, 5.1.7 (loose; reads "4.4.11's delegation signs and 5.1.7's testing form once decided").`
- `DEPS 5.9.4: drop 4.4.5, 5.4.18 (loose: the page's parts are named by kind; reads "4.4.5 and 5.4.18 fill in the career conversation's and the review's parts once decided").`
- `DEPS 5.9.6: drop 2.3.15, 4.7.12, 4.7.13, 5.4.13 (loose; reads "the pulse (2.3.15), the inclusiveness reads (4.7.12, 4.7.13), and the review's upward half (5.4.13) may carry a skip level's function once set").`
- `DEPS 5.9.7: drop 4.1.21, 4.2.6 (loose; reads "the room designation (4.1.21) once defined").`
- `DEPS 5.9.8: drop 4.2.10, 4.3.12, 4.3.13, 5.1.3, 5.4.12, 5.4.13 (loose: the count and the destinations are named by kind; reads "4.2.10 sets the count's threshold; 5.4.13 adds the upward half's route once decided").`
- `DEPS 5.9.9: drop 4.1.36, 4.3.12, 5.8.13 (loose; reads "5.8.13 says who judges the close; 4.3.12 the domain read").`
- `DEPS 5.9.10: drop 2.3.19, 4.2.8 (loose; reads "the leads' review record (2.3.19) and the domain lines (4.2.8) once written").`
- `PHASE 5.9.12: Hiring and training -> Before opening. Reason: the chef partner's adoption of the rules for the station leads follows the kitchen's review holder (5.4.21, before opening), with the other chef-partner tasks.`
- `NARROW 5.9.13. New title: Write the partner's insert for the lead's monthly conversation in the check-in kit. Done-when unchanged. Depends on: 5.9.2, 5.9.3, 5.9.4, 5.9.5, 5.9.6, 5.9.8, 2.3.18. Repeatable: yes. Each partner runs it with their lead; the chef partner with each station lead if 5.9.12 adopts it; any later holder of a lead's conversation. Kit: 2.3.18 (the insert lives in the check-in kit; the lead's page template is 5.9.15's). Old items unchanged.`
- `REMOVE 5.9.14. Keeper: 2.3.18. Reason: the lead's monthly conversation is the lead's check-in; one check-in kit.`
- `MAPPING 5.9: add row | 17tn048qg1z | (the how-to half) | note | 5.9.13 | Unchanged home; the insert now lives in kits/check-in/ rather than a kit of its own |`

### 5.10 Managing out, firing, and layoffs

- `DEPS 5.10.1: drop 4.3.8, 4.3.9, 4.3.10, 4.3.17, 4.8.13, 4.8.24, 5.7.13 (loose: the read takes what exists).`
- `DEPS 5.10.2: replace 5.5.31 with 0.4.`
- `DEPS 5.10.5: drop 4.2.11, 5.1.3 (loose: the never-cited list names a diagnosis and a hypothesis by kind; reads "4.2.11 and 5.1.3 once decided").`
- `DEPS 5.10.7: drop 4.8.4 (loose; reads "the interpreter designation (4.8.4) once defined").`
- `DEPS 5.10.12: drop 4.3.10, 5.5.33 (loose; reads "a lead's departure adds 4.3.10's handoff; final pay is computed by 5.5.33's calculation").`
- `DEPS 5.10.14: drop 3.2.44, 4.1.34, 4.3.7, 5.7.13 (loose; reads "the priority afterwards runs through 3.2.44's internal loop; a retired seat is a 4.1.34 entry; publication is 5.7.13's").`
- `DEPS 5.10.16: drop 5.1.5 (loose; reads "a hypothesis (5.1.5) never names a hardship").`
- `DEPS 5.10.17: drop 3.3.39 (reversed: 3.3.39 now depends on 5.10.17).`
- `DEPS 5.10.19: drop 3.3.40 (loose; reads "the range card (3.3.40) cites the conduct policy once built").`
- `MERGE 5.10.23, 5.10.24, 5.10.25 into 5.10.23. New title: Build the separation records: the flag read and incident records, the hold and departure states, and the exit conversation record. New done-when: the flag read record and the incident record exist in the stack in the closed form 5.10.7 chose, kept apart from the person page, readable by whom 5.10.7 allowed, with the founder variant on the partners' page as 5.10.8 decided, the one-line existence marker on the person page, and the routing from 4.5.11's destination into it; the scheduling surface carries the hold state written from the flag record with no reason field, paying and counting as 5.10.9 decided, visible only as "not scheduled" beyond the person, the lead, and the custodian; the person page carries the departure state with its date and kind, the citation to the package or entry, the person's own words if they choose, the last day, and the written package's place, written by whom 5.10.12 allowed; the access-end moment is enforced by the stack; the exit conversation record holds only the person's own words to 4.8.13's questions, aggregating by theme to the house review as 5.10.18 decided and never to the person page; the consent record for the yearly question exists with its revocation, the contact kept only as counsel allows, the yearly answers aggregating to the reset; all in every house language; where the stack cannot, a manual record with the same rules is recorded on the partners' page. Depends on: 5.10.7, 5.10.8, 5.10.9, 5.10.11, 5.10.12, 5.10.18, 5.8.3, 5.8.22, 3.3.41, 4.5.17, 4.8.13, 4.8.24, 5.5.33, 2.3.22, 2.2.25. Old items: 17tn048qfnq (the employee-side build), 17tn048qfnd (the record build), 17tn048qr4c (the build half), 17tn048qg2c (the build), 17tn048qg27 (the state and block build), 17tn048qg28, 17tn048qg22 (the build half). Repoint dependents of 5.10.24 and 5.10.25 to 5.10.23.`

### 6.1 Manage your time and energy

- `DEPS 6.1.1: drop 4.4.18 (loose: the read takes what exists).`
- `DEPS 6.1.4: drop 4.4.18 (loose; reads "the handover list (4.4.18) once written").`
- `DEPS 6.1.5: drop 2.2.35, 4.4.18 (loose; reads "the alert register (2.2.35) and the handover list (4.4.18) are two of the lists it would read together").`
- `DEPS 6.1.6: drop 4.1.36 (loose; reads "4.1.36 says when a leadership line is added").`
- `DEPS 6.1.10: drop 5.1.17, 5.4.26, 5.8.25 (loose: the tempo is set against modules by name; reads "the modules (5.1.15, 5.4.26, 5.8.24) once built").`
- `DEPS 6.1.11: drop 2.2.30, 2.3.16 (loose; reads "the alert-actor rule (2.2.30) and the loop window (2.3.16) once set").`
- `DEPS 6.1.13: drop 4.4.18 (loose; the protection order names the loads by kind).`
- `DEPS 6.1.14: drop 4.4.18 (as 6.1.13).`
- `PHASE 6.1.16: Hiring and training -> Before opening. Reason: it is written from rules already decided, including the alert-actor rule (2.2.30, before opening), and the absence test (6.1.19, before opening) runs against it.`
- `MAPPING 6.1: add row | 17tn048qr4m | Rows 201 to 213, the center's page beside the cadence and destinations pages, the founder load ledger as the assembly's calendar, seven instrument extensions, twelve findings routed, the vocabulary line, the structural rule, and the audit that the assembled wiki records no founder's interiority and names no founder's external load | Served | 6.1.16 | The center's team-facing half is the page on what the house never depends on a founder for; the load ledger is 6.1.17 if 6.1.5 adopts one; the working-with-me additions are 6.1.12; the interiority audit is CLAUDE.md's rule; the rows, extensions, and findings are machinery |`

### 6.2 Foster relationships

- `DEPS 6.2.1: drop 4.5.10 (loose: the read takes what exists).`
- `DEPS 6.2.2: drop 4.1.32 (loose; reads "the live-risk line's form (4.1.32) is one thing the partners owe each other a read of").`
- `DEPS 6.2.3: drop 2.3.26, 2.3.30 (loose; reads "the gate review and the reset once set").`
- `DEPS 6.2.5: drop 2.2.11, 4.5.10, 5.4.13 (loose; reads "the channels (2.2.11), the unblocking path (4.5.10), and the upward half (5.4.13) once decided").`
- `DEPS 6.2.6: drop 4.3.20, 4.3.5, 4.5.22 (loose; reads "the first-quarter hold (4.3.5, 4.5.22) governs the answer during dinner's first quarter").`
- `DEPS 6.2.11: drop 4.8.21, 4.8.5 (loose; reads "the whole-team statement form (4.8.21) and the record rule (4.8.5)").`

### 6.3 Consider your career

- `DEPS 6.3.1: drop 4.3.8, 4.3.10, 4.4.18, 5.4.13 (loose: the read takes what exists).`
- `DEPS 6.3.2: drop 4.4.18 (loose; reads "the handover list (4.4.18) once written").`
- `DEPS 6.3.4: drop 2.3.30 (loose; reads "the reset and the annual block (2.3.30) once set").`
- `DEPS 6.3.5: drop 4.7.12, 5.4.13 (loose; reads "the inclusiveness read (4.7.12) and the upward half (5.4.13) once decided").`
- `DEPS 6.3.6: drop 4.1.34, 5.2.10 (loose; reads "the structure change entry (4.1.34) and how management absorbs blame (5.2.10) once decided").`
- `DEPS 6.3.7: add 0.4.`
- `DEPS 6.3.9: drop 4.7.17 (loose; reads "the opportunities page (4.7.17) publishes the dates").`
- `PHASE 6.3.10: Before the first hire -> Hiring and training. Reason: the founders' rows depend on the founders' floor rule (6.1.8) and standing with the whole team (6.2.8), both hiring and training; the register's first version (2.2.4) carries the founders' pre-hire rows meanwhile.`
- `PHASE 6.3.12: Hiring and training -> Before opening. Reason: it follows the career conversation kit (4.4.15, before opening).`

## 3. Leftover items

| ID | Fate | Task | Mapping chunk |
|---|---|---|---|
| 17tn048qc2j | Served | 4.8.17 | 4.8 |
| 17tn048qck2 | Served | 4.8.17 | 4.8 |
| 17tn048qepg | Served | 5.4.22 | 5.4 |
| 17tn048qfp4 | Served | 5.8.18 | 5.8 |
| 17tn048qg2f | Served | 4.5.19 (fixed-terms list; rulings are options in 1.3.2 and 5.10.20) | 4.5 |
| 17tn048qg2j | Served | 5.10.20 and 0.4 | 0 |
| 17tn048qr4k | Served | 4.5.19 (fixed-terms list; the rule is 6.1.9's) | 4.5 |
| 17tn048qr4m | Served | 6.1.16 | 6.1 |
| 17tn048qr4n | New task | 2.2.38a | 2.2 |
| 86ajgmxnp | Dropped (machinery) | none | 0 |
| 86ajgn3ep | Dropped (machinery) | none | 0 |
| 86akh2qht | Served | 2.1.13 | 2.1 |
| 86akh2qrp | Served | 2.1.10 | 2.1 |
| 86akh2r4k | Dropped (machinery) | none | 2.1 |
| 86akh3rx4 | Dropped (brand-dependent) | none | 2.1 |
| 86akh3t00 | Served | 2.1.4 | 2.1 |
| 86akh3t27 | Served | 2.1.7 | 2.1 |
| 86akh3tg0 | Served | 2.1.5 | 2.1 |
| 86akh3tjb | Dropped (brand-dependent) | none | 2.1 |
| 86akh3tp5 | Dropped (brand-dependent) | none | 2.1 |
| 86akh5uym | Served | 2.2.15 | 2.2 |
| 86akh681a | Served | 2.3.33 | 2.3 |
| 86akh7rm1 | Served | 3.1.31 | 3.1 |
| 86akh9tau | Served | 3.4.17 | 3.4 |
| 86akhb2xh | Served | 3.3.27 | 3.3 |
| 86akhcz2m | Served | 4.1.17 | 4.1 |
| 86akhcz7t | Served | 4.1.17 | 4.1 |
| 86akhpvvq | Served | 4.2.14 | 4.2 |
| 86akht3fx | Served | 4.5.30 | 4.5 |

- `MAPPING 3.3: add row | 86akhb2xh | The onboarding read's elements into the measure set, and rows 75 to 92 into the assembled test | Served | 3.3.27 | The five elements with no target are what the onboarding read measures; 2.2.25's register receives what 3.3.27 keeps; the readiness rows are 3.3.50's and the instrument list is machinery |`

Totals: served 22, new task 1, dropped 6 (brand-dependent: 86akh3rx4, 86akh3tjb, 86akh3tp5; machinery: 86ajgmxnp, 86ajgn3ep, 86akh2r4k). Inside the served S17 carryovers, the readiness-row counts, instrument-extension bookkeeping, and routed-findings lists are machinery and are not carried; each mapping row says so.

## 4. Multi-row items

All seventeen pairs are a route and its receipt, and stay as they are, with two edits:

- 86akh9tay: three rows today (2.1 routes to 3.x; 3.1 receives at 3.1.42; 3.2 names it without a row). After the changes above: 2.1 routes to 3.x (unchanged); 3.1's row becomes "Routes to 3.2 -> 3.2.48"; 3.2 gains the receipt row at 3.2.48. One home.
- 17tn048qepk, 86akh3vrq, 86akhpvnf, 86akht376 (2.1 routes to 5.5; 5.5 receives): fine as is; 86akhpvnf's and 86akht376's receipts name 5.4 tasks as well as 5.5 ones, which is a receipt recording where the halves went, not a second home. No change.
- 17tn048qfne, 17tn048qfnu (3.2 routes to 3.4; 3.4 receives at two tasks each): fine as is; each names a policy half and a read half.
- 17tn048qr3t, 17tn048qr3v, 17tn048qr44, 17tn048qr4a (2.1 routes to 6.x; 6.1, 6.2, 6.3 receive): fine as is.
- 86akh3uez, 86akh3uhy, 86akh5upw (2.1 routes to 2.2; 2.2 receives): fine as is.
- 86akh5uc7, 86akh676k, 86akht1ud (2.1 routes to 2.3; 2.3 receives): fine as is.

No row is removed.

## 5. Judgment calls

For Brandon to see. Where two duplicates framed a decision differently, the keeper holds the framing that leaves the most options open and the other framing goes into the keeper's session brief; the apply step does not touch session files, so these are listed here for whoever updates `session.md`.

1. **Founders' stage in hiring (3.1.3 keeps; 3.2.6 removed).** 3.2.6 asked whether a founder's "no" must name a read and offered end conditions (a date, a headcount, a number of consecutive clean calibration reads, never). Both go into 3.1.3's brief.
2. **Founders' interviewer training (3.2.13 keeps; 3.1.15 removed).** 3.1.15 framed the minimum as the reads, the stage's questions, the rubric, and a practice interview scored by the other founder, with the record covering the first leads; 3.2.13 offered an outside trainer and practice on consenting non-candidates. Both framings into 3.2.13's brief.
3. **What replaces the founders' read (3.2.42 keeps; 3.1.41 removed).** 3.1.41 wanted the decision made at the first reset with data; 3.2.42 decides before the first frontline packets and rereads at the reset. The timing itself is an option for the brief.
4. **Career conversation (4.4 keeps; 4.6.17, 4.6.22, 4.6.23, 4.6.25 removed).** 4.6.17 framed it as voluntary, possibly for leads only, held in the person's language, with nothing written except where the person agrees; appended to 4.4.3 and 4.4.5 as things to decide, not as answers.
5. **Leads' review and house review (2.3 keeps; 2.2.33, 2.2.34, 2.2.41 removed).** 2.2's refusals (no opening on a lagging figure; never the integration layer the stack should be; never scoring a bandwidth-cost goal as a win) are appended to 2.3.19 and 2.3.23. 2.3.24 becomes the single review kit; the person's formal review keeps its own kit (5.4.29).
6. **Lead's check-in holder (2.2.5 keeps; 2.3.14 narrowed to placement).** If Brandon would rather decide the pairing in the cadence session than in the operating-system session, swap the keeper; the change is mechanical either way.
7. **Phase moves widen "before the first hire".** Twenty-three decisions move earlier under the phase rule (a policy a candidate sees or relies on, or that is legally required): 2.2.7, 2.2.14, 2.2.24, 2.2.29, 2.2.37, 3.1.36, 3.1.37, 3.1.40, 4.1.20, 4.1.29, 4.2.12, 4.3.14, 4.4.2, 4.4.6, 4.4.8, 4.4.9, 4.5.11, 5.1.9, 5.1.12, 5.2.8, 5.3.4, 5.7.7, 5.8.7, 5.8.15. Brandon may prefer some as hiring-and-training decisions with an interim line on the candidate sheet; the ones most arguable are 4.4.2, 4.4.8, 4.4.9, 5.1.9, 5.1.12, and 5.2.8.
8. **4.2's later half moves to before opening (4.2.9, 4.2.10, 4.2.11).** This splits the diagnostic chunk across phases. The alternative is to leave them in hiring and training and treat their dependencies on the house review and the reset as loose; the reset's parameters would then be set without the diagnostic's counts.
9. **The pulse family.** Six decisions across five chunks shape one instrument: 2.3.15 (rhythm), 3.4.9 (hiring and onboarding questions), 4.2.4 (house survey), 4.5.25 (psychological safety), 5.3.11 (feedback culture), 5.6.10 (the stay question). They are kept in their chunks; one working session covering all six may serve better than five.
10. **"First conversation with each lead" actions.** 2.3.17, 4.4.14, 5.1.17, 5.3.19, 5.5.36, 5.6.18, and 6.2.14 each hold a first conversation between a partner and a lead. They are kept as separate actions because each chunk's session unlocks its own; in practice they will run inside the lead onboarding plan (3.3.45).
11. **Pattern tasks and ClickUp volume.** After these changes the list holds roughly 20 "Read what the upstream chunks settle" actions, 15 "Add the entries to the decision-rights register" tasks, and 15 "Run the first read at the mechanism reset" actions. They are each chunk's genuine work, but Brandon may prefer the read tasks as a line in `session.md` rather than ClickUp subtasks (saving 20), and the register and reset tasks as checklists on two standing tasks (saving another 28). Not applied.
12. **Counsel questions register at 0.4.** Chunk 0 becomes the home of every counsel question. The alternative was to leave it inside 5.5.31, where it started; that would make the pay chunk the owner of the separation, hiring, and departure questions too.
13. **"Not currently available" placed in 4.5.** The 3.3 mapping suggested 4.5; the 4.5 mapping suggested 2.3 or 4.5. It is a team-environment promise, so 4.5; the build rides with the attendance states in 5.8.22. 5.10.9's paid hold and 5.10.12's departure state are kept distinct from it in the done-when.
14. **The own-words rule placed in 4.8 (4.8.3a).** It could also sit in 2.3 (the person page) or 5.3. 4.8 holds translation, which is where the rule bites hardest.
15. **The fixed-terms list lives on the internal writing reference card (4.5.19)** rather than as a new deliverable. The vocabulary rulings the old items carried ("lead" never "manager"; the departure words; "the center") are options in 1.3.2, 5.10.20, and 6.1, not rules the list imposes.
16. **4.1.38 moved to before opening** on the assumption that the floor and kitchen interface exists from dinner's first service and does not wait for a second period. If Brandon reads it as a two-period instrument, it goes back to after opening and 4.6.10 and 4.6.19 drop it as loose.
17. **1.1.13's phase** is set to before the first hire with the conditional in the done-when; if 1.1.9 chooses the onboarding timing it is retagged.
18. **Two old halves dropped inside served items:** the brand-canon account of the chef seat in 86akh2qrp (2.1.10 keeps only the white paper's account) and the canon voice tests in 86akh3tg0.
