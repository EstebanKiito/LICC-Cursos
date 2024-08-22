
class LoginServiceAdapter
    def initialize(originalService)
        @originalService = originalService
    end
    # el cliente manda el rut con puntos
    # el servicio original tiene un metodo login_user
    # el cliente espera que tenga un metodo que se llame solo "login"
    # solucion: creamos un objeto con el nombre que el cliente espera
    #           internamente este objeto llamara al servicio original
    #           adaptando el nombre del metodo y el input
    # el adaptador, puede adaptar el nombre del metodo, input, output
    # o lo que fuere necesario y proporcionar unos metodos publicos
    # compatibles con el cliente
    # la idea es no modificar el codigo de client.rb
    # tampoco modificar el codigo de login_service.rb
    # si modificamos podriamos ingresar bugs, pq es codigo introducido por otros devs
    def login(rut, pass)
        adaptedrut = rut.gsub(".", "")
        return   @originalService.login_user(adaptedrut, pass)
    end
end
