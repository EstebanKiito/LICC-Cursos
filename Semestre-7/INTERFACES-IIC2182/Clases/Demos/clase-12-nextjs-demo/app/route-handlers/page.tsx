import Link from 'next/link'
import { ItemsClient } from './ItemsClient'

export default function RouteHandlersPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Route Handlers</h1>
      <p className="opacity-70 mb-6 text-sm">
        El cliente nunca toca la "DB" directamente. Habla con tres endpoints
        bajo <code>/api/items</code>, todos corriendo en el server.
      </p>

      <div className="border border-neutral-200 rounded-lg p-4 mb-6">
        <h2 className="font-semibold mb-2">Endpoints expuestos</h2>
        <ul className="text-sm space-y-1 font-mono">
          <li>
            <span className="bg-green-100 text-green-700 px-2 py-0.5 rounded text-xs mr-2">
              GET
            </span>
            /api/items — listar
          </li>
          <li>
            <span className="bg-sky-100 text-sky-700 px-2 py-0.5 rounded text-xs mr-2">
              POST
            </span>
            /api/items — crear
          </li>
          <li>
            <span className="bg-green-100 text-green-700 px-2 py-0.5 rounded text-xs mr-2">
              GET
            </span>
            /api/items/[id] — obtener uno
          </li>
          <li>
            <span className="bg-rose-100 text-rose-700 px-2 py-0.5 rounded text-xs mr-2">
              DEL
            </span>
            /api/items/[id] — borrar
          </li>
          <li>
            <span className="bg-amber-100 text-amber-700 px-2 py-0.5 rounded text-xs mr-2">
              GET
            </span>
            /api/export — descargar CSV (full-stack)
          </li>
        </ul>
      </div>

      <ItemsClient />

      <div className="mt-6 flex gap-3">
        <a
          href="/api/export"
          className="text-sm bg-amber-600 text-white px-4 py-2 rounded hover:bg-amber-700"
        >
          Descargar CSV
        </a>
        <Link
          href="/route-handlers/webhook"
          className="text-sm border border-neutral-300 px-4 py-2 rounded hover:bg-neutral-50"
        >
          Probar webhook →
        </Link>
      </div>
    </div>
  )
}
