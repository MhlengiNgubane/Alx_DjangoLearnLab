from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    """
    View to list all books or create a new book.
    - GET: List all books.
    - POST: Create a new book (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a book by its ID.
    - GET: Retrieve a book.
    - PUT/PATCH: Update a book (requires authentication).
    - DELETE: Delete a book (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
