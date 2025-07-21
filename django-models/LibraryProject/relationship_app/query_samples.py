from relationship_app.models import Author,Book,Librarian,Library
#Query all books by a particular author

author1 = Author.objects.get(name=author_name)

book1 = Book.objects.get(name=author_name)
book1.objects.filter(author=author)


#List all books in a library.
library1 = Library.objects.get(name=library_name)
library1.books.all()

#Retrieve the librarian for a library.

librarian1 = Librarian.objects.all()
print(librarian1)