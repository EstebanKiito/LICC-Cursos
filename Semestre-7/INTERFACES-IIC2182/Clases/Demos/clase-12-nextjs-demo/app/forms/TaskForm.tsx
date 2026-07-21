'use client'

import { useState } from 'react'
import { useForm, type SubmitHandler } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { taskSchema, type Task, type TaskInput } from './_lib/schema'
import { createTaskAction } from './_lib/actions'

export function TaskForm() {
  const [success, setSuccess] = useState<string | null>(null)

  const {
    register,
    handleSubmit,
    setError,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<TaskInput, unknown, Task>({
    resolver: zodResolver(taskSchema),
    defaultValues: {
      title: '',
      priority: 'medium',
      notes: '',
    },
  })

  const onSubmit: SubmitHandler<Task> = async (data) => {
    setSuccess(null)
    const res = await createTaskAction(data)

    if (!res.ok) {
      // Inyectar errores del server en RHF
      Object.entries(res.fieldErrors).forEach(([field, messages]) => {
        if (messages?.[0]) {
          setError(field as keyof Task, {
            type: 'server',
            message: messages[0],
          })
        }
      })
      return
    }

    setSuccess(`Tarea #${res.id} creada`)
    reset()
  }

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-4 border border-neutral-200 rounded-lg p-4"
    >
      <Field label="Título" error={errors.title?.message}>
        <input
          {...register('title')}
          className="w-full border border-neutral-300 rounded px-3 py-2"
          placeholder="Comprar el libro"
        />
      </Field>

      <Field label="Prioridad" error={errors.priority?.message}>
        <select
          {...register('priority')}
          className="w-full border border-neutral-300 rounded px-3 py-2"
        >
          <option value="low">Baja</option>
          <option value="medium">Media</option>
          <option value="high">Alta</option>
        </select>
      </Field>

      <Field label="Vencimiento" error={errors.dueDate?.message}>
        <input
          type="date"
          {...register('dueDate')}
          className="w-full border border-neutral-300 rounded px-3 py-2"
        />
      </Field>

      <Field
        label="Horas estimadas (opcional)"
        error={errors.estimatedHours?.message}
      >
        <input
          type="number"
          step="0.5"
          {...register('estimatedHours')}
          className="w-full border border-neutral-300 rounded px-3 py-2"
        />
      </Field>

      <Field label="Notas (opcional)" error={errors.notes?.message}>
        <textarea
          {...register('notes')}
          rows={3}
          className="w-full border border-neutral-300 rounded px-3 py-2"
        />
      </Field>

      <div className="flex items-center gap-3">
        <button
          type="submit"
          disabled={isSubmitting}
          className="bg-sky-600 text-white px-4 py-2 rounded hover:bg-sky-700 disabled:opacity-50"
        >
          {isSubmitting ? 'Guardando…' : 'Crear tarea'}
        </button>
        {success && (
          <span className="text-sm text-green-600">{success}</span>
        )}
      </div>
    </form>
  )
}

function Field({
  label,
  error,
  children,
}: {
  label: string
  error?: string
  children: React.ReactNode
}) {
  return (
    <label className="block">
      <span className="block text-sm font-medium mb-1">{label}</span>
      {children}
      {error && <p className="text-xs text-rose-600 mt-1">{error}</p>}
    </label>
  )
}
