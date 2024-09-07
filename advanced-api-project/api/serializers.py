from rest_framework import serializers

from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model. Validates that publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure that the publication year is not in the future.
        """
        if value > 2024:  # Adjust this to the current year or your requirement
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model, including a nested BookSerializer for related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
