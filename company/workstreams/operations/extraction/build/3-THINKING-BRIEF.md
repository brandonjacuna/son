# Fable brief: the thinking files for one run

You write the three files that need judgment: `tasks.md`, `considerations.md`, and `session.md`, for each chunk in your run. Other models handle everything else (the book summaries, the old-item mapping, the templates). Don't write those.

## Read, in this order

1. `/Users/brandonacuna/Desktop/scaling-people:/CLAUDE.md` from disk. It governs; any older CLAUDE.md text in your context is the retired extraction program.
2. `extraction/build/<run>/run.json`: your chunks.
3. Each chunk's `manual/<section>-<slug>/book.md`: the book's guidance, already summarized. The verbatim pages are in `extraction/build/<run>/book.md` if you need exact wording.
4. `extraction/build/<run>/digest.md`: what the old extraction work holds that's worth keeping, plus every old item your run owns. The original page is `extraction/build/<run>/old-page.md`; open a section of it only when the digest isn't enough.
5. `extraction/s01/record.md`: the white paper, the only Sŏn context. Read it in full; don't guess where the relevant passage is. Cite it as "WP p. N".

Don't read the pilot chunk's files, the brand files, the profiles, or the archive. The formats you need are below.

## What to write, per chunk, in `manual/<section>-<slug>/`

**`tasks.md`**: every decision, action, and deliverable the section calls for, in work order, numbered `<section>.1`, `<section>.2`, and so on. Open with a two-line preamble. Each task in exactly this format (an example from chunk 2.1):

### 2.1.1 Read the operating agreement and note what it already settles
- Type: Action
- Phase: Before the first hire
- Book: pp. 71 to 72 (founding documents give every system a common purpose; they cannot contradict the legal instrument beneath them)
- Default assumption: None; the white paper is silent on the operating agreement
- Depends on: None
- Done when: a short note exists listing what the agreement holds on votes, deadlock, admission of a new principal, a principal's departure or incapacity, and ownership of domains, so the founding documents can defer to it by reference rather than restate or contradict it
- Replaces old items: 86akh3t62

Add `- Repeatable: yes. <who produces their own later>. Kit: <kit task number>` to repeatable deliverables. Every old item from the digest should end up served by some task in your run, or be clearly droppable (brand, machinery, duplicate). List the IDs a task replaces on its "Replaces old items" line.

**`considerations.md`**: per topic, in the book's order: what the white paper holds (cited, including where it's silent); considerations from the digest worth keeping; options, each with what it commits Sŏn to; and where Sŏn may diverge from the book. Proportionate: aim well under 5,000 words per chunk, less for short sections.

**`session.md`**: the working-session guide. Sections: 1. Orientation (what the chunk covers, upstream dependencies, who else must agree, why it sits where it does). 2. Agenda (conversations in a default order). 3. One brief per Decision task, and per deliverable or action that needs Brandon's input. An example brief from chunk 2.1:

### 2.1.2 Decide Sŏn's mission and the entity it belongs to

**The question:** what is the one sentence that says why this company exists, and is it the company's sentence or the restaurant's?

**Why it matters now:** the mission is the parent of the long-term goals (2.1.3), the principles (2.1.5), every charter (2.1.15), and the orientation every new person gets first (2.1.20, WP p. 18). Vague here and every metric in 2.2 has no parent. Rushed here and the sentence names the cuisine or the horizon before the founders have chosen to (cons. 2).

**Openers:**
- A line cook on their third week asks you at the pass why this place exists. What do you say in one breath?
- The white paper has five sentences that sound like a mission (cons. 2 lists them). Read them aloud. Which one do you actually say to people?
- Sideways: you have been telling the story to the build audience on camera for months. What line do they repeat back to you? Stripe's mission was a phrase people kept quoting until it was simply accepted (pp. 73 to 74).
- Is this a Korean company, or a company whose first restaurant is Korean? Say it both ways and notice which one you flinch at.
- Picture the morning the layer holds something that is not Sŏn. Does the sentence still read true?

**Narrowing questions:**
- Whose sentence is it: the parent company's or the restaurant's? If the company's, what sentence does Sŏn the restaurant hold beneath it?
- Is the cuisine in the company's sentence, one level down, or not written yet?
- Run the four tests on the candidate: uniquely specific, never fully achieved, never asserts the unproven (WP p. 36), not a description of the restaurant alone (WP p. 34). Which does it fail?
- Could a competitor described in the white paper (a portfolio group, a chef's restaurant) hold this sentence? If yes, it is not specific enough.

**What the book says:** a mission states why you exist; it must be descriptive (no other organization could hold it) and aspirational (unlikely ever to be fully achieved); every layer of the company holds a mission that ladders up (pp. 73 to 76).

**White-paper default:** the mission belongs to the company, whose asset is the connective layer, not the restaurant alone (WP p. 34, stated outright); Sŏn is the only brand the customer meets and the parent stays in the background (WP p. 36, stated outright). No default for the sentence itself: the white paper holds a thesis, not a mission (cons. 2).

**How others have handled it:** General practice, not Sŏn-specific.
- Stripe's mission was a phrase from an early About page that people kept quoting until it became the mission; she treats that as the normal path (pp. 73 to 74).
- Hospitality groups with a customer-facing brand and a background parent commonly keep the parent's purpose out of the customer's sight; the white paper's own peer example runs this way (WP p. 02).
- Missions that survive years tend to describe an effect on the world rather than the product: Microsoft's "a computer on every desk and in every home" is her example (pp. 74 to 75).

**Options:** (a) the company holds the mission, without the cuisine; the restaurant holds its own sentence beneath it, with the cuisine. Commits Sŏn to two sentences and a ladder, and keeps the company's sentence true when the layer holds more. (b) the company holds the mission and names the cuisine. Commits the company to Korean food across whatever it later holds. (c) Sŏn the restaurant holds the only mission for now; the company's is written when the layer holds a second thing. Commits Sŏn to reopening the sentence at the first expansion. Depth: cons. 2.

**Watch for:** a sentence that is really the thesis ("a restaurant is not a room that serves food"), which any reader of the argument could hold; a sentence that asserts the horizon; a sentence Brandon likes but has never said out loud to anyone.

**A finished answer:** one sentence, the entity named, the cuisine question answered either way, all four tests passed out loud, and Brandon can say the restaurant's sentence beneath it (or has parked that as an open item with a closer).

**Needs agreement from:** both seated founders.

Then: 4. Deliverables that follow (with a "Repeatable" note). 5. Kits this session seeds. 6. Parking lot (questions that belong to other chunks, by number).

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


## Writing rules

Plain English. Sentence case headings. No em dashes. "Customer," never "guest." No daypart code names (Good Energy, Dosi, Luxx); refer to service periods by time of day. No financial figures; if one is needed, say financials aren't a source for this work. No performed conviction ("we believe," "our goal is"). No profanity. No retired marks (Recommended, Founder-gated, Chef-gated, Team-filled). No task titled "Ratify." Keep the old program's coined vocabulary out unless the white paper uses the term; define any useful term in plain words the first time.


## When you finish

Grep your files for em dashes, "guest", retired marks, "Ratify", and daypart names, and fix any hits. Reply with, per chunk: the task count by type and phase; the cross-chunk dependencies you named; the kits seeded; the digest items you judged droppable, with the reason; and anything you were unsure about. Keep the reply short.
