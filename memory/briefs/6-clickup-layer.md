# Phase 6: ClickUp manager layer

Design on Fable; build on Opus. Before the first manager hire.

## Goal
Managers do all operational work in ClickUp (Brain, Super Agents, docs) without needing Claude, while Brandon and Dominic keep working in the repo. ClickUp AI stays within 10,000 credits a month for now.

## Work
1. **Research first (verify, do not assume).** What ClickUp's GitHub integration actually exposes to Brain and Super Agents: repo contents, or only links, commits, and pull requests. Current Super Agent capabilities, limits, and credit costs. How Notetaker sharing works on the Business plan (see `clickup-system/STATE.md`).
2. **Design.** Which operational knowledge lives in ClickUp for managers (SOP reference, working-with-me documents from the operations kits) versus Trainual (staff training) versus the repo (source). The publish path from repo to ClickUp and Trainual. How a manager updates an SOP in ClickUp and how that change flows back.
3. **Agents.** Super Agent instructions generated from the phase 3 profiles (lean versions). Messaging tone per person from the working-style documents the operations build-out produces.
4. **Pilot.** One SOP-update flow end to end with Dominic acting as the manager.

## Decisions for Brandon
Which agents managers get; credit budget; whether repo-to-ClickUp publishing is automatic or reviewed.

## Red team
Harsh (employee-facing).
