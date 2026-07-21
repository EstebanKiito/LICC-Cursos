'use client'

import {
  useMutation,
  useQueryClient,
  useSuspenseQuery,
} from '@tanstack/react-query'
import type { ServerInfo } from './types'

async function fetchServerInfo(): Promise<ServerInfo> {
  const r = await fetch('/api/time')
  return r.json()
}

export function ServerTimeCard() {
  const { data } = useSuspenseQuery({
    queryKey: ['server-time'],
    queryFn: fetchServerInfo,
    staleTime: 0,
  })
  const qc = useQueryClient()
  const refetch = useMutation({
    mutationFn: fetchServerInfo,
    onSuccess: (d) => qc.setQueryData(['server-time'], d),
  })

  return (
    <div className="border border-sky-200 bg-sky-50 rounded-lg p-4">
      <h2 className="font-semibold mb-2 text-sky-700">Server time</h2>
      <p className="font-mono text-2xl">
        {new Date(data.timestamp).toLocaleTimeString('es-CL')}
      </p>
      <p className="text-xs opacity-70 mt-1">
        random {data.random.toFixed(4)} · hits {data.hits}
      </p>
      <button
        onClick={() => refetch.mutate()}
        disabled={refetch.isPending}
        className="mt-3 text-xs px-2 py-1 border border-sky-300 rounded hover:bg-sky-100 disabled:opacity-50"
      >
        {refetch.isPending ? 'Actualizando…' : 'Refrescar'}
      </button>
    </div>
  )
}
