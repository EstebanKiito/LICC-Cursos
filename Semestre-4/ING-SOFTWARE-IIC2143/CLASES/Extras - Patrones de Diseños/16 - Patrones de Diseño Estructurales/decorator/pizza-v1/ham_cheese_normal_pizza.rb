require_relative 'pizza'

class HamCheesePizza < Pizza
  def print
    puts 'normal bred'
    puts 'cheese'
    puts 'ham'
  end
  
  def cost
    20 + 5 + 5 
  end
end