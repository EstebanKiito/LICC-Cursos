require_relative 'service'

class Bot
  # este metodo ahora no tiene ningun if
  # en comparacion a la v1
  # agregamos comportamiento (los logs) antes y despues utilizando un objeto proxy
  def perform(service)
    service.operate
  end
end