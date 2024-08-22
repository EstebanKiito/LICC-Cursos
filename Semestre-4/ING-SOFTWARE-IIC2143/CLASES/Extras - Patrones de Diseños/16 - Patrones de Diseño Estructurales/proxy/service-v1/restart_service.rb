require_relative 'service'

class RestartService < Service
  def operate
    puts 'restarting the server'
  end
end