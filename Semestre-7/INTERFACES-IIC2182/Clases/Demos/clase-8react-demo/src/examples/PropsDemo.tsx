import { useState } from "react";

interface PersonProps {
  name: string;
  age: number;
}

function Person({ name, age }: PersonProps) {
  return (
    <p>
      {name}, {age} years old
    </p>
  );
}

interface ChildInputProps {
  onChange: (value: string) => void;
}

function ChildInput({ onChange }: ChildInputProps) {
  return (
    <input
      type="text"
      placeholder="Type a name..."
      onChange={(e) => onChange(e.target.value)}
    />
  );
}

export function PropsDemo() {
  const [name, setName] = useState("Ana");

  return (
    <div>
      <h2>Props & Callbacks</h2>

      <h3>Passing props</h3>
      <Person name="Ana" age={25} />
      <Person name="Pedro" age={30} />

      <h3 style={{ marginTop: 16 }}>Callback from child to parent</h3>
      <ChildInput onChange={(value) => setName(value || "Ana")} />
      <p>Parent received: <strong>{name}</strong></p>
    </div>
  );
}
