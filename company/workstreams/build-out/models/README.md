# Models

- `src/`: canonical geometry as code or text: build123d `.py`, Zoo `.kcl`, `.ifc`. These diff cleanly in git.
- Binary files (SketchUp `.skp`, Blender `.blend`, FreeCAD `.FCStd`) go through Git LFS with a sidecar `<name>.meta.yaml` (version, parent, phase, what changed).
- `exports/`: generated DXF, IFC, PDF, STEP, 3MF. Never hand-edited; regenerate from `src/`.
- Handoff layers follow US National CAD Standard names (e.g. Q-EQPM equipment, P-SANR sanitary, E-POWR power).
