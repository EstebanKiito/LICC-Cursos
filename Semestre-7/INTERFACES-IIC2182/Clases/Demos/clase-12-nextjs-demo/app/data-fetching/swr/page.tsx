'use client'

import useSWR, { mutate } from 'swr'
import { useState } from 'react'
import type { Item } from '../../api/_data/items'

const fetcher = (url: string) => fetch(url).then((r) => r.json())

export default function SwrDemo() {
  const [name, setName] = useState('')
  const { data, error, isLoading, isValidating } = useSWR<Item[]>(
    '/api/items',
    fetcher,
    {
      revalidateOnFocus: true,
      // Polling cada 5s para que se note cuando alguien cambia los datos
      // desde otra pestaña (/route-handlers)
      refreshInterval: 5000,
    },
  )

  async function createItem(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    if (!name.trim()) return
    await fetch('/api/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name }),
    })
    setName('')
    mutate('/api/items') // forzar refetch
  }

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">SWR</h1>
      <p className="opacity-70 mb-4 text-sm">
        <code>useSWR</code> cachea por key (la URL), revalida al volver a la
        tab y hace polling automático. <code>mutate()</code> fuerza refetch.
      </p>

      <div className="flex items-center gap-2 mb-4 text-xs">
        <span
          className={`inline-block w-2 h-2 rounded-full ${
            isValidating ? 'bg-amber-500 animate-pulse' : 'bg-green-500'
          }`}
        />
        <span className="opacity-70">
          {isValidating ? 'Revalidando…' : 'Cache fresco'}
        </span>
        <span className="opacity-50 ml-2">· refresca cada 5s</span>
      </div>

      <form onSubmit={createItem} className="flex gap-2 mb-4">
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Nuevo item"
          className="flex-1 border border-neutral-300 rounded px-3 py-2"
        />
        <button
          type="submit"
          className="bg-sky-600 text-white px-4 py-2 rounded hover:bg-sky-700"
        >
          Crear + mutate()
        </button>
      </form>

      <button
        onClick={() => mutate('/api/items')}
        className="mb-4 px-3 py-1 border border-neutral-300 rounded text-sm"
      >
        Refetch manual
      </button>

      {isLoading && <p className="text-sm opacity-60">Cargando…</p>}
      {error && <p className="text-rose-600">Error al cargar.</p>}

      {data && (
        <ul className="space-y-2">
          {data.map((item) => (
            <li
              key={item.id}
              className="border border-neutral-200 rounded p-2 text-sm flex items-center justify-between"
            >
              <span>
                <span className="font-mono text-xs opacity-50 mr-2">
                  #{item.id}
                </span>
                <span className="font-bold">{item.name}</span>
              </span>
              <span className="text-xs opacity-50">
                {new Date(item.createdAt).toLocaleTimeString('es-CL')}
              </span>
            </li>
          ))}
        </ul>
      )}

      <div className="mt-6 text-xs opacity-60 border-t border-neutral-200 pt-3">
        <p className="mb-1">
          <strong>Probá esto:</strong>
        </p>
        <ul className="list-disc pl-5 space-y-1">
          <li>
            Abrí <code>/route-handlers</code> en otra tab y creá un item ahí.
          </li>
          <li>
            Volvé a esta tab → SWR detecta el focus y hace refetch (verás el
            spinner ámbar).
          </li>
          <li>
            Si te quedás 5s sin tocar nada, igual revalida por el polling.
          </li>
        </ul>
      </div>
    </article>
  )
}
