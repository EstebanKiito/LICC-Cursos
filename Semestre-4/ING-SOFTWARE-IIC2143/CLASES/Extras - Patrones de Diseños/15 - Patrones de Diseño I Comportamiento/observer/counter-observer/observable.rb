class Counter 
  def initialize
    super
    @value = 0
    @att1 = 2
    @att2 = 3
    @observers = []
  end
  def register(observer)
    @observers.push(observer)
  end

  def notifyAll()
    @observers.each do |obs|
      obs.update(self)
    end
  end

  def increment
    @value = @value + 1
    notifyAll()
  end
  
  def print
    puts "counter: #{@value}"
  end
  
  def decrement
    @value = @value - 1
    notifyAll()
  end

  def value
    @value
  end
end