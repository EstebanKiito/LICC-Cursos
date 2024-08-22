require_relative 'login_service'
require_relative 'client'

#str.gsub("subString", "")
originalService= LoginService.new
serviceProxy = LoginProxy.new(originalService)
client = ConsoleClient.new(originalService)
client.run