require_relative 'bot'
require_relative 'service'
require_relative 'restart_service'
require_relative 'scan_service'

bot = Bot.new
bot.perform(ScanService.new, false)

