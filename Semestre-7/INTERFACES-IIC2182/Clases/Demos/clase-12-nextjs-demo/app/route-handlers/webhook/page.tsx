import { WebhookSimulator } from './WebhookSimulator'

export default function WebhookDemoPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Webhook</h1>
      <p className="opacity-70 mb-6 text-sm">
        Un sistema externo (simulado acá con un botón) hace <code>POST</code> a
        nuestro endpoint con un secret en el header. El handler valida la firma
        y registra el evento.
      </p>

      <div className="border border-neutral-200 rounded-lg p-4 mb-6 text-sm">
        <p className="font-semibold mb-2">El patrón completo</p>
        <p className="text-xs mb-2">
          Un sistema externo (CMS, Stripe, GitHub) avisa por webhook que algo
          cambió. Nuestra app: <strong>(1)</strong> verifica la firma,{' '}
          <strong>(2)</strong> muta el estado interno y{' '}
          <strong>(3)</strong> llama <code>revalidateTag('posts')</code>. Las
          páginas cacheadas con ese tag se vuelven stale; en la próxima
          visita Next las re-genera.
        </p>
        <code className="block bg-neutral-100 p-2 rounded text-xs">
          POST /api/webhooks/demo
          <br />
          x-demo-signature: demo-secret-iic2182
          <br />
          {`{ "type": "post.created", "title": "...", "body": "..." }`}
        </code>
        <p className="mt-2 opacity-60 text-xs">
          En producción, la firma se calcularía con HMAC y un secret compartido
          entre el sistema externo y tu app.
        </p>
      </div>

      <WebhookSimulator />
    </div>
  )
}
