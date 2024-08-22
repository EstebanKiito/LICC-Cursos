class Book
  attr_reader :title
  attr_reader :author
  attr_reader :year
  def initialize(title, author, year)
    @title = title
    @author = author
    @year = year
  end
  def print
    puts "#@title by #@author version #@year"
  end
end