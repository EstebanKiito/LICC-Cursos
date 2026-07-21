'use client'

import { useOptimistic, useTransition } from 'react'
import type { Task } from '../_lib/db'
import { toggleTaskAction } from '../_lib/actions'

export function TaskRow({ task }: { task: Task }) {
  const [optimistic, setOptimistic] = useOptimistic(task, (current) => ({
    ...current,
    completed: !current.completed,
  }))
  const [isPending, startTransition] = useTransition()

  return (
    <li className="flex items-center justify-between border border-neutral-200 rounded px-3 py-2">
      <label className="flex items-center gap-3 cursor-pointer flex-1">
        <input
          type="checkbox"
          checked={optimistic.completed}
          disabled={isPending}
          onChange={() => {
            startTransition(async () => {
              setOptimistic(optimistic)
              await toggleTaskAction(task.id)
            })
          }}
        />
        <span className={optimistic.completed ? 'line-through opacity-50' : ''}>
          {optimistic.title}
        </span>
      </label>
      {isPending && <span className="text-xs opacity-50">guardando…</span>}
    </li>
  )
}
