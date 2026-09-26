## ✅ Program live. Read this protocol before every session.

The team is built. The three profiles that run this program are on disk in `profiles/`. The program is ready to run from Session 1. This block is the operating protocol, and it is the only thing a session needs to read to start. Everything below it is reference.

**Reconciled 2026-09-11 against** **`CLAUDE.md`****, which is the governing document for this program.** The source allowlist changed: Sŏn's record is now the Robert Lerma white paper and the brand canon files, all held locally, and the V7 notebook, the archived ClickUp canon doc, Airtable, and Box are excluded outright. If this protocol ever disagrees with `CLAUDE.md`, `CLAUDE.md` wins.

## The frame, in one line

**Her ask → what Sŏn already holds (from the white paper and brand canon) → the gap → the team's recommended position → the decision for Brandon to ratify.**

The book is upstream of Sŏn, not foreign to it. It shaped eighteen months of Brandon's thinking, and Sŏn's own record already contains Sŏn's versions of much of what she teaches. Every concept she raises gets a Sŏn answer. Sometimes that answer is "we deliberately do not do this." That is still a decision. The three profiles already carry this frame; they will not re-derive what the record holds.

## How this program is driven: controller and sessions

Two kinds of chat, opposite jobs. Do not mix them.

**The controller.** A single chat whose only job is orchestration: hold the map, update this tracker, triage carryovers, spawn session prompts, decide sequencing, handle cleanup. It never runs a chapter. It never loads a book chapter or three profiles, so it stays light and coherent. It is the chat you plan from.

**A session.** A fresh chat that runs exactly one chapter's work, dense with that chapter's material, then is discarded. Everything a session decides persists in the Operating System doc, the carryovers, and the ledger, never in the chat.

The controller is a role, not one permanent conversation. Like a session, a controller chat degrades if it runs too long. Its durability lives in this tracker, not in the chat. When a controller chat gets heavy, start a fresh one and it reconstitutes itself in one step by reading this protocol block and the context ledger. **The controller is where you think and route. The tracker and ledger are where state persists.** The chat is always disposable; the record is the memory. This is true for both kinds of chat.

## The team that runs a session

Three profiles, on disk in `profiles/`. A session loads the ones its chapter needs. It does not load all three by default; it loads by ownership.

| Profile | File | Owns | Load for |
| ---| ---| ---| --- |
| Organizational Systems Architect | `profiles/organizational-systems-architect.md` | Her Ch1, Ch2; the progression structure | S1 to S4, S8, S9 |
| People Systems Designer | `profiles/people-systems-designer.md` | Her Ch3, Ch4, Ch5; psych safety as org theory | S5 to S16 |
| Hospitality Operations Realist | `profiles/hospitality-operations-realist.md` | Cross-cutting tempo test | Any session with a floor-execution surface. Most of them |

The Realist is cross-cutting by design. Load it whenever a decision has to survive a real service, which is most sessions from S4 on. The two owners are chapter-bound: the Architect for structure and the operating system, the Designer for people systems.

Two optional profiles exist for depth gaps, most likely at S8 or S12 to S14: Performance and Feedback Systems Designer, and HR Systems Designer. They live in the People & Culture cluster and are **not** loaded by default. A session that hits a depth gap prompts Brandon and loads one only on explicit approval.

Downstream clusters exist and are not loaded here. The Learning & Development cluster and the People & Culture cluster build the instruments and the employee-facing material later. This program produces the recommended positions and specifications they will consume. It does not build instruments. See "What a session produces."

## Cold-start protocol (a session)

New chat. Paste exactly:

> Sŏn. Scaling People, session \[N\]. ClickUp task \[ID\]. Begin.

The session then runs this sequence, in order, before any work:

1. **Fetch the session task** and read the brief.
2. **Fetch the carryover items linked to that task.** Mandatory reads. They are how a decision made three sessions ago reaches the session it affects.
3. **Read the context ledger below** (the running state of the program). The single most important anti-drift step. Short by design.
4. **Read the profiles the session's chapter needs** from `profiles/`, per the table above. By range, not in full, unless the session requires the complete profile.
5. **Read Sŏn's own record broadly for the relevant domain.** The white paper sections and brand guidelines sections that bear on this chapter's topics. See "Reading Sŏn's record" below; this is a correctness step, not a place to economize.
6. **Extract the stated page ranges** from the book and workbook on disk.
7. Work the session.

All sources are local files. Nothing is fetched from Box, and no connector returns whole-file text into context, which is what defeats the page-range discipline.

## Reading Sŏn's record: read broadly, never skim

This is the one place the program cannot be allowed to economize, and it is the opposite of how the book is read. State it plainly so no session gets it wrong.

**The white paper and the brand guidelines are the record of what Sŏn has already decided. They are load-bearing for correctness.** The entire point of this program is that a session does not re-derive or contradict a decision Sŏn already made. That only works if the session actually read the decision. A session that guesses which section is relevant and pulls a narrow range will miss decisions that live in an unexpected paragraph, and it will produce confident, wrong work. That is the exact failure this program exists to prevent.

So the rule is: **read the white paper sections and canon sections that bear on the chapter's topics, in full, top to bottom.** These files are not long. Reading broadly costs little and is the cheapest insurance in the program. If a session is unsure whether a second section is also relevant, it reads that one too. When in doubt, read more of the record, not less. Never skim Sŏn's own record to save tokens.

The book and the workbook are the raw material being processed, not the record of decisions, so those are read by exact page range from the verified chapter map. The savings come from the book PDFs and from not re-reading chats. They never come from the record.

## What a session produces

Three things, and not a fourth.

1. **Recommended positions.** Sŏn's version of each concept, with reasoning. Written as prose into the Sŏn Operating System doc (`2ky45bmy-17253`), one page per session. Declarative, standalone, wiki-ready. Marked **recommended**, **chef-gated**, **founder-gated**, or **team-filled**. Nothing is marked final. Everything is recommended until Brandon ratifies it.
2. **Specifications.** For each instrument she recommends: do we use it, what it must contain, what it must do, what it must refuse to do. Captured exhaustively. This is what the downstream clusters consume when they build the actual instruments later.
3. **Post-extraction work items.** Typed subtasks under the post-extraction parent task (`86akh1hdg`, Founding Punch List `901323485125`). Each carries exactly one type: **founder decision**, **document**, **process**, **instrument**, or **structure**.

Not a fourth: **no instruments.** No SOPs, worksheets, fillable templates, training modules, or finished rubrics. That is downstream, gated on the document methodology (`86ajgn2z5`). The reason is unchanged: building instruments before the methodology exists yields good thinking in inconsistent formats.

## Who supplies what

Claude never generates Brandon's interiority (values, work style, strengths, failure modes) or Sŏn's intent (mission, principles, what good looks like). Claude may propose. Claude may not record a proposal as a recommended position without Brandon's confirmation. Founder-gated work is developed to the ceiling one founder can reach, argued, staked, then marked for what Dominic, the chef, or the team must close. The rule: **never present as landed what only the group can land.** The three profiles enforce this on themselves.

## Anti-drift: the context ledger

Across 17 sessions the risk is not any single session going wrong. It is slow incoherence: session 9 quietly contradicting a decision from session 3, or re-opening something already closed. The defense is a single short running-state section, the **context ledger**, kept at the top of the decisions log below. It holds only:

*   The last session completed, and the one-line state it left.
*   Any decision that binds a future session, with the session it binds.
*   Any open question a future session must close.

Every session reads it at step 3 of cold-start, and updates it before closing. It is deliberately short, a page at most, so reading it costs almost nothing and it never becomes the thing nobody reads. The full decisions log below it is the archive; the ledger is the working memory. A session that finds itself about to contradict the ledger stops and surfaces the conflict rather than quietly overwriting it.

## Tangent protocol (the non-linear lane)

Brandon thinks in lanes, and a session will surface an idea that belongs elsewhere or opens a new thread. That is a feature, not a derailment, but it has to be caught cleanly or it costs mental clarity and muddies the chat. When it happens, the session does not silently follow the tangent and it does not silently drop it. It stops and offers a routed choice:

**First, name what the tangent is:**
*   **A decision that affects another session** → it becomes a carryover item, filed and routed to that session's task, and the current session continues. Zero clarity lost. This is the default and the cheapest.
*   **A thread worth pulling now, in this chat** → the session first parks the current state in the context ledger (so the main line is recoverable), then follows the thread, then returns and un-parks. The park is what protects clarity.
*   **A question needing research or a source Sŏn does not have** → the session offers two timings: _do it now_ (a bounded search, then back to the session) or _come back to it later_ (filed as a carryover with a research flag). It recommends which, based on whether the answer blocks the current decision.

**The session always states its recommendation** ("this is a carryover, keep going" / "this is worth ten minutes now, let me park us first" / "this needs a source, and it can wait"), and Brandon decides. The point is that the non-linear move is always caught, always routed, and never held loose in a chat where it degrades.

## Pause and resume (weeks, not one sitting)

This program runs over weeks, not in one sitting. Stopping is a first-class action, not an interruption. At any point Brandon can say **"pausing here"** and the session will, before ending:

1. Write the current state to the context ledger, including exactly what was mid-flight.
2. File any loose thought as a carryover so nothing lives only in the chat.
3. Confirm what the next action is, so resuming is a single clean prompt.

Resuming never requires re-reading the chat. It requires reading the ledger. That is the whole point of the ledger: the chat is disposable, the ledger is the memory. A session can be abandoned mid-stream and picked up a week later from the ledger with nothing lost.

## Token discipline

The context window is a resource, and this protocol spends it well without changing models. The discipline applies to disposable material, never to Sŏn's record.

*   **Load profiles by ownership.** Read only the profiles the chapter needs (usually one or two), not all three, and never the downstream clusters.
*   **Read the book and workbook by page range.** The PDFs are on disk for exactly this. Pull the chapter's pages from the verified map, not the whole book.
*   **Carry state in the ledger, not the chat.** Never re-read a prior session's chat to get context. The ledger and the carryovers hold it. Cheaper and more reliable.
*   **One session per chat.** Long chats degrade and waste context re-establishing state. A fresh chat reads the ledger to orient.
*   **Close cleanly.** A session that ends with the ledger updated and carryovers filed leaves nothing for the next chat to reconstruct.

**The one exception, stated so it is never violated:** Sŏn's own record (the white paper and brand canon) is read broadly for the relevant domain, never by a guessed range. Skimming the record to save tokens is the one economy that breaks the program. See "Reading Sŏn's record" above.

## Model routing

Opus 5 is the session model. It manages the main loop: reading files, organizing context, coordinating subagents, managing workflow state, reading and writing to ClickUp. Opus does not write final synthesis, recommendations, or deliverable prose.

Fable 5.1 is the brain. When synthesis, consideration, framing, or final writing is needed, Opus spawns a Fable subagent with a curated brief. Fable does its thinking in a focused context and returns the result. Opus writes it to the appropriate location. Fable never burns tokens on file reading, organization, or coordination.

Opus subagents handle extraction and mechanical work. Sonnet 5 or Haiku 4.5 handle pure mechanical tasks: file listing, formatting, search, inventory.

Before spawning a Fable subagent, assess whether the task genuinely requires frontier reasoning. If the remaining Fable budget is thin, prompt Brandon and wait for approval. No silent Fable invocations when budget is constrained.

**A subagent note from Session 3.** Subagent ClickUp access is not reliable, and the failure is not consistent. In Session 3 one subagent reported that the ClickUp server required an authorization it could not complete and created nothing, while a second subagent spawned at the same moment with the same tools wrote a large doc page successfully; a third, spawned later, failed the same way as the first. Treat subagent ClickUp access as something to test rather than assume. A subagent given ClickUp work reports exactly what it wrote, and the session verifies the result against the local source before closing. Bulk task creation is safest done by the session itself.

**A verification note from Session 3.** A large page written to a ClickUp doc is verified by fetching it back and diffing it against the local source with shell tools, never by eye and never on a subagent's own report. Fetching a page of this size returns a result too large for context, and the harness saves it to a file; extract the content with `jq` or python and compare line counts, heading lists, and anchor strings. ClickUp's markdown serializer rewrites styling on read-back: periods and square brackets are escaped, `*italic*` becomes `_italic_`, `-` bullets become `*` , `---` becomes `* * *`, and table cells are padded. Normalize those before comparing; they are not content changes.

## Definition of done

A session is not closed until all six are true:

1. The Sŏn artifact exists as a page in `2ky45bmy-17253`, marked recommended, chef-gated, founder-gated, or team-filled. Recommended positions and specifications, not an instrument.
2. Recommended positions are logged, with reasoning.
3. New carryover items are filed and routed in the Carryover Register (`901327884538`).
4. **The context ledger is updated.**
5. The session task is marked complete.
6. Post-extraction work items are created as typed subtasks under `86akh1hdg`.

## Disposition of the first Session 1

The old S1 page in the Operating System doc (`2ky45bmy-17253`, page `2ky45bmy-30393`) is superseded. Its content was removed on 2026-09-11 and the empty page has since been deleted. Four findings from it carry forward as **inputs**, not settled decisions, and they are already baked into the three profiles:

*   Sŏn compounds without headcount growth; her apparatus assumes otherwise.
*   Two metronomes; only the build metronome takes her "faster than comfortable" advice.
*   Analyzer scarcity across dayparts; service pressure selects for Directors and Promoters.
*   Sŏn has a compensation structure but no compensation philosophy.

The old S1 decision moving the working-with-me exchange before the chef signs is un-made. It was not a call the session had standing to make.

**Superseded by the rerun, 2026-09-11.** The rerun is page `2ky45bmy-31653`. The four findings above were carried into it as inputs and argued; none was restated as settled.

## First action

Run Session 10. New chat:

> Sŏn. Scaling People, session 10. ClickUp task `86ajgmj2u`. Begin.

Session 9 is complete and its page is in the Operating System doc. Session 10 reads the ledger below before anything else. It is Chapter 4, team environment, owned by the People Systems Designer with the Realist at the table. Its inbound constraints from Session 9: team state is read by the diagnostic and never by a survey, and the offsite has no diagnostic role.

* * *

## What this is

A methodical translation of Claire Hughes Johnson's _Scaling People_ into Sŏn's own operating structure and systems. The book is a guide. She wrote for a payments company scaling from 200 to 7,000 knowledge workers. Sŏn is a 120-seat restaurant at 207 E St. Elmo Rd running four dayparts, opening January 2027, compensating on an embedded revenue share rather than tips.

**Space:** Founding Sŏn `90138396180`
**Parent task:** `86ajgmh9a`, Founding Punch List `901323485125`
**Output:** Sŏn Operating System, `2ky45bmy-17253`
**Carryover Register:** `901327884538`
**Post-extraction work:** `86akh1hdg`

## Sources

All sources are local, read-only files. Nothing is fetched from Box or any ClickUp doc outside the allowlist.

| File | What it is |
| ---| --- |
| `sources/scaling-people-book.pdf` | The book, 531 pages. Read by page range |
| `sources/scaling-people-workbook.pdf` | The workbook, 125 pages. Read by page range |
| `sources/robert-lerma-white-paper.pdf` | Sŏn's business strategy, 39 pages. The record |
| `sources/brand-guidelines.md` | Brand canon, text. Positioning, naming, voice, lexicon |
| `sources/brand-guidelines-deck.pdf` | Brand canon, visual, 94 pages. Design system, experiential guidelines |

Page addressing is verified: book and workbook page ranges are PDF page numbers with **zero offset**. Read them as written.

**Workbook structure:**

| Section | Workbook pages |
| ---| --- |
| Chapter 1 | 3 to 10 |
| Chapter 2 | 11 to 41 |
| Chapter 3 | 42 to 88 |
| Chapter 4 | 89 to 102 |
| Chapter 5 | 103 to 125 |

Chapter 2's workbook range is now fully consumed: Session 2 took pages 11 to 22, Session 3 took pages 23 to 41. Session 4 takes its exercise material from the book's own appendix at pages 144 to 166.

## Book chapter map

| Chapter | Pages |
| ---| --- |
| Introduction | 9 to 33 |
| 1\. Essential Operating Principles | 34 to 69 |
| 2\. Foundations and Planning | 70 to 166 |
| 3\. A Comprehensive Hiring Approach | 167 to 260 |
| 4\. Intentional Team Development | 261 to 380 |
| 5\. Feedback and Performance Mechanisms | 381 to 483 |
| Conclusion: You | 484 to 503 |

## Session sequence

Briefs are being rewritten to the frame as each session runs. The profile that owns each session is noted; the Realist joins wherever a floor-execution surface is present.

| # | Task ID | Source | Book pp | Owner |
| ---| ---| ---| ---| --- |
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
| 17 | `86ajgmk27` | Assembly, company wiki. Gated on `86ajgn2z5`. |  | All |

## Carryover Register, open items

Live in the Carryover Register list (`901327884538`). Each links to its target session task. Retriaged against the built profiles; several first-pass items are absorbed into the profiles themselves (the profiles carry the four findings, the seam definitions, the standing rules).

| Item | Task ID | Routed to | State |
| ---| ---| ---| --- |
| Founder job descriptions do not exist | `86ajgnhp7` | S2 | Live |
| Code-bearing vs her hierarchy | `86ajgmm5h` | S3 | Live |
| The 1:1 has no shift-native form | `86ajgnhv9` | S4, S12 | Live |
| Work style demand differs by daypart | `86ajgnhh3` | S5, S6, S8 | Live |
| Working-with-me is pre-signature diligence | `86ajgnj8t` | S7 | Live |
| Chef-gated BOH; four dayparts is not four teams | `86ajgmmc3` | S8 | Live |
| Levels and ladders: does a single house need them | `86ajgnj4e` | S8, S13 | Live |
| Playground philosophy: mechanisms or slogan | `86ajgmmfq` | S10 | Live |
| Compensation philosophy does not exist | `86ajgnhd1` | S13 | Live |
| Scorecard and review rubric are one instrument | `86ajgmmkd` | S13 | Live |
| The steady middle is underweighted | `86ajgmmpg` | S14 | Live |
| Texas/FLSA exposure on embedded comp | `86ajgnhzk` | Counsel | Parked |
| Specifications not instruments; both PDFs every session; no-scale-to-7000; Claude never generates interiority; tech stack already selected | `86ajgn3ep`, `86ajgmxnp`, `86ajgnh8n`, `86ajgnpef`, `86ajgmm86` | All | Absorbed into profiles + protocol |

**Filed by Session 1 rerun, 2026-09-11.** Five items.

| Item | Task ID | Routed to |
| ---| ---| --- |
| The record holds two accounts of the chef seat | `86akh2qnt` | S2 |
| The founder decision-rights rule does not exist | `86akh2qt2` | S2, S3 |
| The founder cadence does not exist | `86akh2qwp` | S4 |
| The nervous system does not read the center | `86akh2qzy` | S16 |
| The room-owning role is named differently in the two halves of the record | `86akh2r3e` | S8 |

**Filed by Session 2, 2026-09-11.** Twelve items, all live.

| Item | Task ID | Routed to |
| ---| ---| --- |
| Canon-charter seam governs how the operating system cites authority | `86akh3ub0` | S3 |
| Decision-rights entries take owner, range, triggers form | `86akh3uez` | S3 |
| Long-term commitments parent every metric; leading indicators only | `86akh3uhy` | S3, S4 |
| Principles version one is pre-opening, with a revision cadence | `86akh3unw` | S4 |
| The daypart charter is the opening gate and the lunch decision's form | `86akh3uxu` | S4, S8 |
| The chef seat ruling gates third-seat recruitment | `86akh3vbd` | S5, S6 |
| Compensation commitments in recruiting; architecture waits for S13 | `86akh3vrq` | S5, S6, S13 |
| Onboarding delivers mission, principles, and standard first | `86akh3w9a` | S7 |
| Cross-strand fluency: S8 defines it, S13 prices it | `86akh3wjw` | S8, S13 |
| The principles are what feedback and review reference | `86akh3wxv` | S12, S13 |
| Founding seat descriptions exclude interiority; S16 carries it | `86akh3x9m` | S16 |
| The charter's design rules apply to every document S17 assembles | `86akh3xe0` | S17 |

**Filed by Session 3, 2026-09-11.** Fifteen items, all live. Forty-three live items now. Every session from S4 through S17 carries at least one; S9, S11, and S15, which carried none after Session 2, each carry one now.

| Item | Task ID | Routed to |
| ---| ---| --- |
| The cadence rows of the readiness test | `86akh5uqx` | S4 |
| The mechanism set and the frequency mapping | `86akh5ur9` | S4 |
| The operating system runs on ratified daypart charters; the period count is a parameter | `86akh5urn` | S4, S8 |
| "Direct lead" means domain lead, and the range travels with the offer | `86akh5ut1` | S5, S6, S7 |
| The floor manager and the Maitre d: one role or two | `86akh5utd` | S8 |
| Interfaces are counted in service periods; the leadership-line list is needed for the variety test | `86akh5utm` | S8 |
| The five failure modes are the house review's standing scorecard | `86akh5uuz` | S9 |
| A goal met at a bandwidth cost is a system failure | `86akh5uw3` | S10, S14 |
| Internal communications: three channels, non-co-presence, the transparency line | `86akh5uw8` | S11 |
| The shift close is the feedback system's first source | `86akh5uwq` | S12, S13 |
| No lagging indicator drives compensation | `86akh5ux8` | S13 |
| Zero targets and protocol breaches as performance events | `86akh5uxm` | S14 |
| Who reviews the leads, and lead-to-lead disagreement | `86akh5uy1` | S15 |
| Brandon's seat owns the operating system; the absence rule | `86akh5uy9` | S16 |
| The team home is the wiki's staff-facing face; the vocabulary line is an audit rule | `86akh5uym` | S17 |

**Filed by Session 4, 2026-09-11.** Twelve items, all live. Fifty-five live items now, one routed to every session from S6 through S17. S5 receives none, because the cadence work did not touch recruiting.

| Item | Task ID | Routed to |
| ---| ---| --- |
| Hiring timeline must produce six consecutive leads' reviews before dinner's gate | `86akh67gj` | S6 |
| The check-in inside the ninety-day plan | `86akh67ny` | S7 |
| Provided and dependent interfaces are the seam between service periods | `86akh67tt` | S8 |
| The mechanism reset and the five failure modes scorecard | `86akh67wy` | S9 |
| The brief's team-making content and the whole-house gathering's content | `86akh67xe` | S10 |
| Every cadence artifact runs through the three channels | `86akh67xk` | S11 |
| The check-in is the coaching surface | `86akh67y5` | S12 |
| The review rhythm, the no-surprises evidence base, and the payment rhythm | `86akh67yb` | S13 |
| The check-in record and the moved-check-in triggers | `86akh67yy` | S14 |
| The lead-and-partner monthly conversation | `86akh680c` | S15 |
| The working-with-me documents are the founder cadence's input | `86akh6813` | S16 |
| The mechanism map is the wiki's cadence page | `86akh681a` | S17 |

## Standing rules on every output

The customer is the "customer," never "guest." No em dashes. No performed conviction: never "we believe," "we hope," "our goal is," "we are committed to." Declarative over aspirational. Sentence case for all headings and labels. No daypart code names; refer to dayparts by time of day or service period. Brand facts defer to brand canon, the local guidelines files; never assert a brand fact from memory. No financial figures generated, estimated, or recalled; financials are not a context source for this program, and where a figure is needed the gap is stated and flagged. Profanity is spoken-only and never appears in written output.

## Decisions log

### Context ledger (working memory: read first, update last)

**Last session completed:** Session 9, 2026-09-14. Chapter 4, Diagnosing team state, team changes and restructuring, (re)building the team, and the workbook's career conversations.

**State:** S9 built the instrument and not the diagnosis, as the session task directed: Sŏn has no team to diagnose, so the page specifies the team-state diagnostic and runs no read. The diagnostic is the record's failure mode reference (WP p.14) assembled into one instrument from what Sessions 3 to 8 built around it, and her chapter is consumed by it rather than replacing it. Every read names one of five objects (the house, the domain, the service roster, the seat, the service period; the last two are not teams), then a mode from a source on a record, then the mechanism the record's fix touches, and reaches a person only for tension slack, last, by one path that hands to S12 and through it to S14 and never to S15. Its unit is a seven-field evidence line (mode, object, source, count, compensation, fix and mechanism, state) that names no person and carries no figure, fed weekly at the leads' review, read quarterly at the house review, corrected at the mechanism reset, and checked at each gate, adding no meeting. Recurrence thresholds are counts of reviews and services. A diagnosis becomes care (logged) or correction (versioned) by four paths, with the line as the change's reason verbatim and a read-back by the source that raised it. Inside dinner's first-quarter freeze the diagnostic reads everything and changes nothing on the room's map; a pre-opening first run records what it can and cannot read. The reset's first read is the Maitre d's seat, its load carried by a designation, the stack, or a procedure, with the refused carriers listed under Brandon's ruling. Her reorganizations, DRIs, delegation framework, skill-will matrix, survey, and Lencioni frame are refused or absorbed; delegation lands on the decision-rights register; a departure is read in three passes and the brief carries coverage only. The career conversation is placed once, after the plan closes and before the first review. Fifty-one positions: forty-four recommended, two founder-gated, two chef-gated, three team-filled. Readiness rows 107 to 118, so the test stands at one hundred eighteen. Eighteen instrument specifications, nine used and nine refused. Thirteen findings inside the record, three of which would surface from a narrow read of WP pp. 13 to 14 and ten of which would not. Page `2ky45bmy-31833`.

**Decisions binding a future session:**

*   **The diagnostic is the failure mode reference, and the mode is named before any person is read. Binds S12, S13, S14, S15, S17.** Every read names its object (house, domain, service roster, seat, service period), then the mode from a source on a record, then the mechanism the record's fix touches. The order is enforced by the evidence line's form, which names no person, carries no verdict, no dimension, and no figure, and adds nothing to the four scorecard dimensions. S9 names this as the one thing on its page a later session cannot revise at ordinary cost: a later session may add sources, change thresholds, and design what S12 to S15 do with a hand-off, and may not let a read open at a person, write a person's name on a line, or add a dimension by way of the diagnostic. S9 P1, P3, P4, P8, P42.
*   **The evidence line is the reason field of every change, verbatim, and every change is read back. Binds every session that proposes a change, S11, and S17.** A diagnosis produces care (a process update from a capture, logged) or correction (a mechanism, a designation's rule, a seat, a line, or a period, versioned) by four paths: a mechanism through the leads' review and the reset; a designation's rule through a structure change entry; a seat through S8's path whole; a line or a period through the variety pass at a gate. A change with no line or with a person as its reason is refused; the next scorecard reads it back as cleared, not cleared, or cannot read. S9 P24, P25, P26.
*   **The diagnostic runs on four rhythms that exist and adds no meeting. Binds S10, S11, S17.** The leads' review's items 2 and 6 are the weekly feeders, the house review's scorecard section is the quarterly read, the mechanism reset is the correction, and the gate review's failed rows are the gate's line. S9 P20.
*   **Recurrence thresholds are counts of reviews and services, never money. Binds S12 to S15 and S17.** Three consecutive leads' reviews on the same object go to the partners' review; two consecutive quarterly lines after a fix go to the reset; a designation held by one person every service for a quarter is a question at the reset about the Maitre d's seat's hours and the designation's rule, never a second seat and never a read of the holder. A domain that repeats is read in three questions (count, sheet, lead's load) before any hiring question. The thresholds are reset parameters. S9 P17, P18, P19, P32.
*   **A diagnostic read reaches a person by one path, for tension slack only. Binds S12, S14, S15.** The seat and adjacent seats named, the domain fix made and read back, the person's own check-in line as the only person-side source, one permitted dated statement after recurrence, then S12, only through S12 to S14, and never to S15. No evidence line, scorecard, or reset record may be cited in a managing-out decision. The skill-will matrix is refused as a read of anyone. S9 P40, P41, P42.
*   **Inside dinner's first-quarter freeze the diagnostic reads everything and changes nothing on the room's mechanism map. Binds S10 and S17.** Lines that would change a frozen mechanism are held on the partners' page for the first reset with their dates. S9 P21.
*   **The reset's first read is the Maitre d's seat, and its carriers are listed. Binds S15, S16, S17.** From nine inputs on the stack and the records. A load finding is carried by a designation, the stack, or a procedure; a second floor seat, a floor manager under any name, an assistant of any title, a permanent room holder, and a service manager are refused carriers. S9 P36, under Brandon's ruling of 2026-09-13.
*   **A departure is read in three passes, and the brief carries coverage only. Binds S11 and S15.** The tension-loss row, the leads' review line, the pool, and the adjacent seats' lines; then whether what the node held was in the system; then the read-back at re-fill. The floor hears which seat is open and who holds its functions this service, and nothing about the person; this reads S3 P11.6, S7 P47, and S8 P49 as one rule, the practice S11's. A lead seat's departure adds a structure change entry with the departure's line as reason. S9 P30.
*   **Delegation lands on the decision-rights register, and DRIs are refused. Binds S12 and S14.** The job is carried by the seat sheet and range card, a one-off by a process change with an owner or a designation, and no task is handed down at a check-in or a brief. S9 P38, P39.
*   **The career conversation is held once, and adds nothing the person has not heard. Binds S10, S12, S13.** In the month after the ninety-day plan closes and before the first review, placed by the stack, paid as shift, between the person and the domain lead, opening on the person page's path line, the sheet's horizons, the tracks, and the fluency record. It writes one track and what the building must supply in the person's words, and refuses levels, titles, ranks, seat promises, pay, the person's history before the house, and any use in placement or delegation. Its length, thirty minutes, is a reset parameter. A lead's waits on `86akhb2jg`; the kitchen's is chef-gated. S9 P43, P44, P45.
*   **The readiness test stands at one hundred eighteen rows. Binds every session from here.** Rows 107 to 118 from S9; rows from S10 start at 119. Rows 111 and 112 are read at the first-reset review, and row 118 fails until `86akhb2jg` closes. S9 section 17.
*   **The floor manager and the Maitre d are one seat, by Brandon's ruling of 2026-09-13, and the room is never held by a second seat. Binds every session from here.** The Maitre d holds the room and the floor team. On services the seat's holder does not work, the room's live functions are held by a room designation named at the brief, and the threshold and the floor side of the pass by the door and sequence designations; each lasts one service. A load finding on the seat is carried by a designation, the stack, or a procedure, never by reinstating a floor manager under another name. Canon still names a floor manager until its owner versions it (`86akh3tjb`). S8 names this as the one thing on its page a later session cannot revise at ordinary cost. S8 section 2, P4, P25.
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
*   **Service-ready is defined once, and the readiness form reads the practical's rows. Binds S8, S13, S14, and S17 above everything else on the S7 page.** A person is service-ready when a readiness form reads ready at the seat sheet's field 6 entry horizon, per seat and per period, and nothing beyond it. The form (I7) uses the same rows as S6's paid practical (I4) plus language, range, and felt-knowledge rows, is scored by an assessor who is not the mentor, is a milestone and never a scorecard, and travels to no review. A candidate and a new hire are read against one list. S7 names this, with the next entry, as the two things on its page a later session cannot revise at ordinary cost. S7 P23, P24, I7.
*   **Nothing is written on a person page during the ninety-day plan but states and the person's own words. Binds S12, S13, S14, S15.** The plan block (I2) holds one goal as a state, milestones as states with dates, the baseline the candidate gave at the first interview, and the six check-in dates, one read per check-in. It refuses dimension marks, ratings, free text about the person, and any probation label. The plan's close is a state, not a review or a verdict. The plan extends once, for a building fix, and never for a person's not holding; a plan not held after one extension is handed to S14 with its record. S7 sections 7.1 to 7.6, P25 to P29.
*   **Nothing is required of a person before their first paid hour. Binds every session.** No module assigned or due before the start date, no pre-arrival reading required; information delivered before arrival is available, not owed. The first shift is a paid orientation block with no table and no station. S7 P15, row 87.
*   **The why block is empty until the charter is ratified. Binds S17 and the founders.** Onboarding delivers mission, principles, and behavioral standard before operational training, in that order, drawn from the charter. The charter is unratified, so the record's own onboarding commitment is unmet and the charter is the blocking dependency. The team recommends charter ratification as a condition of every cohort start date, surfaced as an extension to S5 12.6 and not made. S7 P12, P16.
*   **Operational onboarding runs on S6's training sequence. Binds S12 and S13.** Modules read, live session, observed service, paired services, readiness read, then solo, all on scheduled shift, with two stated differences from S6 P38. No cohort member's first solo is dinner's first service. S7 P10, P18, P23.
*   **The mentor is paid as shift, never scores, never writes on the person page, and comes from a pool. Binds S8, S10, S13.** The pool's five conditions sit beneath S5 P16 as the source of the name recruiting writes. The first wave's mentors are the leads, with provisional marks converted at the mechanism reset. Mentoring, module authorship, and completion pay are S13's, with three constraints. S7 P8, P41, P42, P35.
*   **No synthesized presenter in any module until canon rules. Binds S11 and S17.** Carryover `86ajgmm86` says build into the bought stack; S7 holds Synthesia against canon's prohibition on AI-generated imagery and says so as the one place it does not follow the carryover. S7 P32, finding 19.12.
*   **Cross-domain assessment waits until the person's own plan closes; the own-seat unlock is never held by the plan. Binds S8 and S13.** Tracks are visible from day one. Who signs a cross-domain competency is founder-gated, the receiving lead recommended. S7 P39, P40.
*   **Working-with-me exists for every lead, written between the fourth and sixth check-ins, and never for an hourly seat. Binds S15 and S16.** The chef partner's exchange stands as S1 decided, before the chef signs. S7 P49, P53; the work style grid lives only inside the working-with-me document, and team use is S10's.
*   **A change of domain lead is carried by the person page, not a transition meeting. Binds S15.** S7 P51.
*   **A new period is a module set and a register block, not a second ninety-day plan. Binds S8.** A person already in the house who takes a seat in a new period runs the shorter period plan. S7 P3, P30.
*   **The readiness test stands at ninety-two rows. Binds every session from here.** Rows 75 to 92 from S7. Rows 76, 81, 82, 86, and 88 carry a hold written inside the row and are read as failed at the gate review until it closes. S7 section 17.
*   **The four scorecard dimensions, and Session 13 scores against the same ones. Binds S13 above everything else on the S6 page.** Competency for the seat; self-directed mastery, read in role from the invisible advocate's own record; conduct under the non-negotiables and inside the range; and what the building supplies, scored on the building rather than the person. Nothing is added at review that was not read at hiring. Cross-strand and cross-period fluency are markers to be priced, not dimensions. S6 names this as the one thing on its page a later session cannot revise at ordinary cost, and finding 18.1 is the record's own version of the same seam left open: hiring names three things at WP p.18, review names two others at p.19, and the record never says they are one list. S6 sections 6.2 and 18.1, P33 and P36.
*   **The interview adds nothing to S5's structure, and the anchors carry the rules. Binds S7 and S13.** Eight rules run the question set: every question asked of every candidate in order; at least one situational, one behavioral, and where possible one strict-competency question per read; STAR-shaped probes with "what did you hold" always asked; principles worked in unnamed; anchors written at entry level in any domain; three anchor levels and not four; no presence word in any anchor at any level; the candidate's vocabulary unscored. Questions are public on the sheet; anchors are not. S6 sections 4.1 and 4.2, P17.
*   **Five extensions to Session 5, each surfaced rather than overwritten, each ratified alongside the position it extends. Binds S13 and S17.** P45 adds a mirror trigger for a hire made against a "does not meet." P54 adds a reference note to S5's I14 packet for lead, domain-owner, and Branch B chef seats. P49 adds a count-filled answer to S5's I15. P39 reads S5 I21's refusal of a hand-written training record as applying only once the stack can write one. P46 surfaces S5 P54 as the one position her chapter's function argues against and does not change it. The packet also gains the shadow form, the paired scorecard, and the dissent line. Nothing on the S6 page assumes any of these were ratified. S6 section 19.
*   **The hiring calendar is gates, and three of them are upstream of any hire. Binds S7 and S8.** The chef chain runs with no link skippable; the two leads are in the building at least six weeks before dinner's gate against rows 21 and 56; the compensation architecture's ratification sits on the critical path rather than on a parallel track. A practical is never scheduled to make a start date. S6 section 3.9, P15.
*   **No seat class produces a one-scorecard packet, so no runner was added. Binds S8.** A future seat class that would needs a runner named before it opens. S6 P9.
*   **Role definition lives in recruiting, and the seat sheet is the single account of a seat. Binds S6, S7, S8.** Her recruiting section, not her hiring section, carries role definition and builds the candidate assessment rubric; her hiring section consumes it. Sŏn's form is the seat sheet: sixteen fields, none blank, no seat opened without one, and it is the same document as the documented competency requirements the invisible advocate reads for the next unlock. One account of each seat, read by the candidate, the advocate, and the rubric. S5 sections 4.1 to 4.3.
*   **The rubric's structure is fixed and Session 6 fills it. Binds S6.** S5 set the stages by seat class, the four reads assigned per stage, the must-haves and disqualifiers, who may run each stage and who may not, and the rule that a scorecard carries no free-text verdict. S6 writes the questions, the answer anchors, the interviewer training, and the calibration. S6 adds no read, no stage, no runner, and no verdict column, and opens no rubric for a seat with no sheet. S5 section 14, I7.
*   **Recruiting selects for four reads, and never for nunchi or Jeong. Binds S6 and S14.** The four reads are competency for the strand at entry level, growth potential as self-directed mastery, cultural alignment as the non-negotiables and comfort with distributed authority, and what the building must supply for this person to succeed. Nunchi and Jeong are developed through mastery and accumulated through time; neither is ever a scored attribute. Her work style grid is out of recruiting entirely and may return only as a self-awareness tool in onboarding or team development. S5 sections 3.1, 3.2, 3.4.
*   **No hiring committee, no hiring meeting, and no recruiting seat. Binds S6 and S8.** The decision is the domain lead's on a complete packet of independently submitted scorecards, made the day the packet completes, with the answer sent the same day. No assessor decides and no decider assesses alone. A hole is held rather than filled below the bar. Coordination is the stack's, the candidate-experience standard is the Maitre d's, the record is the Operations Lead's. S5 sections 8.6 and 9.1.

*   **The transparency sheet is held whole, extended by two items, and item 6 gates every offer. Binds S6, S7, S13.** The record's sheet is decided, not re-derived. S5 added the decision-rights range the seat carries and the non-negotiables. No offer is made and no start date committed on a sheet whose compensation mechanics field is unfilled, which puts the compensation architecture on the hiring timeline's critical path. "Direct lead" means domain lead, named by seat. S5 sections 7.3 and 7.4.
*   **Her funnel survives as measurement only. Binds every later session that reads recruiting.** The pipeline is a pipeline of people the house has answered, not leads to convert. An open seat is a load reading on a domain, and a departure is a tension re-establishment rather than a slot vacancy. New people always enter at the outside edge; the web never acquires altitude. S5 sections 2.1 to 2.3.
*   **Her one-third promotion rule does not apply, and succession is a mechanism with a leading measure. Binds S8, S14, S15.** The rule was written for a company scaling past hundreds. The record's stated goal is that the building rarely hires a lead from outside at all. Internal promotion rate is the leading measure, the pool is read before anyone looks outside, and the commitment starts binding once the cohort has a first unlock behind it. S5 sections 11.1 to 11.3.
*   **The readiness test stands at fifty-nine rows. Binds every session from here.** Rows 1 to 20 from S3, 21 to 35 from S4, 36 to 59 from S5. Five of the recruiting rows carry a founder-gated hold written inside the row and are read as failed at the gate review, never waived; the gate does not open around them. The kitchen's rows are held whole on the chef ruling. S5 section 13.
*   **The chef ruling gates the kitchen chain, and the hiring timeline places the chef first. Binds S6 and S8.** Under either branch the kitchen pipeline runs as a chain with no link skippable: ruling, chef seated, canon's Session 1B, menu, kitchen seat sheets, kitchen practicals, kitchen hires, their training, dinner's gate. Until the chef is seated and the menu exists there is nothing for a kitchen practical to reproduce. S5 sections 10.3 and 14.
*   **The vocabulary rule. Binds every session.** "Operating system," unqualified, means the human system of strategy, accountability, and cadence. The software stack is always "the stack" or "the OS surface," never "the OS" alone. The record uses the same words for both, and a session that finds the OS surface and concludes the operating system exists has made a category error. S1 section 4; enforced sentence by sentence on the S3 page, and an S17 audit rule.
*   **Canon is cited by version, and the seam is not a session's to pick. Binds S4 onward.** The two canon artifacts state different six-tier authority hierarchies: `brand-guidelines.md` is Version 1.0, the deck is Version 3.0, and the deck ranks the company non-negotiables at tier 2 where the text version does not rank them at all. Canon also claims to be "the source of truth for every decision made under this name," and neither artifact holds a rule for canon against another founding document. Until the hierarchy ruling (`86akh3rx4`) and the canon reconciliation (`86akh3tjb`) land, every session cites canon by version and marks any position turning on the difference as held. S2 sections 3 and 4. S3 found further drift beyond the hierarchy and added it to the reconciliation item.
*   **The decision-rights rule is written and its register is founded. Binds every session that assigns authority.** Authority sits with the closest competent owner; the range within which that owner acts without asking is stated in advance; the escalation triggers are named before the event, each with a named destination. Three operating rules attach: a trigger names its destination and "escalate" is not one; a range states what the owner may not do as well as what they may; ranges are set one level out from the position that holds them. Every later session writes decision-rights entries in that form and marks an entry missing a part as incomplete rather than filling it by analogy. S3 section 4.
*   **The departure from her hierarchy, stated once. Binds every later session.** At Sŏn, the unit that holds the information sets the goal, holds the metric, and owns the decision inside a pre-stated range; the center integrates and names the commitments; nothing is assigned, reviewed, or escalated by a person standing above another person. Her mechanisms that assume the reverse do not survive. No later session reintroduces a cascade, a division, a team unit in her sense, or a manager who assigns and reviews. S3 section 3.4.
*   **The four goal-bearing units. Binds S4, S8, and every goal or metric session.** Company, service period, domain, and person. They intersect rather than nest. Goals ladder up from the unit that holds the information to a long-term commitment; they never replicate down. S3 section 3.2.
*   **The readiness test is complete at thirty-five rows. Binds every session from here.** Twenty yes-or-no rows from S3 and fifteen cadence rows from S4, each with a check method and a named checker, define "the operating system is running." The test runs before dinner opens and at every phase gate, and its failures map to the record's five failure modes. No session adds a row without a check method and a checker, and no row is met by a document existing. S3 section 12; S4 section 12.
*   **Two operating cadences, not one. Binds S5 onward.** Sŏn runs a pre-opening cadence and an in-service cadence, coexisting until the last proof gate rather than succeeding one another. Seven members are shared and seven are not. The seam carries a four-part protection: no build meeting in the building during service hours; the room's cadence mechanisms frozen for dinner's first quarter except the committed class and shift-close maintenance; first-quarter goals as states and baselines only; the founders' floor presence unchanged on the service metronome. The hazard being protected against is the build habit of speed reaching the room. S4 sections 2.1 to 2.7.
*   **The check-in replaces her 1:1, and it is on the clock. Binds S7, S12, S13, S14, S15.** Fifteen minutes as the first fifteen minutes of a scheduled shift in the pre-service window, paid as shift, placed by the stack when the interval elapses rather than by a lead's memory. Three questions, an upward question, one written line on the person page read back before saving. It refuses verdicts, task assignment, pay, and discipline. Intervals: every two weeks inside the ninety-day plan, monthly after. A later session may design what happens inside the fifteen minutes; no later session may make it unpaid, optional, or dependent on a lead remembering to call it. S4 sections 4.1 to 4.7.
*   **A mechanism must pass the four-part entry test. Binds every session that proposes one.** Any proposed mechanism states what it costs in bandwidth, what it buys, who runs it, and where its record lives. A mechanism that cannot answer all four does not enter the cadence. Canon's Ma framework and her own "a good process should subtract from the number of meetings, not add more" are the same rule from two directions. S4 section 2.2.
*   **Sŏn does not use the OKR name, and no percentage attainment expectation survives. Binds S13 and S14.** The unit is a goal with measures. Counts are at most three per company, service period, and domain, and one per person. Her 70 to 80 percent and 95 percent attainment expectations do not survive: there is no baseline, the record forbids asserting the unproven, and a committed goal is binary. S4 sections 7.1, 7.2, 7.4.
*   **Gates, not dates, and the charter order per period. Binds S8.** Each service period moves through drafted, ruled, built, tested, opened. A gate opens only when every readiness row holds at the review. The record's minimum durations are floors and are not shortened by a gate being met early. Dinner's charter is drafted now; lunch's is not attempted before the first full year and not at all before the three-partner ruling. S4 sections 8.1 to 8.4.
*   **The daypart charter gains two fields. Binds S8 and S17.** Session 2's seven fields plus a bounded risks field and a dependent interfaces field, so both sides of every inter-period interface are written. A period whose dependent interfaces are empty is a separate restaurant, not a period of one. The record's bus failure is an interface failure between periods. S4 sections 8.2 and 11.2.
*   **The metric layer is leading indicators, and every metric ladders to a long-term commitment. Binds S4 and S13.** The record rejects revenue, labor percentage, and food cost as the primary read. Lagging indicators are owned, reviewed last, and never primary; no accountability mechanism opens with one. A proposed lagging metric argues for itself against the record. S2 section 6.2, S3 sections 8.2 and 8.4.
*   **The operating system runs on ratified daypart charters, and the period count is a parameter. Binds S4 and S8.** The record and canon disagree on whether the house has three core service periods or four. Rather than pick, the operating system runs whatever set of periods holds a ratified charter, with dinner alone as the first configuration. No session assumes four, and none builds a lunch team before the three-partner decision is taken. S3 section 13.2.
*   **Stability is a property of the system. Binds S4 onward.** A lead who produces stability by hand, holding the schedule in their head, acting as the integration layer between floor and kitchen, is a node-overload failure, not a good manager, and the fix is to restore the system rather than praise the lead. Every accountability mechanism is designed to run without a lead's memory. Most standard management material assumes the manager is the stabilizer, so this reframe applies to every later chapter.
*   **The prerequisites checklist is retired.** It was run once, in S1, as a gap list. It is not re-run against Sŏn as a scorecard, because several of its rows assume structures Sŏn replaced by design.
*   **The profile override. Binds any session loading a profile until** **`86akh2r4k`** **lands.** The three profiles in `profiles/` predate the current allowlist and are read-only. Four corrections apply and must be carried in the session brief: the white paper, not the V7 notebook, is the record of Sŏn's structural decisions, and it carries the same material; no figure is pulled from Airtable or anywhere else, because financials are not a context source, and a figure-dependent read becomes a stated gap; the four marks are recommended, chef-gated, founder-gated, and team-filled, and nothing is ever marked landed; brand canon is the two local files, not the archived ClickUp doc. At least one profile also embeds a compensation percentage the record itself says is unfinalized, and it is not to be reproduced.
*   **The founders' presence on the floor runs on the service metronome. Binds S4 and S10.** Service tempo is set by the daypart's register and the table, never by a clock and never by the founders. The build tempo is fast by system, and its sequence is gated on proof. The hazard is the build habit of speed leaking into the room during the first quarter of dinner service.
*   **Founding documents are a coherence instrument, not a growth instrument. Binds S4, S8, S17.** Every founding section is tested against one question: does this settle something that would otherwise be re-decided at a different hour, by a different domain, or by a person who arrived later? A section failing that test belongs to the operating system or the cadence, not to the charter. S2 section 2.
*   **No service period opens without a daypart charter. Binds S4 and S8.** Sŏn's replacement for her team charter is one page per service period. It is also the form the lunch decision takes: a lunch charter that cannot be written without describing a worse version of dinner is the record's "no good answer for lunch," reached structurally. S2 section 11.
*   **Compensation splits. Binds S5, S6, and S13.** The founding commitments sit in the charter and are what recruiting and hiring state; the architecture, meaning percentage, point weights, daily calculation, payment rhythm, and the cross-strand premium, belongs to S13. No session states or implies a percentage. Two decision-rights values S3 could not carry, the server's generosity range in value and the financial recovery threshold, are set with Dominic's domain at S13. S2 section 10, S3 section 4.2.

**Open questions a future session must close:**

*   **Which changes need a version.** The record updates a process nightly from a capture with no version step (WP p.13) and the deck allows change only by versioned decision (Deck 3.0); S9 reads the first as care and the second as correction. The versioning authority ratifies. S9 finding 19.8, extending `86akh3t3y`.
*   **The unit of a departure's "calculable" cost.** The record calls the loss of a person bounded and calculable; financials are not a context source, so S9 bounds it as which mechanism now has to be maintained. S9 finding 19.5.
*   **Whether a server's book of regulars is recorded on the tension-loss row.** S9 finding 19.6.
*   **"Diagnostic" reserved for the instrument.** Canon says Nunchi is "not diagnostic inquiry" and the record calls its reference "a diagnostic"; the reconciliation should keep the word for the instrument and off the floor. S9 finding 19.11, extending `86akh3tjb`, with S11.
*   **Who holds a lead's career conversation.** Waits on `86akhb2jg`. S9 P43.
*   **The career conversation's length.** Set at thirty minutes as a reset parameter; a duration, flagged for the founders in case it should stay unset. S9 P43, extending `86akh7rrb`.
*   **The room designation, and the door as the threshold's holder.** Every brief from the first training service names who holds the room on services the Maitre d does not work; canon's Maître d' at the porch steps is read as a register set by whoever holds the door, not a fixed post, which routes to canon's owner. Urgent. S8 P25, P5.
*   **The team-supplied parts of the ruling's decision-rights entries.** The transition's trigger destinations, emergency authority's range and triggers, and the live cross-domain call's range and triggers are the team's, not the record's; the chef seat ratifies the kitchen's half. S8 P2, P52.
*   **Whether the Head of Beverage is a seat and a leadership line.** The record carries it as a designation, a program owner, and a collapsed seat. The team reads a seat, its check-in held by the Maitre d. S8 P9, finding 21.3.
*   **Which of the record's two advancement wordings stands.** The structure runs on the three-seat reading until ratified. S8 P38, extending `86akhb2ja`.
*   **Who holds an event in the room.** The record removes the events team and commits events; nothing holds one. S8 finding 21.9.
*   **The overnight cleaning crew's place in the structure.** The close depends on contracted labor outside the web. S8 finding 21.10.
*   **The leadership-line count.** Four named lines plus the Station Leads; the total is a gap until the chef fills the Station Leads. The check-in load beneath the Maitre d's seat is read first at the mechanism reset; S9 specified that read (nine inputs, one line per mode, the carriers and refused carriers), and the count stays the chef's. S8 P12, P14, S9 P36.
*   **Whether charter ratification is a condition of every cohort start date.** The why block cannot be delivered until the mission and principles land. The team recommends yes. P12, P16, extending `86akh3tdr` and `86akh3tg0`.
*   **The cohort in two waves, decided with the pre-opening hiring burst.** The first wave's mentors are the leads, and the first wave's count is what the leads can carry. P8, with `86akh7qnb`.
*   **Who holds a lead's check-in.** The record runs feedback both directions and names no one for the leads. Urgent since S9: the diagnosis of a lead's own node is half-blind until it closes, the lead's career conversation and the seat holder's line in the reset's first read wait on it, and row 118 fails. The team recommends closing it before the leads are in the building six weeks ahead of dinner's gate. Finding 19.7, P21, S9 P35, `86akhb2jg`.
*   **Whether a coach is engaged for a lead's first months.** A spend; the team recommends none. P22.
*   **Who signs a competency held across two domains.** Placed by S8: the receiving domain's assessors score on the receiving seat's rows and the receiving domain's lead records the form, the kitchen chef-gated. The founders' ratification remains open. P40, S8 P39, `86akhb2ja`.
*   **The two canon uniform tables, reconciled before the first fitting.** Finding 19.4, extending `86akh3tjb`.
*   **Whether internal training sits inside canon's prohibition on AI-generated imagery.** Gates any Synthesia module. Finding 19.12, P32.
*   **Whether a training module may explain a Korean term.** Canon says terminology stands without explanation in all brand contexts. Finding 19.6, with `86akh7r2t`.
*   **Where the employee area and the lockers are.** Promised by the record and absent from canon's spatial sequence; a first-shift walk depends on it. Finding 19.11.
*   **What training pay is.** The transparency sheet carries "the training plan with pay dates" and the record does not define training pay. Financials are not a context source; routed to S13. Finding 19.5.
*   **One reading of "no one touches a table until they are actually ready," ratified with S5 P41.** Read literally it contradicts the paid practical. Finding 19.3.
*   **Who approves a module, and what "qualified" means for authorship.** S7 recommends the module standard; the record names no approver and no test. Finding 19.1, P33.
*   **The incomplete onboarding decision-rights entries.** P56.
*   **How the founders are trained as interviewers before the learning platform exists, and how a first interview runs in a language neither founder holds.** Rows 44, 61, and 74 fail until this closes, so the first lead's first interview cannot run. P39, finding 18.4. Urgent.
*   **Whether the compensation architecture is ratified ahead of Session 13, or dinner's gate slides.** The leads' offers cannot go on an unfilled item 6 and the six-week condition works backward from the gate. The team recommends ratifying ahead, because the six-week condition is a readiness row and the program's sequence is not. Carries S5 P35 and P37. P16. Urgent.
*   **The third seat's hiring loop under the branch the chef ruling chooses.** S6 designed both without picking, as S5 did. P66.
*   **Principles version one, which gates the third read's principle-embedded questions.** After ratification the questions arrive by versioned change rather than a rebuild. P22, extending `86akh3tg0`.
*   **Whether an outside-domain read survives for edge seats after the founder stage ends.** Her Bar Raiser's function is left homeless by S5 P54 at the mechanism reset. Three options argued; the team recommends keeping S5 P54 unchanged. P46.
*   **Which seats are salaried.** Structural half closed by S8: a seat is salaried when it owns a domain or program across every open period, which the Operations Lead, the Maitre d, the chef seat, and the Head of Beverage meet, with the Station Leads chef-gated. The founders ratify the list and S13 prices it. Finding 18.7, S8 P33, P34, `86akh9tbw`.
*   **What a lead enters at.** Structural half closed by S8 as two webs: a lead holds a center seat in the house's web and enters their own inverted web at its center like every person, at the lead seat's entry horizon, never a rank. Founder ratification open; S13 names the entry point. Finding 18.3, S8 P31, P32, `86akh9tbz`.
*   **Whether the Lead Host seat exists at all.** Closed by S8 for the structure: the Lead Host is a per-service designation held by a host seat; the uniform tables are canon's owner's. Finding 18.9, S8 P24.
*   **Who signs off a competency held across two domains.** Merged with the entry above by S8. Finding 18.8.
*   **Where a hire that does not hold is read, and what in the hiring system is fixed when it happens.** The record blames the process everywhere else and is silent here. Finding 18.6, to S14.
*   **The hiring system's leading indicators.** The record names only retention and internal promotion rate, both lagging a hiring decision by a year or more. Finding 18.10, to S17.
*   **Bias measurement's data.** A pattern read until Session 11 rules. P47, with `86akh7r8z`.
*   **The chef seat ruling, now with both branches of third-seat recruitment argued.** S5 specified what recruitment looks like under partner and under hire and did not pick. Until it is filed, dinner's gate cannot open (row 59). `86akh2qrp`, filed at `86akh3tw9`; work item `86akh7qku`.
*   **The hiring partner, and how the pre-opening hiring burst is run.** S4 recommended Brandon's seat and S5 depends on it everywhere: pre-opening the hiring partner opens every seat, runs every pipeline in the leads' place, and decides every packet. Whether contracted recruiting help is engaged is the partners' and is a cost question this program does not price. `86akh7qnb`, extending S4's `86akh6742`.
*   **The owner of the seat inventory.** S8 holds the inventory's structure and reconciled the three seat lists into rows, with kitchen rows chef-gated, the Lead Host a designation mark, and events and the overnight crew recorded as gaps. The owner stays founder-gated: the team recommends the partners' review on the partners' page, the Operations Lead holding the record. Row 36 and row 93 fail until it closes. `86akh7qq4`, S8 P27, P28.
*   **Whether a first interview may run while the compensation mechanics read "being finalized."** The leads' first interviews fall months before S13 can ratify the architecture. `86akh7qry`.
*   **The pre-opening substitute for the dinner in the room.** The record's final round for leadership and salaried seats has no form for the seats hired before the room exists. `86akh7qun`.
*   **The employment form of a paid practical.** No practical runs without it. Operations Lead with counsel, at least in the interim. `86akh7qwd`.
*   **The domain lead for the inward-facing floor strand, and for hosts.** Closed by S8 for the structure under Brandon's ruling: the Maitre d, for both floor strands, runners and hosts included; runner and host seats can open. The founders ratify P21. `86akh7r10`, S8 P21.
*   **The candidate-facing register, and whether Korean terminology stands in a document handed to a candidate.** Canon governs every word and names no surface a candidate reads. `86akh7r2t`, with canon's deferred terminology session.
*   **Whether a referral is paid, and whether a search firm is used for the two leads.** `86akh7r4t`, `86akh7r69`.
*   **Whether the house states a position on the composition of its team.** The record holds inclusion mechanics and no position on who the team is, so the source-dominance read can report and cannot act. Routed to S11. `86akh7r8z`.
*   **The owner of the designed web render.** The record's own open item is the web rendered as a designed artifact rather than a chart, and the transparency sheet's first field cannot be honestly filled with a chart. S5 declined to name the owner. `86akh7ru5`.
*   **Which six-tier authority hierarchy governs, and where the company non-negotiables sit.** Founder decision `86akh3rx4`; canon reconciliation `86akh3tjb`, now extended by S3's drift list.
*   **Whether "the order is the decision" binds.** Bandwidth, then joy, then retention, then results, as an operating tiebreaker rather than a description. S3 attached the allocation consequence: under the order, covers come down before the floor is thinned, and a service period that consumes the team's bandwidth is restructured before it is defended on its results. Brandon with Dominic, `86akh3t00`.
*   **What the current data hub of record is.** The white paper names a specific tool as the hub for everything that is not customer data; the program's source boundary says that tool is out of use. The metric layer, the shift close, the feedback loop, the alert register, and readiness row 15 all run on whatever holds that role. Dominic confirms, and confirms whether the five-layer stack description is current. Until then no operating-system document names a hub tool. `86akh5u6e`.
*   **The interim two-partner decision rule.** Two partners and two equal votes have no majority, and the first reserved-class decision arrives before the chef does. S3's argued interim: domain decides after consultation outside the reserved classes; both or neither inside them with the status quo as default; lunch frozen. Requires Dominic, and the operating agreement is read first. `86akh5u77`, extending `86akh2qht` and `86akh3ty7`.

*   **Whether the floor manager and the Maitre d are one role or two, and which owns the room.** Closed by Brandon's ruling, 2026-09-13: one seat, the Maitre d, as master of the house. Canon's wording routed to `86akh3tjb`. `86akh5u9g`, `86akh5utd`, `86akh2r3e`; S8 section 2.
*   **Whether the operating system is built for three service periods or four.** Canon states four as closed; the white paper states three with lunch removable. A disagreement about status, not altitude. `86akh5ubn`.
*   **The mission sentence, the entity it belongs to, and whether it names the cuisine.** Brandon, `86akh3tdr`.
*   **Selection and wording of the long-term commitments and the principles.** Every metric and goal ladders to a commitment, so the metric layer cannot be finalized until these land. Brandon, `86akh3tg0`.
*   **Ownership of the OS surface.** The record assigns Brandon "the operating systems" and Dominic "the technology build" and "the data architecture," then names the proprietary layer "the OS surface and the agent layer," and never says whose it is. Both founders, `86akh3t27`.
*   **Which account of the chef seat governs, and whether the seat is a partner or a hire.** Gates S5 and S6 on third-seat recruitment. Founder decision `86akh2qrp`, extended by `86akh3tw9`.
*   **The founder deadlock rule in the three-partner case, and the classes of decision reserved to all partners.** The reserved-class list is now extended by three from S3. Depends on what the operating agreement already holds. `86akh2qht`, `86akh3ty7`, `86akh5u8m`.
*   **Whether the operating agreement already holds a voting or deadlock rule the charter must defer to.** Brandon reads and reports, `86akh3t62`.
*   **Versioning authority over canon and over the charter, and the interim before the chef is seated.** Brandon and Dominic, `86akh3t3y`.
*   **The definition of the cultural labor score.** A charter metric candidate with one line in the record. Brandon originated the concept and supplies the question it is built from, the population, and the rhythm. `86akh5u9x`.
*   **What "dinner is steady" means, as the gate that opens the early morning.** S3 supplies the rows and indicators that could read it; the founders pick which constitute the gate. `86akh5uaw`.
*   **The contents of the existential-risk register, and which founder owns each risk.** `86akh5ubc`.
*   **The transparency line: what is shared, when, and with whom.** `86akh5uby`.
*   **The owners the record leaves unnamed in the decision-rights register.** Management sign-off at the sonic system's second tier, now a canon question under the ruling (`86akh3tjb`); leadership review for content; the owner of the David flag. S8 named the person who triggers the pre-service scene and the late-night transition and the holder of emergency authority during a service: the Maitre d for the room. `86akh5u94`.
*   **Confirmation of the founding compensation commitments.** Brandon confirms, Dominic reviews before S13. `86akh3t9p`.
*   **The unreachable canon references.** Both canon artifacts name ClickUp doc `2ky45bmy-15773` as their record of truth, and that doc is archived and excluded. `86akh3tp5`.
*   **When the working-with-me document is exchanged with the chef partner.** Closed by S7: it stands as S1 decided, exchanged before the chef signs, and nothing in her Chapter 3 material changes it. S7 P49. Carryover `86ajgnj8t` stays open in the register for provenance.
*   **Who carries the concept's voice to the team internally.** Founder decision `86akh2qq0`; instrument spec `86akh3u2y`.
*   **The Operations Lead's partner pairing, and which partner owns construction and hiring.** S4 designed the founder cadence and found the record silent on these three. The team's recommendation: Dominic for construction and for the Operations Lead's monthly pairing, Brandon's seat for hiring. `86akh6742`.
*   **The founders' own bandwidth read, and who sets a founder's learning tempo.** S16, carryover `86akh2qzy`.
*   **Whether the house has a closed day, and whether the leads' review and the house review sit on it.** The record is silent. Both are placed at closed hours; if a closed day exists both sit on it. `86akh6739`.
*   **The definition of "dinner is steady," written as readiness rows.** S4 recommends the gate be written in the section 12 form, drawing on the leading indicators having a baseline and on the check-in and leads' review having run a full quarter without a node-overload entry. `86akh6748`, extending `86akh5uaw`.
*   **The seat that starts service and turns the room to late night.** Owner named by S8 under the ruling: the Maitre d as the room's owner for the service, or the room designation on services the Maitre d does not work. Trigger destinations are the team's and open with the ruling's entries above. `86akh5u94`, S8 2.3.
*   **The length of the close window, and what it holds.** The record allocates the server's close to the thank-you note in one place and to the incident capture in another, and never states how long the window is. Both demands are real and the labor is already paid for. S4 findings.

**A note on reading the record.** Session 1 found two conflicts inside Sŏn's own record. Session 2 found three. Session 3 found four. Session 4 found six. Session 5 found thirteen, more than double the previous high, and the count has now risen in every session of the program. Session 5 states the split directly: three of its thirteen would have surfaced from a narrow read and ten would not, and several required reading the white paper and both canon artifacts against each other on the same question. Four of the thirteen move something other than a document. The transparency sheet hands a candidate the one artifact Part I exists to refute. The compensation mechanics sit on the hiring timeline's critical path months before the session that can close them. The record's final round for its most consequential seats cannot run as written for any of them. And the record requires trained interviewers while the platform that trains them cannot exist before the team does. The count rising session over session is the argument for the reading rule, not against it. Read the record in full, including both canon artifacts. Session 7 found twelve, five of which would have surfaced from a narrow read of the onboarding pages (WP pp.17 to 21) and seven of which would not; two turn on the canon artifacts disagreeing with each other, and one sets a bought tool against canon. Session 8 found eleven, five of which would have surfaced from a narrow read of the structure pages (WP pp. 9 to 11, 14, 22) and six of which would not; two turn on canon's two versions against the white paper's management layer, and one found a committed activity, events, that the leadership delta removed and nothing holds. Session 9 found thirteen, three of which would have surfaced from a narrow read of the failure mode reference (WP pp. 13 to 14) and ten of which would not; three set canon against the white paper, including canon reserving the word "diagnostic" against the reference's own name for itself.

**A correction to the S2 brief.** The session brief attributed the phrases "life share, not market share" and "the building is not the asset, the customer is" to Sŏn's record. Neither is verbatim in the white paper. The record's verbatim claim is "The restaurant is the proof of concept. The connective layer is the asset" (WP p.34). Brand facts are not asserted from memory, and that rule applies to session briefs as well as to output.

**Extraction note.** The book PDF renders ligatures as NUL bytes under pypdf, silently corrupting hundreds of words. Use PyMuPDF for `scaling-people-book.pdf`. S3 extracted pages 84 to 134 that way and verified zero NUL bytes. The book PDF carries no bold or italic font flags, so headings are recovered by font size: body runs at 15.0pt, section headings at 21.2pt, pull quotes at 16.9pt, and table and figure text at 11.2pt, which is how Table 1's operating-structures grid was recovered. The workbook, the white paper, and the brand deck are clean under pypdf; the workbook needs hyphenation rejoined across line breaks. Two chapter-map page numbers were corrected by S1. Details are in `reference/chapter-map.md`. S5 corrected the font-size convention: the scale is not constant across the book. In pages 167 to 192 body runs at 11.1pt, sidebar headings at 15.7pt, pull quotes at 12.5pt, and captions at 8.3pt, and no 21.2pt section headings appear at all, since several section headings in that range are rendered as images. A session that applies S3's thresholds to a later range silently mislabels every line. Check the font census for the range before extracting, and expect figures to arrive as image blocks rather than text.

* * *

### Archive

Full decision records, oldest at the bottom. The ledger above is the working memory; this is the permanent record.

**Session 0 and first-pass Session 1 (both superseded, 2026-07-13).** Produced under the wrong frame. Retained only so the four earned findings (now baked into the profiles) have provenance. Not binding. The rerun writes fresh records. First-pass S1 produced: five founder principles, two metronomes, no-scale-to-7000, checklist-as-gap-list, founder mutual accountability mechanism, working-with-me as pre-signature diligence, no work-style-instrument purchase, four-quadrant vocabulary. Session 0 set the mechanics that survive: sequential sessions, no chapter files in Box, workbook as first-class source, specifications not instruments, register beside the punch list.