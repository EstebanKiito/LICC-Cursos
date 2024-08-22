require_relative 'topping'

class Ham < PizzaTopping

  def print
    super
    puts 'ham'
  end
  
  def cost
    super + 5
  end
  
end