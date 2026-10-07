# Batched espresso: detailed design package (D2)

Real parts where they exist, plain-language specifications where they do not. Sized against the
established brewing parameters: 18 g dose, 40 g beverage in 27 s (1.48 g/s), 78 °C at the spout,
9.5 % TDS, 4–6 h hold, 150–270 shots per service day.

Everything here is **D2 — detailed design**. Nothing has been measured. The programme in
`test_program.md` is what turns it into D3 and beyond.

---

## 1. Four specification changes since the last round

These came out of the audit and the sourcing work. Each changes a number you would otherwise buy to.

**1.1 Flow through the coil must be UPWARD.** Previously specified downward for drainage. A CO₂
bubble rises at roughly 200–250 mm/s and the liquid in a 3 mm bore moves at **207 mm/s** — the two
are comparable, so in downward flow bubbles can stall and gas-lock the coil. Inlet at the bottom,
outlet at the top, drain valve at the low point for cleaning.

**1.2 Buy "beer gas", not a custom blend — and check which number is the CO₂.** The coffee needs a
CO₂ partial pressure of **0.45 bar absolute** to hold its as-brewed carbonation at 4 °C. Standard
**beer gas / Guinness gas (25 % CO₂, 75 % N₂)** delivers exactly that at **11–12 psig**. No blender,
no custom mix.

> **Procurement trap, and it is a real one.** Blend naming is not standardised. A UK supplier's
> "30/70" means 30 % CO₂. Micro Matic's MM200 blender calls **70 % CO₂** its "lager blend". If you
> order "70/30" expecting 70 % nitrogen and receive 70 % carbon dioxide, you will over-carbonate the
> coffee and shift its pH. **Order by composition — "25 % CO₂, balance nitrogen" — never by the
> two-number shorthand.**

**1.3 Match the keg to the batch.** This was never specified and it matters more than it sounds.
A 19 L keg holding a 4 L batch has 15 L of headspace carrying **200 mg of oxygen even at 1 %** —
about **166× the entire 6-hour ingress budget**. Use a 6 L mini keg for a 4 L batch.

| Vessel | Headspace on a 4 L batch | O₂ in headspace at 1 % |
|---|---|---|
| 6 L mini corny | 2.0 L | 27 mg |
| 9.5 L corny | 5.5 L | 73 mg |
| 19 L corny | 15.0 L | **200 mg** |

It also cuts purge gas from ~49 L to ~10 L of free gas per batch.

**1.4 The glycol bath spec had an internal contradiction, now resolved.** The earlier bill of
materials said "never below −1 °C" while the setpoint analysis put the freeze boundary at −6.5 °C.
The analysis is correct. **Usable window −6.5 to +5.2 °C; run at +1 °C nominal.**

---

## 2. Buy the beverage-industry chiller, not the laboratory one

This is the largest single cost in the build and the easiest place to overspend by 3×.

Our duty is **192 W mean, 428 W per-shot transient, 856 W if two groups pull together**. A 4 L
glycol bath absorbs the transient as a 0.77 K excursion, so the machine is sized on the mean.

| Option | Capacity | Price (USD) | Verdict |
|---|---|---|---|
| UBC/Kalinka ChillPro 1150H | 1150 BTU/h = 337 W | ~$999 | 1.8× the mean — adequate but little margin |
| **UBC Glycol Chiller G-30** | **2600 BTU/h = 762 W** | **~$1,540** | **Recommended — 4.0× the mean load** |
| Vinservice Power Pack | 2800 BTU/h = 821 W | ~$1,275 | Equivalent |
| Micro Matic Pro-Line MMPP4301 | 2300 BTU/h, 11.5 gal bath | ~$3,092 | Oversized bath, 3× the price |
| Laboratory recirculating chiller | 300–500 W | ~$2,500–6,000 | 2–5× the cost for the same duty |

**None of these units exceeds the 856 W two-group instantaneous peak, and none needs to.** The bath is
the buffer: 4 L of glycol absorbs one shot's 11.5 kJ as a 0.77 K rise, so the machine only has to
remove the **192 W mean**. Sizing a chiller to the instantaneous peak would mean buying roughly four
times the capacity to serve a load that lasts 27 seconds in every 60.

Draft-beer glycol packs natively run their glycol between about −4 and +2 °C — our +1 °C setpoint
sits in the middle of their design range, they come with bath and pump integrated, and they are
built for continuous bar duty. The lab route buys ±0.1 K stability we have no use for, given a
12 K-wide usable window.

**Coolant:** USP/food-grade propylene glycol (e.g. Polar-Flo, ~$58/US gal). Not automotive, not
ethylene glycol — this sits against a food-contact coil.

---

## 3. The one part that must be custom — in plain language

**No off-the-shelf coil works.** Every ready-made beverage coil — jockey-box coils, wort chillers,
immersion coils — uses 3/8 inch (9.5 mm) tube. That is about **ten times our target internal
volume**, which would leave roughly a full shot of coffee sitting in the coil between pulls.

### What to ask a fabricator for

> *A coil of food-grade stainless steel tube.*
>
> *The tube is about 4.4 mm across on the outside with a 3 mm hole down the middle (roughly 1/8 inch
> outside diameter, 0.028 inch wall). It must be 316L stainless, seamless, and suitable for food
> contact.*
>
> *Wind 2.2 metres of it into a flat spiral of 9 turns, each turn about 80 mm across, like a clock
> spring laid flat. The turns should sit directly above one another so the finished coil is a
> cylinder about 80 mm wide and 125 mm tall.*
>
> *Both ends must come out of the coil straight and long enough to pass through the wall of a
> container, finishing with standard food-grade fittings so the coil can be unscrewed and removed
> for cleaning.*
>
> *The hole through the middle must stay open all the way — if the tube kinks or flattens on the
> bends, the part is no good. Fill the tube with sand or use a bending mandrel so the bore keeps at
> least 95 % of its original size.*
>
> *The coil will sit in a bath of cold liquid, with coffee flowing up through it from the bottom.*

Expect roughly **$150–600** depending on who makes it. Any competent brewing, dairy or laboratory
fabricator can do this; it is not specialised work.

**Verify before fabricating:** 3.0 mm bore must map to a tube size your supplier actually stocks.
Ask what real OD/wall combinations are available and take the nearest; then tell me the actual bore
and I will re-run the length, because coil length scales with it.

---

## 4. Bill of materials — the recommended build

| Item | Part | ~USD |
|---|---|---|
| Glycol power pack | UBC G-30, 2600 BTU/h | 1,540 |
| Propylene glycol | Polar-Flo USP, 2 gal | 116 |
| Chiller coil ×2 (one per group) | Custom, §3 | 300–1,200 |
| Serving vessels ×3 | 6 L mini ball-lock corny | 140–400 |
| Blend gas | Beer gas cylinder, 25 % CO₂ | 160–330 |
| Regulator | Taprite dual-gauge, CGA580 | 65–150 |
| Fittings, lines, disconnects | tri-clamp / ball-lock | 150–400 |
| **Service build subtotal** | | **≈ $2,500–4,100** |
| O₂ sensor spots + reader | PreSens SP-PSt3-SA + Fibox 4 / OXY-1 SMA | verify |
| RTDs + logger | 3 ch, 1 Hz | 200–600 |
| Balance | 0.1 g, logging | 150–400 |
| Refractometer | VST / Atago / DiFluid | 150–700 |
| Clear inspection section | PFA or glass, 3 mm bore | 40–120 |
| **Instrumentation subtotal** | | **≈ $550–1,800 + O₂ system** |

The regulator must be a **nitrogen / mixed-gas** regulator with a **CGA580** inlet. A CO₂ regulator
(CGA320) physically will not fit a beer-gas cylinder — a cheap and common ordering mistake.

Prices are indicative, USD, as found in late 2026, and will date. Several are US-market; European
equivalents exist from the same categories.

---

## 5. Oxygen measurement — the one instrument worth being fussy about

The claim this whole system makes is "under 1 % oxygen for 6 hours." Measuring that badly is worse
than not measuring it, because decanting an anoxic liquid through air introduces more oxygen than
you are trying to detect.

**Use bonded optical sensor spots read through the vessel wall.** PreSens SP-PSt3-SA self-adhesive
spots have a detection limit of 0.03 % O₂ (15 ppb dissolved), work from 0–50 °C, and — critically
for a carbonated product — **have no cross-sensitivity to CO₂**. Read them with a Fibox 4 trace or
the cheaper USB-powered OXY-1 SMA. The SP-PSt6 variant covers 0–5 % with better resolution at our
target.

Prices were not published on the public pages; request a quote. If the optical system is out of
budget for G0, a handheld food-packaging headspace analyser is the fallback — less precise, but it
answers "did the purge work" which is what G0 needs.

---

## 6. What is still open

- **Real stocked tube sizes.** The 3.0 mm bore is a design optimum, not a catalogue item. Confirm
  what your supplier stocks before fabricating; the coil length follows from the actual bore.
- **Whether the coil is needed at all.** If G2 shows the two-phase behaviour is severe, the fallback
  is a commercial brazed-plate or counter-flow chiller with a larger bore, accepting more holdup.
  That is a worse design on carryover but it is entirely off-the-shelf.
- **Contract GC-MS pricing**, which varies by region more than any other line here.
- **Dissolved CO₂ measurement.** No affordable instrument found for a 4 L batch; the practical
  substitute is to control it by setting the headspace partial pressure and verifying the gas blend,
  rather than measuring the liquid.

*Engineering and procurement guidance only. Nothing here is a food-safety clearance — see the
regulatory gate in the test programme, which must be satisfied before serving a customer.*
