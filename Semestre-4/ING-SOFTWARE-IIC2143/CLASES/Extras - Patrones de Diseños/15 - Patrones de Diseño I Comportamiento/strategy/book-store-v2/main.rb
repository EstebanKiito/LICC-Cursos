require_relative 'book.rb'
require_relative 'book_store.rb'
require_relative 'strategy.rb'

store = BookStore.new
store.add(Book.new("Testing","juampi",2022))
store.add(Book.new("Ing. Software","jaime",2022))
store.add(Book.new("Testing","rodrigo",2021))

puts("----")
puts 'searching for jaime'
store.filter(FilterByAuthorStrategy.new("jaime"))
puts("----")
puts 'searching for testing'
store.filter(FilterByTitleStrategy.new("Testing"))
puts("----")

puts 'searching for 2021-2021'
store.filter(FilterByYearRangeStrategy.new(2021,2021))
puts("----")