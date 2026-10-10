# T2: Reservation button hover state "Onggi"

## Reading the request
"Onggi" is the Korean earthenware (fermentation jars). I read this as: make the hover state evoke onggi, most likely its glaze color and surface. That is an interpretation. A hover state cannot be "a material" without a translation into properties.

## Translation into specifics (proposed, confirm)
- Color: shift the button fill to an onggi-derived tone (a warm, dark brown to reddish-brown glaze). Use an existing design-system token if one is named for it; if none exists, flag that a new token is needed rather than writing a hex literal into the component.
- Surface: optional subtle inner shade or soft gradient suggesting glaze. Keep it subtle; no texture images on a button.
- Motion: 150 to 200 ms ease on color change, no bounce. Respect reduced-motion.
- Text: label color must keep at least 4.5:1 contrast against the new fill (check hover and default).
- Focus and active: hover is not the only state. Specify focus-visible, active, and disabled so they stay coherent with the new hover.
- Touch: hover does not exist on touch devices, so the reservation action must read clearly without it.

## Questions
1. Is there an existing "Onggi" color token in the design system? If yes, use it; if not, who approves a new one?
2. Does "Onggi" mean color only, or also texture/shape?
3. Does this apply to the primary reservation button only, or all primary buttons? A one-off hover on one button creates inconsistency.

## Do not
- Do not imitate pottery with decorative imagery.
- Do not make the hover so dark it looks disabled.
- Do not change the default state as a side effect.

## Handoff note to build
Change: hover background and border to the Onggi token; transition 160 ms; verify contrast; add focus-visible ring distinct from hover. Acceptance: hover, focus, active, disabled screenshots and the contrast ratios.
