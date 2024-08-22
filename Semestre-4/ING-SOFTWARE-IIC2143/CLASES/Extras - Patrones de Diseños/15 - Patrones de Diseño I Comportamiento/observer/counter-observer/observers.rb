
class Observer
  def update(objCounter)
    raise NotImplementedError
  end
end

class Logger < Observer
  def update(objCounter)
    puts "hey the counter in moving #{objCounter.value}"
  end
end

class BoundaryController < Observer
  def update(counter)
    if counter.value >= 5
      puts "cuidado paso los 5"
    end
  end
end
class FixedObserver < Observer
  def initialize(number)
    @number = number
  end
  def update(counter)
    if counter.value == @number
      puts "es tu turno"
    end
    if counter.value > @number
      puts "perdiste el turno"
    end
  end
end