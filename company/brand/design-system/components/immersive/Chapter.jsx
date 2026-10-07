import React from "react";

/**
 * Pinned, scroll-scrubbed chapter bound to a daypart theme. Vertical scroll
 * drives lateral travel of the inner track; layers ride at different rates
 * (data-imm-rate on direct children, default 1). Motion is position-scrubbed,
 * never fade-in. Uses GSAP ScrollTrigger (window.gsap + window.ScrollTrigger)
 * for the pin and scrub; collapses to a static readable stack under reduced
 * motion or when GSAP is absent.
 */
export function Chapter({
  theme,
  timeLabel,
  scrub = true,
  length = 2.5,
  className = "",
  style = {},
  children,
  ...rest
}) {
  const rootRef = React.useRef(null);
  const trackRef = React.useRef(null);
  const [staticStack, setStaticStack] = React.useState(true);

  React.useEffect(() => {
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const gsap = window.gsap;
    const ST = window.ScrollTrigger;
    if (!scrub || reduced || !gsap || !ST) return; // static stack
    setStaticStack(false);
    gsap.registerPlugin(ST);
    const root = rootRef.current, track = trackRef.current;
    const travel = () => Math.max(0, track.scrollWidth - root.clientWidth);
    const tween = gsap.to(track, {
      x: () => -travel(),
      ease: "none",
      scrollTrigger: {
        trigger: root,
        start: "top top",
        end: () => "+=" + Math.round(length * window.innerHeight),
        pin: true,
        scrub: true,
        invalidateOnRefresh: true,
      },
    });
    const layers = Array.from(track.children).filter((el) => el.dataset.immRate && el.dataset.immRate !== "1");
    const layerTweens = layers.map((el) =>
      gsap.to(el, {
        x: () => -travel() * (parseFloat(el.dataset.immRate) - 1),
        ease: "none",
        scrollTrigger: { trigger: root, start: "top top", end: () => "+=" + Math.round(length * window.innerHeight), scrub: true },
      })
    );
    return () => { tween.scrollTrigger && tween.scrollTrigger.kill(); tween.kill(); layerTweens.forEach((t) => { t.scrollTrigger && t.scrollTrigger.kill(); t.kill(); }); };
  }, [scrub, length]);

  return (
    <section
      ref={rootRef}
      data-theme={theme}
      className={`son-chapter ${className}`}
      style={{
        position: "relative",
        width: "100vw",
        marginLeft: "calc(50% - 50vw)",
        minHeight: staticStack ? "auto" : "100vh",
        overflow: "hidden",
        background: "var(--son-surface-primary)",
        color: "var(--son-text-primary)",
        boxSizing: "border-box",
        ...style,
      }}
      {...rest}
    >
      {timeLabel && (
        <span
          style={{
            position: staticStack ? "static" : "absolute",
            top: "var(--son-space-4)",
            left: "var(--son-margin-page)",
            display: "inline-block",
            padding: staticStack ? "var(--son-space-4) 0 0 var(--son-margin-page)" : 0,
            fontFamily: "var(--son-font-serif)",
            fontSize: "var(--son-text-eyebrow)",
            letterSpacing: "var(--son-tracking-eyebrow)",
            textTransform: "uppercase",
            color: "var(--son-text-primary)",
            zIndex: 2,
          }}
        >
          {timeLabel}
        </span>
      )}
      <div
        ref={trackRef}
        style={
          staticStack
            ? { display: "flex", flexDirection: "column", gap: "var(--son-space-8)", padding: "var(--son-space-8) var(--son-margin-page)" }
            : { display: "flex", alignItems: "center", gap: "var(--son-space-16)", height: "100vh", padding: "0 var(--son-margin-page)", width: "max-content", willChange: "transform" }
        }
      >
        {children}
      </div>
    </section>
  );
}
