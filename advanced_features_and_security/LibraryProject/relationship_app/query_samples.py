import os

import django
from relationship_app.models import Author, Book, Librarian, Library

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")


def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")


def retrieve_librarian_for_library(library_name):
    try:
        library = Librarian.objects.get(library=library_name)
        librarian = library.librarian
        print(f'Librarian for {library_name}: {librarian.name}')
    except Library.DoesNotExist:
        print(f'Library with name "{library_name}" does not exist.')
    except Librarian.DoesNotExist:
        print(f'No librarian found for library "{library_name}".')
