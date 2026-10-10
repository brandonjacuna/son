# Flags format (critic files and the merged flags file)

Every critic file starts with its header, then one table. 2 KB maximum per critic file; 4 KB for a merged `flags.md`.

```
lens: <lens>  run: <a|b|single>  target: <path or slug>  checked: <what you read, one line>
| id | severity | lens | flag | evidence | proposed edit |
|---|---|---|---|---|---|
| F1 | critical | failure-path | <one sentence: what fails, when> | <quote, 20 words max, with row or line id> | <the exact edit, or "cut", or "ask Brandon: <question>"> |
```

Severity (one word):
- `critical`: harm hard to undo. Legal, safety, an employee's hours, pay, record, or dignity, money out, a signature, a promise to someone outside Sŏn. Needs the verified failure path in `evidence`.
- `major`: the target fails its own job as written. Needs the failure path.
- `minor`: everything else worth fixing.

A clean critic file is one header line and `clean: <what you checked, one line>`. No table, no padding, no "consider" items dressed as flags.

Merged `flags.md` (harsh only) adds a column `runs` (`both`, `a`, `b`) and a final line: `dropped: <n> single-run flags without a verified path; see critic files`.
