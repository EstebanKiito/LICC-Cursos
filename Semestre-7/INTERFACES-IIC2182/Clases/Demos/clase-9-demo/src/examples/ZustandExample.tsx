/* eslint-disable react-hooks/refs -- render-count tracking is intentional for this teaching demo */
import { useState, createContext, useContext, useRef } from 'react'
import { create } from 'zustand'
import { ExampleLayout, Section } from '../components/ExampleLayout'
import { CodeBlock } from '../components/CodeBlock'

// ─── Zustand Store ────────────────────────────────────────────

interface CounterStore {
  count: number
  name: string
  increment: () => void
  decrement: () => void
  setName: (name: string) => void
}

const useCounterStore = create<CounterStore>((set) => ({
  count: 0,
  name: 'React',
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  setName: (name) => set({ name }),
}))

// ─── Componentes que usan Zustand ─────────────────────────────

function ZustandCounter() {
  const count = useCounterStore((s) => s.count)
  const increment = useCounterStore((s) => s.increment)
  const decrement = useCounterStore((s) => s.decrement)
  const renderCount = useRef(0)
  renderCount.current++

  return (
    <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-blue-800">Componente A: Counter</span>
        <span className="text-xs px-2 py-1 rounded-full bg-blue-100 text-blue-600">
          renders: {renderCount.current}
        </span>
      </div>
      <div className="flex items-center gap-3 mt-3">
        <button onClick={decrement} className="px-3 py-1 bg-blue-600 text-white rounded-lg text-sm">
          -
        </button>
        <span className="text-2xl font-bold text-blue-900 w-12 text-center">{count}</span>
        <button onClick={increment} className="px-3 py-1 bg-blue-600 text-white rounded-lg text-sm">
          +
        </button>
      </div>
    </div>
  )
}

function ZustandDisplay() {
  const count = useCounterStore((s) => s.count)
  const renderCount = useRef(0)
  renderCount.current++

  return (
    <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-green-800">Componente B: Display</span>
        <span className="text-xs px-2 py-1 rounded-full bg-green-100 text-green-600">
          renders: {renderCount.current}
        </span>
      </div>
      <p className="mt-3 text-sm text-green-700">
        El contador es: <span className="text-2xl font-bold">{count}</span>
      </p>
      <p className="text-xs text-green-500 mt-1">
        Lee el mismo store sin ser hijo del Counter
      </p>
    </div>
  )
}

function ZustandNameEditor() {
  const name = useCounterStore((s) => s.name)
  const setName = useCounterStore((s) => s.setName)
  const renderCount = useRef(0)
  renderCount.current++

  return (
    <div className="p-4 bg-purple-50 border border-purple-200 rounded-lg">
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-purple-800">Componente C: Name</span>
        <span className="text-xs px-2 py-1 rounded-full bg-purple-100 text-purple-600">
          renders: {renderCount.current}
        </span>
      </div>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="mt-3 w-full px-3 py-2 rounded-lg border border-purple-200 text-sm focus:outline-none focus:ring-2 focus:ring-purple-500"
      />
      <p className="text-xs text-purple-500 mt-1">
        Solo se re-renderiza cuando <code>name</code> cambia — no cuando <code>count</code> cambia
      </p>
    </div>
  )
}

// ─── Comparación con Context ──────────────────────────────────

const ContextStore = createContext<{ count: number; setCount: (n: number) => void }>({ count: 0, setCount: () => {} })

function ContextDemo() {
  const [count, setCount] = useState(0)

  return (
    <ContextStore.Provider value={{ count, setCount }}>
      <div className="space-y-3">
        <ContextCounter />
        <ContextDisplay />
        <ContextUnrelated />
      </div>
    </ContextStore.Provider>
  )
}

function ContextCounter() {
  const { count, setCount } = useContext(ContextStore)
  const renderCount = useRef(0)
  renderCount.current++

  return (
    <div className="p-4 bg-amber-50 border border-amber-200 rounded-lg">
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-amber-800">Counter (Context)</span>
        <span className="text-xs px-2 py-1 rounded-full bg-amber-100 text-amber-600">
          renders: {renderCount.current}
        </span>
      </div>
      <button
        onClick={() => setCount(count + 1)}
        className="mt-3 px-4 py-2 bg-amber-600 text-white text-sm rounded-lg"
      >
        Count: {count}
      </button>
    </div>
  )
}

function ContextDisplay() {
  const { count } = useContext(ContextStore)
  const renderCount = useRef(0)
  renderCount.current++

  return (
    <div className="p-4 bg-amber-50 border border-amber-200 rounded-lg">
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-amber-800">Display (Context)</span>
        <span className="text-xs px-2 py-1 rounded-full bg-amber-100 text-amber-600">
          renders: {renderCount.current}
        </span>
      </div>
      <p className="mt-2 text-sm">Valor: {count}</p>
    </div>
  )
}

function ContextUnrelated() {
  const renderCount = useRef(0)
  renderCount.current++

  // Este componente NO usa count, pero se re-renderiza igual
  // porque es hijo del Provider que cambia
  return (
    <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-red-800">Componente NO relacionado</span>
        <span className="text-xs px-2 py-1 rounded-full bg-red-100 text-red-600">
          renders: {renderCount.current}
        </span>
      </div>
      <p className="mt-2 text-xs text-red-500">
        ⚠️ Se re-renderiza con cada cambio del Context aunque NO usa el contador
      </p>
    </div>
  )
}

// ─── Página principal ─────────────────────────────────────────

export function ZustandExample() {
  return (
    <ExampleLayout
      title="Zustand"
      description="Estado global simple — un store es un hook, sin providers"
    >
      <Section title="Demo: Estado compartido con selectores">
        <p className="text-sm text-gray-600">
          Tres componentes independientes comparten el mismo store.
          Observa los contadores de render: el componente C (Name) <strong>no</strong> se
          re-renderiza cuando cambias el counter, y viceversa. Eso es gracias a los selectores.
        </p>
        <div className="grid grid-cols-3 gap-4">
          <ZustandCounter />
          <ZustandDisplay />
          <ZustandNameEditor />
        </div>
        <CodeBlock
          title="store.ts"
          code={`import { create } from 'zustand'

const useCounterStore = create<CounterStore>((set) => ({
  count: 0,
  name: 'React',
  increment: () => set(s => ({ count: s.count + 1 })),
  decrement: () => set(s => ({ count: s.count - 1 })),
  setName: (name) => set({ name }),
}))

// En cualquier componente — sin Provider:
const count = useCounterStore(s => s.count)
//          ↑ selector: solo re-renderiza
//            cuando count cambia`}
        />
      </Section>

      <Section title="Comparación: Context (todos se re-renderizan)">
        <p className="text-sm text-gray-600">
          Con Context, <strong>cualquier</strong> cambio re-renderiza todos los consumidores del
          Provider — incluso los que no usan el valor que cambió.
        </p>
        <ContextDemo />
        <p className="text-xs text-gray-400 mt-2">
          Presiona el counter y observa: el componente "no relacionado" también incrementa su
          render count. Con Zustand eso no pasa.
        </p>
      </Section>

      <Section title="Código: Zustand vs Context">
        <div className="grid grid-cols-2 gap-4">
          <CodeBlock
            title="✅ Zustand — 10 líneas"
            code={`// store.ts — ¡eso es todo!
const useStore = create((set) => ({
  count: 0,
  increment: () =>
    set(s => ({ count: s.count + 1 })),
}))

// Componente — sin Provider
function Counter() {
  const count = useStore(s => s.count)
  const inc = useStore(s => s.increment)
  return <button onClick={inc}>{count}</button>
}`}
          />
          <CodeBlock
            title="❌ Context — mucho boilerplate"
            code={`// 1. Crear contexto
const Ctx = createContext(null!)

// 2. Crear provider + estado
function Provider({ children }) {
  const [count, setCount] = useState(0)
  const value = useMemo(
    () => ({ count, setCount }),
    [count]
  )
  return (
    <Ctx.Provider value={value}>
      {children}
    </Ctx.Provider>
  )
}

// 3. Hook wrapper
function useCount() {
  return useContext(Ctx)
}

// 4. Envolver el árbol
<Provider><App /></Provider>`}
          />
        </div>
      </Section>
    </ExampleLayout>
  )
}
