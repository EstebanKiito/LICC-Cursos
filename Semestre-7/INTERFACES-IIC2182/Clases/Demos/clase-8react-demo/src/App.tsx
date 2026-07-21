import { useState } from "react";
import { CounterDemo } from "./examples/CounterDemo";
import { PropsDemo } from "./examples/PropsDemo";
import { ImmutableStateDemo } from "./examples/ImmutableStateDemo";
import { DerivedStateDemo } from "./examples/DerivedStateDemo";
import { FetchDemo } from "./examples/FetchDemo";
import { ThemeContextDemo } from "./examples/ThemeContextDemo";
import { KeysDemo } from "./examples/KeysDemo";
import { StorageDemo } from "./examples/StorageDemo";

const demos = [
  { name: "Counter (useState)", component: CounterDemo },
  { name: "Props & Callbacks", component: PropsDemo },
  { name: "Immutable State", component: ImmutableStateDemo },
  { name: "Derived State", component: DerivedStateDemo },
  { name: "Fetch (useEffect)", component: FetchDemo },
  { name: "Keys: index vs id", component: KeysDemo },
  { name: "useContext (Theme)", component: ThemeContextDemo },
  { name: "Browser Storage", component: StorageDemo },
] as const;

export default function App() {
  const [activeDemo, setActiveDemo] = useState(0);
  const ActiveComponent = demos[activeDemo].component;

  return (
    <div style={{ maxWidth: 800, margin: "0 auto", padding: 24 }}>
      <h1>IIC2182 - React Demos (Clase 8)</h1>

      <nav style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 24 }}>
        {demos.map((demo, i) => (
          <button
            key={demo.name}
            onClick={() => setActiveDemo(i)}
            style={{
              padding: "8px 16px",
              borderRadius: 8,
              border: "1px solid #ccc",
              background: i === activeDemo ? "#0284c7" : "#fff",
              color: i === activeDemo ? "#fff" : "#333",
              cursor: "pointer",
            }}
          >
            {demo.name}
          </button>
        ))}
      </nav>

      <div style={{ border: "1px solid #e5e7eb", borderRadius: 12, padding: 24 }}>
        <ActiveComponent />
      </div>
    </div>
  );
}
