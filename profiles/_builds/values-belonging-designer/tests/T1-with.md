T1: Peer recognition spec

draft: counsel review required

Verdict: I will not spec this as asked. Two parts fail: the public leaderboard (C5, A3) and the bonus (C15, R3). The rest is rebuilt below.

Why it fails
- A public feed with a most-recognized board is a comparison engine. Felt appreciation drops for most people even when volume is high. It rewards visibility, not the quiet work that carries a service.
- A bonus on top makes the count a target. It stops measuring appreciation and starts measuring who games the feed (C15).
- Pay is a personnel matter. Brandon alone decides it, and it goes through the counsel gate. I do not tie money to this.

Brief that replaces it (tool-neutral, `tool.recognition`)
1. Act first. A team member tells a named colleague what that person did, in specifics, within a day or two of seeing it.
2. Two separate streams.
   - Recognition: for what a person did. Specific and tied to an act.
   - Appreciation: for who the person is. Runs continuously, regardless of output, and is not tied to a shift result.
3. Delivery is private or small-group (the pre-shift circle, a note to the person). Anything public is framed around giving ("who did you notice this week?"), never around receiving.
4. No received-count ranking, badge tally, or "top" list anywhere, including to leaders.
5. Nothing from the feed enters a personnel, developmental, review, or discipline record. It is not a performance input (records wall).
6. Top-down recognition is allowed but cannot be the only channel (C6). Peer and person-directed channels run alongside it.

Pre-committed failure test (R6)
The design failed if team members report feeling compared, if recognition clusters on front-of-house or on the most visible people, or if quiet roles go unnamed for weeks. A rising volume count does not count as success (C11, A6).

Bindings and status
- `tool.recognition`: platform unchosen. Nectar is a candidate, not chosen. Any candidate must meet items 3 to 5 or it is out.
- `team.*`: cadence and ritual home are open. Nothing here is landed until `memory/decisions.md` says so (R12). Funding phase, so no figures or counts are written.

For Brandon to decide
- Confirm no money is tied to recognition. If you want any reward, it goes to counsel and is not tied to received counts.
- Whether to choose a platform now or run on paper and small-group first.
- Check with culture-implementer that this runs on a full night before it ships.
