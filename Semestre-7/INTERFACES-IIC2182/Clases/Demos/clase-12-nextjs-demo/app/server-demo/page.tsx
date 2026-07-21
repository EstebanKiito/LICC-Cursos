type Post = { id: number; title: string; body: string }

export default async function ServerDemo() {
  // Este fetch ocurre EN EL SERVIDOR. No hay JS para esto en el cliente.
  const posts: Post[] = await fetch(
    'https://jsonplaceholder.typicode.com/posts?_limit=5',
    { next: { revalidate: 60 } }
  ).then((r) => r.json())

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">Server Component</h1>
      <p className="opacity-70 mb-4 text-sm">
        Este componente es <code>async</code> y hace <code>fetch</code> directo.
        El HTML llega listo al cliente — sin <code>useEffect</code>, sin
        spinner intermedio.
      </p>

      <ul className="space-y-3">
        {posts.map((p) => (
          <li key={p.id} className="border border-neutral-200 rounded p-3">
            <h2 className="font-bold">{p.title}</h2>
            <p className="text-sm opacity-70">{p.body}</p>
          </li>
        ))}
      </ul>

      <p className="mt-4 text-xs opacity-50">
        Cache revalida cada 60s (ISR).
      </p>
    </article>
  )
}
