CREATE
#Python Command
Book.objects.create(title="1984",author="George Orwell",publication_year="1949")

#Output
<Book: 1984 by George Orwell published in 1949>

READ
#Python Command
Book.objects.all()

#Output
<QuerySet [<Book: 1984 by George Orwell published in 1949>]>

UPDATE
#Python Command
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four") 

#Output
1

DELETE
#Python Command
Book.objects.filter(author="George Orwell").delete()


#Output
(1, {'bookshelf.Book': 1})
