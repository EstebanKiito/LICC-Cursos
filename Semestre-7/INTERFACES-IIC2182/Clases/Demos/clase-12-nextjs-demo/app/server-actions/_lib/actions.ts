'use server'

import { revalidatePath } from 'next/cache'
import { addTask, deleteTask, toggleTask } from './db'

export async function createTaskAction(formData: FormData) {
  const title = (formData.get('title') as string)?.trim()
  if (!title || title.length > 80) return

  await addTask(title)
  revalidatePath('/server-actions/form')
  revalidatePath('/server-actions/client')
}

export async function toggleTaskAction(id: number) {
  const task = await toggleTask(id)
  revalidatePath('/server-actions/form')
  revalidatePath('/server-actions/client')
  return task
}

export async function deleteTaskAction(id: number) {
  await deleteTask(id)
  revalidatePath('/server-actions/form')
  revalidatePath('/server-actions/client')
}
