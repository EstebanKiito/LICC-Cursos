'use client'

import useSWR, { mutate } from 'swr'
import { useState } from 'react'
import type { Item } from '../api/_data/items'

const fetcher = (url: string) => fetch(url).then((r) => r.json())

export function ItemsClient() {
  const { data, error, isLoading } = useSWR<Item[]>('/api/items', fetcher)
  const [name, setName] = useState('')
  const [posting, setPosting] = useState(false)

  async function createItem(e: React.FormEvent) {
    e.preventDefault()
    if (!name.trim()) return
    setPosting(true)
    await fetch('/api/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name }),
    })
    setName('')
    setPosting(false)
    mutate('/api/items')
  }

  async function deleteItem(id: number) {
    await fetch(`/api/items/${id}`, { method: 'DELETE' })
    mutate('/api/items')
  }

  return (
    <div>
      <form onSubmit={createItem} className="flex gap-2 mb-4">
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Nuevo item"
          className="flex-1 border border-neutral-300 rounded px-3 py-2"
        />
        <button
          type="submit"
          disabled={posting}
          className="bg-sky-600 text-white px-4 py-2 rounded hover:bg-sky-700 disabled:opacity-50"
        >
          {posting ? '...' : 'POST'}
        </button>
      </form>

      {isLoading && <p className="text-sm opacity-60">Cargando…</p>}
      {error && <p className="text-sm text-rose-600">Error al cargar</p>}

      <ul className="space-y-2">
        {data?.map((item) => (
          <li
            key={item.id}
            className="flex items-center justify-between border border-neutral-200 rounded px-3 py-2"
          >
            <div>
              <span className="font-mono text-xs opacity-50 mr-2">
                #{item.id}
              </span>
              <span>{item.name}</span>
              <span className="text-xs opacity-50 ml-2">
                {new Date(item.createdAt).toLocaleString('es-CL')}
              </span>
            </div>
            <button
              onClick={() => deleteItem(item.id)}
              className="text-rose-600 text-sm hover:underline"
            >
              Borrar
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}
