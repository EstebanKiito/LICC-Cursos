require_relative 'element'

class SFile < FileElement
  def initialize(name,size)
    @size = size
    @name = name
  end
  def size
    @size
  end
  def print
    puts "#{@name} : #{@size}"
  end
end