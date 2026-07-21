'use server'

import { revalidatePath } from 'next/cache'
import { taskSchema, type Task } from './schema'
import { addTask } from './store'

export type ActionResult =
  | { ok: true; id: number }
  | { ok: false; fieldErrors: Partial<Record<keyof Task, string[]>> }

export async function createTaskAction(input: Task): Promise<ActionResult> {
  // Re-validar SIEMPRE en el server — nunca confiar en validación de cliente.
  const result = taskSchema.safeParse(input)

  if (!result.success) {
    return {
      ok: false,
      fieldErrors: result.error.flatten().fieldErrors as Partial<
        Record<keyof Task, string[]>
      >,
    }
  }

  // Regla "server-only": rechazar títulos con la palabra "test"
  // — para mostrar errores que el cliente no puede saber de antemano.
  if (/\btest\b/i.test(result.data.title)) {
    return {
      ok: false,
      fieldErrors: {
        title: ['Los títulos con "test" están reservados (regla del server)'],
      },
    }
  }

  const stored = addTask(result.data)
  revalidatePath('/forms')
  return { ok: true, id: stored.id }
}
