# Next.js Demo — IIC2182

Proyecto paralelo para las clases 12 y 13. Cada ruta es un ejemplo aislado de un concepto de Next.js.

## Setup

```bash
cd nextjs-demo
npm install        # o pnpm install
npm run dev        # abre http://localhost:3000
```

## Estructura

```
app/
├── layout.tsx                       # layout raíz (navbar + providers)
├── page.tsx                         # Home con links a todos los ejemplos
├── providers.tsx                    # QueryClientProvider (client)
├── globals.css
│
├── routing/
│   ├── basic/page.tsx               # /routing/basic
│   ├── nested/layout.tsx            # layout anidado
│   ├── nested/page.tsx              # /routing/nested
│   ├── nested/details/page.tsx     # /routing/nested/details
│   ├── [id]/page.tsx                # /routing/42, /routing/abc
│   └── catch-all/[...slug]/page.tsx # /routing/catch-all/a, /a/b, /a/b/c…
│
├── server-demo/page.tsx             # async Server Component + fetch
├── client-demo/page.tsx             # "use client" + hooks
│
└── data-fetching/
    ├── server/page.tsx              # fetch con revalidate + tags
    ├── loading/page.tsx             # fetch lento + loading.tsx skeleton
    ├── loading/loading.tsx          # skeleton automático (Suspense)
    ├── swr/page.tsx                 # useSWR
    ├── tanstack/page.tsx            # useQuery + useMutation
    └── optimistic/page.tsx          # onMutate + rollback en error
```

## Guía de uso en clase

### Clase 12 — Fundamentos

| # | Ruta | Concepto | Qué demostrar |
|---|------|----------|---------------|
| 1 | `/routing/basic` | page.tsx | Mostrar archivo y explicar que la carpeta es la URL |
| 2 | `/routing/nested` | Layouts anidados | Navegar entre Home/Details y ver que el sidebar persiste |
| 3 | `/routing/42` | Dynamic route | Cambiar la URL a `/routing/hola` y ver que el param cambia |
| 3b | `/routing/catch-all/a/b/c` | Catch-all `[...slug]` | Ir agregando `/x/y/z` y ver que el array crece |
| 4 | `/server-demo` | Server Component | View source → ver HTML con los posts ya renderizados |
| 5 | `/client-demo` | Client Component | Click en el contador, ver el reloj actualizando |
| 6 | `/data-fetching/server` | fetch + revalidate | Ver el timestamp del server, recargar en <120s vs >120s |
| 6b | `/data-fetching/loading` | loading.tsx + Suspense | Recargar y ver el skeleton ~2s, luego los datos — el navbar no se re-renderiza |
| 7 | `/data-fetching/swr` | SWR | Presionar "Refetch" y comentar revalidación on-focus |
| 8 | `/data-fetching/tanstack` | TanStack Query | Crear tarea, abrir devtools, ver invalidación |
| 8b | `/data-fetching/optimistic` | Optimistic updates | Toggle optimistic ON/OFF con delay 2s — sentir la diferencia; activar "Simular fallo" y ver el rollback |

### Clase 13 — Features Avanzados

(Rutas a agregar durante clase 13: `/server-action`, `/api/items`, `/metadata-demo`, `/streaming`, `/images-demo`, `middleware.ts`.)

## Stack

- Next.js 15 (App Router)
- React 19 + TypeScript
- Tailwind CSS 3
- SWR 2
- TanStack Query 5 + Devtools

## API externa

Todos los ejemplos usan [JSONPlaceholder](https://jsonplaceholder.typicode.com) — REST API pública sin autenticación.
