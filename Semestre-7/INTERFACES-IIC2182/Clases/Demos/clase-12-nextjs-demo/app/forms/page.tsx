import { listTasks } from './_lib/store'
import { TaskForm } from './TaskForm'

export default async function FormsDemo() {
  const tasks = listTasks()

  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">react-hook-form + Zod</h1>
      <p className="opacity-70 mb-6 text-sm">
        Un solo <code>schema.ts</code> con Zod valida en el cliente (instant
        feedback) y en el server (autoridad). El form usa <code>useForm</code>{' '}
        + <code>zodResolver</code>; el submit llama una Server Action que
        re-valida con <code>safeParse</code>.
      </p>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <TaskForm />

        <div>
          <h2 className="font-semibold mb-3">Tareas creadas</h2>
          {tasks.length === 0 && (
            <p className="text-sm opacity-60">
              Aún no hay ninguna. Probá el form de la izquierda.
            </p>
          )}

          <ul className="space-y-2">
            {tasks.map((t) => (
              <li
                key={t.id}
                className="border border-neutral-200 rounded-lg p-3 text-sm"
              >
                <div className="flex items-center justify-between mb-1">
                  <span className="font-semibold">{t.title}</span>
                  <span
                    className={`text-xs px-2 py-0.5 rounded ${
                      t.priority === 'high'
                        ? 'bg-rose-100 text-rose-700'
                        : t.priority === 'medium'
                          ? 'bg-amber-100 text-amber-700'
                          : 'bg-sky-100 text-sky-700'
                    }`}
                  >
                    {t.priority}
                  </span>
                </div>
                <div className="text-xs opacity-70">
                  Vence: {new Date(t.dueDate).toLocaleDateString('es-CL')}
                  {t.estimatedHours && ` · ${t.estimatedHours}h estimadas`}
                </div>
                {t.notes && (
                  <p className="text-xs opacity-60 mt-1">{t.notes}</p>
                )}
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="mt-8 text-xs opacity-60 border-t border-neutral-200 pt-4">
        <p className="mb-1">
          <strong>Cosas para probar:</strong>
        </p>
        <ul className="list-disc pl-5 space-y-1">
          <li>Submit con título de 1 carácter → error de cliente.</li>
          <li>Fecha en el pasado → error de cliente.</li>
          <li>
            Título con la palabra <code>test</code> → pasa cliente,{' '}
            <strong>falla en server</strong> y aparece como error inline.
          </li>
          <li>
            Submit válido → la action persiste y la lista de la derecha se
            refresca por <code>revalidatePath</code>.
          </li>
        </ul>
      </div>
    </div>
  )
}
