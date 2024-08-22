
class AbstractMac
    def print()
        puts "Macbook, #{inch} inch, #{gpu} gpu, #{ram} ram."
    end
    def inch()
        return 14
    end
    def ram()
        return 16
    end
    def gpu()
        return 16
    end
end

class MacBase < AbstractMac
end

class MacDecorator < AbstractMac
    def initialize(mac)
        @decoratedMac = mac
    end
end

class GPU16Upgrade < MacDecorator
    def gpu()
        return @decoratedMac.gpu + 16
    end
end

class GPU32Upgrade < MacDecorator
    def gpu()
        return @decoratedMac.gpu + 32
    end
end

class RAM16Upgrade < MacDecorator
    def ram()
        return @decoratedMac.ram + 16
    end
end

class RAM32Upgrade < MacDecorator
    def ram()
        return @decoratedMac.ram + 32
    end
end
