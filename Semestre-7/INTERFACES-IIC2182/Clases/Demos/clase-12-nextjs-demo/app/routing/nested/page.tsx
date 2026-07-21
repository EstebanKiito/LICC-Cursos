export default function NestedHome() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-2">Layout anidado — home</h1>
      <p className="opacity-70">
        El sidebar de la izquierda viene del layout en{' '}
        <code>app/routing/nested/layout.tsx</code>. Navegá a "Details" y mirá
        cómo el sidebar persiste sin re-renderizar.
      </p>
    </div>
  )
}
