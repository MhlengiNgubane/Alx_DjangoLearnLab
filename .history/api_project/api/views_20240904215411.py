from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Permission class to restrict access to authenticated users only
    permission_classes = [IsAuthenticated]