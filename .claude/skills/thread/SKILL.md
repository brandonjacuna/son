---
name: thread
description: Log a tangent the moment Brandon branches off the core work, say how it connects, then let him choose to follow it now or park it. Use when he raises a new topic, idea, or problem mid-task that is not the step in progress ("also", "side note", "while we're here", "remind me", "what about").
---
# Thread

A tangent is never killed and never silently replaces the core work.

## Steps
1. **Log it first**, before discussing it. Append to `memory/threads.md`:
   `- YYYY-MM-DD | <the thread in one line, his words> | <where it came from: the session's core task> | open`
2. **Connect it.** One or two sentences: how it relates to the core work (blocks it, depends on it, unrelated), and which phase or workstream would own it.
3. **Offer the choice** with one AskUserQuestion. Labels carry the tradeoff:
   - "Follow it now: <core task> pauses at <exact step>"
   - "Park it: back to <core task>"
   - If it is a decision he can answer in one pop-up, a third option: "Answer it now in one question, then back".
4. **Act on the answer.**
   - Follow: set status to `following`. Name the step where the core work paused. When the tangent ends, say "Back to <core task> at <step>" and resume it.
   - Park: set status to `parked` (add "until <trigger>" if he gives one). Return to the core work in the same message.
5. At session close, the `session-close` skill rechecks every `open` or `following` line.

## Rules
- One line per thread; edit only its status field later (`open`, `following`, `parked`, `done`).
- If the tangent is really a new task for someone else, also offer the `capture` skill (ClickUp capture list).
- If two tangents arrive together, log both, then offer one pop-up per tangent.
- Do not argue the tangent's merit in step 2; that is red-team work, done only if he follows it.
