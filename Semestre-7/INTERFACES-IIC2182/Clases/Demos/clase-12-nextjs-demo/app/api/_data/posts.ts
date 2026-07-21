export type Post = {
  id: number
  title: string
  body: string
  publishedAt: string
}

let nextId = 4
const posts: Post[] = [
  {
    id: 1,
    title: 'Bienvenida al curso',
    body: 'Este es el primer post del CMS imaginario.',
    publishedAt: '2026-04-20T10:00:00Z',
  },
  {
    id: 2,
    title: 'Route Handlers en Next.js',
    body: 'Cómo exponer una API dentro del mismo proyecto.',
    publishedAt: '2026-04-22T14:30:00Z',
  },
  {
    id: 3,
    title: 'Webhooks + revalidateTag',
    body: 'El patrón mágico: un sistema externo invalida tu cache.',
    publishedAt: '2026-04-25T09:15:00Z',
  },
]

export function listPosts(): Post[] {
  return [...posts].sort(
    (a, b) =>
      new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime(),
  )
}

export function createPost(input: { title: string; body: string }): Post {
  const post: Post = {
    id: nextId++,
    title: input.title,
    body: input.body,
    publishedAt: new Date().toISOString(),
  }
  posts.push(post)
  return post
}

export function deletePost(id: number): boolean {
  const idx = posts.findIndex((p) => p.id === id)
  if (idx < 0) return false
  posts.splice(idx, 1)
  return true
}
