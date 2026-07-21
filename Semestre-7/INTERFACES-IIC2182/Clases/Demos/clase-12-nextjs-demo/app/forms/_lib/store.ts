import type { Task } from './schema'

export type StoredTask = Task & { id: number; createdAt: string }

let nextId = 1
const tasks: StoredTask[] = []

export function listTasks(): StoredTask[] {
  return [...tasks]
}

export function addTask(data: Task): StoredTask {
  const stored: StoredTask = {
    ...data,
    id: nextId++,
    createdAt: new Date().toISOString(),
  }
  tasks.push(stored)
  return stored
}
