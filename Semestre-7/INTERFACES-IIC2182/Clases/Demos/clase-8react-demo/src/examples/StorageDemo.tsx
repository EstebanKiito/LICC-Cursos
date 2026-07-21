import { useState, useEffect } from "react";

function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    const saved = localStorage.getItem(key);
    return saved ? (JSON.parse(saved) as T) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue] as const;
}

function useSessionStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    const saved = sessionStorage.getItem(key);
    return saved ? (JSON.parse(saved) as T) : initialValue;
  });

  useEffect(() => {
    sessionStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue] as const;
}

function getCookie(name: string): string | null {
  const match = document.cookie
    .split("; ")
    .find((row) => row.startsWith(`${name}=`));
  return match ? match.split("=")[1] : null;
}

function setCookie(name: string, value: string, maxAgeSec: number) {
  document.cookie = `${name}=${value}; max-age=${maxAgeSec}; path=/`;
}

function deleteCookie(name: string) {
  document.cookie = `${name}=; max-age=0; path=/`;
}

export function StorageDemo() {
  // localStorage — persists across tabs and browser restarts
  const [theme, setTheme] = useLocalStorage<"light" | "dark">("demo-theme", "light");

  // sessionStorage — persists within this tab only
  const [step, setStep] = useSessionStorage<number>("demo-step", 1);

  // Cookies
  const [cookieVal, setCookieVal] = useState(() => getCookie("demo-lang") ?? "");

  const handleSetCookie = (lang: string) => {
    setCookie("demo-lang", lang, 60);
    setCookieVal(lang);
  };

  const handleDeleteCookie = () => {
    deleteCookie("demo-lang");
    setCookieVal("");
  };

  const clearAll = () => {
    localStorage.removeItem("demo-theme");
    sessionStorage.removeItem("demo-step");
    deleteCookie("demo-lang");
    // Reset state — the hooks' effects will re-write these to storage
    setTheme("light");
    setStep(1);
    setCookieVal("");
  };

  return (
    <div>
      <h2>Browser Storage</h2>
      <p style={{ color: "#666", fontSize: 14, marginBottom: 16 }}>
        Change values below, then <strong>reload the page</strong> to see what persists.
        Try opening this page in <strong>another tab</strong> to see localStorage sync.
      </p>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 16 }}>
        {/* localStorage */}
        <div style={{ padding: 16, borderRadius: 8, border: "1px solid #bae6fd", background: "#f0f9ff", minWidth: 0 }}>
          <h3 style={{ margin: "0 0 8px", color: "#0369a1" }}>localStorage</h3>
          <p style={{ fontSize: 13, color: "#666", marginBottom: 12 }}>
            Survives reload + close browser. Shared across all tabs of the same origin.
          </p>
          <div style={{ display: "flex", gap: 8 }}>
            <button
              onClick={() => setTheme("light")}
              style={{
                fontWeight: theme === "light" ? "bold" : "normal",
                background: theme === "light" ? "#0284c7" : "#fff",
                color: theme === "light" ? "#fff" : "#333",
              }}
            >
              Light
            </button>
            <button
              onClick={() => setTheme("dark")}
              style={{
                fontWeight: theme === "dark" ? "bold" : "normal",
                background: theme === "dark" ? "#0284c7" : "#fff",
                color: theme === "dark" ? "#fff" : "#333",
              }}
            >
              Dark
            </button>
          </div>
          <p style={{ fontSize: 12, marginTop: 8, color: "#888" }}>
            Stored: <code>{JSON.stringify(theme)}</code>
          </p>
        </div>

        {/* sessionStorage */}
        <div style={{ padding: 16, borderRadius: 8, border: "1px solid #bbf7d0", background: "#f0fdf4", minWidth: 0 }}>
          <h3 style={{ margin: "0 0 8px", color: "#15803d" }}>sessionStorage</h3>
          <p style={{ fontSize: 13, color: "#666", marginBottom: 12 }}>
            Survives reload, lost on close tab. Each tab has its own copy.
          </p>
          <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
            <button onClick={() => setStep((s) => Math.max(1, s - 1))}>-</button>
            <span>
              Step <strong>{step}</strong> / 5
            </span>
            <button onClick={() => setStep((s) => Math.min(5, s + 1))}>+</button>
          </div>
          <p style={{ fontSize: 12, marginTop: 8, color: "#888" }}>
            Stored: <code>{JSON.stringify(step)}</code>
          </p>
        </div>

        {/* Cookies */}
        <div style={{ padding: 16, borderRadius: 8, border: "1px solid #fecdd3", background: "#fff1f2", minWidth: 0, overflow: "hidden" }}>
          <h3 style={{ margin: "0 0 8px", color: "#be123c" }}>Cookies</h3>
          <p style={{ fontSize: 13, color: "#666", marginBottom: 12 }}>
            Sent to server on every request (60s expiry)
          </p>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
            {["es", "en", "fr"].map((lang) => (
              <button
                key={lang}
                onClick={() => handleSetCookie(lang)}
                style={{
                  fontWeight: cookieVal === lang ? "bold" : "normal",
                  background: cookieVal === lang ? "#be123c" : "#fff",
                  color: cookieVal === lang ? "#fff" : "#333",
                }}
              >
                {lang.toUpperCase()}
              </button>
            ))}
            {cookieVal && <button onClick={handleDeleteCookie}>Clear</button>}
          </div>
          <p style={{ fontSize: 12, marginTop: 8, color: "#888", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
            Cookie: <code>{cookieVal || "(empty)"}</code>
          </p>
        </div>
      </div>

      <button onClick={clearAll} style={{ marginTop: 16 }}>
        Clear all storage
      </button>
    </div>
  );
}
