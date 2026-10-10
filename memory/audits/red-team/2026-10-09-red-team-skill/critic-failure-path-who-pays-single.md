lens: failure-path  run: single  target: red-team skill, 3 workers  checked: SKILL.md s1-6 and Rules, flags.md, critic/merger/judge, report.md, profile-build stage 4 row
Steel-man: blind critics, a floor Brandon can only lower himself, and a judge make review repeatable.
| id | severity | lens | flag | evidence | proposed edit |
|---|---|---|---|---|---|
| F1 | major | failure-path | Harsh pairs critic files by lens name, but s3 groups two lenses per agent. A combined a/b file matches no pair, so it merges as single and its one-run flags without a path are dropped. Path: s3 table, then merger rule 1 and 3. | s3: "failure-path + who-pays"; merger 1: "Pair the files by lens (`critic-<lens>-a.md`" | s3: name combined files `critic-<lensA>+<lensB>-<a\|b>.md`. Merger 1: pair by file name, split by `lens:` header. flags.md and critic: "one table per lens"; cap per file |
| F2 | minor | failure-path | Standard targets born in conversation get a session-brief that no standard critic or judge reads; loop runs only at harsh, yet "Brandon already agreed" points to loop. | s2: "standard, when the target came out of this conversation" | s2: brief at harsh only, or pass it to the standard judge |
| F3 | minor | failure-path | Light: the session that carried the idea accepts or rejects flags on it. | s3: "the session reads the file and decides" | "Light: accept only edits that reverse nothing Brandon said; else ask Brandon" |

lens: who-pays  run: single  target: same  checked: s5, s3 note, report.md, judge ask rule, memory/state.md line 50
| id | severity | lens | flag | evidence | proposed edit |
|---|---|---|---|---|---|
| W1 | major | who-pays | Brandon pays in attention. Judge reserves scope, money, people for him, which is every harsh target; s5 sends each ask as its own pop-up, uncapped, while the report caps at three. A walk run becomes 8 pop-ups, unanswered. | s5: "`ask` items go to Brandon one pop-up each" | s5: at most 3 pop-ups, ranked by undo-hardness; rest to "Open questions for Brandon" (exists) |
| W2 | minor | who-pays | Harsh costs 7 to 9 agents plus Fable; Brandon learns it after the spend and can refuse only by saying "lower". | Refused shortcuts: "Harsh is expensive." | s1: before spawning, one line: intensity, agent count, and "say lower to cut" |
