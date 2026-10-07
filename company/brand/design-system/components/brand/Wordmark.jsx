import React from "react";

/**
 * Sŏn wordmark. Typographic lock-up, never a drawn illustration.
 * "Sŏn" sets in GT Sectra Book; 선 sets in the Korean companion, centered
 * below at a constant scale ratio. Color resolves from the active theme
 * (--son-glyph): Plum Ink on light, Bone on dark. Never Jade.
 */
export function Wordmark({
  variant = "lockup",
  size = 64,
  color,
  glyphColor,
  align = "center",
  className = "",
  style = {},
  ...rest
}) {
  const latinColor = color || "var(--son-text-primary)";
  const markColor = glyphColor || color || "var(--son-glyph)";

  const latin = (
    <span
      style={{
        fontFamily: "var(--son-font-wordmark)",
        fontWeight: 400,
        fontSize: size,
        lineHeight: 1,
        letterSpacing: "0.005em",
        color: latinColor,
      }}
    >
      Sŏn
    </span>
  );

  const glyph = (
    <span
      aria-hidden={variant !== "glyph"}
      style={{
        fontFamily: "var(--son-font-korean)",
        fontWeight: 400,
        fontSize: variant === "glyph" ? size : size * 0.42,
        lineHeight: 1,
        color: markColor,
      }}
    >
      선
    </span>
  );

  if (variant === "latin") {
    return (
      <span className={className} role="img" aria-label="Sŏn" style={{ display: "inline-flex", ...style }} {...rest}>
        {latin}
      </span>
    );
  }

  if (variant === "glyph") {
    return (
      <span className={className} role="img" aria-label="Sŏn" style={{ display: "inline-flex", ...style }} {...rest}>
        {glyph}
      </span>
    );
  }

  // vertical lock-up (primary)
  return (
    <span
      className={className}
      role="img"
      aria-label="Sŏn"
      style={{
        display: "inline-flex",
        flexDirection: "column",
        alignItems: align === "left" ? "flex-start" : align === "right" ? "flex-end" : "center",
        gap: size * 0.26,
        ...style,
      }}
      {...rest}
    >
      {latin}
      {glyph}
    </span>
  );
}
