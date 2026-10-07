# Sonnet brief: book.md for each chunk in one run

Read `/Users/brandonacuna/Desktop/scaling-people:/CLAUDE.md` from disk first. Then read `extraction/build/<run>/run.json`, `book.md` (verbatim book pages with `[p.N]` markers), and `exercises.md` if present. For format and tone, read `manual/2.1-founding-documents/book.md` as the example.

For each chunk in `run.json`, write `manual/<section>-<slug>/book.md`. The slug is the title in lowercase kebab case (e.g. `manual/3.1-recruiting/`). If `book.md` already exists there, replace it.

Content: the book's guidance for that section as someone flipping to it would want it: what it is, why it matters, her frameworks, tests, examples, and the exercises that serve it. Cite pages "(p. N)". Paraphrase; quotations a sentence at most. No Sŏn content. End with a pointer to `extraction/build/<run>/book.md` for the full text.

No em dashes. Write only those `book.md` files. Reply with each path and its word count.
