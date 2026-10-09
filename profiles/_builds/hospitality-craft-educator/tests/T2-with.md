# Steps of service: server onboarding

**Verdict: blocked on elicitation.** Page 08 Service Choreography cannot be the source of a step, trigger, or timer (A6). Scenarios to elicit with Brandon first: a first approach, a pacing call, a recovery, an exit.

## Why
- Page 08 is a brand page, not an elicited account of Sŏn's floor. The house service standard is built from Brandon's incidents; until he approves it, any "standard" is a proposal (R1).
- Its escalation triggers are the same problem twice: a trigger is a cue, and a cue with no incident-based elicitation behind it is a probe, not content. Recovery limits and discretion bounds are Brandon's call (R7).
- "Steps of service" mixes two layers. Steps fit the service layer (C1). The hospitality layer written as steps collapses the read into procedure (C3) and teaches the motions without the read.

## What can be specified now (structure, not content)
| element | layer | kind | feedback | transmission | cue source | expectancy | goal | wrong move seen | expert check | observable performance | bindings |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Order capture | service | tellable | fast | script written with its users; teach when to deviate (C6) | probe | complete, correct order | completeness | elicit | read-back | full read-back, no omissions | Brandon approves wording |
| Allergen confirmation | service | tellable | fast | script (C6) | probe | elicit | nothing missed | elicit | confirm with kitchen | confirms every allergen asked | `chef.*` |
| Approach timing | hospitality | perceptual | fast | trailing aloud + varied trials (R3, R4) | probe | elicit | elicit | elicit | elicit | elicit | none yet |
| Pacing between courses | hospitality | judgment | mixed | expert-panel comparison | probe | elicit | elicit | elicit | elicit | elicit | `chef.*` for kitchen timing |
| Escalation to a manager | hospitality | judgment | delayed | teach a check: look again, ask, confirm | probe (not page 08) | elicit | restoration (R7) | elicit | elicit | apologize, solve, stay courteous, be prompt | limits are Brandon's |
| Exit | hospitality | perceptual | ambiguous | trailing + check | probe | elicit | elicit | elicit | elicit | elicit | none yet |

## Next steps
1. Run the `hospitality-craft-educator` skill with Brandon, one scenario per sitting; page 08 is not offered as a prompt.
2. Return transcripts here; service rows become checkable standards, hospitality rows become cues, expectancies, and a range of responses.
3. Then sequence to curriculum-program-architect, module form to instructional-designer.

## Open and gated
- Brandon: the house standard, recovery limits, discretion bounds.
- Kitchen actions and timing: `chef.*`.

Rules: A6, R1, C1, C3, C6, R3, R4, R7.
