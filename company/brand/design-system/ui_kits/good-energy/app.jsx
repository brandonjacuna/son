/* Good Energy — morning standing-order kit (son.theme.morning)
   Pale Jade ground, Peacock structure, Plum Ink text. The morning expression
   of Sŏn: a standing order, warm because the relationship is assumed.
   No urgency, no countdown, no café signifiers. */
const { Button, Card, Divider, Badge, Checkbox } = window.SNDesignSystem_4d795d;
const { useState } = React;

function Screen({ children }) {
  return (
    <div data-theme="morning" style={{
      height: "100%", background: "var(--son-surface-primary)", color: "var(--son-text-primary)",
      display: "flex", flexDirection: "column", fontFamily: "var(--son-font-body)",
    }}>
      {children}
    </div>
  );
}

function Header() {
  return (
    <div style={{ padding: "20px 24px 0" }}>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <span className="son-eyebrow">Good Energy · seven to eleven</span>
        <span style={{ fontFamily: "var(--son-font-korean)", fontSize: 22, color: "var(--son-glyph)" }}>선</span>
      </div>
    </div>
  );
}

function Standing({ onPlace }) {
  const [oat, setOat] = useState(true);
  return (
    <Screen>
      <Header />
      <div style={{ padding: "24px", flex: 1, overflow: "auto" }}>
        <h1 style={{ fontFamily: "var(--son-font-display)", fontWeight: 400, fontSize: 34, lineHeight: 1.1,
          letterSpacing: "-0.01em", margin: "8px 0 0", maxWidth: "12ch" }}>
          The usual, Mia.
        </h1>

        <Card surface="secondary" padding="md" style={{ marginTop: 24 }}>
          <div className="son-eyebrow" style={{ marginBottom: 14 }}>Your standing order</div>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <span style={{ fontFamily: "var(--son-font-display)", fontSize: 24 }}>Doenjang porridge</span>
            <span style={{ fontFamily: "var(--son-font-body)", fontSize: 16, color: "var(--son-text-secondary)" }}>9</span>
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginTop: 12 }}>
            <span style={{ fontFamily: "var(--son-font-display)", fontSize: 24 }}>Barley tea</span>
            <span style={{ fontFamily: "var(--son-font-body)", fontSize: 16, color: "var(--son-text-secondary)" }}>4</span>
          </div>
          <Divider spacing="md" />
          <Checkbox label="Add the oat porridge" checked={oat} onChange={(e) => setOat(e.target.checked)} />
        </Card>

        <div className="son-eyebrow" style={{ margin: "32px 0 12px" }}>Also at the window</div>
        {[["Rice cake, honey", "6"], ["Soft egg, ganjang", "5"], ["Persimmon, set overnight", "5"]].map(([n, p]) => (
          <div key={n} style={{ display: "flex", justifyContent: "space-between", alignItems: "center",
            padding: "14px 0", borderTop: "1px solid var(--son-border-default)" }}>
            <span style={{ fontFamily: "var(--son-font-body)", fontSize: 17 }}>{n}</span>
            <span style={{ fontFamily: "var(--son-font-body)", fontSize: 15, color: "var(--son-text-secondary)" }}>{p}</span>
          </div>
        ))}
      </div>

      <div style={{ padding: "16px 24px 28px", borderTop: "1px solid var(--son-border-default)" }}>
        <Button variant="primary" fullWidth onClick={onPlace}>Place the standing order</Button>
      </div>
    </Screen>
  );
}

function Ready({ onBack }) {
  return (
    <Screen>
      <Header />
      <div style={{ padding: "24px", flex: 1, display: "flex", flexDirection: "column", justifyContent: "center" }}>
        <Badge variant="accent">Placed</Badge>
        <h1 style={{ fontFamily: "var(--son-font-display)", fontWeight: 400, fontSize: 32, lineHeight: 1.12,
          letterSpacing: "-0.01em", margin: "20px 0 0", maxWidth: "14ch" }}>
          Ready at the window in twenty.
        </h1>
        <p style={{ fontFamily: "var(--son-font-body)", fontWeight: 300, fontSize: 18, lineHeight: 1.55,
          marginTop: 18, maxWidth: "30ch", color: "var(--son-text-secondary)" }}>
          The walk-up. We'll have it warm.
        </p>
      </div>
      <div style={{ padding: "16px 24px 28px" }}>
        <Button variant="secondary" fullWidth onClick={onBack}>Back</Button>
      </div>
    </Screen>
  );
}

function App() {
  const [view, setView] = useState("standing");
  return (
    <IOSDevice>
      {view === "standing" ? <Standing onPlace={() => setView("ready")} /> : <Ready onBack={() => setView("standing")} />}
    </IOSDevice>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
