require_relative 'pizza'

class PineableHamCheesePizza < Pizza

  def print
    puts 'normal bred'
    puts 'cheese'
    puts 'ham'
    puts 'pineapple'
  end
  
  def cost
    (20 + 5 + 5)* 2 
    #cada porcion de pineable duplica el costo
    #si ponemos doble queso sera *4
  end
end