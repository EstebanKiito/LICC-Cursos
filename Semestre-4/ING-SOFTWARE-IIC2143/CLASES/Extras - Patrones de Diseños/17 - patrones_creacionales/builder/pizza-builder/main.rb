require_relative 'pizza'
require_relative 'cheese'
require_relative 'pineapple'
require_relative 'ham'
require_relative 'base_pizza'
require_relative 'pizza_builder'


hawaii_pizza = Pineapple.new(Cheese.new(Cheese.new(Ham.new(BasePizza.new))))
hawaii_pizza.print


builder = PizzaBuilder.new
builder.buildHawaiiPizza
hawaii_pizza2 = builder.getBuildedPizza
hawaii_pizza2.print

builder = PizzaBuilder.new
builder.buildWithHam
builder.buildWithCheese
hawaii_pizza3 = builder.getBuildedPizza
hawaii_pizza3.print

