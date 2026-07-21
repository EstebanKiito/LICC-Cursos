export type Task = {
  id: number
  title: string
  completed: boolean
}

let nextId = 4
const tasks: Task[] = [
  { id: 1, title: 'Leer la clase 13', completed: true },
  { id: 2, title: 'Probar el demo de Server Actions', completed: false },
  { id: 3, title: 'Implementar el proyecto final', completed: false },
]

export async function listTasks(): Promise<Task[]> {
  await new Promise((r) => setTimeout(r, 200))
  return [...tasks]
}

export async function addTask(title: string): Promise<Task> {
  await new Promise((r) => setTimeout(r, 400))
  const task = { id: nextId++, title, completed: false }
  tasks.push(task)
  return task
}

export async function toggleTask(id: number): Promise<Task | null> {
  await new Promise((r) => setTimeout(r, 400))
  const task = tasks.find((t) => t.id === id)
  if (!task) return null
  task.completed = !task.completed
  return task
}

export async function deleteTask(id: number): Promise<void> {
  await new Promise((r) => setTimeout(r, 400))
  const idx = tasks.findIndex((t) => t.id === id)
  if (idx >= 0) tasks.splice(idx, 1)
}
