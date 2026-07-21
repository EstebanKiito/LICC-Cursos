import { NextResponse } from 'next/server'
import { findItem, removeItem } from '../../_data/items'

export async function GET(
  _req: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const { id } = await params
  const item = findItem(Number(id))

  if (!item) {
    return new Response('Not found', { status: 404 })
  }
  return NextResponse.json(item)
}

export async function DELETE(
  _req: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const { id } = await params
  const ok = removeItem(Number(id))

  if (!ok) {
    return new Response('Not found', { status: 404 })
  }
  return new Response(null, { status: 204 })
}
