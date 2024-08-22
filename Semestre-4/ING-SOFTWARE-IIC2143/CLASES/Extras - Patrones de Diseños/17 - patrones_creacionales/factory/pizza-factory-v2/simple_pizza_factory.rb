require_relative 'cheese_pizza'
require_relative 'clam_pizza'
require_relative 'pepperoni_pizza'
require_relative 'veggie_pizza'

class SimplePizzaFactory
  # un factory method
  # es un metodo que normalmente crea las clases dentro de una jerarquia
  # en realidad pateamos el problema de dependencias a otra clase
  # esta ahora es la clase que depende de las clases hijas
  # la ventaja es que ahora la creación de pizzas esta centralizada en un solo lugar
  # y si en el futuro alguien quiere crear pizzas, puede usar este metodo
  # y asi no tendra que depende de toda la jerarquia sino solo de la clase padre
  def create(type)
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
    pizza
  end
end