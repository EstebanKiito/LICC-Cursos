export default function NestedDetails() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Details</h1>
      <p className="opacity-70">
        Este contenido cambia pero el sidebar de la izquierda no se re-renderiza
        — así funcionan los layouts anidados.
      </p>
    </div>
  )
}
