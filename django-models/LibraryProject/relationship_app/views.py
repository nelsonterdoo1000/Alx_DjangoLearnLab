from .models import Book, Author, Librarian,Library
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

def BookListView(request):

    books = Book.objects.all()
    context = {'books':books}
    return render(request,'relationship_app/list_books.html',context)



class LibraryDetailsView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

