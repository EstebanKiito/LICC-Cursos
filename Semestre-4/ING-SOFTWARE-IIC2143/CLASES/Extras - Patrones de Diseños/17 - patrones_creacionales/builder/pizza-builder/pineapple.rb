require_relative 'topping'

class Pineapple < PizzaTopping

  def print
    super
    puts 'pineapple'
  end
  def cost
    super * 2
  end
end