# Chapter

Pinned, scroll-scrubbed chapter bound to a daypart. Vertical scroll drives lateral travel of the inner track; direct children carry data-imm-rate ("1.25") to ride at different rates. Motion is position-scrubbed, never fade-in.

- Requires GSAP + ScrollTrigger loaded on the page (window.gsap / window.ScrollTrigger). Without them, or under prefers-reduced-motion, the chapter collapses to a static readable stack: same content, no pin.
- length is the scroll distance in viewport heights (default 2.5).
- timeLabel prints the chapter clock ("06:30") in the eyebrow voice.
