# Report format (what Brandon reads)

The report is short because he moves between projects and often reads on a walk. Three concerns at most, ranked by how hard the harm is to undo, then the counts. Fewer than three is normal; never pad to three. A clean result says so in one line and stops.

```
Red team: <target, one line>. Intensity: <light|standard|harsh> (<why: the stakes floor, or "Brandon asked for <x>; floor was <y>">).
Verdict: sound | sound with caveats | needs rework | investigate first

1. <concern, one line>. Fails when: <the path, one or two sentences>. Earliest sign: <what you would see first>. Done: <the edit applied> | Ask: <question Brandon can answer cold>
2. ...
3. ...

Flags: <n> raised, <n> accepted and applied, <n> rejected (<one reason each, or "see judgment">), <n> to Brandon.
Not examined: <what no lens covered, one line>.
Files: <folder>
```

Verdicts (from the judge, never from the orchestrator's mood):
- `sound`: no flags accepted, or only minors already applied.
- `sound with caveats`: majors found and fixed; no critical remains open. Allowed only when nothing critical or major is still open.
- `needs rework`: a critical or major remains that an edit cannot fix inside this target.
- `investigate first`: a flag turns on a fact nobody checked; name the check.

Light intensity drops the Flags and Verdict lines: three concerns at most, written to strengthen the idea, each with the fix proposed rather than applied.
