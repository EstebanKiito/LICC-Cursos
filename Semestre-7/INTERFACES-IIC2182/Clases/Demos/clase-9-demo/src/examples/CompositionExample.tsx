import { useState } from 'react'
import { ExampleLayout, Section } from '../components/ExampleLayout'
import { CodeBlock } from '../components/CodeBlock'

// ─── Ejemplo MALO: Prop Drilling ──────────────────────────────

function RigidCard({
  title,
  subtitle,
  body,
  footer,
  color,
}: {
  title: string
  subtitle: string
  body: string
  footer: string
  color: string
}) {
  return (
    <div className={`border-2 rounded-lg overflow-hidden ${color}`}>
      <div className="p-4 border-b border-gray-200 bg-gray-50">
        <h3 className="font-bold">{title}</h3>
        <p className="text-xs text-gray-500">{subtitle}</p>
      </div>
      <div className="p-4 text-sm">{body}</div>
      <div className="p-3 bg-gray-50 text-xs text-gray-400">{footer}</div>
    </div>
  )
}

// ─── Ejemplo BUENO: Composición con children ──────────────────

function FlexibleCard({
  children,
  header,
}: {
  children: React.ReactNode
  header: React.ReactNode
}) {
  return (
    <div className="border-2 border-gray-200 rounded-lg overflow-hidden">
      <div className="p-4 border-b border-gray-200 bg-gray-50">{header}</div>
      <div className="p-4">{children}</div>
    </div>
  )
}

// ─── Demo de composición vs prop drilling ─────────────────────

function CompositionDemo() {
  const [activeTab, setActiveTab] = useState<'rigid' | 'flexible'>('rigid')

  return (
    <div className="space-y-4">
      <div className="flex gap-2">
        <button
          onClick={() => setActiveTab('rigid')}
          className={`px-4 py-2 text-sm rounded-lg transition-colors ${
            activeTab === 'rigid'
              ? 'bg-red-100 text-red-700 font-medium'
              : 'bg-gray-100 text-gray-600'
          }`}
        >
          ❌ Prop Drilling
        </button>
        <button
          onClick={() => setActiveTab('flexible')}
          className={`px-4 py-2 text-sm rounded-lg transition-colors ${
            activeTab === 'flexible'
              ? 'bg-green-100 text-green-700 font-medium'
              : 'bg-gray-100 text-gray-600'
          }`}
        >
          ✅ Composición
        </button>
      </div>

      {activeTab === 'rigid' ? (
        <div className="space-y-3">
          <RigidCard
            title="Producto A"
            subtitle="Categoría: Electrónica"
            body="Este card solo acepta strings. ¿Qué pasa si quiero poner un botón, un ícono, o una imagen en el body?"
            footer="$199.990"
            color="border-red-200"
          />
          <p className="text-xs text-red-500">
            Problema: para cada nueva necesidad hay que agregar más props (icon, image, onClick, badge...).
            El componente crece y se vuelve rígido.
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          <FlexibleCard
            header={
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-bold">Producto A</h3>
                  <p className="text-xs text-gray-500">Electrónica</p>
                </div>
                <span className="text-xs px-2 py-1 bg-green-100 text-green-700 rounded-full">
                  En stock
                </span>
              </div>
            }
          >
            <div className="space-y-3">
              <p className="text-sm">
                Con composición, el consumidor decide qué poner adentro.
              </p>
              <button className="px-4 py-2 bg-blue-600 text-white text-sm rounded-lg">
                Agregar al carrito
              </button>
            </div>
          </FlexibleCard>
          <p className="text-xs text-green-600">
            El card no sabe qué contiene — acepta cualquier JSX. Más flexible y reutilizable.
          </p>
        </div>
      )}
    </div>
  )
}

// ─── Demo de Layout con slots ─────────────────────────────────

function DemoLayout({
  sidebar,
  children,
}: {
  sidebar: React.ReactNode
  children: React.ReactNode
}) {
  return (
    <div className="flex rounded-lg border border-gray-200 overflow-hidden h-48">
      <aside className="w-40 bg-gray-100 p-3 border-r border-gray-200 text-xs">
        {sidebar}
      </aside>
      <main className="flex-1 p-3 text-sm">{children}</main>
    </div>
  )
}

function LayoutDemo() {
  return (
    <div className="space-y-4">
      <DemoLayout
        sidebar={
          <div className="space-y-2">
            <p className="font-bold text-gray-700">Navegación</p>
            <p className="text-blue-600 cursor-pointer">Inicio</p>
            <p className="text-blue-600 cursor-pointer">Tareas</p>
            <p className="text-blue-600 cursor-pointer">Config</p>
          </div>
        }
      >
        <h3 className="font-bold text-gray-800">Contenido principal</h3>
        <p className="text-gray-600 mt-1">
          Layout solo decide <strong>dónde</strong> van las cosas.
          El padre decide <strong>qué</strong> va en cada zona.
        </p>
      </DemoLayout>
    </div>
  )
}

// ─── Página principal ─────────────────────────────────────────

export function CompositionExample() {
  return (
    <ExampleLayout
      title="Composición"
      description="Construir UIs flexibles con children y slots"
    >
      <Section title="Prop Drilling vs Composición">
        <p className="text-sm text-gray-600">
          Compara ambos enfoques: un card rígido con muchos props vs uno flexible con children.
        </p>
        <CompositionDemo />
        <div className="grid grid-cols-2 gap-4 mt-2">
          <CodeBlock
            title="❌ RigidCard.tsx — muchos props"
            code={`function RigidCard({
  title, subtitle, body, footer, color,
  icon, badge, onClick, image, ...
}: RigidCardProps) {
  // Crece con cada nueva necesidad
  return (
    <div>
      <h3>{title}</h3>
      <p>{subtitle}</p>
      <div>{body}</div> {/* Solo strings */}
      <footer>{footer}</footer>
    </div>
  )
}

// Uso: inflexible
<RigidCard
  title="A" subtitle="B"
  body="solo texto" footer="$99"
/>`}
          />
          <CodeBlock
            title="✅ FlexibleCard.tsx — composición"
            code={`function FlexibleCard({
  header,   // ReactNode (slot)
  children, // ReactNode (slot)
}: {
  header: React.ReactNode
  children: React.ReactNode
}) {
  return (
    <div className="card">
      <div className="header">{header}</div>
      <div className="body">{children}</div>
    </div>
  )
}

// Uso: el consumidor decide el contenido
<FlexibleCard header={<MyHeader />}>
  <p>Cualquier JSX aquí</p>
  <button>Incluso botones</button>
</FlexibleCard>`}
          />
        </div>
      </Section>

      <Section title="Layout con Slots">
        <p className="text-sm text-gray-600">
          Un Layout acepta <code className="bg-gray-100 px-1 rounded">sidebar</code> y{' '}
          <code className="bg-gray-100 px-1 rounded">children</code> como slots.
          No sabe qué contienen — solo define la estructura visual.
        </p>
        <LayoutDemo />
        <CodeBlock
          title="Layout.tsx + uso"
          code={`// El Layout define DÓNDE van las cosas
function Layout({ sidebar, children }: {
  sidebar: React.ReactNode
  children: React.ReactNode
}) {
  return (
    <div className="flex">
      <aside>{sidebar}</aside>
      <main>{children}</main>
    </div>
  )
}

// El consumidor decide QUÉ va en cada zona
<Layout sidebar={<Navigation />}>
  <TodoList />
</Layout>`}
        />
      </Section>
    </ExampleLayout>
  )
}
