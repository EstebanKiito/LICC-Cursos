import { useState, useEffect, type ComponentType } from 'react'
import { ExampleLayout, Section } from '../components/ExampleLayout'
import { CodeBlock } from '../components/CodeBlock'

// ─── HOC: withLoading ─────────────────────────────────────────
// Agrega un loading state a cualquier componente

function withLoading<P extends object>(
  Component: ComponentType<P>
) {
  return function WithLoading(props: P & { isLoading: boolean }) {
    const { isLoading, ...rest } = props
    if (isLoading) {
      return (
        <div className="flex items-center gap-2 p-4 bg-gray-100 rounded-lg animate-pulse">
          <div className="w-4 h-4 border-2 border-blue-500 border-t-transparent rounded-full animate-spin" />
          <span className="text-sm text-gray-500">Cargando...</span>
        </div>
      )
    }
    return <Component {...(rest as P)} />
  }
}

// ─── HOC: withBorder ──────────────────────────────────────────
// Agrega un borde decorativo a cualquier componente

function withBorder<P extends object>(
  Component: ComponentType<P>,
  color: string = 'blue'
) {
  return function WithBorder(props: P) {
    return (
      <div className={`border-2 border-${color}-300 rounded-lg p-4 bg-${color}-50`}>
        <Component {...props} />
      </div>
    )
  }
}

// ─── Componentes base (simples) ───────────────────────────────

function UserCard({ name, email }: { name: string; email: string }) {
  return (
    <div className="space-y-1">
      <p className="font-semibold text-gray-900">{name}</p>
      <p className="text-sm text-gray-500">{email}</p>
    </div>
  )
}

function ProductCard({ title, price }: { title: string; price: number }) {
  return (
    <div className="space-y-1">
      <p className="font-semibold text-gray-900">{title}</p>
      <p className="text-sm text-green-600 font-mono">${price.toLocaleString()}</p>
    </div>
  )
}

// ─── Componentes envueltos con HOCs ───────────────────────────

const UserCardWithLoading = withLoading(UserCard)
const ProductCardWithLoading = withLoading(ProductCard)
const UserCardWithBorder = withBorder(UserCard, 'blue')
const ProductCardWithBorder = withBorder(ProductCard, 'green')

// ─── Demo 1: withLoading ──────────────────────────────────────

function LoadingDemo() {
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!loading) return
    const timer = setTimeout(() => setLoading(false), 2000)
    return () => clearTimeout(timer)
  }, [loading])

  return (
    <div className="space-y-4">
      <div className="flex gap-3">
        <button
          onClick={() => setLoading(true)}
          className="px-4 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700"
        >
          Simular carga (2s)
        </button>
        <span className={`text-xs px-2 py-1 rounded-full ${loading ? 'bg-amber-100 text-amber-700' : 'bg-green-100 text-green-700'}`}>
          {loading ? 'Cargando...' : 'Listo'}
        </span>
      </div>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <p className="text-xs text-gray-400 mb-2">UserCardWithLoading</p>
          <UserCardWithLoading isLoading={loading} name="María García" email="maria@example.com" />
        </div>
        <div>
          <p className="text-xs text-gray-400 mb-2">ProductCardWithLoading</p>
          <ProductCardWithLoading isLoading={loading} title="MacBook Pro" price={1299990} />
        </div>
      </div>
    </div>
  )
}

// ─── Demo 2: withBorder ───────────────────────────────────────

function BorderDemo() {
  return (
    <div className="grid grid-cols-2 gap-4">
      <div>
        <p className="text-xs text-gray-400 mb-2">UserCard normal</p>
        <UserCard name="Juan Pérez" email="juan@example.com" />
      </div>
      <div>
        <p className="text-xs text-gray-400 mb-2">withBorder(UserCard, 'blue')</p>
        <UserCardWithBorder name="Juan Pérez" email="juan@example.com" />
      </div>
      <div>
        <p className="text-xs text-gray-400 mb-2">ProductCard normal</p>
        <ProductCard title="iPhone 15" price={899990} />
      </div>
      <div>
        <p className="text-xs text-gray-400 mb-2">withBorder(ProductCard, 'green')</p>
        <ProductCardWithBorder title="iPhone 15" price={899990} />
      </div>
    </div>
  )
}

// ─── Página principal ─────────────────────────────────────────

export function HocExample() {
  return (
    <ExampleLayout
      title="Higher-Order Components (HOC)"
      description="Funciones que reciben un componente y retornan uno nuevo con funcionalidad extra"
    >
      <Section title="withLoading — agregar loading state a cualquier componente">
        <p className="text-sm text-gray-600">
          El mismo HOC <code className="bg-gray-100 px-1 rounded">withLoading</code> funciona
          con UserCard, ProductCard, o cualquier otro componente. La lógica de loading se escribe
          una sola vez.
        </p>
        <LoadingDemo />
        <CodeBlock
          title="withLoading.tsx"
          code={`function withLoading<P>(Component: ComponentType<P>) {
  return function WithLoading(
    props: P & { isLoading: boolean }
  ) {
    const { isLoading, ...rest } = props
    if (isLoading) return <Spinner />
    return <Component {...rest as P} />
  }
}

// Uso: envuelve cualquier componente
const UserCardWithLoading = withLoading(UserCard)
const ProductCardWithLoading = withLoading(ProductCard)

<UserCardWithLoading isLoading={true} name="María" />
<ProductCardWithLoading isLoading={false} title="iPhone" />`}
        />
      </Section>

      <Section title="withBorder — envolver con estilo">
        <p className="text-sm text-gray-600">
          Un HOC simple que agrega un borde decorativo. Muestra cómo un HOC puede
          recibir parámetros de configuración además del componente.
        </p>
        <BorderDemo />
        <CodeBlock
          title="withBorder.tsx"
          code={`function withBorder<P>(
  Component: ComponentType<P>,
  color: string = 'blue'
) {
  return function WithBorder(props: P) {
    return (
      <div className={\`border-2 border-\${color}-300 ...\`}>
        <Component {...props} />
      </div>
    )
  }
}

const Fancy = withBorder(UserCard, 'purple')`}
        />
      </Section>

      <Section title="HOCs vs Custom Hooks">
        <div className="grid grid-cols-2 gap-4">
          <div className="p-4 bg-cyan-50 border border-cyan-200 rounded-lg text-sm">
            <p className="font-semibold text-cyan-700 mb-2">HOCs — envolver componentes</p>
            <ul className="space-y-1 text-gray-600">
              <li>Agregan UI alrededor (loading, borders, auth gates)</li>
              <li>Se aplican de forma declarativa en la definición</li>
              <li>Conocidos: <code className="bg-cyan-100 px-1 rounded text-xs">memo()</code>, <code className="bg-cyan-100 px-1 rounded text-xs">forwardRef()</code>, Redux <code className="bg-cyan-100 px-1 rounded text-xs">connect()</code></li>
            </ul>
          </div>
          <div className="p-4 bg-green-50 border border-green-200 rounded-lg text-sm">
            <p className="font-semibold text-green-700 mb-2">Custom Hooks — compartir lógica</p>
            <ul className="space-y-1 text-gray-600">
              <li>Comparten lógica con estado (sin UI adicional)</li>
              <li>Más simples, más fáciles de componer</li>
              <li>Hoy son el approach preferido en la mayoría de casos</li>
            </ul>
          </div>
        </div>
      </Section>
    </ExampleLayout>
  )
}
