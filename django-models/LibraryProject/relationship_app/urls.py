from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('book_list/',list_books ),
    path('library_details/<int:pk>/',LibraryDetailView.as_view()),
]
