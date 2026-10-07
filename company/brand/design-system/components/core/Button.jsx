import React from "react";

/**
 * Sŏn button. Three registers, hairline language, no drop shadow.
 * Primary fills with the inverse surface; secondary is a hairline outline;
 * ghost is type alone. Restraint over decoration.
 */
export function Button({
  variant = "primary",
  size = "md",
  type = "button",
  disabled = false,
  fullWidth = false,
  children,
  className = "",
  style = {},
  ...rest
}) {
  const pad = size === "sm" ? "8px 16px" : size === "lg" ? "16px 32px" : "12px 24px";
  const fs = size === "sm" ? "13px" : size === "lg" ? "16px" : "14px";

  const base = {
    fontFamily: "var(--son-font-serif)",
    fontSize: fs,
    fontWeight: 400,
    letterSpacing: "0.02em",
    lineHeight: 1,
    padding: pad,
    width: fullWidth ? "100%" : undefined,
    border: "1px solid transparent",
    borderRadius: "var(--son-radius-sm)",
    cursor: disabled ? "not-allowed" : "pointer",
    opacity: disabled ? 0.4 : 1,
    transition: "background var(--son-motion-standard) var(--son-ease-standard), color var(--son-motion-standard) var(--son-ease-standard), border-color var(--son-motion-standard) var(--son-ease-standard)",
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: "8px",
    appearance: "none",
    WebkitAppearance: "none",
  };

  const variants = {
    primary: {
      background: "var(--son-surface-inverse)",
      color: "var(--son-surface-primary)",
      borderColor: "var(--son-surface-inverse)",
    },
    secondary: {
      background: "transparent",
      color: "var(--son-text-primary)",
      borderColor: "var(--son-border-strong)",
    },
    ghost: {
      background: "transparent",
      color: "var(--son-text-primary)",
      borderColor: "transparent",
      padding: size === "sm" ? "8px 8px" : size === "lg" ? "16px 12px" : "12px 10px",
    },
  };

  return (
    <button
      type={type}
      disabled={disabled}
      className={`son-btn son-btn--${variant} ${className}`}
      style={{ ...base, ...variants[variant], ...style }}
      {...rest}
    >
      {children}
    </button>
  );
}
