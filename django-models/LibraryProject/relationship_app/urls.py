from django.urls import path
from .views import list_books
from .views import LibraryDetailsView

urlpatterns = [
    path('book_list/',list_books ),
    path('library_details/<int:pk>/',LibraryDetailsView.as_view()),
]
