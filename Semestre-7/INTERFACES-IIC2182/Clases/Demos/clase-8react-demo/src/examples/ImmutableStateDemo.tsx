import { useState } from "react";

interface User {
  name: string;
  age: number;
}

export function ImmutableStateDemo() {
  const [items, setItems] = useState<string[]>(["Apple", "Banana"]);
  const [user, setUser] = useState<User>({ name: "Ana", age: 25 });
  const [input, setInput] = useState("");

  const addItem = () => {
    if (!input.trim()) return;
    // Correct: new array with spread
    setItems([...items, input]);
    setInput("");
  };

  const removeItem = (index: number) => {
    // Correct: filter creates a new array
    setItems(items.filter((_, i) => i !== index));
  };

  const updateName = () => {
    // Correct: new object with spread
    setUser({ ...user, name: "Pedro" });
  };

  return (
    <div>
      <h2>Immutable State</h2>

      <h3>Array (add/remove)</h3>
      <div style={{ display: "flex", gap: 8, marginBottom: 8 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="New item..."
          onKeyDown={(e) => e.key === "Enter" && addItem()}
        />
        <button onClick={addItem}>Add</button>
      </div>
      <ul>
        {items.map((item, i) => (
          <li key={`${item}-${i}`}>
            {item} <button onClick={() => removeItem(i)}>x</button>
          </li>
        ))}
      </ul>

      <h3 style={{ marginTop: 16 }}>Object (update property)</h3>
      <p>
        {user.name}, {user.age}
      </p>
      <button onClick={updateName}>Change name to Pedro</button>
      <button
        onClick={() => setUser({ ...user, name: "Ana" })}
        style={{ marginLeft: 8 }}
      >
        Reset to Ana
      </button>
    </div>
  );
}
