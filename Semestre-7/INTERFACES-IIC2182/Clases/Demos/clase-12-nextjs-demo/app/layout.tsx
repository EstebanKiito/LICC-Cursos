import type { Metadata } from 'next'
import Link from 'next/link'
import Providers from './providers'
import './globals.css'

export const metadata: Metadata = {
  title: 'Next.js Demo — IIC2182',
  description: 'Ejemplos de Next.js para las clases 12 y 13',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="es">
      <body className="min-h-screen">
        <Providers>
          <header className="border-b border-neutral-200 px-6 py-3 flex gap-4 items-center">
            <Link href="/" className="font-bold">
              Next.js Demo
            </Link>
            <span className="text-sm opacity-50">IIC2182</span>
          </header>
          <main className="px-6 py-8 max-w-5xl mx-auto">{children}</main>
        </Providers>
      </body>
    </html>
  )
}
