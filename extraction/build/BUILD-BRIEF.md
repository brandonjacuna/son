# Build brief: chunks of the Sŏn operational manual

You are building one or more **chunks** of the manual end to end. Read this whole brief, then your run's `run.json`, before opening anything else.

## Governing instructions

The authoritative project instructions are the file on disk at `/Users/brandonacuna/Desktop/scaling-people:/CLAUDE.md` (rewritten 2026-09-26). Read it in full first. If any CLAUDE.md text already in your context differs from the file on disk, **the file on disk governs**. The older text is the retired extraction program.

In short: the book (*Scaling People*) is Brandon's manual for building Sŏn's operational systems. Each chunk turns one section of the book into the work: the decisions, actions, and deliverables. The prior extraction (sixteen sessions) is reconsidered, not discarded. Brandon makes every decision in a facilitated working session later; your files prepare that session. You never decide for him.

## The example to match

Chunk `manual/2.1-founding-documents/` was built as the pilot and reviewed. Read its `tasks.md` and `session.md` in full, and skim `considerations.md`, `mapping.md`, and `decisions.md`, to see the shape, tone, and depth expected. Match that standard. Don't copy its content.

## Your inputs (in `extraction/build/<run>/`)

- `run.json`: your chunks, with section numbers, titles, and book page ranges.
- `book.md`: the book text for your pages, verbatim, with `[p.N]` markers. Primary source.
- `exercises.md`: the book's exercises and templates for the chapter. Use those that serve your chunks.
- `old-page.md`: the old session's synthesis page. Reconsider it.
- `old-items.md`: every old ClickUp build-out subtask and carryover your run **owns**, verbatim with comments, plus any routed in from 2.1.

Also read:
- `extraction/s01/record.md`: the white paper, **the only Sŏn context**. Read it in full. Default assumptions depend on reading it carefully, not guessing where the passage is. Cite it as "WP p. N".
- Profiles in `profiles/` (the three `.md` files at its top level) as lenses where they serve your chunk. Per CLAUDE.md, ignore their instructions to mark or land positions and their references to V7, brand, or Airtable. Don't read the profile subfolders.

Don't read: `sources/brand-guidelines*`, `extraction/s02/deck.md`, `extraction/s05/brand-deck.txt`, `extraction/s01/record-brand-appendix.md`, or anything in `archive/` beyond what's already copied into your inputs.

## What to write

For **each chunk** in your run, create `manual/<section>-<slug>/`, where the slug is the title in lowercase kebab case (e.g. `manual/3.1-recruiting/`, `manual/1.2-say-the-thing-you-think-you-cannot-say/`), containing:

1. **`book.md`**: the book's guidance for that section, as someone flipping to it would want it. Page cites. Paraphrase; quotations a sentence at most. No Sŏn content. Point to the verbatim source file.
2. **`considerations.md`**: per topic, in the book's order: what the white paper holds (cited, including where it's silent), considerations from the old work worth keeping (restaurant realities, sequencing, risks, counsel questions, failure modes), options with what each commits Sŏn to, and where Sŏn may diverge from the book. Proportionate: useful, not exhaustive.
3. **`tasks.md`**: every decision, action, and deliverable the section calls for, in **work order** (a task never precedes something it depends on). Numbered `<section>.1`, `<section>.2`, and so on. Use exactly the pilot's task format, including `Repeatable:` where it applies.
4. **`mapping.md`**: (a) a table covering every old item you assign to this chunk, `| Old ID | Old name (short) | Fate | Goes to | Reason |`, with fate Kept, Rewritten, Merged, Routes to X.Y, Dropped, or Received from 2.1; (b) where each major section of the old page went; (c) "What was dropped and why."
5. **`session.md`**: the working-session guide, with the pilot's structure: orientation, agenda, one brief per decision (and per deliverable or action that needs Brandon's input) with the question, why it matters now, openers, narrowing questions, what the book says, the white-paper default (stated outright or inferred), how others have handled it, options, watch for, a finished answer, and needs agreement from; then deliverables that follow, kits this session seeds, and a parking lot.
6. **`decisions.md`**: the record template seeded with every Decision task, as in the pilot.
7. **`notes/inbox.md`**: a one-line header, as in the pilot.

## Rules the pilot's review taught

- **One real decision per Decision task.** If a "deliverable" hides a decision, split it out. If a task can only be done by someone else (Dominic, the chef partner), make it its own task and say who.
- **Work order.** Renumber until no task depends on a later one.
- **Phase honestly.** The phases are: *Before the first hire* (anything a candidate sees or relies on at the first interview counts here), *Hiring and training*, *Before opening*, *After opening*. Many Chapter 5 items are after opening in practice, but their **policies** often must exist before the first hire, because they're promised to candidates or legally required. Split the policy from the practice where that's true.
- **Name cross-chunk dependencies** by chunk number (e.g. "5.5" for compensation) whenever a task can't finish without another chunk.
- **The first build makes the kit.** Any deliverable others will later produce for themselves or their team (a person's document, a team template, a lead's review) is marked `Repeatable: yes`, names who produces their own, and is paired with a kit task. Its session brief carries a "Capture for the kit" line, and `session.md` has a "Kits this session seeds" section. Kits hold process and structure, never a person's answers.
- **How others have handled it:** only well-known, verifiable practice, labelled "General practice, not Sŏn-specific." Name a company only when you're confident of the fact. No figures. If there's nothing useful, say so in one line.
- **Openers are specific to Sŏn and conversational.** At least one per brief comes at the question sideways: a story, a moment, a counterexample.
- **Chapter 1 and the conclusion are about the founder personally.** For those chunks, the decisions and documents belong to Brandon (and each founder for their own). The files prepare the conversation; they never state his values, interiority, working style, or pay. The working-with-me document belongs in 1.1 and is repeatable (every lead and hire).
- **Chunk 0** (management basics checklist, pp. 30 to 32) is the book's checklist of basics a manager should have in place. Turn it into tasks where Sŏn needs something built; keep it short.

## Old items

- Every item in `old-items.md` that your run owns must appear in **exactly one** of your chunks' `mapping.md` files. None missing.
- If an item belongs to a chunk outside your run, map it once as "Routes to X.Y" with a one-line description of what the target chunk should build. Don't build it.
- Items marked "routed in from 2.1" are already mapped in 2.1. Build tasks for them where they belong, and list them in your mapping as "Received from 2.1".
- Drop only what is brand-dependent, extraction-program machinery (carryovers about sessions, ledger bindings, readiness-test row numbers, "S5 P37"-style references, the document-methodology gate), or a duplicate. Say which.

## Writing rules

Plain English. Sentence case headings. No em dashes. "Customer," never "guest." No daypart code names (Good Energy, Dosi, Luxx); refer to service periods by time of day. No financial figures; if one is needed, say financials aren't a source for this work. No performed conviction ("we believe," "our goal is"). No profanity. No retired marks (Recommended, Founder-gated, Chef-gated, Team-filled). No task titled "Ratify." Keep the old program's coined vocabulary out unless the white paper uses the term; define any useful term in plain words the first time.

## Scope of your writes

Write only inside your chunks' `manual/` folders. No ClickUp, no git, no other files.

## When you finish

Before replying, check your own output mechanically: grep your files for em dashes, "guest", retired marks, "Ratify", and daypart names; confirm every owned old-item ID appears in exactly one mapping; confirm every task number referenced anywhere is defined in some tasks.md or is another chunk's number.

Reply with: for each chunk, the task count by type and phase, and the mapping counts by fate; the cross-chunk dependencies you named; kits seeded; items you routed to other chunks (ID and target); and anything you were unsure how to handle.
