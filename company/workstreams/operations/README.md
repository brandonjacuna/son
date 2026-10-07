# Sŏn operational buildout

This repo is Sŏn's operational manual in the making: people systems, operating rhythms, and everything behind the restaurant, built by working through Claire Hughes Johnson's *Scaling People* in the book's order.

The book has been turned into **the work**: every decision to make, action to take, and deliverable to produce, in 33 chunks that follow the book's sections. Nothing here decides anything for Brandon. Where the white paper implies an answer, a task carries it as a labelled default assumption; where earlier work argued a position, it appears as an option with what choosing it commits Sŏn to.

- **The rules** for any session working here: [CLAUDE.md](CLAUDE.md). Read it first.
- **The plan of record:** [RECONSIDERATION-PLAN.md](RECONSIDERATION-PLAN.md).
- **The task list** lives in ClickUp, under [Sŏn Operational Systems Build Out](https://app.clickup.com/t/86akh1hdg): one subtask per chunk, and inside each chunk its tasks, tagged with a type (decision, action, deliverable) and a phase. Filter or group by the phase tag to see what comes next. ClickUp holds the work only; the thinking lives here.

## What's in a chunk

Each chunk has a folder under [manual/](manual/):

| File | What it holds |
|---|---|
| `book.md` | What the book says, with page cites |
| `considerations.md` | White-paper context, research, options, counsel questions, where Sŏn may diverge from the book |
| `tasks.md` | The chunk's decisions, actions, and deliverables (mirrors ClickUp) |
| `session.md` | The working-session guide: orientation, agenda, and one brief per decision |
| `decisions.md` | What Brandon decided, in his words, with his reasoning |
| `mapping.md` | Where every item from the old extraction program went |
| `notes/` | Brain dumps and raw session notes, dated; `inbox.md` collects items raised elsewhere |

Repeatable deliverables (a working-with-me document, a seat description, a team template) get a kit under `kits/<name>/` the first time they are built with Brandon: an intake form, a facilitation guide, a template, and an example only if he agrees. The kits are created as the working sessions produce them.

## How a working session runs

One session covers one chunk. It should feel like having someone across the table who has read everything and prompts each decision, while Brandon thinks out loud.

1. **Open.** The session reads the chunk's `session.md`, `decisions.md`, and `tasks.md`, plus the `decisions.md` of any chunk it depends on. It opens with a short orientation: what the chunk covers, what's already decided upstream, who else must agree (Dominic, the chef partner), and the agenda. Brandon picks where to start.
2. **Each decision.** Open wide with the brief's openers; let Brandon talk. Reflect back what he said, in his words. Bring what he'd want at the table, briefly: the book, the white-paper default, how others have handled it, a consequence he may not have weighed. Narrow to two or three candidate answers. He chooses; the session reads it back and confirms. If it needs Dominic or the chef partner, it's recorded as pending their agreement. Parking is fine.
3. **Brain dumps and tangents** are saved to `notes/` in his words before they're funneled. A tangent that belongs to another chunk goes to that chunk's `notes/inbox.md`.
4. **Close.** Update `decisions.md` and `tasks.md`; in ClickUp, comment the decision on its task and mark it `done` (or leave it open as pending agreement); list the deliverables the decisions unlock and offer drafts; build or update any kit; commit and push; name what the next session picks up.

Full rules: the "Working sessions" section of [CLAUDE.md](CLAUDE.md).

### Starting a session

From any device, including claude.ai/code, open a session on this repo and say:

> Sŏn operational buildout. Working session on chunk 2.1 Founding documents. Read CLAUDE.md, then open the session.

Swap in the chunk you want. In a cloud session, ClickUp goes through the ClickUp connector (a comment and a status change per decision); the REST token and Box are only on the Mac, and nothing a session needs lives outside the repo. Commit and push at the close so the next device picks up where this one left off.

## Chunk index

"First hire" counts the tasks phased before the first hire: anything a candidate sees or relies on at the first interview, which makes it the critical path. Status is taken from each chunk's `decisions.md`.

| Chunk | Tasks | Decisions | First hire | Status |
|---|---|---|---|---|
| [0 Management basics checklist](manual/0-management-basics-checklist/) | 4 | 2 | 4 | Ready |
| [1.1 Build self-awareness to build mutual awareness](manual/1.1-build-self-awareness-to-build-mutual-awareness/) | 13 | 6 | 13 | Ready |
| [1.2 Say the thing you think you cannot say](manual/1.2-say-the-thing-you-think-you-cannot-say/) | 3 | 3 | 3 | Ready |
| [1.3 Distinguish between management and leadership](manual/1.3-distinguish-between-management-and-leadership/) | 3 | 3 | 3 | Ready |
| [1.4 Come back to your operating system](manual/1.4-come-back-to-your-operating-system/) | 4 | 3 | 4 | Ready |
| [2.1 Founding documents](manual/2.1-founding-documents/) | 20 | 9 | 17 | Ready (the pilot) |
| [2.2 The operating system](manual/2.2-the-operating-system/) | 39 | 25 | 11 | Ready; 1 ruling recorded |
| [2.3 Operating cadence](manual/2.3-operating-cadence/) | 34 | 19 | 14 | Ready |
| [3.1 Recruiting](manual/3.1-recruiting/) | 39 | 24 | 36 | Ready |
| [3.2 Hiring](manual/3.2-hiring/) | 46 | 27 | 33 | Ready |
| [3.3 Onboarding](manual/3.3-onboarding/) | 53 | 30 | 20 | Ready |
| [3.4 Hiring mistakes](manual/3.4-hiring-mistakes/) | 18 | 8 | 7 | Ready |
| [4.1 Team structures](manual/4.1-team-structures/) | 37 | 22 | 20 | Ready |
| [4.2 Diagnosing team state](manual/4.2-diagnosing-team-state/) | 21 | 12 | 1 | Ready |
| [4.3 Team changes and restructuring](manual/4.3-team-changes-and-restructuring/) | 21 | 12 | 1 | Ready |
| [4.4 (Re)building the team](manual/4.4-rebuilding-the-team/) | 21 | 10 | 4 | Ready |
| [4.5 Creating the team environment](manual/4.5-creating-the-team-environment/) | 36 | 22 | 3 | Ready |
| [4.6 Team-building complexities](manual/4.6-team-building-complexities/) | 22 | 15 | 4 | Ready |
| [4.7 Diversity and inclusion](manual/4.7-diversity-and-inclusion/) | 19 | 9 | 7 | Ready |
| [4.8 Team communication](manual/4.8-team-communication/) | 24 | 14 | 5 | Ready |
| [5.1 Hypothesis-based coaching](manual/5.1-hypothesis-based-coaching/) | 19 | 11 | 3 | Ready |
| [5.2 Giving hard feedback](manual/5.2-giving-hard-feedback/) | 17 | 8 | 4 | Ready |
| [5.3 Creating a culture of informal feedback](manual/5.3-creating-a-culture-of-informal-feedback/) | 21 | 10 | 1 | Ready |
| [5.4 The formal review process](manual/5.4-the-formal-review-process/) | 29 | 20 | 7 | Ready |
| [5.5 Compensation](manual/5.5-compensation/) | 41 | 26 | 26 | Ready |
| [5.6 Managing high performers](manual/5.6-managing-high-performers/) | 19 | 10 | 4 | Ready |
| [5.7 The steady middle](manual/5.7-the-steady-middle/) | 14 | 7 | 4 | Ready |
| [5.8 Managing low performers](manual/5.8-managing-low-performers/) | 27 | 14 | 13 | Ready |
| [5.9 Managing managers](manual/5.9-managing-managers/) | 20 | 11 | 10 | Ready |
| [5.10 Managing out, firing, and layoffs](manual/5.10-managing-out-firing-and-layoffs/) | 30 | 16 | 16 | Ready |
| [6.1 Manage your time and energy](manual/6.1-manage-your-time-and-energy/) | 20 | 10 | 14 | Ready |
| [6.2 Foster relationships](manual/6.2-foster-relationships/) | 15 | 10 | 9 | Ready |
| [6.3 Consider your career](manual/6.3-consider-your-career/) | 15 | 7 | 8 | Ready |
| **Total** | **764** | **440** | **333** | |

When a session records decisions, update that chunk's status here (for example "3 of 9 decided").

## A suggested starting order

Any chunk can be opened at any time. This default follows the dependencies: each step's decisions are ones the next steps lean on, and the heavy "first hire" chunks come before the leads are interviewed.

1. **2.1 Founding documents.** The mission, principles, and how the partners decide sit upstream of nearly everything. It was the pilot, so its session guide is the most tested.
2. **1.1 to 1.4, and 0.** The founders' own ground: mutual awareness, the working-with-me documents, the words for management and the operating system, and the basics checklist (with the counsel register at 0.4). Short sessions.
3. **2.2 The operating system, then 2.3 Operating cadence.** Metrics, decision rights, goals, and the rhythms that carry them.
4. **4.1 Team structures.** The seats, the leadership line, and what a candidate is hiring into.
5. **5.5 Compensation, then 3.1 Recruiting and 3.2 Hiring.** The candidate sheet promises the pay mechanics at the first interview, so compensation's policy decisions feed recruiting. These three hold the most tasks due before the first hire.
6. **5.4, 5.8, 5.10, 5.9.** The review, performance, conduct, and separation policies a candidate relies on, and how the partners lead the leads.
7. **3.3 Onboarding and 3.4 Hiring mistakes,** during hiring and training.
8. **Chapter 4 (4.2 to 4.8) and the rest of Chapter 5,** mostly before opening.
9. **6.1 to 6.3,** the founders' own time, relationships, and careers. These can be taken whenever they're useful; several of their decisions are phased before the first hire.

## The rest of the repo

| Path | What it is |
|---|---|
| `sources/` | The book and workbook PDFs, and the Sŏn investor white paper (September 2026), the only Sŏn context. Brand material is excluded and gitignored. |
| `profiles/` | Reasoning lenses (people and culture, learning and development, founder development). Never authorities. |
| `sources/extraction/` | The prior extraction program's output and the build pipeline that turned it into the manual (`sources/extraction/build/`, including the handoff and the cross-chunk pass). |
| `archive/` | Removed 2026-10-07; in git history (`git show 644c585:company/workstreams/operations/archive/<path>`). Cited extraction files are in `sources/extraction/`. |

## Writing rules

"Customer," never "guest." No em dashes. Sentence case headings. No performed conviction. No daypart code names; service periods are named by time of day. No financial figures in the repo. The full list is in [CLAUDE.md](CLAUDE.md).
