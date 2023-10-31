# TODO Найдите количество книг, которое можно разместить на дискете

book_size_bite=100*50*25*4
storage_size_bite=1.44*1024*1024

book_quantity=int(storage_size_bite//book_size_bite)

print("Количество книг, помещающихся на дискету:", book_quantity)
