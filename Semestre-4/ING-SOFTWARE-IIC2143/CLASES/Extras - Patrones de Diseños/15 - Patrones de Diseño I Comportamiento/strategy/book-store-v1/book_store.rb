require_relative 'book'

class BookStore

  def initialize
    @books = []
  end
  
  def add(book)
    @books.push(book)
  end

  # problema: este metodo es un clon del metodo filterByTitle
  def filterByAuthor(name)
    @books.each do |book|
      if book.author == name
        book.print
      end
    end
  end
  # problema: este metodo es un clon del metodo filterByAuthor
  # el código duplicado a la larga trae problemas
  # si alguien quiere crear un nuevo tipo de filtro se tendra que crear un nuevo clon
  # por lo extender nuevos tipos de filtro esta insertando clones
  def filterByTitle(title)
    @books.each do |book|
      if book.title == title
        book.print
      end
    end
  end
end