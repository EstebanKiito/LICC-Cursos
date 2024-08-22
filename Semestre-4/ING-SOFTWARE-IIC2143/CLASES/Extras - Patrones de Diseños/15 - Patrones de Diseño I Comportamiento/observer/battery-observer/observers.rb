class Observer
    # la clase bateria no debe saber quien la observa
    # el metodo update recibe la bateria
    # porque no sabe que información necesitaran los objetos que lo observaran
    def update(battery)
        raise NotImplementedError
    end
end

class LowBatteryObserver < Observer
    def update(battery)
        # un problema es que la clase bateria tiene que tener accesores para que los observadores consulten su información
        if battery.carga() < 20
            puts 'low battery'
        end
    end
end
class PowerOffObserver < Observer
    def update(battery)
        if battery.carga() == 0
            puts 'bye bye'
        end
    end
end