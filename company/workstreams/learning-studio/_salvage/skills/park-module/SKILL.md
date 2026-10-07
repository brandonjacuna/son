---
name: park-module
description: Verify a reviewed module is complete except for declared bindings, and mark it parked, the target state until tools and workflows are set.
---

# Park module

Check, and stop at the first failure:

1. `python scripts/lint.py <folder>` has no errors.
2. Every component in `components` exists.
3. Every open item in `review-log.md` is resolved or marked gated, and every gated item the module depends on is a declared binding.
4. No tool-specific or workflow-specific step is written as fact anywhere (read the package for this; lint cannot).
5. If the module has scenarios, `python scripts/build_scorm.py <folder> --draft` builds.

Then set status `parked` in both places and run `python scripts/status.py bindings`.

Commit: `ID parked: <n> open bindings`.
