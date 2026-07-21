import Link from 'next/link'

const examples = [
  {
    href: '/server-actions/form',
    title: 'Server Action básica con <form>',
    desc: 'El form usa action={...} y el server recibe el FormData. Sin fetch, sin endpoint manual.',
  },
  {
    href: '/server-actions/client',
    title: 'Server Function desde un Client Component',
    desc: 'Llamar la action como función normal desde un botón en "use client" — likes, toggles, drag & drop.',
  },
]

export default function ServerActionsIndex() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Server Actions</h1>
      <p className="opacity-70 mb-6 text-sm">
        Mutaciones sin endpoints manuales. Dos patrones de uso.
      </p>

      <ul className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {examples.map((e) => (
          <li key={e.href}>
            <Link
              href={e.href}
              className="block border border-neutral-200 rounded-lg p-4 hover:border-neutral-400 transition"
            >
              <div className="font-semibold mb-1">{e.title}</div>
              <p className="text-sm opacity-70">{e.desc}</p>
              <code className="text-xs opacity-50">{e.href}</code>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
