import React from "react";

/**
 * Sŏn checkbox. Square hairline box, fills with the inverse surface when
 * checked. The check is a hairline mark, not a heavy glyph.
 * Error reads through the message line below — never color alone.
 */
export function Checkbox({
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
        checked={checked}
        defaultChecked={defaultChecked}
        onChange={onChange}
        disabled={disabled}
        aria-invalid={error ? true : undefined}
        className="son-checkbox-input"
        style={{ position: "absolute", opacity: 0, width: 1, height: 1 }}
        {...rest}
      />
      <span
        aria-hidden="true"
        className="son-checkbox-box"
        style={{
          width: 18,
          height: 18,
          flex: "none",
          border: "1px solid var(--son-border-strong)",
          borderRadius: "var(--son-radius-xs)",
          display: "inline-flex",
          alignItems: "center",
          justifyContent: "center",
          color: "var(--son-surface-primary)",
          fontSize: 11,
          lineHeight: 1,
          transition: "background var(--son-motion-fast) var(--son-ease-standard)",
        }}
      >
        ✓
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
