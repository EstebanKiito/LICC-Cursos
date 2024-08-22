
class MainFolder
  # establece le metodo new como privado
  # esto limita a que solo se puedan crear pizzas dentro de esta clase
  private_class_method :new
  def initialize
    @name = "root"
  end
  # creamos un metodo a traves el cual pueden acceder a la unica instancia de la clase
  def self.instance
    # controlamos que solo se cree una instancia
    if @instance == nil
      @instance = new
    end
    return @instance
  end
end
# MainFolder.new (ya no funciona porque new es privad)
# la unica forma/opcion que damos es que acceda al objeto unico mediante el metodo instance
folder = MainFolder.instance

# en ocaciones es util solo tener un objeto de una clase para compartir información
