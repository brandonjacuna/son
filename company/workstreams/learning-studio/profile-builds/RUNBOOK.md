# Runbook: building the two hospitality seats in Claude Code

Verified against Claude Code documentation on 2026-09-26. Re-check versions with `claude --version` before starting.

## What you are building

| Order | Slug | Seat | Why this order |
|---|---|---|---|
| 1 | `hospitality-craft-educator` | Hospitality Craft Educator | The Practice and Simulation Designer consumes this seat's cues and expert rationale. Build it first so the second seat's interfaces point at a real profile. |
| 2 | `practice-simulation-designer` | Practice and Simulation Designer | |

Each seat runs the seven-stage procedure in two sessions: a build session (stages 1 to 5) and a separate validation session (stages 6 and 7). Four sessions total.

## Models and effort

| Session | Model | Effort | Why |
|---|---|---|---|
| Build (stages 1 to 5) | Fable 5.1 (`fable`) | `xhigh`, with the `ultracode` keyword on the research prompts | Fable sustains long sessions and verifies its own work. Ultracode on only where fan-out pays: research and cross-checking. |
| Validate (stages 6 and 7) | Opus 5.5 (`opus`) | `xhigh`, with the `ultracode` keyword on the Stage 6 prompt | The procedure asks for a separate model or a fresh session. This does both. Stage 6 as a workflow gets independent agents checking claims against each other. |

Ultracode as a session setting (`--effort ultracode`) is allowed but not recommended for the whole session: it turns every request into workflows, including small edits, and draws down usage limits much faster. Use the keyword per prompt instead. Drop back with `/effort xhigh` if you turned the setting on.

## Before the first session

1. Update Claude Code: `claude update`. Fable 5.1 needs v2.1.257 or later; ultracode needs v2.1.203 or later; usage-limit pausing in workflows needs v2.1.271 or later.
2. Open `company/workstreams/learning-studio/` in the `son` repo, `pip install -r requirements.txt`.
3. Start Claude Code once: `claude`. Run `/mcp` and sign in to Box and ClickUp. Airtable is not needed for profile builds; disable it.
4. On a Pro plan only: run `/config` and turn on Dynamic workflows.
5. Run `/model`, look at the Fable row. If it says "Requires usage credits," Fable on your plan bills to usage credits. Decide before starting; the build is long.
6. Run `/sync-profiles` so every existing profile is in `profiles/cache/`.
7. Fill "Brandon's answers" at the bottom of each `00-frame.md`. Workflows cannot pause to ask you, so these must be settled first.
8. Commit: `git add -A && git commit -m "PROFILE frames: Brandon's answers"`.

## Seat 1, session A: build (Fable)

```
claude --model fable --effort xhigh
```

Then, in order:

1. `/build-profile hospitality-craft-educator`
   Let it read the frame, the head start, the procedure, and the seam profiles. When it reaches Stage 1, give it this prompt:

   ```
   ultracode: run Stage 1 for hospitality-craft-educator. For each research target in 00-frame.md, research the judgment the seat needs, not a survey. Verify every source marked L in the head-start corpus at its source, confirm or replace it, and extend coverage. Cross-check claims between sources and drop what does not survive. Write 01-corpus.md with a verification status on every row.
   ```

2. Read `01-corpus.md` yourself before going on. This is the one checkpoint that shapes everything after it. Cut sources you do not trust; add any you want in.
3. Tell it: `Continue with stages 2 through 5.` It writes `02-elicit.md`, `03-consolidate.md`, `04-draft.md`, `05-tagged.md`, lints, and commits.
4. Exit.

## Seat 1, session B: validate (Opus, fresh)

```
claude --model opus --effort xhigh
```

1. `/validate-profile hospitality-craft-educator`
2. When it reaches Stage 6, if it has not already launched a workflow:

   ```
   ultracode: run Stage 6 for hospitality-craft-educator. Check every [sourced] claim in 05-tagged.md against 01-corpus.md, fetching sources where possible. Flag credential inflation, generic rules, seam collisions, and standing-rule violations. Have independent agents verify each flag before it is reported.
   ```

3. Let it finish Stage 7 and commit.
4. Read `06-validation.md`. If anything there changed the seat's scope, note it for the hand-back.

## Seat 2

Repeat both sessions with `practice-simulation-designer`. In session A, add to the build prompt: `Read profile-builds/hospitality-craft-educator/06-revised.md and write this seat's interfaces against it.`

## Hand back to claude.ai

Zip each seat's folder: `profile-builds/hospitality-craft-educator/` and `profile-builds/practice-simulation-designer/`. Upload both zips to the Sŏn Home Base chat where the build is on hold. Everything needed is in the folders:

| File | Needed for |
|---|---|
| `06-revised.md` | The final profile. Goes to Box. |
| `06-validation.md`, `07-behavioral-test.md` | The build record for the Replacement Queue row and the registry. |
| `01-corpus.md` | The source manifest check. |
| `00-frame.md` | Your answers, so the manifest and seams match. |

Do not upload the profiles to Box yourself. The claude.ai session does the Box upload into the Learning & Development folder, the Replacement Queue row, the Resource Registry row, the manifest update, and the rebuilt repo in one pass.

## If something goes wrong

- **Usage limit mid-workflow:** on v2.1.271 or later the run pauses and resumes after the reset. Check `/workflows`.
- **A workflow runs away:** `/workflows`, select the run, `x` to stop. Completed agents keep their results.
- **Fable falls back to another model:** Fable's safety classifiers flag biology and cybersecurity content. Hospitality training should not trip them; if a fallback notice appears, note it and continue on Fable with `/model fable`.
- **Lint fails:** fix and re-run `python scripts/lint.py profile-builds/<slug>` before committing.
- **The model built the profile and is asked to validate it:** the validate skill refuses. Open a fresh session on the other model.
