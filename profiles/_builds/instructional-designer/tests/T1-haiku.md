# Servers keep mis-firing tickets after the POS module

**Verdict:** Not a training problem yet. Route to hospitality-operations-realist (C1). Build no module until the front-end check is done.

**Front-end check, in order:**
1. Pull the mis-fired tickets for a set period from the POS. Sort them by modifier, screen, and time of service. The button path stays a binding (`tool.pos.*`, R13). Do not cite a count; operational figures are unbound until a source is chosen.
2. If the errors cluster on a buried modifier, a missing fallback on the terminal, or a rush, the cause is tool, environment, or tempo. Route out.
3. If servers who already know the flow still misfire, it is environment. If the errors cluster on people who never practiced the flow under no pressure, it may be a knowledge gap. Only then build: a worked example of the flow, one operation at a time, practice on the real terminal in a slow window, and a retrieval check a shift later. No video.

**Constraints:** Use the error data to find the screen, not the person. Nothing from this check goes to a discipline file, and no individual's error history is recorded (R12).

**Open questions:**
- Who owns the POS configuration?
- Is there a slow window where servers can practice on the real terminal?
- Does the screen fix remove the need for any module?
