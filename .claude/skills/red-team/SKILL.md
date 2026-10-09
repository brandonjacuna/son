---
name: red-team
description: Adversarial review of anything Brandon puts in place (a plan, draft, design, policy, seat, skill, or decision), scaled to stakes in three intensities. Use when he says "red team", "poke holes", "stress test", "what breaks", "what am I missing", before a draft goes to ClickUp for review, and inside profile-build stage 4. Light for ideation, standard by default, harsh for legal, compliance, money, and anything touching employees.
---
# Red team

Blind critics with assigned lenses, one judge, a three-concern report. The session that runs it is the orchestrator and never critiques the target itself: it wrote or carried the target, so it cannot be blind to it.

## 1. Set the floor
Classify the target's stakes before anything else. The floor is the lowest intensity allowed; a request below it runs at the floor, and the report says so.

| Target | Floor |
|---|---|
| An idea not yet acted on: concept ideation, a sketch, a brainstorm, "just thinking" | light |
| Anything that will be acted on: a plan, a draft, a design, a seat, a skill, a page going to ClickUp for review | standard |
| Legal, compliance, contracts, money (figures, pay, pricing, the raise), anything touching employees (hiring, pay, schedules, discipline, records, training that becomes a gate), safety, anything external-facing (investor, landlord, counsel), anything hard to undo | harsh |

Hard to undo means: money out, a signature, a term in writing to an employee, a promise to someone outside Sŏn. Safety means food, fire, or injury.

Brandon may overrule the floor downward by saying so explicitly; log "run at <x> at Brandon's instruction; floor was <y>" in the report. You never lower it yourself. At harsh, before spawning, tell him the agent count in one line; he may say lower.

## 2. Fix the target
Critics read files, never memory. If the target is an idea in the conversation, write it first to `<folder>/target.md` in Brandon's words (3 KB cap), with what he said he does not want if he said it. Then name the target paths, the purpose (one line: what it is for), the neighbors (seats, skills, documents it touches), and the folder:
- inside profile-build: the build folder, files prefixed `04-`;
- otherwise `memory/audits/red-team/<YYYY-MM-DD>-<slug>/` unless the workstream names its own place.

Harsh only, and standard when the target came out of this conversation: write `<folder>/session-brief.md` (2 KB cap, honest): what Brandon asserted, what the session proposed, what was agreed with an explicit yes, which sources were used and why those, what he said he does not want. This is the only thing the `loop` critic sees besides the target.

## 3. Spawn the critics (one message, all parallel)
Lenses live in `lenses/`. Each critic is `subagent_type: red-team-critic` with the brief: `Target: <paths>. Purpose: <line>. Lens: <lens>[, <lens>]. Neighbors: <paths or none>. Write: <folder>/critic-<lens>-<a|b|single>.md, one file per lens`. A critic given two lenses writes two files, never one combined file (the merger pairs files by lens name). Pass paths, never content. A lens may be a seat: `Lens: .claude/agents/frontline-advocate.md`.

| Intensity | Lenses | Agents | Judge |
|---|---|---|---|
| light | failure-path, vagueness | 1 (both lenses, one file) | the session reads the file and decides |
| standard | failure-path, grounding, rules, seams, vagueness, who-pays | 3: failure-path + who-pays; grounding + rules; seams + vagueness | `red-team-judge` on opus |
| harsh | the standard six, each run twice blind (a and b), plus employee-harm twice (or a domain seat as one of the two) and loop once | 7 to 9 | `red-team-merger`, then `red-team-judge` with `model: fable` |

Several targets under the same lens share one critic (one agent, one file per lens per target) when they are small; a seat at harsh never shares an employee-harm critic. A general-purpose subagent costs about 50k tokens of overhead before it reads anything, a custom worker about 12k (measured 2026-10-07); batch, but never trade blindness for a batch.

## 4. Judge
- Light: read the one critic file (2 KB). Decide each flag yourself: accept, reject, or ask.
- Standard: spawn `red-team-judge` with `Target, Purpose, Flags: <the critic files>, Write: <folder>/judgment.md`, and `Session brief: <path>` when one exists.
- Harsh: spawn `red-team-merger` (`Folder, Write: <folder>/flags.md`), then `red-team-judge` with `model: fable` and `Session brief: <path>` added. You read `flags.md` and `judgment.md` only.
- A caller may raise the judge model (profile-build runs one Fable judge per batch), never lower it.

## 5. Apply and ask
Accepted edits are applied as Edits to the named rows, by you or by one Sonnet applier when there are more than about ten; never a rewrite. At light, fixes are proposed in the report and applied only on Brandon's yes. `ask` items go to Brandon one pop-up each (the `interview` skill), with the flag, the path, and the options in the question so he can answer cold: at most three pop-ups per run, ranked by how hard the harm is to undo; the rest, and every ask when he is not available, go to the "Open questions for Brandon" section of `memory/state.md`. Nothing from a red team is a decision; his answers are recorded by `session-close`.

## 6. Report
Use `templates/report.md`: three concerns at most ranked by how hard the harm is to undo, each with its failure path, earliest sign, and what was done or asked; then counts, what was not examined, the folder. Fewer than three is normal. A clean run is one line.

## Rules
- Blindness is the mechanism. A critic never sees the conversation, the author's reasoning, another critic's file, or the drafter's notes. Lenses are assigned, never chosen by the critic.
- Severity needs a verified failure path. Critical is harm hard to undo; major is the target failing its own job; minor is the rest.
- Clean is normal. Never pad to three concerns; never invent a flag; never soften a critical one.
- The target is critiqued, not the person. The report says what fails and when, never that an idea was bad.
- Caps hold: 2 KB per critic file, 4 KB flags, 3 KB judgment, 3 KB target.md, 2 KB session brief. The orchestrator reads only the judgment (and flags at harsh).
- Workers: `red-team-critic`, `red-team-merger`, `red-team-judge` in `.claude/agents/`. A worker file created in the session became callable within it (2026-10-09); if a `subagent_type` is refused, run a general-purpose agent that reads the worker file and acts as it.

## Refused shortcuts
| Excuse | Reality |
|---|---|
| "I can critique it myself here." | You wrote or carried it. Spawn the critics. |
| "It is small." | Small things reach employees and signatures. The floor decides, not the size. |
| "The critics found nothing, so skip the other lens." | Clean is normal and the floor's lenses still run. |
| "Brandon already agreed." | Agreement is what the `loop` lens checks. |
| "Harsh is expensive." | Harsh targets are the ones where a miss costs more than the tokens. Batch, do not cut. |
