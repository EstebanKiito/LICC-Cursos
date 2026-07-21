export type Item = {
  id: number
  name: string
  createdAt: string
}

let nextId = 4
const items: Item[] = [
  { id: 1, name: 'Notebook', createdAt: '2026-04-01T10:00:00Z' },
  { id: 2, name: 'Mouse', createdAt: '2026-04-05T14:30:00Z' },
  { id: 3, name: 'Teclado mecánico', createdAt: '2026-04-12T09:15:00Z' },
]

export function listItems(): Item[] {
  return [...items]
}

export function findItem(id: number): Item | undefined {
  return items.find((i) => i.id === id)
}

export function createItem(name: string): Item {
  const item: Item = {
    id: nextId++,
    name,
    createdAt: new Date().toISOString(),
  }
  items.push(item)
  return item
}

export function removeItem(id: number): boolean {
  const idx = items.findIndex((i) => i.id === id)
  if (idx < 0) return false
  items.splice(idx, 1)
  return true
}
