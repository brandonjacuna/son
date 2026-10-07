---
name: refresh-capabilities
description: Re-research what a delivery platform (Trainual, Synthesia, H5P/Lumi, or another) can currently do, and update its adapter file and verified dates. Platforms change fast; run before any real render and whenever a new platform is considered.
---

# Refresh capabilities

Usage: `/refresh-capabilities <platform>`

1. Search the platform's own help center, docs, pricing page, and product updates first. Third-party reviews only to find leads, then confirm at the source.
2. For each row in the adapter's capability table: confirm, correct, or mark removed. Add any new capability that changes what the studio can design (new question types, interaction types, tracking, import or API changes, plan changes).
3. Answer specifically: what can be **created** by API or MCP (not just read), what **reports** completion or score, and what is **plan-gated**.
4. Update the `verified` dates. Add new modalities or delivery options to `framework/modality-library.md` when the platform opens one.
5. Summarize what changed and which parked modules it affects.

Commit: `capabilities <platform>: <what changed>`.
