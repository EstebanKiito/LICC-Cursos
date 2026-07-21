import { useState, useMemo } from "react";

export function DerivedStateDemo() {
  const [name, setName] = useState("James");
  const [numbers, setNumbers] = useState(() =>
    Array.from({ length: 1000 }, (_, i) => Math.random() * i),
  );
  const [filter, setFilter] = useState(100);

  // Derived value — no useState needed
  const initial = name[0];

  // useMemo — only recalculates when `filter` changes
  const filteredCount = useMemo(() => {
    console.log("Recalculating filtered count...");
    return numbers.filter((n) => n > filter).length;
  }, [numbers, filter]);

  const reduceNumbers = () => {
    setNumbers(Array.from({ length: 500 }, (_, i) => Math.random() * i));
  };

  return (
    <div>
      <h2>Derived State</h2>

      <h3>Simple derived value (no useState)</h3>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <p>
        Initial: <strong>{initial}</strong> (computed from name, not stored in
        state)
      </p>

      <h3 style={{ marginTop: 16 }}>useMemo (expensive calculation)</h3>
      <p>Filtering 1000 random numbers greater than:</p>
      <input
        type="range"
        min={0}
        max={500}
        value={filter}
        onChange={(e) => setFilter(Number(e.target.value))}
      />
      <span style={{ marginLeft: 8 }}>{filter}</span>
      <p>
        Result: <strong>{filteredCount}</strong> numbers (check console for
        recalculation logs)
      </p>
      <button onClick={reduceNumbers}>Generate fewer numbers (500)</button>
    </div>
  );
}
