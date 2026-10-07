# Adapters

An adapter turns a module source package into something a platform or a person can use. Modules never depend on an adapter; adapters depend on modules. When a platform changes or is replaced, rewrite its adapter and re-render. The modules stay as they are.

| Adapter | For |
|---|---|
| `trainual.md` | The current LMS. Researched capability map, the tracking rule, content mapping, floor-demonstration recording options, and the capability tour plan. |
| `scorm.md` | Tracked rich interactions: the repo's scenario player, H5P via Lumi, commercial authoring tools. |
| `synthesia.md` | AI video, plan-gated interactivity, and the path to tracked branching without the Enterprise plan. |
| `live-and-print.md` | Pre-shift, coaching, role-play kits, floor rubrics, job aid cards. |

Each capability row carries a `verified` date. Run `/refresh-capabilities <platform>` before any real render.
