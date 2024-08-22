require_relative 'track'
require_relative 'strategy'

class MusicPlayer
    def initialize
        @tracks =[]
        @current_index = 0
        @strategy = SequenceStrategy.new
    end

    def add(track)
        @tracks.push(track)
    end
    # permite cambiar la estrategia de reproducción en tiempo de ejecucion
    # osea mientras el programa se esta ejecutando
    def strategy=(name)
        @strategy = name
    end
    def playFirst()
        if @tracks.length > 0
            @tracks[0].play()
        end
    end
    # metodo generico que aplica cualquier estrategia de reproducción
    # la complejidad del metodo tambien reduco, hay muchos menos ifs
    def playNext()
        if @tracks.length > 0
            @tracks[@current_index].stop()
            @current_index = @strategy.nextIndex(@current_index,@tracks.length)
            @tracks[@current_index].play()
        end
    end
    # comparado con la v1
    # se delego la impresion a la clase Track para reducir acoplamiento
    def print()
        @tracks.each do |track|  
            track.print()
        end
    end

end