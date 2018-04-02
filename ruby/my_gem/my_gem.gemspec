
lib = File.expand_path("../lib", __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require "my_gem/version"

Gem::Specification.new do |spec|
  spec.name          = "my_gem"
  spec.version       = MyGem::VERSION
  spec.authors       = ["shashank"]
  spec.email         = ["standon@tavisca.com"]

  

spec.summary = "builder gem for calculation"
  spec.files         = [
 "lib/my_gem.rb"
  ]
  
  spec.bindir        = "exe"
  spec.require_paths = ["lib"]

end
