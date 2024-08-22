

class ConsoleClient
    def initialize(service)
        @service = service
    end
    def run
        puts "Ingrese RUT:"
        rut = gets
        puts "Ingrese ClaveUnica:"
        clave = gets
        if @service.login(rut,clave) then
            puts "autenticacion exitosa"
        else 
            puts "autenticacion fallida"
        end
    end
end