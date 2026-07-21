'use client'

import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { useState } from 'react'

type Post = {
  id: number
  title: string
  likes: number
  likedByMe: boolean
}

// Base en memoria (simula un backend)
const initialPosts: Post[] = [
  { id: 1, title: 'Learn Next.js App Router', likes: 12, likedByMe: false },
  { id: 2, title: 'Server Components are wild', likes: 34, likedByMe: true },
  { id: 3, title: 'TanStack Query rocks', likes: 57, likedByMe: false },
]

let fakeDb: Post[] = [...initialPosts]

// Fetch simulado
async function fetchPosts(): Promise<Post[]> {
  await new Promise((r) => setTimeout(r, 300))
  return [...fakeDb]
}

// Mutation simulada con delay + fallo configurable
async function toggleLike({
  id,
  shouldFail,
  delay,
}: {
  id: number
  shouldFail: boolean
  delay: number
}): Promise<Post> {
  await new Promise((r) => setTimeout(r, delay))
  if (shouldFail) throw new Error('Server rechazó el like')

  fakeDb = fakeDb.map((p) =>
    p.id === id
      ? {
          ...p,
          likedByMe: !p.likedByMe,
          likes: p.likes + (p.likedByMe ? -1 : 1),
        }
      : p
  )
  return fakeDb.find((p) => p.id === id)!
}

export default function OptimisticDemo() {
  const [optimistic, setOptimistic] = useState(true)
  const [shouldFail, setShouldFail] = useState(false)
  const [delay, setDelay] = useState(1500)

  const qc = useQueryClient()
  const { data: posts = [], isLoading } = useQuery({
    queryKey: ['optimistic-posts'],
    queryFn: fetchPosts,
  })

  const mutation = useMutation({
    mutationFn: (id: number) => toggleLike({ id, shouldFail, delay }),

    onMutate: async (id) => {
      if (!optimistic) return
      await qc.cancelQueries({ queryKey: ['optimistic-posts'] })
      const previous = qc.getQueryData<Post[]>(['optimistic-posts'])

      qc.setQueryData<Post[]>(['optimistic-posts'], (old) =>
        (old ?? []).map((p) =>
          p.id === id
            ? {
                ...p,
                likedByMe: !p.likedByMe,
                likes: p.likes + (p.likedByMe ? -1 : 1),
              }
            : p
        )
      )

      return { previous }
    },

    onError: (_err, _id, context) => {
      if (optimistic && context?.previous) {
        qc.setQueryData(['optimistic-posts'], context.previous)
      }
    },

    onSettled: () => {
      qc.invalidateQueries({ queryKey: ['optimistic-posts'] })
    },
  })

  const isLikingId =
    mutation.isPending ? (mutation.variables as number) : null

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">Optimistic Updates</h1>
      <p className="opacity-70 mb-4 text-sm">
        Comparar la experiencia con y sin optimistic update. Configurá el delay
        y el fallo simulado para ver qué pasa cuando el server no responde como
        esperás.
      </p>

      <section className="border border-neutral-200 rounded-lg p-3 mb-4 space-y-2 bg-neutral-50">
        <label className="flex items-center gap-2 text-sm">
          <input
            type="checkbox"
            checked={optimistic}
            onChange={(e) => setOptimistic(e.target.checked)}
          />
          <span className="font-bold">Optimistic mode</span>
          <span className="opacity-60 text-xs">
            ({optimistic ? 'actualizo cache antes del fetch' : 'espero respuesta del server'})
          </span>
        </label>
        <label className="flex items-center gap-2 text-sm">
          <input
            type="checkbox"
            checked={shouldFail}
            onChange={(e) => setShouldFail(e.target.checked)}
          />
          <span className="font-bold text-rose-600">Simular fallo</span>
          <span className="opacity-60 text-xs">
            (si está activo y es optimistic, verás el rollback)
          </span>
        </label>
        <label className="flex items-center gap-2 text-sm">
          <span className="font-bold">Delay</span>
          <input
            type="range"
            min="200"
            max="3000"
            step="100"
            value={delay}
            onChange={(e) => setDelay(Number(e.target.value))}
            className="flex-1"
          />
          <span className="text-xs font-mono w-14 text-right">{delay}ms</span>
        </label>
      </section>

      {isLoading && <p>Cargando…</p>}

      <ul className="space-y-2">
        {posts.map((p) => (
          <li
            key={p.id}
            className="border border-neutral-200 rounded p-3 flex items-center justify-between"
          >
            <span>{p.title}</span>
            <button
              onClick={() => mutation.mutate(p.id)}
              disabled={isLikingId === p.id}
              className={`px-3 py-1 rounded border text-sm flex items-center gap-1.5 ${
                p.likedByMe
                  ? 'bg-rose-50 border-rose-300 text-rose-700'
                  : 'bg-white border-neutral-300'
              } ${isLikingId === p.id ? 'opacity-50' : ''}`}
            >
              <span>{p.likedByMe ? '♥' : '♡'}</span>
              <span className="font-mono">{p.likes}</span>
              {isLikingId === p.id && (
                <span className="text-xs opacity-60">…</span>
              )}
            </button>
          </li>
        ))}
      </ul>

      <div className="mt-6 text-xs opacity-70 border-l-2 border-neutral-300 pl-3 space-y-1">
        <div className="font-bold mb-1">Cómo leerlo:</div>
        <div>• <span className="font-bold">Optimistic ON + éxito</span>: el contador cambia al instante.</div>
        <div>• <span className="font-bold">Optimistic OFF + éxito</span>: esperás el delay antes de ver el cambio.</div>
        <div>• <span className="font-bold">Optimistic ON + fallo</span>: el contador cambia, espera el delay, y se revierte (rollback).</div>
        <div>• <span className="font-bold">Optimistic OFF + fallo</span>: esperás y nada cambia.</div>
      </div>
    </article>
  )
}
