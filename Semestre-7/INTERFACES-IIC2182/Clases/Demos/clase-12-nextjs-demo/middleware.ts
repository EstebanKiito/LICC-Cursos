import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl
  const session = req.cookies.get('demo-session')?.value

  // Proteger /protected/* — sin cookie redirige a /login
  if (pathname.startsWith('/protected') && !session) {
    const url = req.nextUrl.clone()
    url.pathname = '/login'
    url.searchParams.set('next', pathname)
    return NextResponse.redirect(url)
  }

  // Si ya hay sesión y entra a /login, mandar a /protected
  if (pathname === '/login' && session) {
    const url = req.nextUrl.clone()
    url.pathname = '/protected'
    url.search = ''
    return NextResponse.redirect(url)
  }

  return NextResponse.next()
}

// Sólo correr el middleware en estas rutas — performance
export const config = {
  matcher: ['/protected/:path*', '/login'],
}
