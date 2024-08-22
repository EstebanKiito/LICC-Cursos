
class FilterStrategy
    # al hacer un metodo abstracto
    # las clases hijas estan obligadas a sobre escribir este metodo
    # sino ruby arroja un error
    def check(book)
        raise NotImplementedError
    end
end
# cada filtro nuevo involucrara la creación de una clase que herede de filter
# la ventaja es que no hay código duplicado
# otra ventaja es que para agregar un nuevo tipo de filtro no tengo que modificar la clase BookStore
# para agregar un nuevo tipo de filtro, se crea otra clase, si es posible en otro archivo
# esto facilita la creación de filtros
class FilterByAuthorStrategy < FilterStrategy
    def initialize(name)
        @name = name
    end

    def  check(book)
        return book.author == @name
    end
end

class FilterByTitleStrategy < FilterStrategy

    def initialize(title)
        @title = title
    end

    def check(book)
        return book.title == @title
    end
end

class FilterByYearRangeStrategy < FilterStrategy

    def initialize(yearIni,yearFin)
        @yearIni = yearIni
        @yearFin = yearFin
    end

    def check(book)
        return book.year >= @yearIni && book.year <= @yearFin
    end
end