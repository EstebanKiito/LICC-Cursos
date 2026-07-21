import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

async function loginAction(formData: FormData) {
  'use server'
  const username = (formData.get('username') as string)?.trim()
  if (!username) return

  const store = await cookies()
  store.set('demo-session', username, {
    httpOnly: true,
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60, // 1 hora
  })

  const next = (formData.get('next') as string) || '/protected'
  redirect(next)
}

export default async function LoginPage({
  searchParams,
}: {
  searchParams: Promise<{ next?: string }>
}) {
  const { next } = await searchParams

  return (
    <div className="max-w-sm">
      <h1 className="text-2xl font-bold mb-2">Login</h1>
      <p className="opacity-70 mb-6 text-sm">
        Ingresá cualquier nombre. La action setea una cookie{' '}
        <code>demo-session</code>; el middleware ya verá que tenés sesión y
        dejará pasar a <code>/protected</code>.
      </p>

      <form action={loginAction} className="space-y-3">
        <input type="hidden" name="next" value={next ?? '/protected'} />
        <input
          name="username"
          placeholder="Tu nombre"
          required
          className="w-full border border-neutral-300 rounded px-3 py-2"
        />
        <button
          type="submit"
          className="bg-sky-600 text-white px-4 py-2 rounded hover:bg-sky-700"
        >
          Iniciar sesión
        </button>
      </form>
    </div>
  )
}
