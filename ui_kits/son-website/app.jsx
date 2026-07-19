/* Sŏn — reservation website UI kit
   A type-forward dinner-register site: home → reserve → confirmed.
   Composes the design-system primitives; theme-aware via [data-theme="dinner"]. */
const { Wordmark, Button, Tabs, Input, Select, Checkbox, Divider, Badge, Card } = window.SNDesignSystem_4d795d;
const { useState } = React;

function TopNav({ onReserve, onHome }) {
  return (
    <nav style={{ display: "flex", alignItems: "center", justifyContent: "space-between",
      padding: "28px 56px", borderBottom: "1px solid var(--son-border-default)" }}>
      <button onClick={onHome} style={{ background: "none", border: 0, cursor: "pointer", padding: 0 }}>
        <Wordmark variant="latin" size={26} />
      </button>
      <div style={{ display: "flex", gap: 40, alignItems: "center" }}>
        <span style={{ fontFamily: "var(--son-font-serif)", fontSize: 14, color: "var(--son-text-secondary)" }}>The room</span>
        <span style={{ fontFamily: "var(--son-font-serif)", fontSize: 14, color: "var(--son-text-secondary)" }}>The table</span>
        <span style={{ fontFamily: "var(--son-font-serif)", fontSize: 14, color: "var(--son-text-secondary)" }}>Dayparts</span>
        <Button variant="secondary" size="sm" onClick={onReserve}>Reserve a table</Button>
      </div>
    </nav>
  );
}

function Home({ onReserve }) {
  return (
    <div>
      <section style={{ minHeight: 560, display: "flex", flexDirection: "column", justifyContent: "center",
        padding: "0 56px", position: "relative" }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 12, marginBottom: 44 }}>
          <span style={{ fontFamily: "var(--son-font-wordmark)", fontSize: 84, lineHeight: 1, color: "var(--son-text-primary)" }}>Sŏn</span>
          <span style={{ fontFamily: "var(--son-font-korean)", fontSize: 34, lineHeight: 1, color: "var(--son-glyph)" }}>선</span>
        </div>
        <h1 style={{ fontFamily: "var(--son-font-display)", fontWeight: 400, fontSize: 56, lineHeight: 1.1,
          letterSpacing: "-0.015em", maxWidth: "16ch", color: "var(--son-text-primary)", margin: 0 }}>
          Scored before the fire. A table available tonight.
        </h1>
        <p style={{ fontFamily: "var(--son-font-body)", fontWeight: 300, fontSize: 20, lineHeight: 1.55,
          maxWidth: "44ch", marginTop: 28, color: "var(--son-text-secondary)" }}>
          Most restaurants are pointed at the plate. We are pointed at the relationship.
        </p>
        <div style={{ marginTop: 40, display: "flex", gap: 16 }}>
          <Button variant="primary" onClick={onReserve}>Reserve a table</Button>
          <Button variant="ghost">View the menu</Button>
        </div>
      </section>

      <section style={{ padding: "0 56px 64px" }}>
        <Divider label="선" spacing="lg" />
        <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 28, marginTop: 8 }}>
          {[
            ["Good Energy", "Seven to eleven", "morning"],
            ["Dosi", "Korean lunch, resolved", "dosi"],
            ["Sŏn", "The anchor", "dinner"],
            ["After hours", "The room after the room", "luxe"],
          ].map(([t, s]) => (
            <div key={t}>
              <div className="son-eyebrow" style={{ marginBottom: 10 }}>{s}</div>
              <div style={{ fontFamily: "var(--son-font-display)", fontSize: 26, color: "var(--son-text-primary)" }}>{t}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

function Reserve({ onConfirm, onBack }) {
  const [daypart, setDaypart] = useState("dinner");
  return (
    <section style={{ padding: "56px", display: "grid", gridTemplateColumns: "0.9fr 1.1fr", gap: 72, alignItems: "start" }}>
      <div>
        <div className="son-eyebrow" style={{ marginBottom: 24 }}>Reserve</div>
        <h2 style={{ fontFamily: "var(--son-font-display)", fontWeight: 400, fontSize: 44, lineHeight: 1.1,
          letterSpacing: "-0.012em", maxWidth: "13ch", color: "var(--son-text-primary)", margin: 0 }}>
          We may already have your record.
        </h2>
        <p style={{ fontFamily: "var(--son-font-body)", fontWeight: 300, fontSize: 18, lineHeight: 1.55,
          maxWidth: "38ch", marginTop: 24, color: "var(--son-text-secondary)" }}>
          Enter the email on your table. A returning morning customer is read before being seated.
        </p>
      </div>

      <Card surface="secondary" padding="lg" style={{ maxWidth: 520 }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
          <Input label="Email on the record" type="email" placeholder="mia@" />
          <div>
            <div className="son-eyebrow" style={{ marginBottom: 14 }}>Daypart</div>
            <Tabs value={daypart} onChange={setDaypart} items={[
              { id: "dosi", label: "Dosi" },
              { id: "dinner", label: "Sŏn" },
              { id: "luxe", label: "Late night" },
            ]} />
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
            <Input label="Date" type="text" defaultValue="Sat · Mar 14" />
            <Select label="Party" defaultValue="2">
              <option>1</option><option>2</option><option>3</option>
              <option>4</option><option>5</option><option>6</option>
            </Select>
          </div>
          <Checkbox label="Outdoor seating, if held" defaultChecked />
          <div style={{ display: "flex", gap: 14, marginTop: 4 }}>
            <Button variant="primary" onClick={onConfirm}>Confirm the table</Button>
            <Button variant="ghost" onClick={onBack}>Back</Button>
          </div>
        </div>
      </Card>
    </section>
  );
}

function Confirmed({ onHome }) {
  return (
    <section style={{ padding: "96px 56px", display: "flex", flexDirection: "column", justifyContent: "center", minHeight: 480 }}>
      <Badge variant="accent">Confirmed</Badge>
      <h2 style={{ fontFamily: "var(--son-font-display)", fontWeight: 400, fontSize: 48, lineHeight: 1.1,
        letterSpacing: "-0.012em", maxWidth: "18ch", color: "var(--son-text-primary)", margin: "28px 0 0" }}>
        Your table is confirmed for Saturday at 7.
      </h2>
      <p style={{ fontFamily: "var(--son-font-body)", fontWeight: 300, fontSize: 20, lineHeight: 1.55,
        maxWidth: "40ch", marginTop: 24, color: "var(--son-text-secondary)" }}>
        Outdoor seating, as requested. We'll see you then.
      </p>
      <div style={{ marginTop: 40 }}>
        <Button variant="secondary" onClick={onHome}>Return</Button>
      </div>
    </section>
  );
}

function App() {
  const [view, setView] = useState("home");
  return (
    <div data-theme="dinner" style={{ minHeight: "100vh", background: "var(--son-surface-primary)" }}>
      <TopNav onReserve={() => setView("reserve")} onHome={() => setView("home")} />
      {view === "home" && <Home onReserve={() => setView("reserve")} />}
      {view === "reserve" && <Reserve onConfirm={() => setView("confirmed")} onBack={() => setView("home")} />}
      {view === "confirmed" && <Confirmed onHome={() => setView("home")} />}
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
