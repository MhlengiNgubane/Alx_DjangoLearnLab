from django.urls import path

from .views import (BookCreateView, BookDeleteView, BookDetailView,
                    BookListView, BookUpdateView)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a specific book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update a specific book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a specific book
]
