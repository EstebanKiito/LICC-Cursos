require 'colorize'
require_relative 'track'
require_relative 'music_player'

player = MusicPlayer.new()
player.add(Track.new("A1",10))
player.add(Track.new("A2",20))
player.add(Track.new("A3",11))
player.add(Track.new("A4",13))
player.add(Track.new("A5",15))
player.add(Track.new("A6",18))

run = true
player.playFirst()
player.print()
while run
    command = gets.strip
    puts command
    if command == "next"
        player.playNext()
    elsif command == "exit"
        run = false
    else
        player.strategy= command
    end
    player.print()
end

