import Link from 'next/link'

type Example = {
  href: string
  title: string
  desc: string
  tag: 'routing' | 'components' | 'data' | 'actions' | 'api' | 'platform'
}

const examples: Example[] = [
  { href: '/routing/basic', title: 'Routing básico', desc: 'page.tsx + layout.tsx', tag: 'routing' },
  { href: '/routing/nested', title: 'Layouts anidados', desc: 'Layouts que se acumulan', tag: 'routing' },
  { href: '/routing/42', title: 'Dynamic route [id]', desc: 'Params desde la URL', tag: 'routing' },
  { href: '/routing/catch-all/docs/getting-started', title: 'Catch-all [...slug]', desc: 'N segmentos como array', tag: 'routing' },
  { href: '/server-demo', title: 'Server Component', desc: 'async + fetch directo', tag: 'components' },
  { href: '/client-demo', title: 'Client Component', desc: '"use client" + hooks', tag: 'components' },
  { href: '/data-fetching/server', title: 'Fetch server-side', desc: 'cache + revalidate', tag: 'data' },
  { href: '/data-fetching/loading', title: 'Loading state', desc: 'loading.tsx + Suspense', tag: 'data' },
  { href: '/data-fetching/swr', title: 'SWR', desc: 'stale-while-revalidate', tag: 'data' },
  { href: '/data-fetching/tanstack', title: 'TanStack Query', desc: 'queries + mutations', tag: 'data' },
  { href: '/data-fetching/tanstack-suspense', title: 'TanStack + Suspense', desc: 'useSuspenseQuery — sin isLoading, fallback declarativo', tag: 'data' },
  { href: '/data-fetching/optimistic', title: 'Optimistic updates', desc: 'actualizá UI antes de la respuesta', tag: 'data' },
  { href: '/route-handlers', title: 'Route Handlers (CRUD + CSV)', desc: 'GET/POST/DELETE bajo /api/items + export CSV', tag: 'api' },
  { href: '/route-handlers/webhook', title: 'Webhook + revalidateTag', desc: 'CMS dispara webhook → muta store → revalidateTag → /blog se re-renderiza', tag: 'api' },
  { href: '/blog', title: 'Blog (cache + tag)', desc: 'Server Component con fetch tag-cacheado — invalidado por el webhook', tag: 'api' },
  { href: '/streaming', title: 'Streaming con Suspense', desc: 'Tres secciones con fetch lento — el shell aparece ya', tag: 'data' },
  { href: '/server-actions/form', title: 'Server Action con <form>', desc: "form action + 'use server' + revalidatePath", tag: 'actions' },
  { href: '/server-actions/client', title: 'Server Action desde Client Component', desc: 'Llamar la action como función desde un botón', tag: 'actions' },
  { href: '/forms', title: 'react-hook-form + Zod', desc: 'Schema único, validación cliente + server con safeParse', tag: 'actions' },
  { href: '/protected', title: 'Middleware — ruta protegida', desc: 'Redirect a /login si no hay cookie de sesión', tag: 'platform' },
]

const tagStyle: Record<Example['tag'], string> = {
  routing: 'bg-sky-100 text-sky-700',
  components: 'bg-green-100 text-green-700',
  data: 'bg-purple-100 text-purple-700',
  actions: 'bg-amber-100 text-amber-700',
  api: 'bg-cyan-100 text-cyan-700',
  platform: 'bg-rose-100 text-rose-700',
}

export default function Home() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-2">Next.js Demo</h1>
      <p className="opacity-70 mb-8">Un ejemplo por concepto. Clickeá cualquier tarjeta.</p>

      <ul className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {examples.map((e) => (
          <li key={e.href}>
            <Link
              href={e.href}
              className="block border border-neutral-200 rounded-lg p-4 hover:border-neutral-400 transition"
            >
              <div className="flex items-center justify-between mb-1">
                <span className="font-semibold">{e.title}</span>
                <span className={`text-xs px-2 py-0.5 rounded ${tagStyle[e.tag]}`}>
                  {e.tag}
                </span>
              </div>
              <p className="text-sm opacity-70">{e.desc}</p>
              <code className="text-xs opacity-50">{e.href}</code>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
