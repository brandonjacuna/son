# Bindings

A binding is a declared gap: a piece of module content that depends on something not yet decided. Bindings are how a module can be finished before the operation is.

## Syntax

In any module file, write `{{bind:KEY}}` where the content would go. Declare every key in the module's `bindings.yaml`. Lint fails if a key is used but not declared, and warns if one is declared but never used.

```
Flag the allergy on the ticket using {{bind:tool.pos.allergen_flag}}.
```

## Namespaces

| Prefix | Means | Who fills it | When |
|---|---|---|---|
| `tool.` | A specific software or hardware step. POS, reservations, KDS, scheduling, the LMS. | Whoever owns the tool decision | When the tool is chosen and configured |
| `workflow.` | A sequence not yet set: the opening order, the handoff at the pass, who calls what. | Operations Lead, Maitre d, or chef, per domain | When the SOP is set |
| `fact.` | A figure or a changing fact: a price, a count, a time standard. | Financial figures from the current Investor Review workbook (Box); operational figures unbound until a source is chosen (Airtable retired); or the owning doc | At bind time, never before |
| `brand.` | A brand element: a phrase, a name, a service step defined in canon. | Confirmed by Brandon; Brand Guidelines (canon line pending phase 1 session B), Box file `2281626080747` | At bind time |
| `chef.` | Back-of-house specifics: station layout, recipe, plating, the allergen matrix. | The chef | When the menu and stations are set |
| `people.` | A role title, a named contact, a reporting line. | Brandon | When roles are staffed |
| `founder.` | A decision only Brandon can make. | Brandon | When decided |

## bindings.yaml

```yaml
bindings:
  - key: tool.pos.allergen_flag
    needs: The exact steps to attach an allergen alert to a ticket in the POS.
    gate: team-gated          # none | founder-gated | chef-gated | team-gated
    status: open              # open | filled
    value: null
    source: null              # where the value came from when filled
```

## Working across modules

`python scripts/status.py bindings` writes `bindings/registry.md`: every open binding, grouped by key, with the modules that depend on it. When a tool gets chosen, run `/bind tool.pos` and fill every module that needs the POS in one pass.

## What should never be a binding

The craft. How to read a table, how to recover a mistake, why the standard exists, what good looks like. That is durable content and it gets written now. If a module is mostly bindings, it is probably a procedure that belongs in a job aid after the tool is chosen, not a module to build today. Park the idea in the catalog as `identified` and move on.
