# Claude Code kickoff prompt — Blender build

Paste everything below the line. Put these five files in the working directory first:
`build_scene.py`, `blender_handoff_brief.md`, `blender_component_schedule.csv`,
`blender_placement.csv`, `fig_fill_station_layout.png`.

---

I need photoreal Blender renders of a piece of café/restaurant equipment: a back-of-house
station that pulls espresso shots, chills each one inline, and fills a single keg under an
oxygen-free gas blanket, holding it at 4 °C until it's carried to the front of house.

**Deliverables — five stills, 2400×1600, Cycles:**
1. The whole station on its counter, wide.
2. Same, three-quarter view from the right.
3. **The gas-blanket keg assembly in high detail, cutaway** — this is the most important one.
4. The keg's posts, disconnects and purge manifold from above.
5. The chiller coil in its glycol bath, close.

**Start here.** `build_scene.py` builds the entire scene parametrically — geometry, five
cameras, lighting, render settings. Run it, fix whatever breaks, then improve the look. It was
written against Blender 4.x and has 3.x fallbacks noted inline, but **it has never been
executed** — treat the first run as a debug pass. Read `blender_handoff_brief.md` before
changing any dimension.

**Dimensions and provenance.** `blender_component_schedule.csv` lists every part. Read the
`provenance` column:
- `DERIVED` — computed from the thermal design. Exact. Don't change these.
- `PUBLISHED` — real manufacturer spec.
- `SET` — a design decision; adjustable.
- `VERIFY` — **placeholder box at a plausible size.** The espresso machine, grinder, glycol
  pack and fill well are stand-ins. Improve them visually, but the renders must not imply a
  specific commercial product.
- `CUSTOM` / `DESIGN_NOTE` — must be fabricated, or carries a caveat.

**Coordinate system:** origin at the counter's left end / front edge / floor. +X right along
the run (0–2000 mm), +Y back toward the wall (0–650 mm), +Z up (counter top at 900 mm). The
script works in metres; the CSVs are in millimetres.

## Five things that are easy to get wrong

**1. This is not nitro coffee.** No stout faucet, no restrictor plate, no cascade, no foam. A
nitro dispense system would strip out the CO₂ this design exists to preserve. If you reach for
nitro cold-brew reference images you will model the wrong thing. There is also **no tap and no
dispensing hardware at all** in this scene — that lives in the front of house and isn't designed
yet.

**2. The gas blanket is the product, so spend the detail budget there.** A 4 L batch in a 6 L
keg: liquid 97 mm deep, **182 mm of headspace** above it holding 25 % CO₂ / 75 % N₂ at 11.7 psig
instead of air. Excluding oxygen is worth about +40 percentage points of aroma retention; that
headspace is the whole engineering point. Render it as a faint volumetric tint so it reads as
present — a hint, not a fog bank. A boolean wedge cut out of the keg body reads far better than
a transparent shell. Get the conventions right: **grey disconnect = gas, black = liquid**; the
gas post has a notched collar, the liquid post is plain; the gas tube is only 25 mm long and
must terminate in the headspace, while the liquid dip tube runs to 5 mm off the floor.

**3. Flow through the coil is upward — inlet at the bottom.** Espresso leaves the group head
about 3× supersaturated with CO₂, so the hot first third of the coil runs at up to 35 % gas by
volume. Bubbles rise at ~200–250 mm/s and the liquid moves at 207 mm/s, so a downward coil
stalls them and gas-locks. Model the drain valve at the low point. Two coils, one per group head.

**4. The sight glass is load-bearing, not decoration.** The optical oxygen sensor is read
*through* a transparent wall, and a stainless keg is opaque — so the instrumented keg has a
Ø25 mm welded window with a Ø5 mm sensor spot bonded inside it. It belongs in the detail shot.

**5. The coil geometry is exact.** 4.4 mm OD × 0.7 mm wall giving a 3.0 mm bore; Ø80 mm helix,
9 turns, 15.5 mm pitch, 2266 mm developed length, 139.5 mm rise, 16.0 mL internal volume. The
11.1 mm gap between turns is deliberate — glycol flows through it. Don't close it up. Use
`res=48` points per turn for the close shot, `res=24` elsewhere.

## Look

A working bar, not a showroom. Café-plausible lighting is already set up: broad key from the
shopfront, cool fill, warm pendant. Add fine fingerprint and water-spot variation to the
stainless — perfectly clean steel reads as CGI. Coffee is very dark but not black (base colour
≈ 0.07, 0.035, 0.018, slightly translucent at the meniscus).

## Please flag rather than invent

Some things aren't specified: the plumbing runs between coil outlet and keg post (use
`coil_endpoints_mm()` for the coil ends), the purge manifold's internal porting, electrical,
drainage. Route or model them plausibly — but **tell me in your reply exactly what you invented
and where.** This package may end up in front of a fabricator, so a render with a stated hole
is much more useful than one that quietly fills gaps.

## Done means

Five renders, a short note on what broke in the script and how you fixed it, a list of anything
you invented or substituted, and the updated `build_scene.py` so the scene rebuilds from source.
