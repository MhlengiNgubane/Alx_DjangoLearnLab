from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookL

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer