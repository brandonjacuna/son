# T1 (skill)

Reader: a six-month hire, maybe second language, mid-shift, on a phone.

## Rewrite

Allergen mistakes can hurt a customer, so check before you serve. Before service, check tonight's menu against the allergen sheet. Then check the allergen flags in the POS. If a flag and the sheet disagree, tell your manager before you take the order.

(The last two sentences are a draft. The POS step and the escalation step are `tool.*` bindings; see below.)

## What changed and why

- V3, V2: "Verification ... must be completed by the guest-facing team member prior to the commencement of service" had the action buried in "verification" and no doer. Now: "you check," before service.
- V9: the reason comes first in one line, then the first action.
- V1: "the guest-facing team member" becomes "you."
- Standing rule: "guest" becomes "customer."
- V14 / C15: "in the spirit of jeong toward every guest" is cut. "Jeong" is a Korean philosophy term, outside the 2026-10-07 brand line (Korean words are dish and ingredient names only). It is also warmth in a procedure (V8, C13). Nothing teachable is lost; the reason line carries the stakes.
- V7: "POS allergen flag procedure" is kept as real working vocabulary, but the procedure itself is not written out here.

## Bindings held open (V-rule 4, C14)

- `tool.pos.allergen-flag`: I do not know the actual POS steps or where the flag appears. The sentence "check the allergen flags in the POS" names the task only. Fill the exact taps from the tool binding.
- `chef.allergen-escalation`: who the cook tells, and whether the order is held, is a kitchen specific. The "tell your manager" line is a placeholder until the chef confirms it.
- Tone: this is an allergen failure, so the register is grave. Tone flexes, voice does not (V13).

## Hand-off

Run `scripts/lint.py` on the module file. Then send the draft cold to the materials-author-editor agent.
