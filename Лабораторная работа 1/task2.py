# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
strings = 50
symbols = 25
cost = 4
Kb = 1024
Mb = 1024 * Kb
volume = 1.44 * Mb

symbols_in_book = symbols * strings * pages
cost_of_book = cost * symbols_in_book
num_of_books = round(volume / cost_of_book)

print("Количество книг, помещающихся на дискету:", num_of_books)
