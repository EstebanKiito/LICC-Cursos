import { Link } from 'react-router-dom'

const examples = [
  {
    path: '/usecallback',
    title: '1. useCallback',
    description: 'Estabilizar referencias de funciones para evitar re-renders innecesarios',
    color: 'bg-blue-50 border-blue-200 hover:border-blue-400',
    icon: '⚡',
  },
  {
    path: '/useeffect-cleanup',
    title: '2. useEffect Cleanup',
    description: 'La return function que evita memory leaks y efectos acumulados',
    color: 'bg-rose-50 border-rose-200 hover:border-rose-400',
    icon: '🧹',
  },
  {
    path: '/usetransition',
    title: '3. useTransition',
    description: 'Mantener la UI responsiva durante actualizaciones pesadas (filtrar 5.000 ítems)',
    color: 'bg-orange-50 border-orange-200 hover:border-orange-400',
    icon: '⏳',
  },
  {
    path: '/custom-hooks',
    title: '4. Custom Hooks',
    description: 'Extraer lógica reutilizable en hooks propios (useDebounce, useLocalStorage)',
    color: 'bg-green-50 border-green-200 hover:border-green-400',
    icon: '🪝',
  },
  {
    path: '/composition',
    title: '5. Composición',
    description: 'Construir UIs flexibles con children y slots en vez de prop drilling',
    color: 'bg-purple-50 border-purple-200 hover:border-purple-400',
    icon: '🧩',
  },
  {
    path: '/hoc',
    title: '6. Higher-Order Components',
    description: 'Funciones que envuelven componentes para agregar funcionalidad (withLoading, withAuth)',
    color: 'bg-cyan-50 border-cyan-200 hover:border-cyan-400',
    icon: '🎁',
  },
  {
    path: '/zustand',
    title: '7. Zustand',
    description: 'Estado global sin boilerplate — un store es un hook',
    color: 'bg-amber-50 border-amber-200 hover:border-amber-400',
    icon: '🐻',
  },
]

export function Home() {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-8">
      <div className="max-w-3xl w-full space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gray-900">Clase 9 — Advanced React</h1>
          <p className="text-gray-500 mt-2">
            IIC2182 · Cada ejemplo demuestra un concepto de forma aislada
          </p>
        </div>

        <div className="space-y-3">
          {examples.map((ex) => (
            <Link
              key={ex.path}
              to={ex.path}
              className={`block p-5 rounded-xl border-2 transition-all ${ex.color}`}
            >
              <div className="flex items-center gap-3">
                <span className="text-2xl">{ex.icon}</span>
                <div>
                  <h2 className="font-semibold text-gray-900">{ex.title}</h2>
                  <p className="text-sm text-gray-600">{ex.description}</p>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}
