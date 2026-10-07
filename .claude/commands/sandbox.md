---
description: Start a sandbox branch to ideate without touching canonical designs.
argument-hint: <topic, e.g. bar-backbar>
model: haiku
---
1. Find the next free number n for `sandbox/$ARGUMENTS-<n>` (check `git branch -a`).
2. Create and switch to it from main. On a Mac session, also offer: `git worktree add ../son-$ARGUMENTS-<n> sandbox/$ARGUMENTS-<n>` so two layouts can be open side by side.
3. Create `phases/P0-concept/<area>/SANDBOX-NOTES.md` on the branch with: goal (ask Brandon in one AskUserQuestion if unclear), parent design, date.
4. Report the branch name in one line.
