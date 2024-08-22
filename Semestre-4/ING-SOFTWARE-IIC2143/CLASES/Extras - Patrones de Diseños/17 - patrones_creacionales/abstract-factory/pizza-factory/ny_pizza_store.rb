require_relative 'pizza_store'
require_relative 'newyork_pizza'

class NYPizzaStore < PizzaStore
  # crea objetos de una familia (de una misma jerarquia)
  def create(type)
    if type == 'cheese'
      pizza = NYCheesePizza.new
    elsif type == 'pepperoni'
      pizza = NYPepperoniPizza.new
    elsif type == 'clam'
      pizza = NYClamPizza.new
    elsif type == 'veggie'
      pizza = NYVeggiePizza.new
    elsif
      raise NotSupportedPizza
    end
    pizza
  end
  
end