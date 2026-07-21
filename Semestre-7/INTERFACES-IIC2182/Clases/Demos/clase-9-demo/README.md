# Clase 9 — Advanced React (Demo)

Proyecto complementario para la clase 9 de IIC2182. Cada ruta es un **ejemplo aislado** que demuestra un concepto de forma independiente, con demo interactivo + código fuente visible.

## Setup

```bash
cd clase9-demo
npm install
npm run dev
```

Abrir http://localhost:5173 — la página Home lista todos los ejemplos.

## Estructura del proyecto

```
src/
├── App.tsx                  # Router — una ruta por concepto
├── main.tsx                 # Setup de QueryClientProvider
├── components/
│   ├── CodeBlock.tsx        # Muestra código en pantalla
│   └── ExampleLayout.tsx    # Layout compartido (header + volver)
└── examples/
    ├── Home.tsx                      # /
    ├── UseCallbackExample.tsx        # /usecallback
    ├── UseEffectCleanupExample.tsx   # /useeffect-cleanup
    ├── CustomHooksExample.tsx        # /custom-hooks
    ├── CompositionExample.tsx        # /composition
    ├── ZustandExample.tsx            # /zustand
    └── TanstackQueryExample.tsx      # /tanstack-query
```

Cada archivo en `examples/` es **autocontenido** — define sus propios hooks, stores, y componentes localmente para que los alumnos puedan leer UN solo archivo y entender el concepto completo.

## Guía de uso en clase

### Orden sugerido (sigue los slides)

| # | Ruta | Concepto | Qué mostrar | Archivo |
|---|------|----------|-------------|---------|
| 1 | `/usecallback` | useCallback | Presionar el counter y comparar re-renders con vs sin useCallback | `UseCallbackExample.tsx` |
| 2 | `/useeffect-cleanup` | useEffect Cleanup | Timer sin cleanup (se acelera) vs con cleanup; log visual del ciclo de vida | `UseEffectCleanupExample.tsx` |
| 3 | `/custom-hooks` | Custom Hooks | Escribir rápido en el input de debounce; recargar página para ver localStorage | `CustomHooksExample.tsx` |
| 4 | `/composition` | Composición | Alternar entre tabs "Prop Drilling" y "Composición"; mostrar el Layout con slots | `CompositionExample.tsx` |
| 5 | `/zustand` | Zustand | Cambiar counter y ver que el componente Name NO se re-renderiza; comparar con Context | `ZustandExample.tsx` |
| 6 | `/tanstack-query` | Tanstack Query | Ver loading states, cambiar de usuario (cache hit), crear tarea con mutation | `TanstackQueryExample.tsx` |

### Puntos clave por ejemplo

#### 1. useCallback (`/usecallback`)

**Qué demostrar:**
- Presionar "Counter" en ambas versiones y comparar el badge "renders:" de cada item
- Sin useCallback: todos los items incrementan su render count
- Con useCallback: los items se mantienen en renders: 1

**Pregunta para los alumnos:** ¿Por qué `memo()` no basta si la función se recrea?

**Archivo:** `UseCallbackExample.tsx` — todo en ~120 líneas

#### 2. useEffect Cleanup (`/useeffect-cleanup`)

**Qué demostrar:**
- **Timer sin cleanup**: presionar Iniciar/Detener/Iniciar — el contador se acelera (memory leak)
- **Timer con cleanup**: mismo flujo pero siempre hay 1 solo interval
- **Cleanup con deps**: escribir en el input y ver el log de "Timer creado" / "Cleanup: cancelado"
- **Mount/Unmount**: desmontar el hijo y ver el log de cleanup en la consola

**Pregunta para los alumnos:** ¿Qué pasa si un fetch tarda 5 segundos pero el usuario navega a otra página antes?

**Archivo:** `UseEffectCleanupExample.tsx` — 4 demos visuales progresivas

#### 3. Custom Hooks (`/custom-hooks`)

**Qué demostrar:**
- **useDebounce**: Escribir rápido y ver que el valor "debounced" se actualiza con delay
- **useLocalStorage**: Escribir algo, recargar la página (F5), el valor persiste

**Pregunta para los alumnos:** ¿Cuándo es mejor crear un custom hook vs una función normal?

**Archivo:** `CustomHooksExample.tsx` — hooks definidos al inicio del archivo (~15 líneas c/u)

#### 4. Composición (`/composition`)

**Qué demostrar:**
- Tab "Prop Drilling": card rígido que solo acepta strings — ¿cómo le pondrías un botón?
- Tab "Composición": el consumidor decide qué JSX poner adentro
- Layout con slots: sidebar y contenido como props ReactNode

**Pregunta para los alumnos:** ¿Cuántos props tiene tu componente más grande? ¿Podría usar children en vez?

**Archivo:** `CompositionExample.tsx`

#### 5. Zustand (`/zustand`)

**Qué demostrar:**
- Tres componentes (Counter, Display, Name) comparten el mismo store
- Cambiar el counter: Counter y Display se re-renderizan, Name NO
- Escribir en Name: solo Name se re-renderiza
- Comparar con la versión Context: todos se re-renderizan siempre

**Pregunta para los alumnos:** ¿Qué pasaría si no usáramos selectores? (`useCounterStore()` sin función)

**Archivo:** `ZustandExample.tsx` — store definido en ~10 líneas al inicio

#### 6. Tanstack Query (`/tanstack-query`)

**Qué demostrar:**
- La lista de usuarios se carga con loading state automático
- Cambiar de usuario en la sección de "Query Keys": primera vez hace fetch, segunda vez es instantáneo (cache)
- Crear una tarea: ver los estados pending → success
- Abrir React Query Devtools (botón flotante abajo) para ver el cache

**Pregunta para los alumnos:** ¿Qué ventaja tiene `queryKey: ['todos', userId]` vs `queryKey: ['todos']`?

**Archivo:** `TanstackQueryExample.tsx`

## Stack

- React 19 + TypeScript
- Vite
- Tailwind CSS v4
- React Router DOM
- Zustand (ejemplo 4)
- Tanstack Query (ejemplo 5)

## API utilizada

Todos los ejemplos de fetching usan [JSONPlaceholder](https://jsonplaceholder.typicode.com) — API pública gratuita que no requiere autenticación.
