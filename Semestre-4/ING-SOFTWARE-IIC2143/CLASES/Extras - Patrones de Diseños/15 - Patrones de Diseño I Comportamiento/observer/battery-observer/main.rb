

b = Battery.new
b.register(LowBatteryObserver.new)
b.register(NoBatteryObserver.new)

b.consume(10)
b.consume(10)
b.consume(10)
