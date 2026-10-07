---
name: interview
description: Walk Brandon through decisions or unclear intake one question at a time using pop-up choices. Use for any clarification, design decision, or tradeoff before work proceeds.
allowed-tools: AskUserQuestion, Read, Write
---
# Interview

Brandon wants each decision as a pop-up he can talk through. He is an operator, not an engineer.

## Rules
- **One question per AskUserQuestion call.** Wait for the answer before the next.
- 2 to 4 options. Put the key tradeoff in the option label itself, because descriptions sometimes do not render. Example label: "36 in deep: fits 2 people, loses 1 cooler".
- Keep the header short ("Datum?", "Measured?").
- "Other" is automatic. When he answers there, he is often dictating: restate his answer in one line and confirm before moving on.
- Define any technical term in one sentence inside the question.
- Branch: skip questions his earlier answers already settled.
- Stop after at most 7 questions per round. Summarize and ask whether to continue.

## Mandatory probes for intake
1. What is this, and what decision does it support?
2. Which area and which phase?
3. Which dimensions were measured, and which are guesses?
4. What is the reference point (datum), for example the finished floor or a wall corner?
5. What is fixed, and what can move?
6. Which equipment is locked in, and which is a placeholder?

## Output
Update the card or decision file with his answers in his words. Unanswered items go to `open_questions` and `decisions/open.md`.
