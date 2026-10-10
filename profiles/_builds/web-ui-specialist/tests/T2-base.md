# T2: Pinned, scroll-scrubbed word-by-word hero

## Answer
Buildable, and it can be done well, but "premium" is earned by restraint and performance, not by the effect. Here is the plan with the conditions that keep it from hurting the site.

## Approach
- Pin the hero with CSS `position: sticky` inside a tall container (for example 250 to 300vh), and drive progress from scroll position.
- Use CSS scroll-driven animations (`animation-timeline: scroll()` / `view()`) where supported, with a small JS fallback (IntersectionObserver plus requestAnimationFrame, or GSAP ScrollTrigger if already in the stack). Animate only `opacity` and `transform`; no layout properties.
- Split the hero line into word spans in the markup, with the full sentence also available as one accessible string (`aria-label` on the container, spans `aria-hidden`), so screen readers read the line once.

## Conditions (not optional)
1. **Reduced motion:** with `prefers-reduced-motion`, show the complete line at once with no pinning.
2. **No-JS and slow devices:** the full line is visible by default; the effect is progressive enhancement.
3. **Mobile:** test touch scroll and browser toolbar resizing (use `svh`/`dvh`). Shorten scroll length so the user is not trapped; 2 screens maximum.
4. **Don't hide the way forward:** show a scroll cue; the page must not feel stuck. Total pinned scroll under about 3 seconds of scrolling at normal speed.
5. **Keyboard and anchor links:** keyboard scrolling, Page Down, and in-page links must work and land on finished states.
6. **SEO/LCP:** the headline is real text in the HTML, not an image or canvas; Largest Contentful Paint should stay under 2.5 s. Avoid heavy video behind the effect.
7. **Contrast:** each word state (dim and lit) must still meet contrast on the background.

## What makes it feel premium
Short line (6 to 9 words), a quiet ease (no bounce), consistent timing per word, a one-time reveal that ends in a stable, readable state, and nothing else competing. If the line is long or the audience is mostly mobile, a simple fade-in on load beats the scrub.

## Questions
1. What is the line and the background (film, image)?
2. Is there an existing motion standard in the design system?
3. Is the scrub required, or is the goal "feels premium" (several routes exist)?

## Deliverable
Component with tokens for timing and easing, reduced-motion path, and a performance check on a mid-range phone.
