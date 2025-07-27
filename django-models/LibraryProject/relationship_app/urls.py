from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from relationship_app.views import RegisterView
from django.contrib.auth.views import LoginView,LogoutView




urlpatterns = [
    path('book_list/',list_books ),
    path('library_details/<int:pk>/',LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('signup/',RegisterView.as_view(template_name='relationship_app/register.html'),name='signup'),
]
