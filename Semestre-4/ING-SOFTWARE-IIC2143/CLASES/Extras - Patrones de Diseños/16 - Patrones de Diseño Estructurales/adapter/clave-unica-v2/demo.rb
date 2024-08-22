require_relative 'login_service'
require_relative 'adapter'
require_relative 'client'

#str.gsub("subString", "")
service = LoginService.new
adaptador = LoginServiceAdapter.new(service)
client = ConsoleClient.new(adaptador)
client.run