import React from "react";

/**
 * Edge-to-edge section that breaks the page margin. The dark registers
 * (dinner, luxe) are the hero grounds. Immersive surfaces only.
 */
export function FullBleedSection({
  theme,
  ground = "primary",
  as: Tag = "section",
  minHeight = "100vh",
  className = "",
  style = {},
  children,
  ...rest
}) {
  return (
    <Tag
      data-theme={theme}
      className={`son-fullbleed ${className}`}
      style={{
        position: "relative",
        width: "100vw",
        marginLeft: "calc(50% - 50vw)",
        minHeight,
        background: `var(--son-surface-${ground === "inverse" ? "inverse" : ground === "secondary" ? "secondary" : "primary"})`,
        color: ground === "inverse" ? "var(--son-surface-primary)" : "var(--son-text-primary)",
        boxSizing: "border-box",
        padding: "var(--son-space-12) var(--son-margin-page)",
        ...style,
      }}
      {...rest}
    >
      {children}
    </Tag>
  );
}
