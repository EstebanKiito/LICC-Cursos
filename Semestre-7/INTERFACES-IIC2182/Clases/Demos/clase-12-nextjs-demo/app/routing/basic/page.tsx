export default function BasicRoutingPage() {
  return (
    <article className="prose">
      <h1 className="text-2xl font-bold mb-3">Routing básico</h1>
      <p className="opacity-70 mb-4">
        Este archivo vive en <code>app/routing/basic/page.tsx</code>. La carpeta
        define la URL, el archivo <code>page.tsx</code> hace la ruta accesible.
      </p>
      <p className="text-sm">
        No hay router ni configuración — es pura convención de carpetas.
      </p>
    </article>
  )
}
