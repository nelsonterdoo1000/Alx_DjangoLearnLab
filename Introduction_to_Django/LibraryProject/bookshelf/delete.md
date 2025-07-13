#Python Command
book = Book.objects.get(author="George Orwell")
book.delete()


#Output
(1, {'bookshelf.Book': 1})
