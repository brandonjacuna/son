---
name: session-close
description: The only way to end a Sŏn session that changed anything. Verifies the real repo state, rewrites memory/state.md, appends decisions Brandon confirms, parks open threads, lists promotions from workstream notes, reports open sandboxes, commits, and lands the branch on main (merge, or pull request for system changes and sandboxes). Use when Brandon says "close", "wrap up", "end the session", "that's it for today", or when the context-rot cue fires.
---
# Session close

Run every step in order. Do not skip a step because "nothing changed there": say "none" for it in the report instead.

## Context-rot cue (when to offer a close unprompted)
Offer to close, in one line, when any of these is true:
- The conversation has been summarized once already, or you are re-reading files you read earlier to recall what they said.
- The session has moved to a second phase or workstream.
- You catch yourself unsure what was agreed versus what you proposed.
Closing early and starting a fresh session beats carrying a fuzzy context.

## Refused rationalizations
None of these is a reason to skip or shorten a close:
- "It was a small session." Small sessions are how state goes stale.
- "Brandon is busy / already left." Write everything; queue the decision read-back as the first item of the next session in `memory/state.md` instead of recording unconfirmed decisions.
- "I'll remember next time." No session remembers anything not in the repo.
- "The state file is basically right." Verify it against the repo, line by line.
- "This was my recommendation and he seemed to agree." Only an explicit yes is a decision.
- "The branch can be merged later." Work left on a side branch is invisible to every later session.

## Steps

### 1. Verify the real state (before writing anything)
Run and read:
```
git status --short
git branch --show-current
git fetch origin main --quiet && git log --oneline origin/main..HEAD
git diff --stat origin/main...HEAD
git branch -a --list '*sandbox/*'
```
Write state from what these show plus what is reachable live (ClickUp, Box) if the session touched it, never from your recollection of the conversation. If a claim in `memory/state.md` cannot be checked, keep it and say so.

### 2. Rewrite `memory/state.md`
- One line per item: `what | owner | next step`. Rewrite freely; delete lines that are done (move a short line to "Done YYYY-MM-DD" for this session's work).
- The first line under "Now" is the next session's starting point.
- Add or update the "Open sandboxes" section from step 1 (branch, what it is, waiting on).

### 3. Decisions: read back, then append
- List every candidate decision from this session in Brandon's words, one line each.
- Read them back with AskUserQuestion (multiSelect: true, "Which of these did you agree to?"). Each option label carries the decision itself.
- Append only the ones he selects to `memory/decisions.md` as `- YYYY-MM-DD | area | decision | Brandon` (or `Brandon and Dominic`). Append only; never edit earlier lines.
- Your own recommendations, and anything he did not select, go to `memory/pending/` or the "Open questions" section of `memory/state.md`, never to decisions.
- If he cannot answer now, put "Confirm decisions from <date> session" first in state.md with the list.

### 4. Park threads
Every tangent still open goes to `memory/threads.md` (use the `thread` skill format). Mark threads finished this session `done`.

### 5. Promotions
Read the notes files the session touched in any workstream (`STATE.md`, `DECISIONS.md`, `decisions/`, `HANDOFF.md`, workstream `CLAUDE.md`). List anything that belongs in root memory: a company fact (`memory/context.md`), a founders fact (`founders/context.md`, never under `company/`), or a cross-workstream decision. List them in the report; apply only facts Brandon has stated, and only after he says so.

### 6. Commit
- Stage specific paths, not `git add -A` blindly; check nothing in `imports/` or secrets is staged by accident.
- Commit message: what changed and why, in one line, then details.

### 7. Land the branch
Decide from step 1:
| Branch or change | Action |
|---|---|
| `sandbox/*` | Push the branch. Ask Brandon (AskUserQuestion) before anything reaches `main`: "Open a pull request", "Leave on the sandbox", "Merge now". |
| Changed the system (`.claude/`, hooks, settings, any CLAUDE.md rule) | Push the branch, open a pull request to `main`, tell Brandon in one line what it changes. |
| Routine work | `git checkout main && git pull origin main && git merge --no-ff <branch>`, push `main`, then push the side branch too. |
If a merge conflicts, stop and report; do not resolve conflicts in `memory/decisions.md` by dropping lines.

### 8. Report (five lines or fewer, plus lists)
- Where it landed (merged / PR link / sandbox).
- Next step (the first "Now" line).
- Decisions recorded; decisions waiting on confirmation.
- Threads parked.
- Promotions proposed. Open sandboxes.

## Never
- Record a decision Brandon did not confirm.
- Write a second state store (no session logs, no handoff files outside `memory/`).
- Leave work unmerged without saying so.
