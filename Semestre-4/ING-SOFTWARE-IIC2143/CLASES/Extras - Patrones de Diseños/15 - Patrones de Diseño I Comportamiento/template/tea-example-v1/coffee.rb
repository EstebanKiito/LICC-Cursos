
# esta clase tiene codigo duplicado
# con la clase tea
class Coffee
  # este metodo en particular es parecido al de la clase Tea
  # con excepcion de un par de pasos 
  def prepareRecipe
    boilWater
    brewCoffeeGrinds
    pourInCup
    addSugarAndMilk
  end
  def boilWater
    puts 'boiling water'
  end
  def brewCoffeeGrinds
    puts 'dripping coffee through filter'
  end
  def pourInCup
    puts 'Pouring in cup'
  end
  def addSugarAndMilk
    puts 'adding sugar and milk'
  end
end