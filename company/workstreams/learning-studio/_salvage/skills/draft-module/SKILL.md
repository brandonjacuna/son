---
name: draft-module
description: Write the module source package from its design, in the library voice, with every tool or workflow dependency as a declared binding.
---

# Draft module

Load: Educational Materials Author and Editor; Practice and Simulation Designer for `scenarios.md` and `video-script.md`.

1. Pull the Brand Guidelines Verbal Identity page (ClickUp `2ky45bmy-15773`) for voice. Pull any canon page the content touches rather than recalling it.
2. Write each component the design calls for, using the formats in `framework/module-spec.md`.
3. Any tool step, workflow step, figure, back-of-house specific, role name, or founder decision is `{{bind:key}}`, declared in `bindings.yaml`.
4. For scenarios: every scenario has at least one recoverable path; the expert rationale explains what was noticed, not just what was right. Build and preview: `python scripts/build_scorm.py <folder> --draft`, then open `index.html` from the zip in a browser.
5. Run `python scripts/lint.py <folder>` until it has no errors.
6. Set status `drafted` in both places.

Commit: `ID drafted: <components>`.
