interface CodeBlockProps {
  code: string
  title?: string
}

export function CodeBlock({ code, title }: CodeBlockProps) {
  return (
    <div className="rounded-lg border border-gray-200 overflow-hidden text-left">
      {title && (
        <div className="bg-gray-800 px-4 py-2 text-xs font-mono text-gray-400 border-b border-gray-700">
          {title}
        </div>
      )}
      <pre className="p-4 text-sm overflow-x-auto bg-gray-900 text-gray-100 leading-relaxed">
        <code>{code}</code>
      </pre>
    </div>
  )
}
