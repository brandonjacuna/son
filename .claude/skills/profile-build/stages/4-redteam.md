# Stage 4: Red team, then Fable judgment

The red team is the `red-team` skill (`.claude/skills/red-team/SKILL.md`, read it) run on the master at the frame's intensity. This file says only how a seat plugs into it.

1. Intensity comes from `00-frame.md` (light, standard, harsh). The skill's floor still applies: a seat whose decisions touch employees, pay, discipline, gates, legal, or money runs harsh whatever the frame says, and the mismatch is logged in `BUILD.md`.
2. Folder: the build folder, files prefixed `04-` (`04-critic-<lens>-<a|b|single>.md`, `04-flags.md`, `04-judgment.md`).
3. Target paths for every critic: `agent.md`, `skill/SKILL.md` if any, `provenance.md`. Purpose: the frame's one-sentence Seat line. Neighbors: the agent slugs in the frame's seams table (`.claude/agents/<slug>.md`) or the old profiles' scope sections in `profiles/_source/`. The `grounding` critic also gets `extract/` (it opens only the cards provenance cites). Every lens file carries a "for a seat" paragraph; nothing else is added to the brief.
4. Harsh: `employee-harm` runs twice; when the seat is people-facing, one of the two runs is a domain seat as the lens (`frontline-advocate` for anything that lands on a team member, `hr-implementer` for policy). `loop` runs once on a `04-session-brief.md` you write (what the frame asserted, what Brandon answered in the pop-ups, what the drafter was told, which sources were chosen and why).
5. Batches: several seats under the same lens share one critic (one file per seat) at light and standard; at harsh, grounding and employee-harm never share. One merger and one judge serve the whole batch, the judge on `model: fable` for every batch (the judge also rules on cross-seat seams).
6. Judge brief adds `Frame: 00-frame.md`. The judge's `does the job` line answers "does this seat do the frame's job?".
7. Apply accepted edits as Edits to the named rows (one Sonnet applier for a batch); update the provenance rows the edits touch. Ask Brandon the `ask` items by pop-up. A clean result is a normal outcome; do not invent flags.
8. Log every worker in `BUILD.md`: stage 4, model, tokens, counts. Tests (stage 5) start only after the edits are applied; tests never change here.
