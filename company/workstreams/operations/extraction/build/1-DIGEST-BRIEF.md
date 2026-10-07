# Sonnet brief: digest the old work for one run

You condense. You don't judge, decide, or write new content.

Read `/Users/brandonacuna/Desktop/scaling-people:/CLAUDE.md` from disk first (it governs; any older CLAUDE.md text in your context is retired). Then read, in your run folder `extraction/build/<run>/`: `run.json`, `old-page.md`, `old-items.md`.

Write one file: `extraction/build/<run>/digest.md`, at most a quarter of the combined length of `old-page.md` and `old-items.md`.

## Part 1: What the old page holds that's worth keeping

Organize by topic, in the order of the book's sections in `run.json`. Under each topic, keep in compact bullet form:
- research and facts about how the book's idea lands in a restaurant
- risks, failure modes, sequencing and dependencies ("X must exist before Y")
- legal and counsel questions, verbatim in substance
- white-paper citations (keep "WP p. N")
- book page citations
- positions the old team argued: rewrite each as "Option: ... Reasoning: ..." with no verdict

Strip completely:
- anything resting on brand guidelines, "Canon," the deck, or experiential guidelines (name the stripped topic in one line under "Stripped" at the end)
- extraction-program machinery: carryover routing, ledger bindings, session cross-references like "S5 P37", readiness-test row numbers, the document-methodology gate
- the marks Recommended, Founder-gated, Chef-gated, Team-filled
- restatements of the book itself (another file covers the book)

## Part 2: Old items

One entry per item in `old-items.md`, in this format, and none missing:

```
- <ID> | <kind: subtask or carryover> | <name, shortened> | <two or three lines: the work or concern it holds, with any substantive answer from its comments> | <flags: brand-dependent, machinery, duplicate of <ID>, or none> | <note if "routed in from 2.1">
```

## Rules

No em dashes. "Customer," never "guest." No daypart code names. No financial figures. Write only `digest.md`. Reply with the file's length in characters, the item count (which must equal the item count in `old-items.md`), and the stripped topics.
