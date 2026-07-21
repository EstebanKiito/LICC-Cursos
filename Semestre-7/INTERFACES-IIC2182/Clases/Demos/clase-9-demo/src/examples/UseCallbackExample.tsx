import { useState, useCallback, useRef, memo } from 'react'
import { ExampleLayout, Section } from '../components/ExampleLayout'
import { CodeBlock } from '../components/CodeBlock'

// ─── Componente hijo memorizado ───────────────────────────────
// memo() evita re-renders si las props no cambian.
// Pero si el padre le pasa una función NUEVA cada vez, memo no sirve.

const ExpensiveItem = memo(function ExpensiveItem({
  label,
  onClick,
}: {
  label: string
  onClick: () => void
}) {
  const renderCount = useRef(0)
  renderCount.current++

  return (
    <div className="flex items-center justify-between p-3 bg-white rounded-lg border border-gray-200">
      <span className="text-sm">{label}</span>
      <div className="flex items-center gap-3">
        <span className="text-xs px-2 py-1 rounded-full bg-amber-100 text-amber-700">
          renders: {renderCount.current}
        </span>
        <button
          onClick={onClick}
          className="text-xs px-3 py-1 bg-blue-100 text-blue-700 rounded-lg hover:bg-blue-200"
        >
          Click
        </button>
      </div>
    </div>
  )
})

// ─── Demo SIN useCallback ─────────────────────────────────────

function WithoutUseCallback() {
  const [count, setCount] = useState(0)

  // ❌ Se recrea en cada render → memo no puede optimizar
  const handleClick = () => {
    console.log('clicked')
  }

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-3">
        <button
          onClick={() => setCount((c) => c + 1)}
          className="px-4 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700"
        >
          Counter: {count}
        </button>
        <span className="text-xs text-gray-400">
          Cada click re-renderiza el padre → los hijos también
        </span>
      </div>
      <ExpensiveItem label="Item A" onClick={handleClick} />
      <ExpensiveItem label="Item B" onClick={handleClick} />
      <ExpensiveItem label="Item C" onClick={handleClick} />
    </div>
  )
}

// ─── Demo CON useCallback ─────────────────────────────────────

function WithUseCallback() {
  const [count, setCount] = useState(0)

  // ✅ Misma referencia entre renders → memo funciona
  const handleClick = useCallback(() => {
    console.log('clicked')
  }, [])

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-3">
        <button
          onClick={() => setCount((c) => c + 1)}
          className="px-4 py-2 bg-green-600 text-white text-sm rounded-lg hover:bg-green-700"
        >
          Counter: {count}
        </button>
        <span className="text-xs text-gray-400">
          Cada click re-renderiza el padre → los hijos NO (misma referencia)
        </span>
      </div>
      <ExpensiveItem label="Item A" onClick={handleClick} />
      <ExpensiveItem label="Item B" onClick={handleClick} />
      <ExpensiveItem label="Item C" onClick={handleClick} />
    </div>
  )
}

// ─── Página principal ─────────────────────────────────────────

export function UseCallbackExample() {
  return (
    <ExampleLayout
      title="useCallback"
      description="Estabilizar referencias de funciones entre renders"
    >
      <Section title="❌ Sin useCallback — los hijos se re-renderizan siempre">
        <p className="text-sm text-gray-600">
          Presiona el counter y observa cómo el contador de renders de cada item sube.
          Aunque los items usan <code className="bg-gray-100 px-1 rounded">memo()</code>,
          la función <code className="bg-gray-100 px-1 rounded">handleClick</code> se recrea
          en cada render, así que memo ve una prop "nueva" cada vez.
        </p>
        <WithoutUseCallback />
      </Section>

      <Section title="✅ Con useCallback — los hijos se mantienen estables">
        <p className="text-sm text-gray-600">
          Mismo ejemplo pero con <code className="bg-gray-100 px-1 rounded">useCallback</code>.
          Los items mantienen su render count en 1 porque la referencia de la función no cambia.
        </p>
        <WithUseCallback />
      </Section>

      <Section title="Código">
        <div className="grid grid-cols-2 gap-4">
          <CodeBlock
            title="❌ sin-usecallback.tsx"
            code={`function Parent() {
  const [count, setCount] = useState(0)

  // Se recrea en CADA render
  const handleClick = () => {
    console.log('clicked')
  }

  return (
    <>
      <button onClick={() => setCount(c => c + 1)}>
        {count}
      </button>
      {/* memo() no sirve: handleClick es
          un objeto nuevo cada vez */}
      <MemoizedChild onClick={handleClick} />
    </>
  )
}`}
          />
          <CodeBlock
            title="✅ con-usecallback.tsx"
            code={`function Parent() {
  const [count, setCount] = useState(0)

  // Misma referencia entre renders
  const handleClick = useCallback(() => {
    console.log('clicked')
  }, []) // [] = nunca se recrea

  return (
    <>
      <button onClick={() => setCount(c => c + 1)}>
        {count}
      </button>
      {/* memo() funciona: handleClick
          es siempre el mismo objeto */}
      <MemoizedChild onClick={handleClick} />
    </>
  )
}`}
          />
        </div>
        <CodeBlock
          title="MemoizedChild.tsx"
          code={`const MemoizedChild = memo(function Child({
  onClick
}: {
  onClick: () => void
}) {
  // Solo se re-renderiza si onClick cambia
  return <button onClick={onClick}>Click me</button>
})`}
        />
      </Section>
    </ExampleLayout>
  )
}
