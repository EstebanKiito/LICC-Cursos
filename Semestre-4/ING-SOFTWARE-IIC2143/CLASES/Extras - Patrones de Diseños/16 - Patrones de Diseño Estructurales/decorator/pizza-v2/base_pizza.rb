require_relative 'pizza'

class BasePizza < Pizza

  def print
    puts 'normal bred'
  end

  def cost
    20
  end
end