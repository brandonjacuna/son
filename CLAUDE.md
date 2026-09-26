# Sŏn operational buildout

## What this project is

Brandon is building Sŏn's operational systems (people systems, operating rhythms, back of house, everything behind the restaurant) using Claire Hughes Johnson's *Scaling People* as the manual. He has used this book as a manual in his consulting work and follows it the same way here.

The book gets turned into **the work**: the decisions to make, the actions to take, and the deliverables to produce, in the book's order. That saves Brandon from rereading the book and dictating "we need to decide this." Sŏn will diverge from the book in places. That's expected; note it, don't argue it.

The extraction phase (Sessions 1 to 16, September 2026) is complete. This project is now in **reconsideration**: turning that extraction into the manual and the task list described below. The plan of record is `RECONSIDERATION-PLAN.md`.

## The rule: no decisions made for Brandon

- Name every decision the book calls for. Never make it.
- Where the white paper implies an answer, attach it as **"Default assumption (white paper p. N): ..."**, a starting point he can accept or discard.
- Where earlier work argued a position, present it as an **option with its reasoning** and what choosing it commits Sŏn to. Never "recommended," never a verdict, never a request to "ratify."
- The old marks (Recommended, Founder-gated, Chef-gated, Team-filled) are retired. Don't use them.
- Never record Brandon's personal values, interiority, working style, or pay as a position.
- When asked to extract or list work, do it. Don't gate extraction on process.

## What this project produces

### In ClickUp: the work, nothing else

One parent task: **Sŏn Operational Systems Build Out** (`86akh1hdg`) in Founding Punch List (`901323485125`).

- **Chunks** are subtasks named by book section, numbered so they sort in book order: `0 Management basics checklist`, `1.1 Build self-awareness to build mutual awareness`, ..., `2.1 Founding documents`, ..., `6.3 Consider your career`. The full list is in `RECONSIDERATION-PLAN.md` section 5.
- **Tasks** are subtasks of a chunk, named `2.1.1 Decide ...`, `2.1.2 Write ...`. Each is typed **Decision**, **Action**, or **Deliverable**, and tagged with one **phase**: before the first hire, hiring and training, before opening, or after opening. Titles start with a verb; never "Ratify."
- Build order is shown by phase tags and dependencies, not by reordering chunks.

Synthesis, research, and reasoning do **not** live in ClickUp. They live in the repo.

### In the repo: the manual

```
manual/<section>-<slug>/
  book.md            what the book says, with page cites (paraphrase, short quotes only)
  considerations.md  white-paper context, research, options, counsel questions, divergences
  tasks.md           the chunk's decisions, actions, deliverables (mirrors ClickUp)
  mapping.md         fate of every old ClickUp item and old page section for this chunk
```

## Sources

### Read

| Source | Use |
|---|---|
| `sources/scaling-people-book.pdf` | The manual. Read by page range. Use PyMuPDF (fitz), not pypdf: pypdf silently corrupts ligatures in this file. |
| `sources/scaling-people-workbook.pdf` | The book's exercises and templates. |
| `sources/son-investor-white-paper-sept-2026.pdf`, the Sŏn investor white paper, September 2026, from Box `00. Pitch Materials / White Paper` (full text in `extraction/s01/record.md`, identical apart from the cover line) | **The only Sŏn context.** Source of default assumptions. Read broadly for any chunk; don't guess which paragraph matters. |
| `extraction/` and `archive/clickup-export-2026-09-26/` | The prior extraction and synthesis. Treat it as seriously as the book: keep what serves the build, rewrite verdicts as options, drop what's brand-dependent or program machinery. |
| `profiles/` | Reasoning lenses for considerations. Never authorities. |

### Profiles

Profiles sharpen what a chunk's considerations cover. Load only those that serve the chunk at hand.

The profiles were written for the extraction program. In every profile, **ignore**: instructions to mark, stake, or "land" positions; references to the V7 Business Strategies Notebook, the brand guidelines, or Airtable as authorities; and any rule this file supersedes. Use their discipline expertise: mental models, cue tables, failure modes, and sources.

Brandon approved (2026-09-26) copying these Box profile folders into `profiles/`, verbatim:

| Box folder | ID | Destination |
|---|---|---|
| People & Culture | `400281721352` | `profiles/people-and-culture/` |
| Learning & Development | `400224498698` | `profiles/learning-and-development/` |
| Founder Development Plan | `406910319980` | `profiles/founder-development/` |

After they're copied, work from the repo copies. Once in the repo, the Founder Development profiles are used only for chunks 1.1 to 1.4 and 6.1 to 6.3.

### Excluded (hard boundary)

- `sources/brand-guidelines.md` and `sources/brand-guidelines-deck.pdf`, and their copies in `extraction/s02/deck.md` and `extraction/s05/brand-deck.txt`. These are startup-phase pre-work; there is no property yet. They are gitignored.
- Business Strategies Notebook (ClickUp `2ky45bmy-11873`), all versions.
- ClickUp Brand Guidelines doc (`2ky45bmy-15773`) and Research Capture doc (`2ky45bmy-16853`).
- Airtable.
- Any other white paper version.
- Box, except the three profile folders above and the white paper named above: in particular Voice, Design Translating Team, Narrative and Structure, and Investment.
- Financial figures of any kind. If one is needed, say financials aren't a source for this work.

## Writing rules

- "Customer," never "guest."
- No em dashes. Use commas, colons, semicolons, or restructure.
- No performed conviction ("we believe," "our goal is"). Plain and declarative.
- Sentence case for headings and labels.
- No daypart code names (Good Energy, Dosi, Luxx). Refer to service periods by time of day.
- No financial figures.
- No profanity in writing.
- Keep the old program's coined vocabulary out unless the white paper uses the term. Define any useful coined term in plain words the first time.

## How work runs

### Model routing

- The session model coordinates: reads files, prepares briefs, runs ClickUp and git, verifies output.
- **Fable 5.1** writes synthesis and manual prose. Give it a curated brief file listing exactly what to read. It stays the synthesis model even under usage pressure. If budget is thin, ask Brandon before spawning it.
- Sonnet 5 or Haiku 4.5 handle mechanical work: copying, counting, formatting, verification.

### Per chunk

1. Gather the chunk's inputs into `extraction/chunk-<section>/`: book pages, workbook pages, the old session page section(s), and the old ClickUp items that touch it, from the archive export.
2. Write a brief and run Fable. It writes the four `manual/` files.
3. Verify: every old item appears in `mapping.md`, and no brand material or retired marks remain.
4. Brandon reviews. Adjust.
5. Commit and push.
6. After review: create the chunk and its tasks in ClickUp, then handle old items per the approved mapping.

The pilot is `2.1 Founding documents`. Its reviewed output sets the pattern for the rest.

### ClickUp mechanics

- Use REST through `extraction/s13/cu.py` (token in `~/.clickup_token`) for bulk work. The MCP connector caps at 1,000 calls a day.
- A page replace can return a 500 error yet still apply, truncating the page. After any error, re-read the page before retrying. `extraction/s17/restore.py` is the pattern.
- Never retype long content into ClickUp. Pass files and verify.
- Old ClickUp items are deleted or archived only after their fate is mapped and Brandon approves.

### Retiring the extraction machinery

Kept verbatim in `archive/clickup-export-2026-09-26/` and retired from ClickUp after migration, with Brandon's approval each time:
- Carryover Register (list `901327884538`): archive. No new carryovers.
- Operating System doc (`2ky45bmy-17253`) and tracker doc (`2ky45bmy-17233`): archive, don't delete.
- The 400 old build-out subtasks: replaced per each chunk's mapping.

The context ledger is retired. State lives in the repo: `RECONSIDERATION-PLAN.md` and each chunk's files. To resume, read the plan and `git log`.

### Git

- Repo: `brandonjacuna/son-operational-buildout` (private).
- Commit and push after each meaningful step, so work continues from any device.
- Never commit the excluded brand files or any token.

## History

The extraction program's original instructions are preserved at `archive/CLAUDE-extraction-program.md`. They describe how the prior work was produced, not how this project runs.
