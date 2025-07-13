#Python Command
from bookshelf.models import Book
book = Book.objects.get(author="George Orwell")
book.delete()


#Output
(1, {'bookshelf.Book': 1})
