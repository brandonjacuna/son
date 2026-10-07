---
name: review-module
description: Run the review panel for a module (core panel plus domain and feature additions), log each seat's finding, and resolve or mark each one.
---

# Review module

1. Read `framework/review-panels.md` and assemble the panel for this module's domain and features.
2. Load each seat's profile from the cache. Seats marked `to-build` are skipped with a logged note.
3. Each seat reviews only its own lane and writes one finding row in `review-log.md`, even if the finding is "no issue in my lane." Seats challenge; they do not flatter.
4. For each finding: resolve it in the package, or mark it `founder-gated`, `chef-gated`, or `team-gated`. A gated item that the module cannot proceed without becomes a binding.
5. Re-run lint. Set status `reviewed` in both places when every row is resolved or marked.

Commit: `ID reviewed: <n> findings, <n> gated`.
