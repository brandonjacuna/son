# Sŏn

One repo for building Sŏn (Sŏn Hospitality LLC; first restaurant at 207 E St. Elmo Rd, Austin). Founders: Brandon John Acuña-Cardona (CEO; legal documents use Brandon John Acuña) and Dominic Thomas (CFO).

## Start of every session
1. Read `memory/state.md` (what is in flight), `memory/plan.md` (phase order and briefs), and the last ~20 lines of `memory/decisions.md`. Stable facts: `memory/context.md` (company) and `founders/context.md` (founders only).
2. If the work is inside a workstream, its own CLAUDE.md loads when you work there. Read it.
3. Never assume a fact from an earlier session is still true if it can be checked live (ClickUp, Box, workbook).

## Layout
- `company/`: anything a future manager could eventually see. Workstreams: `learning-studio`, `operations` (Scaling People build-out), `nerve` (external digests), `clickup-system` (ClickUp knowledge base, runbooks, Meetings Agent), `build-out` (construction), `science` (`espresso-chiller`, `matcha-sonication`). `company/brand/design-system` is the Sŏn design system (code).
- `founders/`: governance, operating agreement, comp, capital raise, founder development. Founders only. This boundary is where the repo splits later; never put founder-only material under `company/`.
- `profiles/`: master copy of every specialist profile. `.claude/agents/` holds lean agent versions generated from them. Box (Sŏn / 10. AI Projects / Profiles) is a read-only mirror.
- `kb/`: knowledge about tools (`kb/tools/`) and domains (`kb/domains/`). Every file has frontmatter `review_every` and `last_verified`.
- `prompts/scheduled/`: the exact prompt of every scheduled task. Edit here, then sync the task.
- `memory/`: the repo's memory (see below).
- `imports/`: raw material waiting to be sorted. Nothing in it is canon. Old chats arrive through `prompts/chat-handoff.md`.
- Sandboxes: experiments, including changes to this system itself, go on `sandbox/<name>` branches and merge only when Brandon says so.
- Build-out work lives in `company/workstreams/build-out/`. Its skills and commands use paths relative to that folder. Its phase lock (P0 concept until the lease is signed) is enforced by the root hooks in `.claude/hooks/`.

## Memory protocol
- `memory/state.md`: current in-flight work, one line each, with owner and next step. Rewrite freely.
- `memory/decisions.md`: append-only, dated. A decision is recorded only when Brandon (or Brandon and Dominic) agreed to it. Never record your own recommendation as a decision.
- `memory/threads.md`: parked threads (see Threads).
- `memory/pending/`: ideas being considered but not agreed. They can sit for weeks. Nothing in `pending/` is canon or may be applied elsewhere.
- Before ending any session that changed something, run the `session-close` procedure: update state, append decisions, park threads, commit.
- Landing work on `main`: cloud sessions work on a side branch. Work left on a side branch is invisible to every later session (this is how the learning studio and nerve builds got stranded). At session close, merge the session's branch into `main` and push, unless the session changed the system itself (`.claude/`, hooks, settings, CLAUDE.md rules) or ran on a `sandbox/` branch: then open a pull request and tell Brandon in one line what it changes. Never leave work unmerged without saying so.

## Routing
- Financial figures: only from the current Investor Review workbook in Box (Sŏn / 02. Capital Raise). Never from memory, decks, or Airtable (retired). If it is not reachable, say so.
- Review: anything Brandon or Dominic must review lives in ClickUp while in review (that is where they comment). First drafts may start here; once pushed to ClickUp, the ClickUp copy is canonical until approved, and the repo keeps a pointer. Approved finals go to Box (or Trainual / ClickUp for operational reference docs).
- ClickUp task shape: parent = the outcome; second level = phases (A, B, C...); third level = every action item, numbered (A1, A2...) and prefixed by kind (FRAME, DECIDE, CONFIRM, FLAG, ACTION, GENERATE, SIGN).

## Scope and exclusions
Sŏn only. The Josephine, Sanctuary, and former partners are out of scope: never reference, plan for, or carry material over from them. Pullman Market is Brandon's consulting work: its material never carries into Sŏn work, but a mention of Pullman (bio, investor context, relationships) is fine and is not flagged. The one exception is the Pullman LnD Import folder in Box, a reference for the learning studio build (phase 5) only. The Experiential Guidelines are a reference file in Box, never guidelines. Sŏn is a Korean restaurant; the brand canon line on Korean cultural material is in `memory/decisions.md` (2026-10-07, `brand`). The white paper (September 2026) is canon for most things; the V7 Business Strategies Notebook is background only.

## Standing rules (all written output)
"Customer," never "guest." No em dashes. No performed conviction ("we believe," "we hope," "our goal is"). Declarative over aspirational. Profanity is spoken-only, never written.

## Working with Brandon
- He thinks fast and outputs a lot; intake must be distilled and chunked.
- Decisions go to him as pop-up questions (AskUserQuestion), each carrying the full context he needs to answer cold, since he moves between projects. He often answers on walks.
- He often reasons from what he does NOT want. Elicit both: what do you want, what do you not want.
- Define legal, entity, and finance jargon in one sentence when it comes up.
- Threads: when he branches into a tangent, log it in `memory/threads.md` immediately, then offer: follow it now, or park it and return to the core work. Do not kill the tangent; do not let it silently replace the core work.
- Red team everything he puts in place, scaled to stakes (see the `red-team` skill): light for concept ideation, standard by default, harsh for legal, compliance, and anything touching employees.

## Model policy
Fable only for strategy, system design, and orchestrating agents. Opus for building and drafting. Sonnet or Haiku subagents for searching, inventorying, extraction, and mechanical edits. If the current task does not need the current model, say so.
