require_relative 'topping'


class Cheese < PizzaTopping
  
  def print
    @decoratedPizza.print
    puts 'cheese'
  end
  def cost
    return @decoratedPizza.cost  + 5
  end
end