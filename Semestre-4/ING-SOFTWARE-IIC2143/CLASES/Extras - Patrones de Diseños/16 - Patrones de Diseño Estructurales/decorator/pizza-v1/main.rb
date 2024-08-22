require_relative 'ham_cheese_normal_pizza'
require_relative 'pineapple_ham_cheese_normal_pizza'


#el problema de esta solucion
# es que para cada combinacino de topping
# tenemos que crear una pizza
# si tenemos 3 tipos de toopings
# podriamos combinar ham+  pineable+ cheesse
# double cheesse + ham
# y asi sucesivamente
hawaii_pizza = PineableHamCheesePizza.new
hawaii_pizza.print
puts "#{hawaii_pizza.cost}"


basic_pizza = HamCheesePizza.new
basic_pizza.print
puts "#{basic_pizza.cost}"