'use client'

import { useSuspenseQuery } from '@tanstack/react-query'

async function fetchItemCount(): Promise<{ count: number }> {
  const r = await fetch('/api/items')
  const items = await r.json()
  await new Promise((res) => setTimeout(res, 1500)) // delay artificial
  return { count: items.length }
}

export function ItemCountCard() {
  const { data } = useSuspenseQuery({
    queryKey: ['item-count'],
    queryFn: fetchItemCount,
  })

  return (
    <div className="border border-green-200 bg-green-50 rounded-lg p-4">
      <h2 className="font-semibold mb-2 text-green-700">Item count</h2>
      <p className="font-mono text-2xl">{data.count}</p>
      <p className="text-xs opacity-70 mt-1">
        Con delay artificial de 1.5s para mostrar el fallback
      </p>
    </div>
  )
}
