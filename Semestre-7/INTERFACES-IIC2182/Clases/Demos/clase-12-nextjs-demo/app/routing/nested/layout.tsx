import Link from 'next/link'

export default function NestedLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="grid grid-cols-[180px_1fr] gap-6">
      <nav className="border-r border-neutral-200 pr-4 space-y-2 text-sm">
        <div className="font-bold mb-2">Sub-menú (layout anidado)</div>
        <Link href="/routing/nested" className="block hover:underline">
          Home
        </Link>
        <Link
          href="/routing/nested/details"
          className="block hover:underline"
        >
          Details
        </Link>
      </nav>
      <section>{children}</section>
    </div>
  )
}
