# TODO Найдите количество книг, которое можно разместить на дискете

bytes_in_sign = 4
signs_in_line = 25
lines_in_page = 50
pages_in_book = 100
disket_size = 1.44

book_size = bytes_in_sign * signs_in_line * lines_in_page * pages_in_book
max_books_in_disket = int(disket_size * 1024 ** 2 // book_size)
print("Количество книг, помещающихся на дискету:", max_books_in_disket)
