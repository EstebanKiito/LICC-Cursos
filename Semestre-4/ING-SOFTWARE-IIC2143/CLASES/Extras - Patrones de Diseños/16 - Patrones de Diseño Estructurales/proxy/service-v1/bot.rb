require_relative 'service'

class Bot
  def perform(service,monitor)
    # aqui si es que el flag monitor es true, imprimimos logs antes y despues
    # si queremos agregar mas tipos de accioens antes y despues tendriamos que agregar mas ifs a este metodo
    if monitor
      puts "starting #{service.class.name}"
    end
    
    service.operate
    
    if monitor
      puts "#{service.class.name} finished"
    end
  end
end