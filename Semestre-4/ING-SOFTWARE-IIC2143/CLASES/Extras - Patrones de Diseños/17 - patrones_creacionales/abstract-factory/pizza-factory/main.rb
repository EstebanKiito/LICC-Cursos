require_relative 'chicago_pizza_store'
require_relative 'ny_pizza_store'


storefactory = NYPizzaStore

store = storefactory.new
pizza = store.orderPizza('cheese')
pizza = store.orderPizza('cheese')
pizza = store.orderPizza('cheese')


