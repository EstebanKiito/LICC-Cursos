type Post = { id: number; title: string; body: string }

async function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

async function getSlowPosts(): Promise<Post[]> {
  // Fetch real + delay artificial para que el loading state sea visible
  await sleep(2000)
  const r = await fetch(
    'https://jsonplaceholder.typicode.com/posts?_limit=5',
    { cache: 'no-store' } // forzamos dynamic para que se ejecute en cada request
  )
  return r.json()
}

export default async function LoadingDemo() {
  const posts = await getSlowPosts()

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">Loading state — server fetch</h1>
      <p className="opacity-70 mb-4 text-sm">
        Mientras <code>page.tsx</code> esperaba el fetch (~2s), Next mostró
        automáticamente el skeleton de <code>loading.tsx</code> — sin re-renderizar
        el layout.
      </p>

      <ul className="space-y-3">
        {posts.map((p) => (
          <li key={p.id} className="border border-neutral-200 rounded p-3">
            <h2 className="font-bold">{p.title}</h2>
            <p className="text-sm opacity-70">{p.body}</p>
          </li>
        ))}
      </ul>

      <div className="mt-6 text-xs opacity-60 border-l-2 border-neutral-300 pl-3 space-y-1">
        <div>
          Archivo del skeleton:{' '}
          <code>app/data-fetching/loading/loading.tsx</code>
        </div>
        <div>
          Archivo que trae los datos:{' '}
          <code>app/data-fetching/loading/page.tsx</code>
        </div>
      </div>
    </article>
  )
}
