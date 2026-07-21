import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

async function logoutAction() {
  'use server'
  const store = await cookies()
  store.delete('demo-session')
  redirect('/login')
}

export default async function ProtectedPage() {
  const store = await cookies()
  const session = store.get('demo-session')?.value

  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Página protegida</h1>
      <p className="opacity-70 mb-6 text-sm">
        Si llegaste acá es porque el middleware encontró tu cookie{' '}
        <code>demo-session</code>. Sin ella, te habría redirigido a{' '}
        <code>/login</code>.
      </p>

      <div className="border border-green-200 bg-green-50 rounded-lg p-4 mb-6">
        <p className="text-sm">
          Hola, <strong>{session}</strong> 👋
        </p>
        <p className="text-xs opacity-70 mt-1">
          (Tu sesión vive en la cookie HttpOnly por 1 hora.)
        </p>
      </div>

      <form action={logoutAction}>
        <button
          type="submit"
          className="text-sm border border-neutral-300 px-4 py-2 rounded hover:bg-neutral-50"
        >
          Cerrar sesión
        </button>
      </form>

      <div className="mt-8 text-xs opacity-60">
        <p>
          <strong>Lo que pasó técnicamente:</strong> en cada request a{' '}
          <code>/protected/*</code>, <code>middleware.ts</code> corrió antes
          que tu page, leyó la cookie, y decidió dejar pasar. Si no hubiera
          existido, habría devuelto un <code>NextResponse.redirect</code>{' '}
          hacia <code>/login?next=/protected</code>.
        </p>
      </div>
    </div>
  )
}
