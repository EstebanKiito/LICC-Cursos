import { NextResponse } from 'next/server'
import { createItem, listItems } from '../../api/_data/items'

export async function GET() {
  return NextResponse.json(listItems())
}

export async function POST(req: Request) {
  const body = await req.json().catch(() => ({}))
  const name = (body?.name ?? '').toString().trim()

  if (!name) {
    return NextResponse.json(
      { error: 'name es requerido' },
      { status: 400 },
    )
  }

  const item = createItem(name)
  return NextResponse.json(item, { status: 201 })
}
