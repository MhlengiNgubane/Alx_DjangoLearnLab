from django.db import models


class Author(models.Model):
    """
    Represents an author with a name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with a title, publication year, and an associated author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
