import { useState } from "react";

export function CounterDemo() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
    // count is still the old value here — setState is async!
    console.log("count after setCount immediately:", count);
  };

  const handleDoubleIncrement = () => {
    // Both use the same stale `count` — only increments by 1!
    setCount(count + 1);
    setCount(count + 2);
  };

  const handleDoubleIncrementCorrect = () => {
    // Updater function gets the latest value — increments by 2
    setCount((prev) => prev + 1);
    setCount((prev) => prev + 1);
  };

  console.log("count after setCount:", count);

  return (
    <div>
      <h2>Counter: {count}</h2>
      <p style={{ color: "#666", fontSize: 14 }}>
        Open the console to see that setState is async
      </p>
      <div style={{ display: "flex", gap: 8, marginTop: 16 }}>
        <button onClick={handleClick}>+1 (check console)</button>
        <button onClick={handleDoubleIncrement}>
          +2 broken example (uses stale count)
        </button>
        <button onClick={handleDoubleIncrementCorrect}>
          +2 correct (updater fn)
        </button>
        <button onClick={() => setCount(0)}>Reset</button>
      </div>
    </div>
  );
}
