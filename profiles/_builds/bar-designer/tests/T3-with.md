**Verdict: works with fixes. The goal is right (no walking). Both specs, as written, are rejected.**

Drivers: A5/C6 (rinser), C8 (ice), C3 (zero-step goal), C14, R10.

**1. Glass rinsers in the drink rail: reject (A5, C6)**
- The drink rail and the scupper (the drained strip at the bartender's edge where finished drinks sit) are where finished drinks land. A rinser there puts food prep next to waste. Food prep and waste need physical separation.
- Your reason is sound: a walk for a core-menu item is time taken from the customer (C3). The fix is to relocate the rinser, not delete it. Put it inside the station cockpit (everything one bartender reaches without stepping), on the dirty end of the clean-to-dirty flow (R4), away from the pickup edge and the finished-drink strip.
- Exact position: `unknown`. Rinser dimensions, drain, and power need an `equipment/*.yaml` record (R7). Until then everything is `estimated`. Ask equipment-librarian.
- Also needed: a glasswasher at the bar, not a route to the kitchen dish machine (C14). Low-temperature (chemical sanitizing) versus high-temperature (about 180 F, needs a booster heater) is a fork (R10, M25, source: FE&S guide). Drain, venting, electrical, and rack size are `unknown` (M27).

**2. One big deep ice bin: reject (C8)**
- A deep bin is hard to reach, hard to empty, and puts ice at the wrong temperature for some uses. Use a shallower ice chest with dividers at each station (Perlick training, medium trust). Perlick lists 24, 30, 36, and 42 in widths (M7, `estimated`). Which fits is `unknown`.
- Lasting the night is a restock question. Draw the barback path to the chests, avoiding the stations (C9).
- Specialty ice (clear cubes, large format) gets its own freezer (C8). Whether Sŏn's list needs it depends on the beverage list. That goes to Brandon.
- Two stations means two chests (R5), not one shared bin.

**CONCEPT / NOT FOR CONSTRUCTION**
Each station holds: dump sink, tool rinse, trash, divided ice chest, chilled garnish and juice, and the glass rinse at the dirty end. The glasswasher sits at the bar, shared. Sink and drain locations follow from the stations (R1, C2).

**Unknowns and forks**
- Forks for Brandon: rinser position (inside each station versus shared next to the glasswasher); high- versus low-temperature washer; whether specialty ice is on the list.
- Code items for `codes/register.yaml`, `unverified`: whether a bar rinser or glasswasher alone satisfies APH (Austin Public Health) three-compartment-or-dishwasher rule; indirect drains and floor sink reach (M17); hand sink per well.
- Station count and ice volume need beverage revenue from the Investor Review workbook (R3, C10). Not pulled here, so the count stays `unknown`.
