from django.urls import path
from .views import BookListView, LibraryDetailsView

urlpatterns = [
    path('book_list/',BookListView ),
    path('library_details/<int:pk>/',LibraryDetailsView.as_view()),
]
