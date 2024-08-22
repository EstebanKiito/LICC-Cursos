require_relative 'topping'


class Cheese < PizzaTopping
  
  def print
    super
    puts 'cheese'
  end
  def cost
    super + 5
  end
end