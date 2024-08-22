require_relative 'base_pizza'

# una clase builder
# proporciona un conjuntod e metodos "build*" que permiten crear (armar) un objeto complejo
# tambien tiene un metodo que devuelve el objeto creado
class PizzaBuilder
  def initialize
    @pizza = BasePizza.new
  end
  def buildWithCheese
    @pizza = Cheese.new(@pizza)
  end
  def buildWithPineapple
    @pizza = Pineapple.new(@pizza)
  end
  def buildWithHam
    @pizza = Ham.new(@pizza)
  end
  def buildHawaiiPizza
    buildWithHam
    buildWithCheese
    buildWithCheese
    buildWithPineapple
  end
  def getBuildedPizza
    @pizza
  end
  
end