# T2: LEA module, upward feedback step

## Core issue
True anonymity is not achievable on a small restaurant team. With 3 to 8 people under a manager, one comment, a shift pattern, or a writing style identifies the author. Promising "anonymous" and then being identifiable is worse than promising less. So the design promises what it can keep: confidential, aggregated, and protected from retaliation.

## Design

**What is promised (say it exactly this way):**
"Your name is not attached to your answers. Results are shown only in groups of 5 or more. Comments are edited to remove identifying detail. Retaliation for honest feedback is a fireable offense for the manager."

**Mechanics**
1. Collection by a third party or a tool the manager cannot see into (a form owned by Brandon/Dominic, not the manager being rated). No login names stored.
2. Five to seven scaled questions about observable behavior, e.g. "I know what is expected of me this week," "My manager gives feedback I can act on," "I can raise a problem without worry," plus two open comments: "Keep doing" and "Change."
3. Minimum reporting group of 5. Below 5 responses, the scores roll up to the next level (e.g. whole front of house) or the item is held until the next cycle. Never show per-shift or per-role splits on small teams.
4. Comments pass through a reviewer (Dominic or Brandon) who strips names, dates, specific incidents, and recognizable phrasing, and does not forward anything about harassment, safety, or legal issues without a plan (see below).
5. Manager receives themes, not raw text, and sees results with a facilitator within 7 days.
6. Manager must reply in front of the team within 14 days: one thing heard, one thing they will change, one thing they will not change and why. This closes the loop; without it participation drops.
7. Cadence: twice a year at first. Same questions each time so trend is visible.

**Carve-outs (tell people up front)**
Reports of harassment, discrimination, safety hazards, or illegal conduct cannot stay anonymous in effect; the company has a duty to act. Offer a named path to Brandon or Dominic for those, with non-retaliation stated.

**Red team**
- Small team deanonymization: handled by min group 5 and comment editing.
- Revenge hunting: stated policy plus no raw data to the manager.
- Gaming or a bad-day pile-on: use 2 cycles of trend before action.
- Managers who get defensive: train them on receiving feedback first (thank, ask a question, no explaining).
- Do not use results in pay or firing decisions on their own.

## Decision for Brandon
Approve the "confidential, not anonymous" framing and who owns the tool.
