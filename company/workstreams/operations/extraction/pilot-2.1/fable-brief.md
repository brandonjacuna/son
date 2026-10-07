# Pilot brief: chunk 2.1, founding documents

You are reconsidering one section of a large body of prior work. Read this whole brief before opening any file.

## The program, as Brandon now states it (2026-09-26)

Brandon is a founder of Sŏn, a restaurant opening in 2027. In his consulting work he has used Claire Hughes Johnson's *Scaling People* as a manual for building a company's operational systems, and he is using it the same way to build Sŏn: every back-of-house system, people system, and operating rhythm.

The purpose of the extraction was simple. Instead of Brandon rereading the book and saying "we need to decide this, we need to write that," the book gets turned into the **work**: the decisions to make, the actions to take, and the deliverables to produce, in the book's order. Where Sŏn's white paper already implies an answer, the work item carries it as a **default assumption** to save him time when the decision comes up. He expects Sŏn to diverge from the book in places. That's fine and gets noted, not argued.

Over sixteen sessions the prior work drifted. It wrote about 700 "Recommended" positions for Brandon to ratify, invented a lot of Sŏn-specific vocabulary and machinery, and read the brand guidelines and the experiential deck as authoritative. Brandon has ruled:

1. **No decisions are made for him.** No verdicts, no "Recommended," "Founder-gated," "Chef-gated," or "Team-filled" marks. A position becomes an **option with its reasoning**. Where the white paper supports a default, state it as "Default assumption (white paper p. N): ...", a starting point he can accept or discard.
2. **Brand guidelines and the experiential deck are out of scope.** They are startup-phase pre-work, and there is no property yet. Anything that rests on them ("Canon," "Deck," brand voice, lexicon, named rooms or rituals from the brand work, the canon-versus-charter authority question) is removed from the working manual. If a consideration survives without the brand support, keep it on its own merits. If it only exists because of the brand work, drop it and note that in the mapping.
3. **It's a reconsideration, not a teardown.** The prior synthesis holds real research: how the book's ideas land in a restaurant, legal and counsel questions, failure modes, sequencing, floor realities. Treat it as seriously as the book. Keep what serves the build, rewrite what was framed as a verdict, and drop only what is brand-dependent, program machinery (carryovers, ledger bindings, session routing, readiness-test row numbers, "S5 P37" cross-references), or duplicate.
4. **The white paper is the only Sŏn context.** `robert-lerma-white-paper.pdf`, extracted in full at `extraction/s01/record.md`, cited by page as "WP p. N".

## The chunk

**2.1 Founding documents**: book pp. 71 to 83 (Chapter 2's opening and the "Founding documents" section), plus the chapter's exercises that serve it.

Chunks follow the book's sections: 0, 1.1 to 1.4, 2.1 to 2.3, 3.1 to 3.4, 4.1 to 4.8, 5.1 to 5.10, 6.1 to 6.3. Adjacent sections that material may belong to:
- 2.2 The operating system (pp. 84 to 134): goals, OKRs, metrics, planning, decision-making frameworks, team charters
- 2.3 Operating cadence (pp. 135 to 143)
- 1.x the four operating principles; 4.1 team structures (roles and seats); 5.5 compensation; 6.x the founder personally

Material in the S2 page that belongs to another chunk is **not lost**: list it in the mapping as "routes to X.Y" with a one-line note on what it is.

## Files to read (all paths relative to `/Users/brandonacuna/Desktop/scaling-people:/`)

1. `extraction/s02/book.md`: the book text for pp. 70 to 83, verbatim. Primary source.
2. `extraction/pilot-2.1/book-exercises-145-150.md`: the book's Chapter 2 exercises (Stripe's operating principles, team charter, organizational foundations).
3. `extraction/s02/workbook.md`: the same exercises in the workbook, pp. 11 to 22.
4. `extraction/s01/record.md`: the white paper in full. Read the whole thing. It is the only Sŏn context, and default assumptions depend on reading it carefully rather than guessing where the relevant passage is.
5. `archive/clickup-export-2026-09-26/operating-system-doc/03-2ky45bmy-31673.md`: the old Session 2 synthesis page (71,000 characters). This is what you're reconsidering.
6. `extraction/pilot-2.1/old-items.md`: every old ClickUp build-out subtask and carryover that touches this chunk, verbatim with comments (71,000 characters).
7. Optional lens: `profiles/organizational-systems-architect.md` (the reasoning profile the old session used). Use it as a lens for considerations only, never as authority.

Do not read `sources/brand-guidelines.md`, `sources/brand-guidelines-deck.pdf`, `extraction/s02/deck.md`, or `extraction/s02/record-brief.md`.

## What to write

Create the folder `manual/2.1-founding-documents/` and write four files.

### `book.md`: what the manual says

The book's guidance for this section, organized as someone flipping to it would want it: what founding documents are, what each one contains, why they matter, her tests and examples, and the exercises. Cite pages as "(p. N)". Paraphrase: short quotations only where her exact phrasing is the point, no more than a sentence each. This is Brandon's quick reference, not a reproduction. Point to `extraction/s02/book.md` for the full text. No Sŏn content in this file.

### `considerations.md`: what's worth knowing before doing the work

For each topic in the section, in the book's order:
- **What the white paper already holds**, cited by page. State it plainly, including where it is silent.
- **Considerations** from the old synthesis worth keeping: restaurant realities, sequencing, risks, counsel questions, failure modes. Each is written as information or an option, never a verdict.
- **Options** where the old work argued a position: name the option(s) and the reasoning for each, and say what choosing it commits Sŏn to. No "we recommend."
- **Where Sŏn may diverge from the book**, if the white paper suggests it.

Keep it proportionate: useful, not exhaustive. A reader should come away with what they need to make each decision well, in a fraction of the old page's length.

### `tasks.md`: the work

Every decision, action, and deliverable this section of the book calls for, in the order they'd naturally be done. Numbered `2.1.1`, `2.1.2`, and so on. For each:

```
### 2.1.N <Verb-first title, e.g. "Decide Sŏn's mission statement">
- Type: Decision | Action | Deliverable
- Phase: Before the first hire | Hiring and training | Before opening | After opening
- Book: pp. N to N (what she says to do, one line)
- Default assumption: (white paper p. N) ... | None; the white paper is silent
- Depends on: 2.1.M, or another chunk's number if clearly needed | None
- Done when: one line
- Replaces old items: ClickUp IDs from old-items.md | None
```

Rules for tasks:
- Titles start with a verb: Decide, Write, Define, Draft, Choose, Set, Hold, Review, and so on. Never "Ratify."
- A **Decision** is a choice. A **Deliverable** is a document or artifact to produce. An **Action** is something to do (a meeting, a conversation, a review).
- Include the book's exercises as deliverables or actions where they apply to Sŏn.
- Don't split finely. One task per real piece of work. Expect roughly 8 to 20 tasks for this section.
- Where a decision needs the chef partner or a co-founder, say so in "Done when" (e.g. "agreed by all founders"). Don't assign ownership beyond that.

### `mapping.md`: the fate of every old item

1. A table covering **every** item in `old-items.md` (every build-out subtask and every carryover): `| Old ID | Old name (short) | Fate | Goes to | Reason |`. Fate is one of: **Kept** (same work, maps to a new task), **Rewritten** (e.g. "Ratify X" becomes "Decide X"), **Merged** (into a new task with others), **Routes to X.Y** (belongs in another chunk), or **Dropped** (brand-dependent, program machinery, or duplicate). No item may be missing.
2. A short section listing the **S2 page's major sections** (its numbered headings) and where each one's content went: into this chunk's considerations, routed to another chunk, or dropped and why.
3. A short **"What was dropped and why"** paragraph, so Brandon can see exactly what brand-dependent or machinery material left the working manual. The original remains verbatim in the archive.

## Writing rules (all four files)

- Plain, direct English. Sentence case headings.
- No em dashes. Use commas, colons, semicolons, or restructure.
- "Customer," never "guest."
- Don't use daypart code names (Good Energy, Dosi, Luxx). Refer to service periods by time of day.
- No financial figures. If one is needed, say financials aren't a source for this work.
- No performed conviction ("we believe," "our goal is").
- Keep the old program's private vocabulary out unless the white paper itself uses the term. If a coined term is genuinely useful, define it in plain words the first time.
- No profanity.

## When you finish

Reply with: the four file paths; the task count by type and phase; the mapping's counts by fate; the three to five most consequential things you dropped or reframed; and anything you were unsure how to handle, so the controller can raise it with Brandon.
