import { listItems } from '../_data/items'

export async function GET() {
  const items = listItems()

  const rows = items.map((i) => [i.id, i.name, i.createdAt])
  const csv = [
    'id,name,created_at',
    ...rows.map((r) =>
      r.map((cell) => `"${String(cell).replace(/"/g, '""')}"`).join(','),
    ),
  ].join('\n')

  return new Response(csv, {
    headers: {
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': 'attachment; filename="items.csv"',
    },
  })
}
