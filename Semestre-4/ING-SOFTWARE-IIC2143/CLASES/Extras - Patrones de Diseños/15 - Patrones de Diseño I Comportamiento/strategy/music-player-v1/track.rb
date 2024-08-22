
class Track
    attr_reader :title
    attr_reader :duration
    def initialize(title,duration)
        @title = title
        @duration = duration
        @playing = false
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