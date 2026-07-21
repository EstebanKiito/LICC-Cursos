import { headers } from 'next/headers'

type ServerInfo = {
  timestamp: string
  random: number
  hits: number
}

async function getServerInfo(): Promise<ServerInfo> {
  // Cache + revalidate explícito. Next guarda esta respuesta en su Data Cache
  // y la sirve sin volver a llamar al endpoint hasta que pasen 10s.
  const h = await headers()
  const host = h.get('host') ?? 'localhost:3000'
  const proto = h.get('x-forwarded-proto') ?? 'http'

  const r = await fetch(`${proto}://${host}/api/time`, {
    next: { revalidate: 10, tags: ['server-info'] },
  })
  return r.json()
}

export default async function ServerFetchDemo() {
  const info = await getServerInfo()
  const renderedAt = new Date().toLocaleTimeString('es-CL')

  return (
    <article>
      <h1 className="text-2xl font-bold mb-2">Server-side Fetch</h1>
      <p className="opacity-70 mb-2 text-sm">
        <code>fetch</code> con{' '}
        <code>{`{ next: { revalidate: 10, tags: ['server-info'] } }`}</code>. El
        endpoint <code>/api/time</code> es dinámico (cambia en cada llamada),
        pero Next lo cachea por 10s.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
        <Stat
          label="Endpoint timestamp"
          value={new Date(info.timestamp).toLocaleTimeString('es-CL')}
          hint="Hora en que /api/time corrió"
          tone="sky"
        />
        <Stat
          label="Random"
          value={info.random.toFixed(6)}
          hint="Número aleatorio del server"
          tone="green"
        />
        <Stat
          label="Hits a /api/time"
          value={info.hits.toString()}
          hint="Cuenta cuántas veces corrió el handler"
          tone="purple"
        />
      </div>

      <div className="border border-neutral-200 rounded-lg p-4 text-sm">
        <p className="mb-2">
          <span className="opacity-60">Página renderizada (browser):</span>{' '}
          <code>{renderedAt}</code>
        </p>
        <ul className="text-xs opacity-70 space-y-1 list-disc pl-5">
          <li>
            Recargá la página varias veces seguidas — el timestamp y el random
            del server <strong>no cambian</strong> (Next sirve el cache).
          </li>
          <li>
            Esperá 10s y recargá — Next revalida y verás valores nuevos.
          </li>
          <li>
            El contador de <code>hits</code> crece <em>solo</em> cuando Next
            efectivamente vuelve a llamar al endpoint, no en cada visita.
          </li>
        </ul>
      </div>
    </article>
  )
}

function Stat({
  label,
  value,
  hint,
  tone,
}: {
  label: string
  value: string
  hint: string
  tone: 'sky' | 'green' | 'purple'
}) {
  const tones = {
    sky: 'border-sky-200 bg-sky-50 text-sky-700',
    green: 'border-green-200 bg-green-50 text-green-700',
    purple: 'border-purple-200 bg-purple-50 text-purple-700',
  }
  return (
    <div className={`border rounded-lg p-4 ${tones[tone]}`}>
      <div className="text-xs opacity-70 mb-1">{label}</div>
      <div className="font-mono text-xl font-bold">{value}</div>
      <div className="text-xs opacity-60 mt-2">{hint}</div>
    </div>
  )
}
