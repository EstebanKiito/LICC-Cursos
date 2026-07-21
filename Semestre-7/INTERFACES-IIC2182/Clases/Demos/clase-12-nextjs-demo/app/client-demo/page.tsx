'use client'

import { useState, useEffect } from 'react'

export default function ClientDemo() {
  const [count, setCount] = useState(0)
  const [now, setNow] = useState<string>('')

  useEffect(() => {
    const t = setInterval(() => setNow(new Date().toLocaleTimeString()), 1000)
    return () => clearInterval(t)
  }, [])

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">Client Component</h1>
      <p className="opacity-70 mb-4 text-sm">
        La primera línea del archivo es <code>&apos;use client&apos;</code>. Se
        hidrata en el cliente — ahora sí se pueden usar hooks, event handlers y
        browser APIs.
      </p>

      <div className="border border-neutral-200 rounded-lg p-4 space-y-3">
        <div>
          <div className="text-sm opacity-60">useState</div>
          <button
            onClick={() => setCount((c) => c + 1)}
            className="mt-1 px-3 py-1 bg-sky-600 text-white rounded"
          >
            clicks: {count}
          </button>
        </div>

        <div>
          <div className="text-sm opacity-60">useEffect + setInterval</div>
          <div className="text-lg font-mono">{now || '—'}</div>
        </div>
      </div>
    </article>
  )
}
