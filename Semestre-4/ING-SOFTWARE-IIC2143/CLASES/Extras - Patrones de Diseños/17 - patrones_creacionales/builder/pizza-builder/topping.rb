require_relative 'pizza'

class PizzaTopping < Pizza
  def initialize(decoratedPizza)
    @decoratedPizza = decoratedPizza
  end
  def cost
    @decoratedPizza.cost
  end
  def print
    @decoratedPizza.print
  end
end