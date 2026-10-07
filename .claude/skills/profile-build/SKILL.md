---
name: profile-build
description: Use when Brandon asks to build, rebuild, revise, slim, or merge a specialist profile (a seat), or to turn an old Box profile into an agent or skill. One builder for every profile; replaces build-profile, validate-profile, and profile-forge.
disable-model-invocation: true
argument-hint: <slug> [new|rebuild|revise|merge]
---
# Profile build

One profile, one build folder, seven short stages. The session you run in is the orchestrator: it holds only the frame, the source list, flags, test verdicts, and lint output. Workers read the heavy material and write files; they hand back a path and a line, never content.

Usage: `/profile-build <slug> [mode]`. Modes:
- `new`: no profile exists. Full pipeline.
- `rebuild`: an old profile exists and needs new grounding. The old file is one source among several; research only the gaps the frame names.
- `revise` (keep and slim): no new research. Extract the old profile, re-draft into the split, red-team light, test.
- `merge`: two or more old profiles become one seat. Each old file is a source.

Run the orchestrator session on Opus. Fable is used twice, as subagents: writing the frame (stage 0) and the final judgment (stage 4). Workers run on Sonnet unless a stage says otherwise.

## Where things go
- Build folder (working files, deletable after ship): `profiles/_builds/<slug>/`
- Master (the seat itself): `profiles/<cluster>/<slug>/` with `agent.md`, `reference/`, `skill/` (modes only), `provenance.md`, `tests.md`, `BUILD.md`. Founder-only seats: `founders/profiles/<cluster>/<slug>/`, and ask Brandon before generating their agent into `.claude/agents/`.
- Generated copies (never edited by hand): `.claude/agents/<slug>.md` from `agent.md`; `.claude/skills/<slug>/` from `skill/`.
- Measurement log: `profiles/_builds/MEASUREMENTS.md` (one row per build).

## Stages and budgets
Read each stage file only when you reach that stage. Budgets are hard caps; a worker that would exceed one stops and reports.

| # | Stage | Runs on | Reads | Writes | Cap |
|---|---|---|---|---|---|
| 0 | Frame | Fable subagent, then Brandon by pop-up | brief, old profile headings, neighbor agent descriptions | `00-frame.md`, `00-tests.md` | 6 KB file (8 KB rebuild or merge) |
| 1 | Sources | Sonnet scouts, one per research target, parallel | one target each | `01-sources.md` | 1.5 KB per scout return; 6 KB file |
| 2 | Extract | Sonnet extractors: one per external source, one for all of an old profile | one source each | `extract/NN-*.md` | 3.5 KB per external card; 5 KB per old-profile section card; 40 KB total |
| 3 | Draft | Opus drafter, one pass | frame + cards only | the master: `agent.md`, `reference/`, `provenance.md`, `skill/` if any | agent core 10 KB target, 12 KB cap; reference 30 KB |
| 4 | Red team | `red-team` skill, then a Fable judge | core + provenance + cards (blind to the draft's history) | `04-flags.md`; fixes as edits | 4 KB flags |
| 5 | Test | two Sonnet runners (all with-runs, all baselines) and a Sonnet grader | `tests.md` + the master | results into `tests.md` | 3 to 5 scenarios |
| 6 | Ship | orchestrator + scripts | lint and measure output | generated copies, rows, commit | orchestrator total under 60k tokens |

Stage files: `stages/0-frame.md` to `stages/6-ship.md`. Worker prompts: `workers/`. Templates: `templates/`. Pass workers the PATH of their prompt file and their parameters; do not paste the prompt into the brief.

## Rules that hold in every stage
- Fewest agents. Every subagent costs about 50k tokens of fixed overhead before it reads anything (measured 2026-10-07). Batch small jobs into one agent; spawn a separate agent only where blindness, a different model, or parallel speed earns it.
- Write once, edit after. The master is drafted once in stage 3. Every later change is an Edit to a named row, never a full rewrite. Tags never go inline: provenance lives in `provenance.md`, keyed by row id (C1, R3, A2).
- Context isolation. The drafter reads only the frame and the extraction cards. Red-team critics read only the master, provenance, and cards, never the drafter's notes or your conversation. The orchestrator never opens a card or a source.
- Judgment over survey. A row that would not change what the seat notices or decides is cut or moved to `reference/`.
- Encode what the expert does, not who they are. No credentials, no biography, no "You are a world-class...".
- Shared rules live in CLAUDE.md (subagents load it). Profiles carry no project_block, interaction guide, reanchor, or standing-rule restatement. A profile states only the rules specific to its seat.
- Never reconstruct a practice from Brandon's lineage; flag it. Sŏn only; no out-of-scope ventures.
- Every worker return is logged in `BUILD.md`: stage, model, tokens (from the agent's usage line), files written with bytes.
- Brandon decides by pop-up (AskUserQuestion), each question carrying the context needed to answer cold. Two checkpoints only: the frame (stage 0) and the source list (stage 1).

## Refused shortcuts
| Excuse | Reality |
|---|---|
| "Faster to read the cards myself and draft here." | That is the context blow-up this builder exists to prevent. Spawn the drafter. |
| "The tags are quicker to add inline." | Inline tags were 18% of every loaded profile. Provenance file only. |
| "The old profile is good; copy its sections across." | Copying keeps survey and plumbing. Extract rows, then draft the split. |
| "Tests can be skipped this time." | Skipped validation is how both learning-studio seats shipped unaudited. Run at least the red team light pass and three scenarios. |
| "The core is 14 KB but it is all judgment." | Move worked examples and long cue detail to `reference/`. The cap holds. |
