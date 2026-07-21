export default function Loading() {
  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">Loading state — server fetch</h1>
      <p className="opacity-70 mb-4 text-sm">
        Esta página hace un fetch lento (~2s) para que el loading state sea
        visible. Fijate que el layout (navbar) no se re-renderiza.
      </p>

      <div className="space-y-3">
        {Array.from({ length: 5 }).map((_, i) => (
          <div
            key={i}
            className="border border-neutral-200 rounded p-3 space-y-2"
          >
            <div className="h-5 bg-neutral-200 animate-pulse rounded w-3/4" />
            <div className="h-3 bg-neutral-200 animate-pulse rounded w-full" />
            <div className="h-3 bg-neutral-200 animate-pulse rounded w-5/6" />
          </div>
        ))}
      </div>

      <p className="mt-4 text-xs opacity-50 italic">
        Este skeleton viene de <code>loading.tsx</code> — Next lo muestra
        automáticamente mientras <code>page.tsx</code> resuelve su promise.
      </p>
    </article>
  )
}
