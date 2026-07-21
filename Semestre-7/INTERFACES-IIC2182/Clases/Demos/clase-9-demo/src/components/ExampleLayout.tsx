import { Link } from 'react-router-dom'

interface ExampleLayoutProps {
  title: string
  description: string
  children: React.ReactNode
}

export function ExampleLayout({ title, description, children }: ExampleLayoutProps) {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b border-gray-200">
        <div className="max-w-5xl mx-auto px-6 py-4 flex items-center gap-4">
          <Link
            to="/"
            className="text-sm text-gray-400 hover:text-gray-600 transition-colors"
          >
            ← Volver
          </Link>
          <div>
            <h1 className="text-xl font-bold text-gray-900">{title}</h1>
            <p className="text-sm text-gray-500">{description}</p>
          </div>
        </div>
      </header>
      <main className="max-w-5xl mx-auto px-6 py-8 space-y-8">
        {children}
      </main>
    </div>
  )
}

export function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="space-y-4">
      <h2 className="text-lg font-semibold text-gray-800 border-b border-gray-200 pb-2">
        {title}
      </h2>
      {children}
    </section>
  )
}
