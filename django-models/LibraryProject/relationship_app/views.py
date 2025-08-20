from .models import Library
from .models import Book
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .mixins import RoleRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse



def list_books(request):

    books = Book.objects.all()
    context = {'books':books}
    return render(request,'relationship_app/list_books.html',context)



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# class AdminView(RoleRequiredMixin,TemplateView):
#     template_name = ''
#     allowed_roles = ['Admin']

# class LibrarianView(RoleRequiredMixin,TemplateView):
#     template_name = ''
#     allowed_roles = ['Librarian']

# class MemberView(RoleRequiredMixin,TemplateView):
#     template_name = ''
#     allowed_roles = ['Member']

def is_admin(user):
    return user.is_authenticated and hasattr(user,'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request,'relationship_app/admin_view.html')

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and  user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request,'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and hasattr(user,'userprofile') and  user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request,'relationship_app/member_view.html')
