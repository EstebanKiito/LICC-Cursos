import { useState, useEffect } from 'react'
import { ExampleLayout, Section } from '../components/ExampleLayout'
import { CodeBlock } from '../components/CodeBlock'

// ─── Hook: useDebounce ────────────────────────────────────────

function useDebounce<T>(value: T, delay: number): T {
  const [debounced, setDebounced] = useState(value)

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay)
    return () => clearTimeout(timer)
  }, [value, delay])

  return debounced
}

// ─── Hook: useLocalStorage ────────────────────────────────────

function useLocalStorage<T>(key: string, initial: T) {
  const [value, setValue] = useState<T>(() => {
    const stored = localStorage.getItem(key)
    return stored ? JSON.parse(stored) : initial
  })

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value))
  }, [key, value])

  return [value, setValue] as const
}

// ─── Demo: useDebounce ────────────────────────────────────────

function DebounceDemo() {
  const [text, setText] = useState('')
  const debouncedText = useDebounce(text, 500)

  return (
    <div className="space-y-4">
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Escribe algo rápido..."
        className="w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <div className="grid grid-cols-2 gap-4">
        <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
          <div className="text-xs text-red-500 font-semibold mb-1">Valor en tiempo real</div>
          <div className="text-sm font-mono">{text || '(vacío)'}</div>
        </div>
        <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
          <div className="text-xs text-green-600 font-semibold mb-1">Valor debounced (500ms)</div>
          <div className="text-sm font-mono">{debouncedText || '(vacío)'}</div>
        </div>
      </div>
      <p className="text-xs text-gray-400">
        El valor debounced se actualiza 500ms después de que dejas de escribir.
        Ideal para búsquedas y filtros.
      </p>
    </div>
  )
}

// ─── Demo: useLocalStorage ────────────────────────────────────

function LocalStorageDemo() {
  const [name, setName] = useLocalStorage('demo-name', '')
  const [count, setCount] = useLocalStorage('demo-count', 0)

  return (
    <div className="space-y-4">
      <div className="flex gap-4">
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Tu nombre..."
          className="flex-1 px-4 py-2.5 rounded-lg border border-gray-200 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          onClick={() => setCount((c) => c + 1)}
          className="px-4 py-2.5 bg-purple-600 text-white text-sm rounded-lg hover:bg-purple-700"
        >
          Contador: {count}
        </button>
      </div>
      <div className="p-4 bg-purple-50 border border-purple-200 rounded-lg text-sm">
        <p>
          <span className="font-semibold">Nombre guardado:</span> {name || '(vacío)'}
        </p>
        <p>
          <span className="font-semibold">Contador guardado:</span> {count}
        </p>
        <p className="text-xs text-purple-500 mt-2">
          Recarga la página (F5) — los valores persisten en localStorage.
        </p>
      </div>
      <button
        onClick={() => {
          setName('')
          setCount(0)
        }}
        className="text-xs text-gray-400 hover:text-gray-600 underline"
      >
        Resetear valores
      </button>
    </div>
  )
}

// ─── Página principal ─────────────────────────────────────────

export function CustomHooksExample() {
  return (
    <ExampleLayout
      title="Custom Hooks"
      description="Extraer lógica reutilizable que usa hooks de React"
    >
      <Section title="useDebounce — retrasar actualizaciones">
        <p className="text-sm text-gray-600">
          Un custom hook que espera a que el usuario deje de escribir antes de actualizar
          el valor. Evita hacer fetch o filtrar en cada tecla.
        </p>
        <DebounceDemo />
        <CodeBlock
          title="useDebounce.ts"
          code={`function useDebounce<T>(value: T, delay: number): T {
  const [debounced, setDebounced] = useState(value)

  useEffect(() => {
    const timer = setTimeout(
      () => setDebounced(value),
      delay
    )
    return () => clearTimeout(timer)
  }, [value, delay])

  return debounced
}

// Uso:
const [query, setQuery] = useState('')
const debouncedQuery = useDebounce(query, 500)
// debouncedQuery se actualiza 500ms después
// de que query deja de cambiar`}
        />
      </Section>

      <Section title="useLocalStorage — persistir estado">
        <p className="text-sm text-gray-600">
          Funciona igual que <code className="bg-gray-100 px-1 rounded">useState</code>,
          pero guarda el valor en localStorage. El estado sobrevive recargas de página.
        </p>
        <LocalStorageDemo />
        <CodeBlock
          title="useLocalStorage.ts"
          code={`function useLocalStorage<T>(
  key: string,
  initial: T
) {
  const [value, setValue] = useState<T>(() => {
    const stored = localStorage.getItem(key)
    return stored ? JSON.parse(stored) : initial
  })

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value))
  }, [key, value])

  return [value, setValue] as const
}

// Uso: idéntico a useState
const [theme, setTheme] = useLocalStorage('theme', 'light')
// Persiste automáticamente en localStorage`}
        />
      </Section>

      <Section title="¿Cuándo crear un custom hook?">
        <div className="grid grid-cols-3 gap-4">
          <div className="p-4 bg-green-50 border border-green-200 rounded-lg text-sm">
            <p className="font-semibold text-green-700 mb-1">✅ Sí</p>
            <p className="text-gray-600">Lógica con useState/useEffect que se repite en 2+ componentes</p>
          </div>
          <div className="p-4 bg-green-50 border border-green-200 rounded-lg text-sm">
            <p className="font-semibold text-green-700 mb-1">✅ Sí</p>
            <p className="text-gray-600">Lógica compleja que oscurece el render del componente</p>
          </div>
          <div className="p-4 bg-red-50 border border-red-200 rounded-lg text-sm">
            <p className="font-semibold text-red-600 mb-1">❌ No</p>
            <p className="text-gray-600">Funciones simples sin hooks — eso es solo una función normal</p>
          </div>
        </div>
      </Section>
    </ExampleLayout>
  )
}
