# Review: design-translating-team (10 profiles, 273 KB)

Need source: roster-needs.md (learning-studio render stage for 01 to 09; brand decision pending; 10 a retirement candidate). Em dash and "guest" checks: clean in all ten.

Stale in every file: brand facts deferred to "Brand Guidelines (ClickUp 2ky45bmy-15773)" and "knowledge lives in ClickUp, profiles in Box" (brand canon now lives in `company/brand/design-system`; Box is a read-only mirror); Claude Design framed as the anchor generation tool; "Investment team / Investor Design Director / investor website chain" references (02-order pipeline not in the repo).

| profile | size KB | need | judgment vs survey (1-5) | stale or out-of-scope items | recommendation | why (15 words) |
|---|---|---|---|---|---|---|
| 01 Design Brief Translator | 21.1 | learning-studio render; brand (auto-trigger) | 4 | common items; "five Design Translator documents" corpus lives in ClickUp | revise | Best candidate for the code-first front door; slim and absorb routing from 08. |
| 02 Platform Prompt Specialist | 25.4 | learning-studio render | 3 | Midjourney, DALL-E, Flux grammars (image tools barred from public use); Claude Design notes flagged volatile | merge (into 01) | Code-first needs only Claude Design/Code grammar; tool survey belongs in a kb/tools file. |
| 03 Brand Identity Specialist | 21.3 | none (identity locked) | 4 | common items; wordmark, palette, type already locked and linted in design system | retire | Identity is canon in code with adherence linters; no logo redesign work remains. |
| 04 Editorial Layout Specialist | 22.9 | learning-studio render | 4 | common items; deck destination is Investment team output | keep and slim | Decks and long-form still need composition judgment; design system has deck template. |
| 05 Web UI Specialist | 24.5 | learning-studio render; brand | 4 | common items | keep and slim | Closest seat to design-in-code; absorb the motion earn test and reduced-motion contract. |
| 06 Environmental Signage Specialist | 26.2 | build-out gap (no seat) | 4 | common items; 2,868 sq ft patio and one-sign site facts need live check | keep and slim | Only physical-world seat; code cannot replace it; ties to build-out. |
| 07 Image Campaign Specialist | 26.4 | learning-studio render | 4 | common items; persona names and camera stack (Fuji, DJI, Kino) are brand/production specifics | revise | Real-photography direction still earns a seat; move brand specifics out to kb. |
| 08 Design Director | 23.8 | learning-studio render | 3 | common items; routing chain assumes all 9 seats exist | merge (into 01) | Routing and baseline are thin once the design-system skill holds non-negotiables. |
| 09 Creative Director | 30.0 | brand | 5 | Ma, Yubaek-ui-mi, Jaeyeonmi used as canon (decision 2026-10-07: brand pages 06/07/08 reference only); investor-website chain | revise | Subtractive "irreducible" judgment is the highest-value rule set; strip Korean canon terms. |
| 10 Motion Interaction Specialist | 44.9 | none | 4 | 46 KB, about 3.8 KB per rule; daypart codenames rule; investor site focus | retire | Not in manifest; design system has motion guidelines and tokens; fold earn test into 05. |

Counts: keep and slim 3, revise 3, merge 2, retire 2, rebuild 0, move 0.

## Design-in-code question
Seats that still earn a place: 05 (the system and states, now partly enforced by design-system tokens), 09 (taste and kill decisions code cannot supply), 04 (decks/documents), 06 (physical), 07 (real photography direction), 01 (as a thin front door). Seats code makes redundant: 03 (locked, linted), 10 (tokens and motion guidelines exist), 02 and 08 (tool-grammar and routing collapse when the tool is the design-system skill plus Claude Code).

## Auto-trigger for the Design Translator (01)
- Costs: one extra pass on every design request (profile is 21 KB, roughly 5 to 6K tokens loaded, plus a brief the builder must read); friction on small edits to existing components; risk the brief defers to the stale ClickUp Brand Guidelines instead of `company/brand/design-system/readme.md`.
- Saves: forces medium, audience, function and the one thing the artifact must do before any code; catches adjective-only requests; seven-layer extraction turns a pasted reference into portable parameters instead of copying surface marks; splits multi-artifact asks.
- Suggested scope if adopted: fire only when a request is a new surface, carries a reference image or link, or names more than one artifact. Skip edits inside existing components. Slim 01 to about 8 KB and repoint brand facts to the design system.

## Overlaps
- 01 and 08: both sit at the front of the chain (intake versus routing); Director invokes Translator first, so one seat suffices.
- 05 and 10: Web UI owns state/feedback motion, Motion owns narrative motion; seam is written but 10 is 46 KB for a rare need.

## Gaps
- No seat reads the design-system `readme.md`, `AUDIT.md` and adherence linters as its source; every profile still points at ClickUp.
- No reviewer for design-in-code output (accessibility in browser, token adherence); 05 covers it only partly.
