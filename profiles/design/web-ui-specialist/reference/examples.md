# Worked examples

Read for the shape of a critique. Each is adapted from a case a source describes; none is invented.

## E1. Detecting convergence
A landing page draft. Pass 1: uppercase eyebrow over a giant H1, headline plus subtext plus two buttons, three equal feature cards with rounded-square icons, 100px padding on every section, Inter throughout. Every one of those is the statistical center of the corpus. It is compositionally valid and says nothing specific to Sŏn; none of it is a made decision. I direct: kill the eyebrow, decide what the hero argues, vary section spacing to content weight, and take the type from `tokens/typography.css` instead of Inter. First fix: the hero, because it sets whether the page has a point of view. The novice error avoided is calling it clean because nothing is broken.

## E2. The pre-ship pass
A screen ready to ship. The primary states look finished. Contrast was checked in the design file, not the browser, and the ghost button on the hero image fails on the rendered background. Focus rings are browser defaults and differ between buttons and inputs. The empty state is a blank panel, loading is a browser spinner, and the error is a red border with default text, which also gives no text description of the error. Verdict: blocked. First fix: re-verify contrast in the browser and on a physical device and fix the ghost button, because an accessibility failure is foundational. Then one focus-ring spec on every interactive element, then all three states to primary quality. The novice error avoided is trusting the design file for what only the render can show.

## E3. The earn test on a pinned hero
A pinned, scrubbed hero where the language already carries the thesis. I remove the motion and read it: the argument survives, so the pin was decoration, and it spends the customer's scroll for nothing. I direct: drop the pin, keep a short entrance and one held anchor line, nothing on scroll; the weight goes into type and space. "No narrative motion here" is the verdict, not a gap. The novice error avoided is adding motion to make it feel premium.

## E4. A reduced-motion block that hides content
A staggered reveal with a reduced-motion query that sets duration to zero and leaves the delays. With reduced motion on, each item still waits out its delay, invisible, then snaps in: staggered invisibility. I strip the gate classes, read top to bottom, and tab every control; a link inside an un-entered item receives focus while invisible. I direct: zero the delay too, arm focusable content at once, and make the visible state the stylesheet default. The novice error avoided is reading "duration: 0" as "reduced motion handled."
