import { Suspense } from 'react'

export default function StreamingDemoPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Streaming con Suspense</h1>
      <p className="opacity-70 mb-6 text-sm">
        El shell aparece inmediato. Cada sección se revela cuando su fetch
        termina — el server mantiene la conexión abierta y empuja chunks.
      </p>

      <div className="mb-4 text-xs opacity-60">
        <strong>Tip:</strong> abrí DevTools → Network y mirá esta página como
        document. Verás que el HTML sigue llegando después de la primera
        respuesta.
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Suspense fallback={<Skeleton title="Stats" />}>
          <Stats />
        </Suspense>

        <Suspense fallback={<Skeleton title="Activity" />}>
          <Activity />
        </Suspense>

        <Suspense fallback={<Skeleton title="Recommendations" />}>
          <Recommendations />
        </Suspense>
      </div>
    </div>
  )
}

function Skeleton({ title }: { title: string }) {
  return (
    <div className="border border-neutral-200 rounded-lg p-4">
      <h2 className="font-semibold mb-2">{title}</h2>
      <div className="space-y-2">
        <div className="h-3 bg-neutral-100 rounded animate-pulse" />
        <div className="h-3 bg-neutral-100 rounded animate-pulse w-3/4" />
        <div className="h-3 bg-neutral-100 rounded animate-pulse w-1/2" />
      </div>
      <p className="text-xs opacity-50 mt-3">Cargando…</p>
    </div>
  )
}

async function Stats() {
  await new Promise((r) => setTimeout(r, 800))
  return (
    <div className="border border-sky-200 bg-sky-50 rounded-lg p-4">
      <h2 className="font-semibold mb-2 text-sky-700">Stats</h2>
      <p className="text-3xl font-bold">1,247</p>
      <p className="text-sm opacity-70">usuarios activos</p>
      <p className="text-xs opacity-50 mt-3">Llegó después de ~800ms</p>
    </div>
  )
}

async function Activity() {
  await new Promise((r) => setTimeout(r, 2200))
  return (
    <div className="border border-green-200 bg-green-50 rounded-lg p-4">
      <h2 className="font-semibold mb-2 text-green-700">Activity</h2>
      <ul className="text-sm space-y-1">
        <li>• Usuario A creó un item</li>
        <li>• Usuario B descargó CSV</li>
        <li>• Usuario C marcó tarea</li>
      </ul>
      <p className="text-xs opacity-50 mt-3">Llegó después de ~2.2s</p>
    </div>
  )
}

async function Recommendations() {
  await new Promise((r) => setTimeout(r, 4000))
  return (
    <div className="border border-purple-200 bg-purple-50 rounded-lg p-4">
      <h2 className="font-semibold mb-2 text-purple-700">Recommendations</h2>
      <ul className="text-sm space-y-1">
        <li>• Activar notificaciones</li>
        <li>• Completar perfil</li>
        <li>• Invitar a tu equipo</li>
      </ul>
      <p className="text-xs opacity-50 mt-3">Llegó después de ~4s</p>
    </div>
  )
}
