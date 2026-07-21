import { NextResponse } from 'next/server'
import { listPosts } from '../_data/posts'

export async function GET() {
  // Simular latencia de un CMS real
  await new Promise((r) => setTimeout(r, 800))
  return NextResponse.json({
    posts: listPosts(),
    fetchedAt: new Date().toISOString(),
  })
}
