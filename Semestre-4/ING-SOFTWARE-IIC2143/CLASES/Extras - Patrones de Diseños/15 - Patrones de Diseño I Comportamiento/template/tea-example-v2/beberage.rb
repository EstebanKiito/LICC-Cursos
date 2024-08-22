
class Beberage
    # abstraemos la preparacion de la bebida
    # este metodo es una plantilla
    # el paso 2 y 4 son pasos faltantes que completan las clases hijas
    def prepareRecipe
        #paso 1: comun para tea y cafe
        boilWater
        #paso 2: varia para tea o cafe
        steepMainIngredient
        #paso 3: comun
        pourInCup
        #paso 4 varia
        steepTooping
    end
    def steepMainIngredient
        raise NotImplementedError
    end
    def steepTooping
        raise NotImplementedError
    end
    def pourInCup
        puts 'Pouring in cup'
    end
    def boilWater
        puts 'boiling water'
      end
end