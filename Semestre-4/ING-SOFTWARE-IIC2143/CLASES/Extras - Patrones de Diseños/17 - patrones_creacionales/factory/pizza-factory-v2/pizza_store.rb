require_relative 'simple_pizza_factory'


class PizzaStore
  # esta version (v2)
  # la clase pizza store, no depeden de las clases hijas
  # solo sabe que el metodo create, le devolvera una pizza
  # no sabe si sera chese, jam o otra
  # ya no esta acoplada
  def orderPizza(type)
    pizza = SimplePizzaFactory.new.create(type)
    pizza.prepare
    pizza.bake
    pizza.cut
    pizza.box
    pizza
  end
end