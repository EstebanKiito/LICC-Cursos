import { NextResponse } from 'next/server'
import { revalidateTag } from 'next/cache'
import { recordEvent } from '../../_data/webhook-log'
import { createPost, deletePost } from '../../_data/posts'

const SHARED_SECRET = 'demo-secret-iic2182'

export async function POST(req: Request) {
  // Verificación de firma simulada — en producción sería HMAC
  const signature = req.headers.get('x-demo-signature')
  if (signature !== SHARED_SECRET) {
    return NextResponse.json(
      { error: 'Invalid signature' },
      { status: 401 },
    )
  }

  const body = await req.json().catch(() => ({}))
  const type = body?.type ?? 'unknown'
  const event = recordEvent(type, body)

  // Reaccionar al evento — mutar el "DB" y revalidar el cache de /blog
  let revalidated = false
  if (type === 'post.created' && body?.title) {
    createPost({ title: body.title, body: body.body ?? '' })
    revalidateTag('posts')
    revalidated = true
  } else if (type === 'post.deleted' && typeof body?.postId === 'number') {
    deletePost(body.postId)
    revalidateTag('posts')
    revalidated = true
  }

  return NextResponse.json({ ok: true, eventId: event.id, revalidated })
}
