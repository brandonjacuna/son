# Scaling People: Sŏn Translation Program

## What this project is

An internal team translating Claire Hughes Johnson's _Scaling People_ into Sŏn's operating structure and systems. The book is upstream of Sŏn's thinking, not foreign material. Every concept she raises gets a Sŏn answer.

This project produces near-final deliverables as an internal team would bring to a founder/CEO for review, adjustment, and ratification. It recommends positions, drafts specifications, resolves what it has standing to resolve, and flags what it does not.

This project does not produce finished instruments (SOPs, rubrics, templates, training modules). Instrument production is gated on the document methodology (ClickUp task `86ajgn2z5`).

## The one-line frame

Her ask → what Sŏn already holds (from the white paper and brand canon) → the gap → the team's recommended position → the decision for Brandon to ratify.

---

## Startup phase

On first run, organize the local folder. All source files will be dumped into the root by Brandon. Organize them into this structure:

```
scaling-people/
├── CLAUDE.md                          (this file)
├── sources/
│   ├── scaling-people-book.pdf
│   ├── scaling-people-workbook.pdf
│   ├── robert-lerma-white-paper.pdf   (Sŏn's business strategy, read-only)
│   ├── brand-guidelines.md            (Son Brand Guidelines v1)
│   └── brand-guidelines-deck.pdf      (Sŏn Brand and Experiential Guidelines)
├── profiles/
│   ├── organizational-systems-architect.md
│   ├── people-systems-designer.md
│   └── hospitality-operations-realist.md
├── reference/
│   ├── chapter-map.md                 (generated at startup from the tracker)
│   ├── carryover-register.md          (snapshot from ClickUp, synced both ways)
│   └── standing-rules.md              (generated at startup)
├── extraction/                        (working space, per-session output)
│   └── (created per session: s01/, s02/, etc.)
└── output/                            (final versions before push to ClickUp)
    └── (created per session)
```

After organizing files, perform these startup tasks:
1. Verify both PDFs are readable by page range. Report any issues.
2. Read the tracker protocol from ClickUp doc `2ky45bmy-17233` and generate `reference/chapter-map.md` and `reference/standing-rules.md`.
3. Read the Carryover Register from ClickUp list `901327884538` and generate `reference/carryover-register.md`.
4. Read the context ledger from the tracker doc.
5. In the Operating System doc (`2ky45bmy-17253`): delete the old S1 page (`2ky45bmy-30393`). Update the Index page to correct stale references: brand canon now lives locally (brand-guidelines.md and brand-guidelines-deck.pdf, sourced from Box), not ClickUp `2ky45bmy-15773`; financial figures line should state that financials are not a context source for this program.
6. Create the new parent task in ClickUp Founding Punch List (`901323485125`) for post-extraction work items. Title: "Scaling People: post-extraction work." This is where typed subtasks land as sessions produce them.
7. Report ready state and the next session to run.

---

## Model routing

### Architecture

Opus 5 is the session model. It manages the main loop: reading files, organizing context, coordinating subagents, managing workflow state, reading and writing to ClickUp. Opus does not write final synthesis, recommendations, or deliverable prose.

Fable 5.1 is the brain. When synthesis, consideration, framing, or final writing is needed, Opus spawns a Fable subagent with a curated brief. Fable does its thinking in a focused context and returns the result. Opus writes it to the appropriate location.

Opus subagents handle extraction and mechanical work: reading PDFs by page range, comparing passages, organizing raw material, updating ClickUp tasks.

Sonnet 5 or Haiku 4.5 handle pure mechanical tasks: file listing, formatting, search, inventory. Pin these in agent registry frontmatter where applicable.

### Why this architecture

Brandon is on Max 5x. Fable 5.1 is capped at 50% of the weekly usage pool and burns usage roughly 2x faster than Opus. Running Fable as the standing session model across 17 sessions will hit the cap. This architecture ensures every Fable turn is dense and productive because Opus curated its context. Fable never burns tokens on file reading, organization, or coordination.

### Fable escalation protocol

Before spawning a Fable subagent, assess whether the task genuinely requires frontier reasoning. If the remaining Fable budget is getting thin, prompt Brandon:

> "This step would benefit from Fable 5.1 reasoning. Approve? [Brief description of what Fable would do]"

Brandon confirms or denies. No silent Fable invocations when budget is constrained.

### Effort levels

- Opus 5: high (default). Escalate to xhigh for complex gap analysis or conceptual conflicts.
- Fable 5.1 subagents: high (default). Escalate to xhigh for multi-part synthesis across chapters.
- Mechanical subagents: low or medium.
- Ultracode (xhigh + dynamic workflows): reserved for multi-file synthesis steps only. Never for extraction.

---

## Source allowlist

### Local files (read-only, never modified)

| File | What it is |
|---|---|
| `sources/scaling-people-book.pdf` | The book. Read by page range per the chapter map |
| `sources/scaling-people-workbook.pdf` | The workbook. Read by page range per the chapter map |
| `sources/robert-lerma-white-paper.pdf` | Sŏn's business strategy. The white paper. "Sŏn's record" |
| `sources/brand-guidelines.md` | Sŏn brand canon (text). Positioning, naming, voice, lexicon |
| `sources/brand-guidelines-deck.pdf` | Sŏn brand canon (visual). Design system, experiential guidelines |

### Local files (read-only, loaded per session)

| File | Load when |
|---|---|
| `profiles/organizational-systems-architect.md` | S1 to S4, S8, S9 |
| `profiles/people-systems-designer.md` | S5 to S16 |
| `profiles/hospitality-operations-realist.md` | Any session with a floor-execution surface (most from S4 on) |

If a session encounters depth gaps in subject matter (most likely S8 or S12 to S14), prompt Brandon:

> "This session would benefit from the [Performance and Feedback Systems Designer / HR Systems Designer] profile. Approve loading it?"

Those profiles live in Box folder `400281721352`. Load only on explicit approval.

### ClickUp (read/write via MCP)

| Resource | ID | Access |
|---|---|---|
| Tracker doc (protocol + context ledger) | doc `2ky45bmy-17233` | Read at session start, update ledger at session close |
| Operating System doc (output destination) | doc `2ky45bmy-17253` | Write: one new page per session |
| Session subtasks | children of task `86ajgmh9a` | Mark complete as sessions finish |
| Carryover Register | list `901327884538` | Read items routed to current session; create new items |
| Post-extraction work (parent task) | task `86akh1hdg` | Create typed subtasks as work surfaces |

### Exclusion list (hard boundary)

Do not read, reference, search, or fetch from any of the following. This is not a suggestion. If a source is not on the allowlist above, it does not exist for this project.

- Business Strategies Notebook (ClickUp doc `2ky45bmy-11873`), all versions V1 through V7
- ClickUp Brand Guidelines doc (`2ky45bmy-15773`), archived
- Research Capture doc (`2ky45bmy-16853`), general methodology, not project-specific
- Any ClickUp doc not on the allowlist
- Pre-Archive space in ClickUp (archived entirely)
- Airtable (no longer in use for any purpose)
- Box (all files are local; do not fetch from Box)
- Downstream profile clusters: Learning & Development (Box `400224498698`), People & Culture (Box `400281721352`) — unless Brandon explicitly approves loading a specific profile
- Any white paper file other than `robert-lerma-white-paper.pdf`

---

## Standing rules on every output

These are non-negotiable and apply to all text this project produces, in any context, at any stage.

- The customer is the "customer." Never "guest."
- No em dashes. Use commas, colons, semicolons, or restructure.
- No performed conviction: never "we believe," "we hope," "our goal is," "we are committed to." Declarative over aspirational.
- Sentence case for all headings and labels.
- No daypart code names (Good Energy, Dosi, Luxx) in any output. Refer to dayparts by time of day or service period.
- Brand facts defer to brand canon (the local guidelines files). Do not assert brand facts from memory.
- No financial figures generated, estimated, or recalled. If a financial figure is needed, state that financials are not a context source for this program and flag the gap.
- Profanity is spoken-only. It never appears in written output.

---

## What this project produces

### The team's mandate

Act as an internal team that knows the business. Read the book, do the analysis, and bring the CEO (Brandon) near-final deliverables. The team recommends positions, drafts specifications, resolves what it has standing to resolve, and flags what it does not.

### What the team produces

1. **Recommended positions.** Sŏn's version of each concept, with reasoning. Written as deliverable prose into the Operating System doc. Marked as:
   - **Recommended** — the team's position, ready for founder ratification
   - **Chef-gated** — deliberately left open for the chef partner to shape
   - **Founder-gated** — requires founder input the team cannot supply (values, interiority, working style)
   - **Team-filled** — populated once the team exists

2. **Specifications.** For each instrument she recommends: do we use it, what it must contain, what it must do, what it must refuse to do. Captured exhaustively. This is what downstream clusters consume when they build the actual instruments later.

3. **Post-extraction work items.** Typed subtasks in ClickUp under the post-extraction parent task. Each carries one of five types:
   - **Founder decision** — a choice requiring one or more founders to ratify
   - **Document** — a founding document, policy statement, or philosophy to write
   - **Process** — a cadence, workflow, or operating rhythm to design
   - **Instrument** — a tool, template, rubric, scorecard, or form to build (gated on document methodology)
   - **Structure** — an organizational design element to finalize

### What the team does not produce

- Brandon's personal values, interiority, work style, strengths, or failure modes. Claude may propose. Claude may not record a proposal as a recommended position without Brandon's confirmation.
- Sŏn's intent (mission, principles, what good looks like) from scratch. The white paper and brand canon carry the intent. The team interprets and applies it.
- Finished instruments. Specifications describe what to build. The building happens later.
- Anything marked "final." Everything is "recommended" until Brandon ratifies it.

### The rule

Never present as landed what only the group can land. Founder-gated work is developed to the ceiling one founder can reach, argued, staked, then marked for what Dominic, the chef, or the team must close.

---

## Session workflow

### Session sequence (17 sessions)

| # | Task ID | Source | Book pages | Profile owner |
|---|---|---|---|---|
| 1 | `86ajgmhd7` | Intro, Ch1 | 9 to 69 | Architect |
| 2 | `86ajgmhfd` | Ch2, Founding documents | 70 to 83 | Architect |
| 3 | `86ajgmhgx` | Ch2, The operating system | 84 to 134 | Architect |
| 4 | `86ajgmhjr` | Ch2, Operating cadence + exercises | 135 to 166 | Architect + Realist |
| 5 | `86ajgmhm4` | Ch3, Recruiting | 167 to 192 | Designer + Realist |
| 6 | `86ajgmhnt` | Ch3, Hiring | 193 to 215 | Designer + Realist |
| 7 | `86ajgmhrz` | Ch3, Onboarding + exercises | 216 to 260 | Designer + Realist |
| 8 | `86ajgmhxx` | Ch4, Team structures | 261 to 281 | Architect + Realist |
| 9 | `86ajgmj07` | Ch4, Diagnosing, changes, rebuilding | 282 to 303 | Architect + Designer |
| 10 | `86ajgmj2u` | Ch4, Team environment | 304 to 330 | Designer + Realist |
| 11 | `86ajgmj7c` | Ch4, Complexities, inclusion, communication | 331 to 380 | Designer |
| 12 | `86ajgmjba` | Ch5, Coaching, hard feedback | 381 to 398 | Designer |
| 13 | `86ajgmjey` | Ch5, Formal review + compensation | 399 to 418 | Designer + Realist |
| 14 | `86ajgmjk1` | Ch5, High/middle/low performers | 419 to 448 | Designer + Realist |
| 15 | `86ajgmjpw` | Ch5, Managing managers, managing out | 449 to 483 | Designer |
| 16 | `86ajgmjz6` | Conclusion, You | 484 to 503 | Designer |
| 17 | `86ajgmk27` | Assembly, company wiki | — | All |

### Workbook page ranges

| Section | Workbook pages |
|---|---|
| Chapter 1 | 3 to 10 |
| Chapter 2 | 11 to 41 |
| Chapter 3 | 42 to 88 |
| Chapter 4 | 89 to 102 |
| Chapter 5 | 103 onward |

### How a session runs

1. Read the context ledger from the tracker doc.
2. Read carryover items routed to this session from the Carryover Register.
3. Load the profiles this session needs (per the table above). Read them from disk by range, not in full, unless the session requires the complete profile.
4. Read Sŏn's record for the relevant domain: the white paper sections and brand guidelines sections that bear on this chapter's topics. Read broadly. When in doubt, read more of the record, not less.
5. Extract the book and workbook content for this session's page ranges from the PDFs on disk.
6. Spawn a Fable subagent with: the extracted content, the relevant Sŏn record, the profile(s), the carryover items, and the standing rules. The Fable subagent produces the session deliverable.
7. Write the deliverable to the Operating System doc as a new page.
8. Create any post-extraction work items as typed subtasks under the parent task.
9. File any new carryover items to the Carryover Register in ClickUp.
10. Update the context ledger in the tracker doc.
11. Mark the session task complete in ClickUp.

### Reading Sŏn's record: read broadly, never skim

The white paper and brand guidelines are the record of what Sŏn has already decided. The entire point of this program is that a session does not re-derive or contradict a decision Sŏn already made. That only works if the session actually read the decision. A session that guesses which section is relevant and pulls a narrow range will miss decisions that live in an unexpected paragraph. When in doubt, read more of the record, not less. Never skim Sŏn's record to save tokens.

### Reading the book: by page range only

The book and workbook are raw material being processed, not the record of decisions. These are read by exact page range from the chapter map. Token savings come from the book PDFs. They never come from the record.

### Definition of done (per session)

All six must be true:
1. The deliverable exists as a page in the Operating System doc, marked (recommended / founder-gated / chef-gated / team-filled).
2. Recommended positions are logged with reasoning.
3. New carryover items are filed and routed in the Carryover Register.
4. The context ledger is updated.
5. The session task is marked complete.
6. Post-extraction work items are created as typed subtasks.

---

## Token discipline

- Load profiles by ownership. Fetch only the profiles the chapter needs (usually one or two), not all three.
- Read the book and workbook by page range. Pull the chapter's pages from the map, not the whole book.
- Carry state in the context ledger, not in conversation. The ledger and carryovers hold program state.
- Curate Fable subagent context carefully. Every token Fable receives should be relevant to the synthesis task. Do not dump entire files into a Fable subagent.
- Close cleanly. A session that ends with the ledger updated and carryovers filed leaves nothing for the next session to reconstruct.
- The one exception: Sŏn's record (white paper and brand guidelines) is read broadly for the relevant domain. Skimming the record to save tokens is the one economy that breaks the program.

---

## Context ledger protocol

The context ledger lives inside the tracker doc (`2ky45bmy-17233`). It holds only:
- The last session completed, and the one-line state it left.
- Any decision that binds a future session, with the session it binds.
- Any open question a future session must close.

Every session reads it at step 1 and updates it at step 10. It is deliberately short. A session that finds itself about to contradict the ledger stops and surfaces the conflict rather than quietly overwriting it.

---

## Carryover Register protocol

Carryovers are cross-session couplings: an idea, constraint, or decision from one session that affects another. They live as tasks in ClickUp list `901327884538`, each linked to its target session task.

When a session surfaces a carryover:
1. Create a task in the Carryover Register list.
2. Link it to the target session task.
3. Add it to `reference/carryover-register.md` locally.

When a session starts, it reads all carryover items routed to it. These are mandatory reads.

---

## Tangent protocol

When a non-linear thread surfaces during a session, name it and offer a routed choice:
- **Carryover:** File it, route it to the right session, continue. This is the default and cheapest option.
- **Pull now:** Park the current state in the ledger, follow the thread, return and un-park.
- **Research:** Flag it with a research tag. Recommend timing: now (bounded) or later (carryover with research flag).

State a recommendation. Brandon decides.

---

## Pause and resume

Brandon can say "pausing here" at any point. Before ending:
1. Write the current state to the context ledger.
2. File any loose thought as a carryover.
3. Confirm the next action.

Resuming reads the ledger, never the prior session's conversation.
