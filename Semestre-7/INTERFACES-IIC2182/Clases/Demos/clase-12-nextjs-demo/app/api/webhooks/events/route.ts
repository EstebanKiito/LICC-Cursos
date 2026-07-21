import { NextResponse } from 'next/server'
import { clearEvents, listEvents } from '../../_data/webhook-log'

export async function GET() {
  return NextResponse.json(listEvents())
}

export async function DELETE() {
  clearEvents()
  return new Response(null, { status: 204 })
}
