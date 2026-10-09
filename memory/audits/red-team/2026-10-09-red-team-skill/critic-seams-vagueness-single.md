lens: seams  run: single  target: red-team skill, lenses, templates, 3 agents  checked: all targets; profile-build + stage 0/4, REGISTRY, thread, session-close, interview, frontline-advocate scope, CLAUDE.md
| id | severity | lens | flag | evidence | proposed edit |
|---|---|---|---|---|---|
| S1 | major | seams | Standard gives one agent two lenses; no file name, brief or header covers it. At harsh the merger finds no `critic-seams-a.md`, so combined files go unmerged. | critic: "ONE assigned lens"; merger: "Pair the files by lens" | SKILL s3: name `critic-<l1>-<l2>-<run>.md`; flags.md: one header+table per lens; merger pairs on full name. |
| S2 | major | seams | Stage 4 forces Fable on every batch and expects `04-flags.md`, which no merger writes below harsh. | stage 4 item 5: "fable for every batch"; skill: standard "opus" | ask Brandon: Fable judge on every seat (costlier), or follow the skill's table? |
| S3 | major | seams | Revise runs light, but a seat is "acted on": floor is standard, so the judge is skipped wrongly. | profile-build: "red-team light"; skill s1: "a skill" = standard | profile-build l.14 and shortcuts row: "at the frame's intensity, never below the skill's floor". |
| S4 | minor | seams | Light report proposes fixes; skill s5 applies them. | report.md: "proposed rather than applied" | SKILL s5: at light, apply on Brandon's yes. |
| S5 | minor | seams | Stage 4 cites a paragraph loop.md lacks. | "Every lens file carries a 'for a seat' paragraph" | Add one to loop.md. |

lens: vagueness  run: single  target: same  checked: same files
| id | severity | lens | flag | evidence | proposed edit |
|---|---|---|---|---|---|
| V1 | major | vagueness | Harsh floor turns on undefined terms; two sessions classify one target differently. | s1: "safety, anything external-facing, anything hard to undo" | Define hard to undo: money out, a signature, a written term to an employee, an external promise; safety: food, fire, injury. |
| V2 | minor | vagueness | No test. | s3: "when they are small"; s2: "honest" | Share under 3 KB; tag brief lines asserted, proposed, agreed-yes. |
| V3 | minor | vagueness | "Dropped" has no actor; the steel-man has no home in the file. | failure-path 1: "ignores the steel-man ... is dropped" | Put it in `checked:`; judge rejects flags that ignore it. |
| V4 | minor | vagueness | Padding: repeated in 8 lenses and critic.md. | "Zero flags is a valid result." | Cut from the lenses. |
