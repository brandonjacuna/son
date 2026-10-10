lens: failure-path  run: single  target: .claude/skills/profile-build/stages/4-redteam.md  checked: target, red-team SKILL, profile-build SKILL, 5-test head, lenses
| id | severity | lens | flag | evidence | proposed edit |
|---|---|---|---|---|---|
| F1 | major | failure-path | Item 5 orders a merger and Fable judge for every batch; the skill has no merger below harsh and no judge at light. Light spawns two extra agents or guesses. | item 5: "One merger and one judge serve the whole batch, the judge on `model: fable` for every batch" | "Merger at harsh only. Judge: light = session reads file; standard = red-team-judge; harsh = fable."
| F2 | major | failure-path | A batch spans seats with separate build folders; item 2 names one folder and the filename has no seat slug, so files collide. | item 2: "`04-critic-<lens>-<a\|b\|single>.md`" | Add batch folder and `<slug>` to the filename; light's two-lens file uses `<lens1>+<lens2>`. |
| F3 | minor | failure-path | Item 6 omits `Session brief:` for the harsh judge; the skill requires it. | item 6: "Judge brief adds `Frame: 00-frame.md`." | Append "; at harsh also `Session brief: 04-session-brief.md`." |

lens: vagueness  run: single  target: .claude/skills/profile-build/stages/4-redteam.md  checked: same
| id | severity | lens | flag | evidence | proposed edit |
|---|---|---|---|---|---|
| V1 | minor | vagueness | "Lands on a team member" vs "policy" has no test; a seat can be both. | item 4: "`frontline-advocate` for anything that lands on a team member, `hr-implementer` for policy" | "Both: frontline-advocate is a; hr-implementer is b if the seat writes policy." |
| V2 | minor | vagueness | "Every lens file carries a 'for a seat' paragraph" is false: `loop.md` has none. | item 7 last sentence | "Every lens file except `loop`." |
| V3 | minor | vagueness | "or the old profiles' scope sections" has no trigger. | item 3 | "Seams table; if absent, old scope sections." |
