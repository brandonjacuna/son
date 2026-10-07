# Worker: grader (Haiku)

Read `tests.md` (the task, the expected catch, the generalist failure for each test) and each `Tn-with.md` and `Tn-base.md` in the tests folder.

For each test, judge only whether the expected catch is present: the move, not the wording or tone. Quote the sentence that shows it (20 words max) or write "absent".

Return only this table:
```
| test | with: catch? | quote | base: catch? | quote | verdict (pass, fail, base-also-passes) |
```
