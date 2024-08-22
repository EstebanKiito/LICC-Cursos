require_relative 'folder'
require_relative 'file'


main = SFolder.new('main')
main.add(SFile.new('a',4))
main.add(SFile.new('b',6))

doc = SFolder.new('docs')
doc.add(SFile.new('c',2))
doc.add(SFile.new('d',3))
main.add(doc)
doc.add(SFile.new('x',10))

puts "#{main.size}"
main.print