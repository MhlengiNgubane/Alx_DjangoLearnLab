
### Compile Documentation**

```markdown
# CRUD Operations Documentation

## Create Operation
```python
from bookshelf.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()
print(book)

<Book: 1984>

## Retrieve Operation
book = Book.objects.get(title='1984')
print(book)

<Book: 1984>

## Update Operation
book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
print(book)

<Book: Nineteen Eighty-Four>

## Delete Operation
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
books = Book.objects.all()
print(books)

<QuerySet: []>
