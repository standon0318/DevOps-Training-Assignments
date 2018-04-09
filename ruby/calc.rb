require 'my_gem'

class Deff
	include MyGem
	include Neha
end
obj = Deff.new
puts obj.Addition(2,3)
puts obj.Substraction(92,3)

puts obj.SayHello
puts obj.SayBie