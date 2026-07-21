import { useState, useTransition, useMemo } from "react";
import { ExampleLayout, Section } from "../components/ExampleLayout";
import { CodeBlock } from "../components/CodeBlock";

// ─── Data: 5.000 productos ───────────────────────────────────

const hugeList = Array.from({ length: 5000 }, (_, i) => ({
  id: i,
  name: `Producto ${i} — ${["Laptop", "Mouse", "Teclado", "Monitor", "Auriculares", "Cámara", "Tablet", "Cargador"][i % 8]}`,
}));

// ─── Demo SIN useTransition (laggy) ──────────────────────────

function WithoutTransition() {
  const [value, setValue] = useState("");
  const [filterText, setFilterText] = useState("");

  const handleChange = (newValue: string) => {
    setValue(newValue);
    // ❌ Ambos setState tienen la misma prioridad
    // El filtrado pesado bloquea la actualización del input
    setFilterText(newValue);
  };

  const filtered = useMemo(
    () =>
      hugeList.filter((item) =>
        item.name.toLowerCase().includes(filterText.toLowerCase()),
      ),
    [filterText],
  );

  return (
    <div className="space-y-3">
      <input
        type="text"
        value={value}
        onChange={(e) => handleChange(e.target.value)}
        placeholder="Buscar en 5.000 productos..."
        className="w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <div className="text-xs text-gray-400">{filtered.length} resultados</div>
      <div className="max-h-48 overflow-y-auto space-y-1">
        {filtered.map((item) => (
          <div
            key={item.id}
            className="p-2 bg-white border border-gray-100 rounded text-xs"
          >
            {item.name}
          </div>
        ))}
        {filtered.length > 200 && (
          <p className="text-xs text-gray-400 text-center py-2">
            ...y {filtered.length - 200} más
          </p>
        )}
      </div>
    </div>
  );
}

// ─── Demo CON useTransition (smooth) ─────────────────────────

function WithTransition() {
  const [value, setValue] = useState("");
  const [filterText, setFilterText] = useState("");
  const [isPending, startTransition] = useTransition();

  const handleChange = (newValue: string) => {
    setValue(newValue); // ← urgente: actualiza el input YA

    startTransition(() => {
      // ← no urgente: puede esperar
      setFilterText(newValue);
    });
  };

  const filtered = useMemo(
    () =>
      hugeList.filter((item) =>
        item.name.toLowerCase().includes(filterText.toLowerCase()),
      ),
    [filterText],
  );

  return (
    <div className="space-y-3">
      <input
        type="text"
        value={value}
        onChange={(e) => handleChange(e.target.value)}
        placeholder="Buscar en 5.000 productos..."
        className="w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm focus:outline-none focus:ring-2 focus:ring-green-500"
      />
      <div className="flex items-center gap-2 text-xs">
        <span className="text-gray-400">{filtered.length} resultados</span>
        {isPending && (
          <span className="px-2 py-0.5 bg-amber-100 text-amber-700 rounded-full">
            Filtrando...
          </span>
        )}
      </div>
      <div
        className={`max-h-48 overflow-y-auto space-y-1 transition-opacity ${isPending ? "opacity-60" : ""}`}
      >
        {filtered.slice(0, 200).map((item) => (
          <div
            key={item.id}
            className="p-2 bg-white border border-gray-100 rounded text-xs"
          >
            {item.name}
          </div>
        ))}
        {filtered.length > 200 && (
          <p className="text-xs text-gray-400 text-center py-2">
            ...y {filtered.length - 200} más
          </p>
        )}
      </div>
    </div>
  );
}

// ─── Página principal ─────────────────────────────────────────

export function UseTransitionExample() {
  return (
    <ExampleLayout
      title="useTransition"
      description="Mantener la UI responsiva durante actualizaciones pesadas"
    >
      <Section title="❌ Sin useTransition — input laggy">
        <p className="text-sm text-gray-600">
          Escribe rápido y nota cómo el input se siente lento. Cada tecla filtra
          5.000 productos con la <strong>misma prioridad</strong> que actualizar
          el input, así que React intenta hacer todo junto.
        </p>
        <WithoutTransition />
      </Section>

      <Section title="✅ Con useTransition — input fluido">
        <p className="text-sm text-gray-600">
          Mismo filtrado, pero envuelto en{" "}
          <code className="bg-gray-100 px-1 rounded">startTransition</code>. El
          input responde inmediatamente y el filtrado se hace cuando React tiene
          tiempo. Observa el badge "Filtrando..." y la opacidad reducida.
        </p>
        <WithTransition />
      </Section>

      <Section title="Código">
        <div className="grid grid-cols-2 gap-4">
          <CodeBlock
            title="❌ sin useTransition"
            code={`function App() {
  const [value, setValue] = useState('')
  const [filterText, setFilterText] = useState('')

  const handleChange = (newValue) => {
    setValue(newValue)
    // Misma prioridad → bloquea el input
    setFilterText(newValue)
  }
  // ...
}`}
          />
          <CodeBlock
            title="✅ con useTransition"
            code={`function App() {
  const [value, setValue] = useState('')
  const [filterText, setFilterText] = useState('')
  const [isPending, startTransition] = useTransition()

  const handleChange = (newValue) => {
    setValue(newValue) // urgente

    startTransition(() => {
      setFilterText(newValue) // puede esperar
    })
  }

  return (
    <>
      <input ... />
      {isPending && <p>Filtrando...</p>}
      <List items={filtered} />
    </>
  )
}`}
          />
        </div>
      </Section>
    </ExampleLayout>
  );
}
