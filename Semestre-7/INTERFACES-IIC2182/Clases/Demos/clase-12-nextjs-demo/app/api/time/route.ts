import { NextResponse } from 'next/server'

// Forzar que el handler corra en cada request — sin esto Next podría cachearlo
export const dynamic = 'force-dynamic'

// Hits acumulados desde que arrancó el server (en memoria)
let hits = 0

export async function GET() {
  hits += 1

  return NextResponse.json({
    timestamp: new Date().toISOString(),
    random: Math.random(),
    hits,
  })
}
