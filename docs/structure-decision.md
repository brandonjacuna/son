# Structure and funnel decision

The structure and conversion decision for the Sŏn investor site. It changes nothing
in `src/`. It fixes the shape of the argument and the funnel so copy can be written
against a settled structure. Copy is provisional: every sentence on the current site
will be rewritten. What this document carries forward is the argument and the order,
not the wording.

Companion inputs: `docs/reference-spec.md` (the extraction), and
`refs/notes/current-site-inventory.md` (the current version, eight surfaces in one
scrolling document).

## The funnel this serves

The site is the ungated first surface of a two-gate investor funnel.

- Gate one: the site earns a narrative white paper. The site's single job is to turn a
  reader into a white paper request.
- Gate two: the white paper earns the meeting.

The reader is an already-qualified, motivated investor who arrived warm, by forwarding.
Traffic is confirmed warm and forwarded only, with no cold, paid, or search channel. The
ask is low friction: a request for a document the reader likely already wants, not money
and not a call. The site is read fast, often on a phone.

Every decision below is argued from that funnel, not from the purposes of the reference
sites.

## 1. Structure: continuous

Decision: continuous. One scrolling document, one URL, in-page anchors to the ask. Not
routed. Not a routed-page hybrid.

The routed-versus-continuous choice does not turn on the delivery mechanic (routed page
loads versus one lazy-mounted scroll). It turns on exit management. Routed buys hard exits
and shareable per-chapter URLs. Continuous buys neither. Measured against this funnel, both
routed affordances fall the same way.

- Hard exits are a liability here, not a feature. This funnel wants minimum leakage before
  a single terminal ask. A routed structure manufactures the highest-friction exit there
  is, a full page boundary, at every chapter, on a site whose whole job is to carry the
  reader past those boundaries to one place. The reference primary can afford twelve gated
  routes because it sells nothing and every exit is free. This site cannot, because every
  exit before the ask is a lost request. Every section break is an exit, and free readers
  leave.
- Shareable per-chapter URLs solve a problem this funnel mostly does not have, and create a
  small one. The forwarding unit here is the whole site, or, after gate one, the white
  paper. A chapter forwarded cold lands on a reader with none of the belief ladder installed
  beneath it, so per-chapter URLs invite fragment-forwarding that strips the argument. The
  sharing that matters, the whole arc, is served by one URL.

The reference spec corroborates from the other side. The one reference site that routes and
gates every chapter carries no conversion object. All three secondary sites, which do
convert, are single continuous vertical scrolls under one URL with no routing and no gate.
The sites whose job is to convert converge on continuous.

Two qualifications, so this is recorded honestly.

- The current site is already continuous. Part of this decision is ratification. Its value
  is naming what the extraction must not teach us: its most seductive feature, twelve gated
  routes each behind a "Start the experience" gate, is exactly the move this funnel refuses.
- The routed-page hybrid is rejected too. No part of the argument benefits from being pulled
  out of the ladder. The disclaimer belongs inline at the ask, not on a page. The team is a
  rung on the belief ladder, not a destination. The only surface that legitimately deserves
  to be its own thing is the post-submit confirmation state, and that is a legitimate hard
  exit precisely because conversion has already happened. The accurate label is continuous,
  with one confirmation state after the gate.

Motion note, because "type, color, and motion carry the site" could be misread as license
for the reference primary's scrub model. Motion here is restrained reveal on the load-bearing
beats, not scroll-jacking. A pinned or scrubbed hero produces a section that reads as the end
of the page, which is this funnel's exit failure by another name. The motion lens and the
exit lens reach the same place independently. This is a structure-adjacent note, not a motion
specification.

## 2. Carryover: the argument survives, the order takes two moves

The argument, the section logic, and most of the order carry forward. Read as a belief
ladder, the current case is sound and in a defensible dependency order. Every section installs
a required investor belief. No section is a darling with nothing downstream depending on it.

| Position | Belief it installs | Verdict |
| --- | --- | --- |
| Hero | Orientation: one Korean room, all day, dinner is the peak | Keep, re-scope to also open the loop |
| The concept (current 01) | Pointed at the relationship, not the plate; earns all day | Fold into the hero |
| Why this (current 02) | The moat: value is the memory and relationship that compound; most restaurants lose it; Sŏn keeps it | Load-bearing spine. Keep at full weight |
| The opportunity (current 03) | Timing: Korean cuisine at top recognition, Austin on the same curve, the customer already here | Keep |
| The team (current 04) | Execution credibility. The only photographic moment | Keep, before the model |
| The model (current 05) | The return: one footprint, four dayparts, one set of fixed costs; opens the loop to the briefing | Load-bearing. Gate-adjacent. Keep |
| The ask (current 06) | The single conversion | Keep |
| Footer | Quiet close, no further ask | Keep |

Two moves, both settled.

Move one, approved: fold the concept into the hero. The removal test drives this. Cut the
concept section, and does anything break? Why this re-installs the relationship premise itself
("a people business is a memory business"). The model re-installs the all-day premise itself
("one footprint... against one set of fixed costs"). The concept's beliefs are re-seeded by the
very sections that depend on them, so its real job is a ramp from hero into the Renata narrative,
not belief-installation. The hero currently only orients and opens no loop. The concept's sharpest
line, that the plate is how you earn the right to a relationship, is a stronger loop-opener than
anything in the hero now. Folding it up collapses two setup beats into one that both orients and
opens the tension, which directly answers the front-loading risk (two "what we are" beats before
the load-bearing claim).

Move two, decided: the team stays at position four, before the model. Credibility early is how a
raise is read. A reader who does not yet believe the team can execute discounts the model while
reading it, so the team at four is what makes the model land. The texture sequence cuts the same
way: the daypart color band straight into founder headshots would stack the two highest-texture
beats back to back ahead of a quiet ask. Team before model keeps the band and the headshots apart
and keeps the credibility rung ahead of the return it underwrites.

## 3. Conversion: one ask, low density

The framing that the site must both tell a story and carry the secondary sites' conversion density
is inflated. It does not hold for this funnel.

The reference split is real and purpose-driven: the primary tells a story, the secondaries convert.
The secondaries carry persistent chrome calls to action, repeated inline prompts, and an FAQ
accordion because they serve cold, browsing, unqualified visitors who might convert at any depth and
need the ask always in reach, plus objection handling. Both conditions are the inverse of this
funnel. This reader is warm and motivated, and the ask is low stakes. That density solves problems
this site does not have, and importing it would read as performed conviction, which breaks canon and
undercuts the quiet authority the brand sells.

Conversion model: tell the story, one ask where the reader is most convinced, with one quiet path to
it for the reader who arrives already convinced.

- One conversion surface: the terminal form. This is the only place the site asks.
- One persistent quiet affordance: "Request the briefing" in the header, a wayfinding jump to that
  form. It is not a second ask, it is a shortcut for the already-convinced reader who should not have
  to travel the whole argument to convert.
- One inline soft link, at the single belief-completion point: the model section's pointer that the
  amount, the structure, and the returns are in the briefing. It lands exactly where the reader first
  wants numbers and answers that specific curiosity by pointing at the gated document. This is the one
  earned inline path, not density.
- Nothing else. No repeated inline prompts, no floating call-to-action bar, no FAQ, no exit-intent.
  The footer's refusal to ask again is part of the design.

What this costs, recorded plainly: with density this low, structure carries the conversion, not
buttons. A reader who leaves mid-argument and does not use the header shortcut is lost with no safety
net. The correct mitigation is not more calls to action, it is a tight belief ladder and the header
affordance. This site bets conversion on the sequence being right, which is the correct bet for this
reader and raises the stakes on section 2.

The form is a qualifying form, not a capture form. The free-text field ("what interests you about
Sŏn?") stays. Twelve serious requests beat forty, and the field is the only early read on what an
investor cares about before the meeting. The friction is intentional and on-brand with "by request
only" and "a small number of partners."

## 4. Copy slot map

The structure as named slots, in order, with the belief each installs and a rough word budget. This
is the brief copy is written against. Budgets are grounded in the current site's own lean counts,
roughly 470 to 560 words of body across the whole argument. This is a low-word, typography-carried
site, and the budgets keep it there.

1. Hero, orient and open. Ground: Plum Ink. Job: say what and where in one line, and open the loop
   the moat will close. Absorbs the concept's sharpest premise as the loop-opener. Load-bearer: the
   display sentence. Budget: 15 to 30 words (display line, location tag, nav).
   - Header affordance: "Request the briefing," a jump to the ask. 2 to 3 words.

2. Why this, the moat. Ground: Plum Ink, the dark emotional core. Job: install the load-bearing claim,
   that a restaurant's durable value is the memory and relationship that compound, most restaurants lose
   it, and Sŏn is built to keep it. The one section allowed to run long, because it carries the feeling,
   which is a protected prerequisite, not fat. Load-bearer: the "memory business" pull-line. Budget: 180
   to 230 words.

3. The opportunity, why now. Ground: Bone with the 선 accent split. Job: install timing (Korean cuisine
   at top recognition, Austin on the same curve, the customer already here in concentration). Load-bearer:
   the "same curve" or "intersection" line. Budget: 50 to 70 words.

4. The team, who executes. Ground: Parchment. Job: install execution credibility. The only photographic
   moment (founder headshots, the sole photography the site is allowed). Position: before the model.
   Budget: about 110 words (two bios near 50 each) plus captions.

5. The model, the return. Ground: Bone with the daypart color band, the site's one strong graphic rupture.
   Job: install the economic engine (one footprint, four dayparts, one set of fixed costs; each daypart
   another return on the same rent) and open the loop to the briefing. This is the gate-adjacent beat, and
   the loop points at the briefing generically, not bound to a specific white-paper opening. Load-bearer:
   "one footprint... against one set of fixed costs" plus the band. Budget: 50 to 70 words plus band labels.

6. The ask. Ground: Aubergine. Job: the single conversion, scarcity-framed, qualifying form plus the
   securities disclaimer inline. Budget: 25 to 40 words of surrounding copy; the form carries the rest.
   - Confirmation state after submit. The one separate surface, a legitimate exit because conversion has
     happened.

7. Footer, close. Ground: Plum Ink. Job: quiet close, no further ask. Budget: under 15 words (mark,
   location).

Numbering note: folding the concept into the hero removes the standalone "01 · The concept" eyebrow.
Whether the remaining sections renumber or move to semantic eyebrows is a copy-layer decision, resolved
when copy is written. The order above is fixed; the eyebrow labels are wording.

## 5. Open inputs and what is still needed

- White paper structure is in build, not final. The model section's loop points at the briefing
  generically. The handoff is deliberately not bound to a specific white-paper opening, and will be
  tightened when the paper locks.
- Traffic is confirmed warm and forwarded only. The low-density conversion argument stands on that
  premise. If a cold, paid, or search channel is ever added, the density calculus must be revisited.
- The form is settled as qualifying. The free-text field stays.

The one input that will refine, not block, this structure is the white paper's own opening, which sets
whether the model loop should stay generic or point somewhere specific.

## Canon carried into build

Non-negotiable, recorded here so it does not resurface at build.

- No internal daypart code names on any external surface, ever. The daypart band labels are descriptive
  (Coffee, Lunch, Dinner, Late night), never the internal code names.
- No photography except founder headshots. No stock, no AI imagery, on any public surface. Property
  agnostic, pre-lease, no chef, no menu. Type, color, and motion carry the site.
- Closed eight-color palette.
- Voice: customer, never guest. No em dashes. Sentence case. Declarative over aspirational, no performed
  conviction.
