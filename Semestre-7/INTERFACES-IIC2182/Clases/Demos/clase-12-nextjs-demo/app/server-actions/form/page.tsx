import { listTasks } from '../_lib/db'
import { createTaskAction } from '../_lib/actions'
import { DeleteButton } from './DeleteButton'

export default async function ServerActionFormDemo() {
  const tasks = await listTasks()

  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Server Action con &lt;form&gt;</h1>
      <p className="opacity-70 mb-6 text-sm">
        El <code>form action</code> apunta directo a una función con <code>'use server'</code>.
        El componente es un Server Component — no hay <code>'use client'</code>.
      </p>

      <form action={createTaskAction} className="flex gap-2 mb-6">
        <input
          name="title"
          placeholder="Nueva tarea"
          required
          maxLength={80}
          className="flex-1 border border-neutral-300 rounded px-3 py-2"
        />
        <button
          type="submit"
          className="bg-sky-600 text-white px-4 py-2 rounded hover:bg-sky-700"
        >
          Crear
        </button>
      </form>

      <ul className="space-y-2">
        {tasks.map((t) => (
          <li
            key={t.id}
            className="flex items-center justify-between border border-neutral-200 rounded px-3 py-2"
          >
            <span className={t.completed ? 'line-through opacity-50' : ''}>
              {t.title}
            </span>
            <DeleteButton id={t.id} />
          </li>
        ))}
      </ul>

      <div className="mt-8 text-xs opacity-60">
        <p>
          <strong>Lo que pasa:</strong> el form se envía al servidor; la action
          valida, mutea y llama <code>revalidatePath</code>. Next re-renderiza
          esta página con los datos actualizados.
        </p>
      </div>
    </div>
  )
}
