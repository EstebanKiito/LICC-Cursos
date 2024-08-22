require_relative 'element'

class SFolder < FileElement
  def initialize(name)
    @name = name
    @elements = []
  end
  def add(element)
    @elements.push(element)
  end
  def print
    puts "#{@name}"
    @elements.each do |each|
      each.print
    end
  end
  def size
    total = 0
    @elements.each do |each|
      total = total + each.size
    end
    total
  end
end