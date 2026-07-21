import { listTasks } from '../_lib/db'
import { TaskRow } from './TaskRow'

export default async function ServerActionClientDemo() {
  const tasks = await listTasks()

  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">
        Server Function desde un Client Component
      </h1>
      <p className="opacity-70 mb-6 text-sm">
        El listado es un Server Component (carga los datos en el server).
        Cada fila es un <code>'use client'</code> que llama la Server Action
        como una función normal — sin <code>fetch</code>, sin endpoint.
      </p>

      <ul className="space-y-2">
        {tasks.map((t) => (
          <TaskRow key={t.id} task={t} />
        ))}
      </ul>

      <div className="mt-8 text-xs opacity-60">
        <p>
          <strong>Lo que pasa:</strong> al hacer click, React llama
          <code> toggleTaskAction(id)</code> como si fuera una función local.
          El bundler la reemplaza por un RPC al server. La función nunca se
          envía al cliente — solo el stub.
        </p>
      </div>
    </div>
  )
}
