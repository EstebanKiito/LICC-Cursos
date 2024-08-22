require_relative 'solution'
mac = MacBase.new
mac.print
mac2 = GPU16Upgrade.new(mac)
mac2.print
mac3 = RAM16Upgrade.new(GPU16Upgrade.new(mac))
mac3.print