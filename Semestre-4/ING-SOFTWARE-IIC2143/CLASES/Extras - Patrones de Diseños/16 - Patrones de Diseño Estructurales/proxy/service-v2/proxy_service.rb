require_relative 'service'

class ProxyService < Service
  def initialize(service)
    @originalService = service
  end
  # la diferencia entre el adapter y el proxy
  # es que el proxy no adapta nada
  # llama al mismo metodo del objeto original
  # lo que si hace es cosas adicionales antes y despues de llamar al objeto original
  # por ejemplo, imprimir en consola la operacion actual que se esta ejecutando
  def operate
    puts "starting #{@originalService.class.name}"
    @originalService.operate
    puts "#{@originalService.class.name} finished"
  end
end