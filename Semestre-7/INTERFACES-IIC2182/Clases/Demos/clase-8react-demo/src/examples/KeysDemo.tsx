import { useState } from "react";

let nextId = 4;

interface Item {
  id: number;
  name: string;
}

const initialItems: Item[] = [
  { id: 1, name: "Apple" },
  { id: 2, name: "Banana" },
  { id: 3, name: "Cherry" },
];

function ListWithIndexKey({ items, onRemove }: { items: Item[]; onRemove: (id: number) => void }) {
  return (
    <ul style={{ listStyle: "none", padding: 0 }}>
      {items.map((item, index) => (
        <li key={index} style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 8 }}>
          <span style={{ width: 80 }}>{item.name}</span>
          <input placeholder={`Type in ${item.name}...`} />
          <button onClick={() => onRemove(item.id)}>x</button>
        </li>
      ))}
    </ul>
  );
}

function ListWithIdKey({ items, onRemove }: { items: Item[]; onRemove: (id: number) => void }) {
  return (
    <ul style={{ listStyle: "none", padding: 0 }}>
      {items.map((item) => (
        <li key={item.id} style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 8 }}>
          <span style={{ width: 80 }}>{item.name}</span>
          <input placeholder={`Type in ${item.name}...`} />
          <button onClick={() => onRemove(item.id)}>x</button>
        </li>
      ))}
    </ul>
  );
}

export function KeysDemo() {
  const [itemsA, setItemsA] = useState<Item[]>(initialItems);
  const [itemsB, setItemsB] = useState<Item[]>(initialItems);

  const removeA = (id: number) => setItemsA((prev) => prev.filter((i) => i.id !== id));
  const removeB = (id: number) => setItemsB((prev) => prev.filter((i) => i.id !== id));

  const addA = () => {
    const name = `Item ${nextId}`;
    setItemsA((prev) => [{ id: nextId++, name }, ...prev]);
  };
  const addB = () => {
    const name = `Item ${nextId}`;
    setItemsB((prev) => [{ id: nextId++, name }, ...prev]);
  };

  const reset = () => {
    setItemsA(initialItems);
    setItemsB(initialItems);
    nextId = 4;
  };

  return (
    <div>
      <h2>Keys: index vs id</h2>
      <p style={{ color: "#666", fontSize: 14, marginBottom: 16 }}>
        Type something in each input, then delete the <strong>first</strong> item.
        Watch how the inputs behave differently.
      </p>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
        <div>
          <h3 style={{ color: "#dc2626" }}>key=index (broken)</h3>
          <ListWithIndexKey items={itemsA} onRemove={removeA} />
          <button onClick={addA}>Add to top</button>
        </div>
        <div>
          <h3 style={{ color: "#16a34a" }}>key=item.id (correct)</h3>
          <ListWithIdKey items={itemsB} onRemove={removeB} />
          <button onClick={addB}>Add to top</button>
        </div>
      </div>

      <button onClick={reset} style={{ marginTop: 16 }}>Reset both</button>

      <div
        style={{
          marginTop: 20,
          padding: 12,
          background: "#fef9c3",
          borderRadius: 8,
          fontSize: 13,
          border: "1px solid #fde68a",
        }}
      >
        <strong>What happens:</strong> With key=index, when you delete "Apple" (index 0),
        React thinks index 0 is now "Banana" — but the old input DOM stays in place.
        The text you typed in "Apple" now appears next to "Banana". With key=id,
        React correctly removes the DOM for the deleted item.
      </div>
    </div>
  );
}
