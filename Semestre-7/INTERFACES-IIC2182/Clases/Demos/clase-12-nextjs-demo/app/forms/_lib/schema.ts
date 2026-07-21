import { z } from 'zod'

export const taskSchema = z.object({
  title: z
    .string()
    .min(3, 'Mínimo 3 caracteres')
    .max(80, 'Máximo 80 caracteres'),

  priority: z.enum(['low', 'medium', 'high'], {
    message: 'Elegí una prioridad',
  }),

  dueDate: z.coerce
    .date({ message: 'Fecha inválida' })
    .refine((d) => d.getTime() > Date.now(), {
      message: 'La fecha debe ser futura',
    }),

  estimatedHours: z.coerce
    .number({ message: 'Debe ser un número' })
    .positive('Debe ser positivo')
    .max(40, 'Máximo 40 horas')
    .optional(),

  notes: z
    .string()
    .max(500, 'Máximo 500 caracteres')
    .optional(),
})

// Input: lo que el form envía (strings de inputs HTML)
// Output: lo que sale tras la coerción (Date, number)
export type TaskInput = z.input<typeof taskSchema>
export type Task = z.output<typeof taskSchema>
