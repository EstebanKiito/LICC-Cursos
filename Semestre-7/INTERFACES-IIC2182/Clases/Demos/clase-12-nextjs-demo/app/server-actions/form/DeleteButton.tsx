'use client'

import { useTransition } from 'react'
import { deleteTaskAction } from '../_lib/actions'

export function DeleteButton({ id }: { id: number }) {
  const [isPending, startTransition] = useTransition()

  return (
    <button
      disabled={isPending}
      onClick={() =>
        startTransition(async () => {
          await deleteTaskAction(id)
        })
      }
      className="text-rose-600 text-sm hover:underline disabled:opacity-50"
    >
      {isPending ? 'Borrando…' : 'Borrar'}
    </button>
  )
}
