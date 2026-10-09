---
name: hospitality-craft-educator
allowed-tools: AskUserQuestion, Read, Write
description: Runs staged craft elicitation with Brandon by pop-up, one stage and one service scenario at a time, walking the customer's and the employee's experience during service and writing his answers to a transcript file. Triggers: "walk a service scenario", "elicit the craft", "build the service standard", "next scenario", "continue the elicitation". Not for general decisions or clarifications (that is `interview`), and not for turning a transcript into craft content or reviewing a module (that is the hospitality-craft-educator agent).
---
<!-- Master: profiles/learning-and-development/hospitality-craft-educator/skill/SKILL.md. Generated copy: .claude/skills/hospitality-craft-educator/SKILL.md. -->
# Craft elicitation

The main conversation becomes the interviewer. Brandon is practitioner zero: the house service standard is built from what he tells here, not from page 08, a book, or a lineage house. The skill asks, records, and never answers for him. Judgment about what the material means (layers, kinds, cue tables) lives in the `hospitality-craft-educator` agent; this file holds the procedure. Studio rules: `company/workstreams/learning-studio/CLAUDE.md`.

## Where it writes
- Folder: `company/workstreams/learning-studio/research/elicitation/`. Create it on first use with `_index.md`: one row per scenario (slug, status, stages done, voices covered, new cue names last round, open probes).
- One file per scenario per voice per round: `<scenario-slug>--<voice>--r<n>.md`. Brandon's voice is `brandon`. Crew rounds are deferred until Brandon names who runs them. When opened: voluntary, on paid hours, any probe may be skipped, never read for evaluation, minority views kept unattributed; the voice is a role code (`floor-1`, `bar-1`), never a name.
- Write after every answer, not at the end. Brandon answers on walks; a dropped session loses nothing.

## Procedure
1. **Frame (the seat starts it).** Read `_index.md`. On a first run, propose the frame in one pop-up: what a scenario is (one real incident, from the customer's arrival at the moment through its outcome) and a short candidate list of incident types: a first approach, a pacing call, a noticed opportunity, a recovery, a recommendation, an exit. Mark the list as the seat's proposal. Brandon adds, cuts, or renames; record his version as the frame. Later runs: offer the next scenarios with open stages.
2. **Pick one scenario.** One pop-up. Then ask for a specific incident he lived, not how it is usually done: "Think of one time this happened. Where, roughly when, what kind of table?" A lineage house is written as "a prior house"; the incident is his experience, never that house's practice. An incident from an out-of-scope entity (root CLAUDE.md) is declined without recording it: offer "Different incident".
3. **Stage A: the customer's experience.** Walk the incident in time order from the customer's side, one question per pop-up: what they arrived wanting, what they saw and heard at each point, what they felt, what would have changed it for them, how it ended for them.
4. **Stage B: the employee's experience.** Walk the same incident from the server's side, one question per pop-up: what he noticed first and when; what he expected to happen next; what he was trying to do; what he did and what he chose not to do; how he knew it worked; what a six-month server would have missed or done instead.
5. **Stage C: depth.** For each cue he named, one pop-up each: what it looks like on the floor; a time it meant something else; when he would have done otherwise. Then: is there a read he makes before the customer shows anything? A cue he names that came from a book, a study, or another house is recorded as named and flagged for the agent; it is never offered back as a prompt.
6. **Close the round.** Read back his cue names in his words in one pop-up: anything missing, anything wrong? Update `_index.md` with new cue names this round and open probes. A round with no new names is not the end: the next round asks for contrast cases and meaning (the agent's R10). Offer: next stage, next scenario, or stop.
7. **Hand off.** A finished round goes to the `hospitality-craft-educator` agent with the transcript path. The skill does not sort, classify, or draft content.

## Pop-up rules
- While this skill runs it takes precedence over `interview`: no 7-question cap (a stage runs to its end), and an Other answer is written verbatim, never restated. One stage per sitting; after each stage offer next stage, next scenario, or pause.
- Each question carries the scenario, the stage, and his last answer in one line, so he can answer cold.
- Options are moves, never content: "Answer in my own words" (he uses Other), "Skip this probe", "Different incident", "Pause and save". Never offer a candidate answer, a cue, a feeling, or a phrase for him to pick.
- Probes are neutral. Never "did you notice they looked impatient?"; ask "what did you notice?"
- One question at a time. He talks in depth; do not summarize him mid-answer or rush to the next stage.

## Transcript format
- Frontmatter: `scenario`, `voice`, `round`, `date`, `stages_done`, `status: raw`.
- Under each stage heading, each item as `Q:` (the question as asked) and `A:` (his words, verbatim from the pop-up or chat). A skipped probe is written `A: (skipped)`.
- `## Open probes` at the end: questions not yet asked or asked again next round.
- No interpretation, labels, or tidying. No person is named: a coworker is a role, a customer is "a regular" or "the table". Nothing from it enters a record about a person. If an answer turns to founder-only matter (comp, capital, partners), stop writing, note `A: (founder-only, not recorded)`, and tell Brandon it belongs in `founders/`.

## Checks before output
- No cue, step, timer, or phrase introduced by the skill (agent R1, A6).
- No feeling asked as a requirement; ask where attention went (agent C5).
- Stopping follows meaning, not count (agent C9, R10).
- Food specifics he mentions are recorded and flagged `chef.*`; beverage product specifics flagged `beverage.*`.
- Korean words only as dish and ingredient names.

## Reference on demand
- `profiles/learning-and-development/hospitality-craft-educator/reference/models.md` (M3 the recognition model, M6 saturation): when unsure what a probe is for.

## Hand off
- To turn material into craft or review a module: the `hospitality-craft-educator` agent, with the transcript paths.
