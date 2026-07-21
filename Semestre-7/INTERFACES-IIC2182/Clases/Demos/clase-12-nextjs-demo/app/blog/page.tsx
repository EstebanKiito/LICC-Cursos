import { headers } from 'next/headers'
import Link from 'next/link'
import type { Post } from '../api/_data/posts'

type PostsResponse = {
  posts: Post[]
  fetchedAt: string
}

async function getPosts(): Promise<PostsResponse> {
  const h = await headers()
  const host = h.get('host') ?? 'localhost:3000'
  const proto = h.get('x-forwarded-proto') ?? 'http'

  // Cachear con un TAG. El webhook llamará revalidateTag('posts')
  // y este fetch volverá a ejecutarse en la próxima visita.
  const r = await fetch(`${proto}://${host}/api/posts`, {
    next: { tags: ['posts'] },
  })
  return r.json()
}

export default async function BlogPage() {
  const { posts, fetchedAt } = await getPosts()
  const renderedAt = new Date().toLocaleTimeString('es-CL')

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">Blog</h1>
      <p className="opacity-70 mb-2 text-sm">
        Server Component con <code>fetch</code> +{' '}
        <code>{`{ next: { tags: ['posts'] } }`}</code>. Mientras nadie llame a{' '}
        <code>revalidateTag('posts')</code>, esta página sirve <strong>el
        mismo HTML cacheado</strong> sin volver a llamar la API.
      </p>

      <div className="grid grid-cols-2 gap-3 mb-6 text-xs">
        <div className="border border-sky-200 bg-sky-50 rounded px-3 py-2">
          <div className="opacity-70">API fetched (cacheado):</div>
          <code className="font-mono">
            {new Date(fetchedAt).toLocaleTimeString('es-CL')}
          </code>
        </div>
        <div className="border border-purple-200 bg-purple-50 rounded px-3 py-2">
          <div className="opacity-70">Página renderizada (browser):</div>
          <code className="font-mono">{renderedAt}</code>
        </div>
      </div>

      <ul className="space-y-3">
        {posts.map((p) => (
          <li
            key={p.id}
            className="border border-neutral-200 rounded-lg p-4"
          >
            <div className="flex items-baseline justify-between mb-1">
              <h2 className="font-semibold">{p.title}</h2>
              <span className="text-xs opacity-50">
                {new Date(p.publishedAt).toLocaleDateString('es-CL')}
              </span>
            </div>
            <p className="text-sm opacity-80">{p.body}</p>
            <span className="text-xs opacity-40 font-mono">#{p.id}</span>
          </li>
        ))}
      </ul>

      <div className="mt-8 border border-amber-200 bg-amber-50 rounded-lg p-4 text-sm">
        <p className="font-semibold text-amber-700 mb-1">
          Probá el flujo completo del webhook
        </p>
        <ol className="list-decimal pl-5 space-y-1 text-xs">
          <li>Recargá esta página varias veces — el timestamp del API no cambia (cache HIT).</li>
          <li>
            Andá a{' '}
            <Link href="/route-handlers/webhook" className="underline">
              /route-handlers/webhook
            </Link>{' '}
            y dispará <code>post.created</code>.
          </li>
          <li>
            El webhook muta el store y llama <code>revalidateTag('posts')</code>.
          </li>
          <li>Volvé acá y recargá → el API fetched cambió y el post nuevo aparece.</li>
        </ol>
      </div>
    </article>
  )
}
