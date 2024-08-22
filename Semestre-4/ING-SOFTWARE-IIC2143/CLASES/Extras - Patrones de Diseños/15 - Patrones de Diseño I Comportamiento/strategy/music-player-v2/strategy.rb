
class PlayStrategy
    # la estrategia solo dice el indice de la sig cancion a reproducir
    def nextIndex(current_index,len)
        raise NotImplementedError
    end
end


class RandomStrategy < PlayStrategy
    def nextIndex(current_index,len)
        return rand(len)
    end
end

class SequenceStrategy < PlayStrategy
    def nextIndex(current_index,len)
        return (current_index + 1) % len
    end
end

class RepeatStrategy < PlayStrategy
    def nextIndex(current_index,len)
        return current_index
    end
end

# agregar nuevos tipos de reproducción ahora es mas facil
# no tenemos que modificar el código anterior, solo crear una nueva clase y todo funcionara
# por lo que podriamos decir que este código es mas facil de extender que el de la v1
