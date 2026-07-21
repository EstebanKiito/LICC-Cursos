'use client'

import useSWR, { mutate } from 'swr'
import { useState } from 'react'
import Link from 'next/link'
import type { WebhookEvent } from '../../api/_data/webhook-log'

const fetcher = (url: string) => fetch(url).then((r) => r.json())

type EventConfig =
  | {
      type: 'post.created'
      label: string
      payload: { title: string; body: string }
    }
  | { type: 'post.deleted'; label: string; payload: { postId: number } }
  | { type: 'user.signup'; label: string; payload: { email: string } }

const eventConfigs: EventConfig[] = [
  {
    type: 'post.created',
    label: 'Crear post — dispara revalidateTag',
    payload: {
      title: `Hot take ${new Date().toLocaleTimeString('es-CL')}`,
      body: 'Post creado vía webhook desde un CMS imaginario.',
    },
  },
  {
    type: 'post.deleted',
    label: 'Borrar post #3 — dispara revalidateTag',
    payload: { postId: 3 },
  },
  {
    type: 'user.signup',
    label: 'Signup — solo loguea, sin revalidación',
    payload: { email: 'user@uc.cl' },
  },
]

export function WebhookSimulator() {
  const { data: events } = useSWR<WebhookEvent[]>(
    '/api/webhooks/events',
    fetcher,
    { refreshInterval: 2000 },
  )
  const [sending, setSending] = useState<string | null>(null)
  const [useBadSecret, setUseBadSecret] = useState(false)
  const [lastResult, setLastResult] = useState<string | null>(null)

  async function fireEvent(config: EventConfig) {
    setSending(config.type)
    setLastResult(null)

    const res = await fetch('/api/webhooks/demo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-demo-signature': useBadSecret
          ? 'wrong-secret'
          : 'demo-secret-iic2182',
      },
      body: JSON.stringify({ type: config.type, ...config.payload }),
    })

    const json = (await res.json().catch(() => ({}))) as {
      revalidated?: boolean
    }

    setLastResult(
      `${res.status} ${res.statusText}${
        json.revalidated ? ' · revalidateTag("posts") ✓' : ''
      }`,
    )
    setSending(null)
    mutate('/api/webhooks/events')
  }

  async function clearAll() {
    await fetch('/api/webhooks/events', { method: 'DELETE' })
    mutate('/api/webhooks/events')
  }

  return (
    <div>
      <div className="mb-4 flex items-center gap-3 text-sm">
        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={useBadSecret}
            onChange={(e) => setUseBadSecret(e.target.checked)}
          />
          Enviar con firma inválida (probar el 401)
        </label>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-2 mb-2">
        {eventConfigs.map((c) => (
          <button
            key={c.type}
            onClick={() => fireEvent(c)}
            disabled={sending !== null}
            className="bg-sky-600 text-white text-sm px-3 py-2 rounded hover:bg-sky-700 disabled:opacity-50 text-left"
          >
            <div className="font-mono text-xs opacity-80">{c.type}</div>
            <div>{sending === c.type ? '…' : c.label}</div>
          </button>
        ))}
      </div>

      {lastResult && (
        <p className="text-xs opacity-70 mb-2">
          Última respuesta: <code>{lastResult}</code>
        </p>
      )}

      <div className="border border-amber-200 bg-amber-50 rounded p-3 mb-6 text-xs">
        <p className="mb-1">
          <strong>Para ver el efecto del revalidateTag:</strong>
        </p>
        <ol className="list-decimal pl-5 space-y-0.5">
          <li>
            Abrí{' '}
            <Link href="/blog" className="underline" target="_blank">
              /blog
            </Link>{' '}
            en otra tab — vas a ver "API fetched" con un timestamp.
          </li>
          <li>Recargá /blog 2-3 veces — el timestamp NO cambia (cache HIT).</li>
          <li>Volvé acá y dispará <code>post.created</code>.</li>
          <li>
            Recargá /blog → el timestamp cambió y aparece el post nuevo. El
            cache se invalidó por el tag.
          </li>
        </ol>
      </div>

      <div className="flex items-center justify-between mb-2">
        <h2 className="font-semibold">Eventos recibidos</h2>
        <button
          onClick={clearAll}
          className="text-xs text-rose-600 hover:underline"
        >
          Limpiar
        </button>
      </div>

      {!events?.length && (
        <p className="text-sm opacity-60">
          Aún no se recibieron eventos. Dispará uno arriba.
        </p>
      )}

      <ul className="space-y-2">
        {events?.map((event) => (
          <li
            key={event.id}
            className="border border-neutral-200 rounded px-3 py-2"
          >
            <div className="flex items-center justify-between">
              <span className="font-mono text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded">
                {event.type}
              </span>
              <span className="text-xs opacity-50">
                {new Date(event.receivedAt).toLocaleTimeString('es-CL')}
              </span>
            </div>
            <pre className="text-xs mt-1 bg-neutral-50 rounded p-2 overflow-x-auto">
              {JSON.stringify(event.payload, null, 2)}
            </pre>
          </li>
        ))}
      </ul>
    </div>
  )
}
