import Link from "next/link";

export default async function DynamicRoute({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  return (
    <article>
      <h1 className="text-2xl font-bold mb-3">Dynamic Route</h1>
      <p className="opacity-70 mb-4">
        Este archivo vive en <code>app/routing/[slug]/page.tsx</code>. El valor
        de <code>slug</code> viene de la URL.
      </p>

      <div className="border border-neutral-200 rounded-lg p-4 bg-neutral-50">
        <div className="text-sm opacity-60">params.slug =</div>
        <div className="text-2xl font-mono font-bold text-sky-600">{slug}</div>
      </div>

      <div className="mt-6 flex gap-2 text-sm">
        <span className="opacity-70">Probá otras URLs:</span>
        <Link className="underline" href="/routing/1">
          /routing/1
        </Link>
        <Link className="underline" href="/routing/hola">
          /routing/hola
        </Link>
        <Link className="underline" href="/routing/abc-123">
          /routing/abc-123
        </Link>
      </div>
    </article>
  );
}
