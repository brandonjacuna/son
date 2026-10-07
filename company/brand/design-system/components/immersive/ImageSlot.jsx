import React from "react";

const RATIOS = { "full-bleed": null, portrait: "3 / 4", landscape: "16 / 9" };

/**
 * Image container with three sanctioned ratios and a required intentional
 * empty state for when real photography is not yet shot: a flat daypart
 * ground with a small set caption. Never a gray box, never a placeholder
 * texture, never an AI or stock image.
 */
export function ImageSlot({
  ratio = "landscape",
  src,
  alt = "",
  caption,
  emptyCaption = "Photography to come. Found light, no stock, no AI.",
  theme,
  className = "",
  style = {},
  ...rest
}) {
  const bleed = ratio === "full-bleed";
  return (
    <figure
      data-theme={theme}
      className={`son-imageslot ${className}`}
      style={{
        margin: 0,
        position: "relative",
        overflow: "hidden",
        width: bleed ? "100vw" : "100%",
        marginLeft: bleed ? "calc(50% - 50vw)" : 0,
        height: bleed ? "100vh" : "auto",
        aspectRatio: RATIOS[ratio] || undefined,
        background: "var(--son-surface-secondary)",
        ...style,
      }}
      {...rest}
    >
      {src ? (
        <img src={src} alt={alt} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover" }} />
      ) : (
        <span
          style={{
            position: "absolute", left: "var(--son-space-3)", bottom: "var(--son-space-3)",
            fontFamily: "var(--son-font-body)", fontSize: "var(--son-text-fine)",
            letterSpacing: "var(--son-tracking-open)", color: "var(--son-text-primary)",
          }}
        >
          {emptyCaption}
        </span>
      )}
      {src && caption && (
        <figcaption
          style={{
            position: "absolute", left: "var(--son-space-3)", bottom: "var(--son-space-3)",
            fontFamily: "var(--son-font-body)", fontWeight: "var(--son-weight-light)",
            fontSize: "var(--son-text-body)", color: "var(--son-text-on-dark)",
          }}
        >
          {caption}
        </figcaption>
      )}
    </figure>
  );
}
