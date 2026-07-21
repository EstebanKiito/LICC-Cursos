'use client'

import { Suspense, useState } from 'react'
import dynamic from 'next/dynamic'

// Importar los Cards SOLO en el cliente — useSuspenseQuery + fetch a una URL
// relativa no funciona durante SSR (no hay base URL en Node).
const ServerTimeCard = dynamic(
  () => import('./ServerTimeCard').then((m) => m.ServerTimeCard),
  { ssr: false },
)
const ItemCountCard = dynamic(
  () => import('./ItemCountCard').then((m) => m.ItemCountCard),
  { ssr: false },
)

export default function TanstackSuspenseDemo() {
  const [seed, setSeed] = useState(0)

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">TanStack Query + Suspense</h1>
      <p className="opacity-70 mb-4 text-sm">
        Con <code>useSuspenseQuery</code>, las queries{' '}
        <span className="font-semibold">tiran un Promise</span> que{' '}
        <code>&lt;Suspense&gt;</code> sabe atrapar — sin <code>isLoading</code>{' '}
        ni <code>data?</code> opcional. Cada componente declara su propio
        skeleton con <code>fallback</code>.
      </p>

      <button
        onClick={() => setSeed((s) => s + 1)}
        className="mb-6 px-3 py-2 bg-purple-600 text-white rounded text-sm hover:bg-purple-700"
      >
        Re-mount sub-árboles (seed = {seed})
      </button>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Suspense
          key={`time-${seed}`}
          fallback={<Skeleton title="Server time" />}
        >
          <ServerTimeCard />
        </Suspense>

        <Suspense
          key={`count-${seed}`}
          fallback={<Skeleton title="Item count" />}
        >
          <ItemCountCard />
        </Suspense>
      </div>

      <div className="mt-6 text-xs opacity-60 border-t border-neutral-200 pt-3">
        <p className="mb-1">
          <strong>Lo que esto demuestra:</strong>
        </p>
        <ul className="list-disc pl-5 space-y-1">
          <li>
            Cada <code>&lt;Suspense&gt;</code> es independiente — el de
            "Server time" aparece antes que el de "Item count" (que tiene
            1.5s de delay artificial).
          </li>
          <li>
            Dentro de los componentes, <code>data</code> está garantizado —
            sin <code>isLoading</code>, sin <code>?.</code>, código limpio.
          </li>
          <li>
            "Re-mount" cambia el <code>key</code> de los Suspense → vuelven a
            ejecutar la query y muestran el fallback.
          </li>
          <li>
            Los Cards están bajo <code>next/dynamic</code> con{' '}
            <code>ssr: false</code> porque <code>useSuspenseQuery</code>{' '}
            requiere window.fetch con URL relativa.
          </li>
        </ul>
      </div>
    </article>
  )
}

function Skeleton({ title }: { title: string }) {
  return (
    <div className="border border-neutral-200 rounded-lg p-4">
      <h2 className="font-semibold mb-2 opacity-50">{title}</h2>
      <div className="space-y-2">
        <div className="h-6 bg-neutral-100 rounded animate-pulse w-1/2" />
        <div className="h-3 bg-neutral-100 rounded animate-pulse w-3/4" />
      </div>
    </div>
  )
}
