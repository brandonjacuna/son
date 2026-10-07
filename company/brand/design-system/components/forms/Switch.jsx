import React from "react";

/**
 * Sŏn switch. A hairline track with a sliding mark. Marks state change only.
 * No spring, no bounce. On state uses the theme accent.
 * Error reads through the message line below — never color alone.
 */
export function Switch({
  label,
  checked,
  defaultChecked,
  onChange,
  disabled = false,
  error,
  id,
  className = "",
  style = {},
  ...rest
}) {
  const fieldId = id || (label ? `son-${String(label).replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return (
    <div className={className} style={{ display: "inline-flex", flexDirection: "column", gap: "6px", ...style }}>
    <label
      htmlFor={fieldId}
      className={`son-control${disabled ? " son-control--disabled" : ""}`}
      style={{ display: "inline-flex", alignItems: "center", gap: "12px", cursor: disabled ? "not-allowed" : "pointer" }}
    >
      <input
        id={fieldId}
        type="checkbox"
        role="switch"
        checked={checked}
        defaultChecked={defaultChecked}
        onChange={onChange}
        disabled={disabled}
        aria-invalid={error ? true : undefined}
        className="son-switch-input"
        style={{ position: "absolute", opacity: 0, width: 1, height: 1 }}
        {...rest}
      />
      <span
        aria-hidden="true"
        className="son-switch-track"
        style={{
          width: 40,
          height: 22,
          flex: "none",
          border: "1px solid var(--son-border-strong)",
          borderRadius: "var(--son-radius-pill)",
          position: "relative",
          transition: "background var(--son-motion-standard) var(--son-ease-standard), border-color var(--son-motion-standard) var(--son-ease-standard)",
        }}
      >
        <span
          className="son-switch-thumb"
          style={{
            position: "absolute",
            top: 2,
            left: 2,
            width: 16,
            height: 16,
            borderRadius: "50%",
            background: "var(--son-text-primary)",
            transition: "transform var(--son-motion-standard) var(--son-ease-standard), background var(--son-motion-standard) var(--son-ease-standard)",
          }}
        />
      </span>
      {label && (
        <span style={{ fontFamily: "var(--son-font-body)", fontSize: "15px", color: "var(--son-text-primary)" }}>{label}</span>
      )}
    </label>
    {error && (
      <span className="son-field-error" style={{ fontFamily: "var(--son-font-body)", fontSize: "var(--son-text-fine)", color: "var(--son-text-primary)" }}>{error}</span>
    )}
    </div>
  );
}
