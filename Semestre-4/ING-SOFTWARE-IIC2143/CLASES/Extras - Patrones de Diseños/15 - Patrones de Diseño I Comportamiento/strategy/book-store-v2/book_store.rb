require_relative 'book'

class BookStore
  def initialize
    @books = []
  end
  
  def add(book)
    @books.push(book)
  end
  # este metodo permite aplicar un filtro con diferentes estrategias
  # a diferencia de la v1, tenemos un metodo de filtrado generico
  # funciona con cualquier estrategia de filtro
  def filter(strategy)
    @books.each do |book|
      if strategy.check(book)
        book.print
      end
    end
  end
  
end