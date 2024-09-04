


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer