require_relative 'battery'
require_relative 'observers'

bat = Battery.new
bat.add(LowBatteryObserver.new)
bat.add(PowerOffObserver.new)
bat.consume(256000)
