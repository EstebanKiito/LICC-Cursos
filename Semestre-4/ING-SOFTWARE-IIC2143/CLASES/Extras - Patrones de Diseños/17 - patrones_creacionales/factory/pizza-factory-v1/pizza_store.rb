require_relative 'cheese_pizza'
require_relative 'clam_pizza'
require_relative 'pepperoni_pizza'
require_relative 'veggie_pizza'

class PizzaStore
  # en esta version (v1) la clase pizza store depende (acoplada) de todas las clases hijas de pizza 
  # CheesePizza, PeperoniPizza, ClamPizza, etc
  # no es tan buena idea que una clase dependa de todas las clases hijas de una jerarquia
  # lo ideal es que solo dependa de la clase padre

  def orderPizza(type)
    if type == 'cheese'
      pizza = CheesePizza.new
    elsif type == 'pepperoni'
      pizza = PepperoniPizza.new
    elsif type == 'clam'
      pizza = ClamPizza.new
    elsif type == 'veggie'
      pizza = VeggiePizza.new
    elsif
      raise NotSupportedPizza
    end
    
    pizza.prepare
    pizza.bake
    pizza.cut
    pizza.box
    
    pizza
  end
end