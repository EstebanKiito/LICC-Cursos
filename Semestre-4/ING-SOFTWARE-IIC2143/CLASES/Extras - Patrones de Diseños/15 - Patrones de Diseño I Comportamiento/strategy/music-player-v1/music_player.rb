require_relative 'track'

class MusicPlayer
    def initialize
        @tracks =[]
        @current_index = 0
        @strategy = "sequence"
    end

    def add(track)
        @tracks.push(track)
    end

    def strategy=(name)
        @strategy = name
    end
    def playFirst()
        if @tracks.length > 0
            @tracks[0].play()
        end
    end
    
    # para agregar una nueva estrategia de reproducción
    # es necesario modificar el codigo de este metodo
    def playNext()
        if @tracks.length > 0
            @tracks[@current_index].stop()
            if @strategy == "sequence"
                @current_index = (@current_index + 1) % @tracks.length
            elsif @strategy == "random"
                @current_index = rand(@tracks.length)
            end
            @tracks[@current_index].play()
        end
    end

    # este metodo esta muy acoplado a la clase Track
    # un buen diseño es bajo acoplamiento, maxima cohesion
    def print()
        @tracks.each do |track|
            if track.playing?
                puts (track.title + ":" + track.duration.to_s).green
            else
                puts (track.title + ":" + track.duration.to_s).blue
            end
        end
    end

end