require_relative 'topping'

class Ham < PizzaTopping

  def print
    @decoratedPizza.print
    puts 'ham'
  end
  
  def cost
    return @decoratedPizza.cost + 5
  end
  
end