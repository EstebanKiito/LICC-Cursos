require_relative 'observers'
require_relative 'observable'

counter = Counter.new
#counter.register(Logger.new)
counter.register(FixedObserver.new(3))

counter.increment
counter.increment
counter.increment
counter.increment
counter.increment
counter.decrement