require_relative 'book.rb'
require_relative 'book_store.rb'

store = BookStore.new
store.add(Book.new("Testing","juampi",2022))
store.add(Book.new("Ing. Software","jaime",2022))
store.add(Book.new("Testing","rodrigo",2021))

puts 'searching for jaime'
store.filterByAuthor("jaime")

puts 'searching for testing'
store.filterByTitle("Testing")