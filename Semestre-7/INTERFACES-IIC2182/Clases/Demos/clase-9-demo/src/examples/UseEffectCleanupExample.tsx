import { useState, useEffect } from 'react'
import { ExampleLayout, Section } from '../components/ExampleLayout'
import { CodeBlock } from '../components/CodeBlock'

// ─── Demo 1: Timer sin cleanup (memory leak) ─────────────────

function BrokenTimer() {
  const [count, setCount] = useState(0)
  const [active, setActive] = useState(false)
  const [toggleCount, setToggleCount] = useState(0)

  useEffect(() => {
    if (!active) return

    // ❌ Cada vez que active cambia a true, se crea un NUEVO interval
    // pero los anteriores siguen corriendo
    setInterval(() => {
      setCount((c) => c + 1)
    }, 1000)
  }, [active])

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-4">
        <button
          onClick={() => {
            setActive(!active)
            if (!active) setToggleCount((c) => c + 1)
          }}
          className={`px-4 py-2 text-sm rounded-lg text-white ${
            active ? 'bg-red-500 hover:bg-red-600' : 'bg-blue-600 hover:bg-blue-700'
          }`}
        >
          {active ? 'Detener' : 'Iniciar'}
        </button>
        <span className="text-2xl font-bold font-mono">{count}</span>
        {toggleCount > 1 && (
          <span className="text-xs px-2 py-1 bg-red-100 text-red-600 rounded-full">
            iniciado {toggleCount}x — {toggleCount} intervals apilados
          </span>
        )}
      </div>
      <p className="text-xs text-red-500">
        Prueba: presiona Iniciar, luego Detener, luego Iniciar otra vez.
        El contador se acelera porque los intervals anteriores nunca se limpiaron.
      </p>
    </div>
  )
}

// ─── Demo 2: Timer con cleanup (correcto) ────────────────────

function CorrectTimer() {
  const [count, setCount] = useState(0)
  const [active, setActive] = useState(false)

  useEffect(() => {
    if (!active) return

    const id = setInterval(() => {
      setCount((c) => c + 1)
    }, 1000)

    // ✅ Cleanup: limpia el interval antes del próximo effect
    return () => clearInterval(id)
  }, [active])

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-4">
        <button
          onClick={() => setActive(!active)}
          className={`px-4 py-2 text-sm rounded-lg text-white ${
            active ? 'bg-red-500 hover:bg-red-600' : 'bg-green-600 hover:bg-green-700'
          }`}
        >
          {active ? 'Detener' : 'Iniciar'}
        </button>
        <span className="text-2xl font-bold font-mono">{count}</span>
        <span className="text-xs px-2 py-1 bg-green-100 text-green-600 rounded-full">
          siempre 1 interval
        </span>
      </div>
      <p className="text-xs text-green-600">
        Puedes iniciar y detener cuantas veces quieras — siempre hay máximo 1 interval activo.
      </p>
    </div>
  )
}

// ─── Demo 3: Cleanup con dependencias (debounce visual) ──────
// El log se actualiza en el event handler (no en el effect)
// para representar visualmente qué hace React internamente.

function CleanupWithDeps() {
  const [input, setInput] = useState('')
  const [result, setResult] = useState('')
  const [log, setLog] = useState<string[]>([])

  useEffect(() => {
    const timer = setTimeout(() => {
      setResult(input)
    }, 800)

    return () => clearTimeout(timer)
  }, [input])

  const handleChange = (value: string) => {
    // Simula visualmente el ciclo cleanup → setup que React hace internamente
    const newEntries: string[] = []
    if (input) {
      newEntries.push(`🧹 Cleanup: cancelado timer de "${input}"`)
    }
    newEntries.push(`⏱ Setup: timer creado para "${value}"`)
    setLog((prev) => [...prev.slice(-6), ...newEntries])
    setInput(value)
  }

  return (
    <div className="space-y-4">
      <input
        type="text"
        value={input}
        onChange={(e) => handleChange(e.target.value)}
        placeholder="Escribe algo..."
        className="w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <div className="grid grid-cols-2 gap-4">
        <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <div className="text-xs text-blue-500 font-semibold mb-1">Resultado (800ms delay)</div>
          <div className="text-sm font-mono">{result || '(vacío)'}</div>
        </div>
        <div className="p-4 bg-gray-900 rounded-lg max-h-40 overflow-y-auto">
          <div className="text-xs text-gray-500 font-semibold mb-2">Lifecycle log:</div>
          {log.map((entry, i) => (
            <div key={i} className={`text-xs font-mono ${entry.startsWith('🧹') ? 'text-amber-400' : 'text-green-400'}`}>
              {entry}
            </div>
          ))}
          {log.length === 0 && (
            <div className="text-xs text-gray-600">Escribe para ver el log...</div>
          )}
        </div>
      </div>
      <p className="text-xs text-gray-500">
        Cada tecla ejecuta: <span className="text-amber-600 font-semibold">cleanup</span> (cancela timer anterior)
        → <span className="text-green-600 font-semibold">setup</span> (crea timer nuevo).
        Solo el último timer (cuando dejas de escribir 800ms) se ejecuta.
      </p>
    </div>
  )
}

// ─── Demo 4: Mount/Unmount ────────────────────────────────────

function ChildComponent() {
  useEffect(() => {
    console.log('🟢 Effect: componente montado')

    return () => {
      console.log('🔴 Cleanup: componente desmontado')
    }
  }, [])

  return (
    <div className="p-4 bg-green-50 border border-green-200 rounded-lg space-y-2">
      <p className="text-sm font-semibold text-green-800">Componente hijo activo</p>
      <p className="text-xs text-green-600">
        El effect se ejecutó al montar. Abre la consola del navegador (F12) para ver los logs.
      </p>
      <div className="p-2 bg-green-100 rounded text-xs font-mono text-green-700">
        console → 🟢 Effect: componente montado
      </div>
    </div>
  )
}

function MountUnmountDemo() {
  const [show, setShow] = useState(true)

  return (
    <div className="space-y-3">
      <button
        onClick={() => setShow(!show)}
        className="px-4 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700"
      >
        {show ? 'Desmontar hijo' : 'Montar hijo'}
      </button>
      {show ? (
        <ChildComponent />
      ) : (
        <div className="p-4 bg-red-50 border border-red-200 rounded-lg space-y-2">
          <p className="text-sm font-semibold text-red-800">Componente desmontado</p>
          <div className="p-2 bg-red-100 rounded text-xs font-mono text-red-700">
            console → 🔴 Cleanup: componente desmontado
          </div>
        </div>
      )}
      <div className="p-3 bg-amber-50 border border-amber-200 rounded-lg text-xs text-amber-700">
        <span className="font-semibold">Nota (StrictMode):</span> En desarrollo, React ejecuta
        los effects <span className="font-semibold">dos veces</span> (mount → cleanup → mount)
        para ayudarte a detectar bugs de cleanup. Por eso verás el log duplicado.
        En producción solo se ejecuta una vez.
      </div>
    </div>
  )
}

// ─── Página principal ─────────────────────────────────────────

export function UseEffectCleanupExample() {
  return (
    <ExampleLayout
      title="useEffect Cleanup"
      description="La función de retorno que evita memory leaks y efectos acumulados"
    >
      <Section title="¿Qué es la cleanup function?">
        <CodeBlock
          title="Estructura de useEffect con cleanup"
          code={`useEffect(() => {
  // 1. SETUP — se ejecuta al montar y cuando cambian las deps
  const timer = setInterval(() => tick(), 1000)

  // 2. CLEANUP — se ejecuta:
  //    - Antes del próximo setup (cuando deps cambian)
  //    - Cuando el componente se desmonta
  return () => {
    clearInterval(timer)
  }
}, [dependency])`}
        />
      </Section>

      <Section title="❌ Sin cleanup — memory leak">
        <p className="text-sm text-gray-600">
          Cada Iniciar/Detener crea un nuevo <code className="bg-gray-100 px-1 rounded">setInterval</code> sin
          limpiar el anterior. El contador se acelera porque múltiples intervals corren simultáneamente.
        </p>
        <BrokenTimer />
      </Section>

      <Section title="✅ Con cleanup — correcto">
        <p className="text-sm text-gray-600">
          El <code className="bg-gray-100 px-1 rounded">return () =&gt; clearInterval(id)</code> limpia
          el interval anterior antes de crear uno nuevo. Siempre hay máximo 1 activo.
        </p>
        <CorrectTimer />
        <CodeBlock
          title="Timer con cleanup"
          code={`useEffect(() => {
  if (!active) return

  const id = setInterval(() => {
    setCount(c => c + 1)
  }, 1000)

  return () => clearInterval(id) // ← cleanup
}, [active])`}
        />
      </Section>

      <Section title="Cleanup con dependencias — patrón debounce">
        <p className="text-sm text-gray-600">
          Cada tecla dispara un nuevo effect. El cleanup <strong>cancela el timer anterior</strong>,
          así solo el último timer (cuando dejas de escribir) se ejecuta. Observa el log.
        </p>
        <CleanupWithDeps />
        <CodeBlock
          title="Debounce con cleanup"
          code={`useEffect(() => {
  // Cada cambio de input crea un timer
  const timer = setTimeout(() => {
    setResult(input)
  }, 800)

  // Cleanup cancela el timer anterior
  // antes de crear el nuevo
  return () => clearTimeout(timer)
}, [input])
// Tecla 1: crea timer → Tecla 2: cleanup + nuevo timer
// → Tecla 3: cleanup + nuevo timer → 800ms sin teclas: ¡ejecuta!`}
        />
      </Section>

      <Section title="Cleanup al desmontar">
        <p className="text-sm text-gray-600">
          Cuando un componente se desmonta, React ejecuta el cleanup del último effect.
          Abre la consola del navegador (F12) y presiona el botón.
        </p>
        <MountUnmountDemo />
      </Section>

      <Section title="Resumen: cuándo necesitas cleanup">
        <div className="grid grid-cols-2 gap-4">
          <div className="p-4 bg-green-50 border border-green-200 rounded-lg text-sm">
            <p className="font-semibold text-green-700 mb-2">✅ Necesitas cleanup</p>
            <ul className="space-y-1 text-gray-600">
              <li><code className="bg-green-100 px-1 rounded text-xs">setInterval</code> / <code className="bg-green-100 px-1 rounded text-xs">setTimeout</code></li>
              <li><code className="bg-green-100 px-1 rounded text-xs">addEventListener</code></li>
              <li><code className="bg-green-100 px-1 rounded text-xs">fetch</code> con AbortController</li>
              <li>WebSocket connections</li>
              <li>Subscripciones (observables, stores)</li>
            </ul>
          </div>
          <div className="p-4 bg-gray-50 border border-gray-200 rounded-lg text-sm">
            <p className="font-semibold text-gray-700 mb-2">No necesitas cleanup</p>
            <ul className="space-y-1 text-gray-600">
              <li>Actualizar el DOM (React lo maneja)</li>
              <li>Logging / analytics</li>
              <li><code className="bg-gray-100 px-1 rounded text-xs">setState</code> sin efecto secundario</li>
              <li>Operaciones síncronas</li>
            </ul>
          </div>
        </div>
      </Section>
    </ExampleLayout>
  )
}
