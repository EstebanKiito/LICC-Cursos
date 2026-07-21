import { createContext, useContext, useState } from "react";

interface ThemeContextValue {
  theme: "light" | "dark";
  setTheme: (theme: "light" | "dark") => void;
}

const ThemeContext = createContext<ThemeContextValue>({
  theme: "light",
  setTheme: () => {},
});

function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button
      onClick={() => setTheme(theme === "light" ? "dark" : "light")}
      style={{
        padding: "8px 16px",
        borderRadius: 8,
        border: "1px solid",
        background: theme === "dark" ? "#1e293b" : "#fff",
        color: theme === "dark" ? "#e2e8f0" : "#1e293b",
        cursor: "pointer",
      }}
    >
      Toggle Theme (current: {theme})
    </button>
  );
}

function ThemedCard() {
  const { theme } = useContext(ThemeContext);

  return (
    <div
      style={{
        padding: 16,
        borderRadius: 8,
        marginTop: 16,
        background: theme === "dark" ? "#334155" : "#f1f5f9",
        color: theme === "dark" ? "#e2e8f0" : "#1e293b",
      }}
    >
      <p>This card reads the theme from context — no prop drilling needed.</p>
      <p style={{ fontSize: 13, opacity: 0.7 }}>
        ThemedCard does not receive theme as a prop.
      </p>
    </div>
  );
}

export function ThemeContextDemo() {
  const [theme, setTheme] = useState<"light" | "dark">("light");

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <div>
        <h2>useContext (Theme)</h2>
        <p style={{ color: "#666", fontSize: 14, marginBottom: 16 }}>
          ThemeContext.Provider wraps everything — any child can consume it directly
        </p>
        <ThemedButton />
        <ThemedCard />
      </div>
    </ThemeContext.Provider>
  );
}
