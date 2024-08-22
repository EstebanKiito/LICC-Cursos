require_relative 'topping'

class Pineapple < PizzaTopping

  def print
    @decoratedPizza.print
    puts 'pineapple'
  end
  def cost
    return @decoratedPizza.cost * 2
  end
end