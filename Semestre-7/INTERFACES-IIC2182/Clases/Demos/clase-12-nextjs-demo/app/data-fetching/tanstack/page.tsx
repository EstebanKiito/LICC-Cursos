'use client'

import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useState } from 'react'
import type { Item } from '../../api/_data/items'

async function fetchItems(): Promise<Item[]> {
  const r = await fetch('/api/items')
  return r.json()
}

async function createItem(name: string): Promise<Item> {
  const r = await fetch('/api/items', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name }),
  })
  if (!r.ok) throw new Error('Create failed')
  return r.json()
}

async function deleteItem(id: number): Promise<void> {
  const r = await fetch(`/api/items/${id}`, { method: 'DELETE' })
  if (!r.ok) throw new Error('Delete failed')
}

export default function TanstackDemo() {
  const qc = useQueryClient()
  const [name, setName] = useState('')

  const query = useQuery({
    queryKey: ['items'],
    queryFn: fetchItems,
  })

  const create = useMutation({
    mutationFn: createItem,
    onSuccess: () => qc.invalidateQueries({ queryKey: ['items'] }),
  })

  const remove = useMutation({
    mutationFn: deleteItem,
    onSuccess: () => qc.invalidateQueries({ queryKey: ['items'] }),
  })

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">TanStack Query</h1>
      <p className="opacity-70 mb-4 text-sm">
        <code>useQuery</code> + <code>useMutation</code> +{' '}
        <code>invalidateQueries</code>. Las mutaciones disparan un refetch
        automático. Abrí los DevTools (ícono flotante abajo a la derecha) para
        ver el cache vivo.
      </p>

      <form
        onSubmit={(e) => {
          e.preventDefault()
          if (!name.trim()) return
          create.mutate(name)
          setName('')
        }}
        className="flex gap-2 mb-4"
      >
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Nuevo item"
          className="border border-neutral-300 rounded px-3 py-2 flex-1"
        />
        <button
          type="submit"
          disabled={create.isPending}
          className="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700 disabled:opacity-50"
        >
          {create.isPending ? 'Creando…' : 'Crear'}
        </button>
      </form>

      {query.isLoading && <p className="text-sm opacity-60">Cargando…</p>}
      {query.error && <p className="text-rose-600">Error</p>}

      {query.data && (
        <ul className="space-y-2">
          {query.data.map((item) => (
            <li
              key={item.id}
              className="border border-neutral-200 rounded p-2 text-sm flex items-center justify-between"
            >
              <span>
                <span className="font-mono text-xs opacity-50 mr-2">
                  #{item.id}
                </span>
                {item.name}
              </span>
              <button
                onClick={() => remove.mutate(item.id)}
                disabled={remove.isPending}
                className="text-rose-600 text-xs hover:underline disabled:opacity-50"
              >
                Borrar
              </button>
            </li>
          ))}
        </ul>
      )}

      <div className="mt-6 text-xs opacity-60 border-t border-neutral-200 pt-3">
        <p>
          <strong>Lo que pasa:</strong> al crear o borrar,{' '}
          <code>invalidateQueries</code> marca <code>['items']</code> como
          stale; TanStack lo detecta y dispara un nuevo <code>fetchItems</code>.
          La lista se actualiza sin refresh manual.
        </p>
      </div>
    </article>
  )
}
