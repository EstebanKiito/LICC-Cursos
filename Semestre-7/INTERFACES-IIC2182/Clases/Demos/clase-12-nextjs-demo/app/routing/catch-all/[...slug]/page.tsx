import Link from 'next/link'

export default async function CatchAllRoute({
  params,
}: {
  params: Promise<{ slug: string[] }>
}) {
  const { slug } = await params

  return (
    <article>
      <h1 className="text-2xl font-bold mb-3">Catch-all Route</h1>
      <p className="opacity-70 mb-4">
        Este archivo vive en <code>app/routing/catch-all/[...slug]/page.tsx</code>. El
        prefijo <code>...</code> captura <span className="font-bold">todos los segmentos</span> de
        la URL después de <code>/routing/catch-all/</code> y los entrega como un array.
      </p>

      <div className="border border-neutral-200 rounded-lg p-4 bg-neutral-50 space-y-2">
        <div>
          <div className="text-sm opacity-60">params.slug (array) =</div>
          <pre className="text-sm font-mono bg-white border border-neutral-200 rounded p-2 mt-1">
{JSON.stringify(slug, null, 2)}
          </pre>
        </div>
        <div>
          <div className="text-sm opacity-60">Cantidad de segmentos:</div>
          <div className="text-lg font-mono font-bold text-sky-600">
            {slug.length}
          </div>
        </div>
        <div>
          <div className="text-sm opacity-60">Reconstruido:</div>
          <div className="text-lg font-mono font-bold text-purple-600">
            /{slug.join('/')}
          </div>
        </div>
      </div>

      <div className="mt-6">
        <div className="text-sm opacity-70 mb-2">Probá distintas profundidades:</div>
        <div className="flex flex-wrap gap-2 text-sm">
          <Link
            className="underline px-2 py-1 bg-sky-50 rounded"
            href="/routing/catch-all/docs"
          >
            /catch-all/docs
          </Link>
          <Link
            className="underline px-2 py-1 bg-sky-50 rounded"
            href="/routing/catch-all/docs/getting-started"
          >
            /catch-all/docs/getting-started
          </Link>
          <Link
            className="underline px-2 py-1 bg-sky-50 rounded"
            href="/routing/catch-all/blog/2026/04/hello-world"
          >
            /catch-all/blog/2026/04/hello-world
          </Link>
          <Link
            className="underline px-2 py-1 bg-sky-50 rounded"
            href="/routing/catch-all/a/b/c/d/e/f/g"
          >
            /catch-all/a/b/c/d/e/f/g
          </Link>
        </div>
      </div>

      <div className="mt-6 text-xs opacity-60 border-l-2 border-neutral-300 pl-3">
        <div className="font-bold mb-1">Diferencia con <code>[slug]</code>:</div>
        <div>
          <code>[slug]</code> captura <span className="font-bold">un solo</span> segmento
          como string. <code>[...slug]</code> captura <span className="font-bold">N segmentos</span> como
          array. Se usa para docs, blogs, y rutas jerárquicas de profundidad variable.
        </div>
      </div>
    </article>
  )
}
