from relationship_app.models import Author,Book,Librarian,Library
#Query all books by a particular author

book1 = Book.objects.get(id=1)


#List all books in a library.
library1 = Library.objects.get(name='Francis Idachaba')
print(library1)

#Retrieve the librarian for a library.

librarian1 = Librarian.objects.all()
print(librarian1)