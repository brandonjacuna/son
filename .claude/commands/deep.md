---
description: Escalate one hard problem to Fable (top-tier model). Use sparingly.
disable-model-invocation: true
model: claude-fable-5-1
argument-hint: <the problem, or a path to a brief>
---
You are running on the top-tier model because Brandon explicitly asked. Spend it well.

Problem: $ARGUMENTS

1. Read only what the problem needs. Prefer existing summaries in `kb/` and `decisions/` over raw files.
2. Reason through the hard part: constraints, conflicts between trades, code risk, what a senior practitioner would catch.
3. Output: a decision or recommendation, the three biggest risks, and what to verify before relying on it. Keep it under 600 words.
4. Write the result to `decisions/deep-YYYY-MM-DD-<slug>.md`.
