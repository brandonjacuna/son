# Lens: failure-path

The pre-mortem. It is six months later and the target failed as written. Trace how.

Ask, in this order:
1. Steel-man first: write the strongest case for the target as written in two lines under the file header. Only then attack. A flag that ignores the steel-man is a straw man: do not write it.
2. Which assumptions are load-bearing? For each: what would have to be true, who checked it, and what happens at Sŏn if it is false. Only low-confidence, high-impact assumptions become flags.
3. Walk one concrete path from a real input (a Friday at 8:15 with the real crew, a new hire's first week, an investor's question, a landlord's reply) to the bad outcome. No vague doom: name the step where it breaks.
4. Inversion: what does the opposite choice, or doing nothing, produce? If that is as good, the target has not earned its cost.
5. Second-order: what does the target incentivize once people adapt to it?
6. Reversibility: which parts can be undone in a week, and which cannot (money out, a signature, a term in writing to an employee, an external promise)? Irreversible parts get the stricter reading.

For a seat (agent or skill): a cue that fires on the wrong input, a decision rule that produces the wrong call on a realistic case, a failure mode the seat lists but its rules do not prevent.

Severity needs a verified path: before writing critical or major, state what you checked (the row, the figure, the decision line) and where the path runs.
