from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import admin_view
from .views import librarian_view
from .views import member_view
from django.contrib.auth.views import LoginView,LogoutView
from . import views




urlpatterns = [
    path('book_list/',list_books ),
    path('library_details/<int:pk>/',LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('signup/',views.register,name='signup'),
    path('admin_view/',admin_view),
    path('librarian_view/',librarian_view),
    path('member_view/',member_view),

]
