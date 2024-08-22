
class Track
    def initialize(title,duration)
        @title = title
        @duration = duration
        @playing = false
    end

    def print()
        if playing?
            puts (@title + ":" + @duration.to_s).green
        else
            puts (@title + ":" + @duration.to_s).blue
        end
    end

    def playing?
        return @playing
    end
    def play()
        @playing = true
    end
    def stop()
        @playing = false
    end
end