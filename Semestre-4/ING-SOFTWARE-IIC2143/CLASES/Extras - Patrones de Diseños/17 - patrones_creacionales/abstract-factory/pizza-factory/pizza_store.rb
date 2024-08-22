class PizzaStore
  
  
  def orderPizza(type)
    pizza = create(type)
    pizza.prepare
    pizza.bake
    pizza.cut
    pizza.box
    pizza
  end
  # este es un abstract factory method
  # un metodo que crea objetos y es abstract
  # lo definen las clases hija
  # cada clase hija se encarga de crear una familia de objetos
  # cuando decimos familia de clases, nos referimos a clases que son parte de una jerarquia
  # normalmente cuando se implementa un abstract-factory, hay 2 o mas jerarquia de clases
  # la jerarquia de clases normalmente hereda de la misma clase, como en este ejemplo, que ambas familias heredan de pizza
  def create(type)
    raise NotImplementedError
  end
end