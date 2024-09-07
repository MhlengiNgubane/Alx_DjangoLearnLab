
## API Endpoints

### List and Create Books

- **URL:** `/books/`
- **Methods:** `GET`, `POST`
- **Permissions:** `IsAuthenticatedOrReadOnly`
- **Description:** Retrieve a list of all books or create a new book.

### Retrieve, Update, and Delete a Book

- **URL:** `/books/<int:pk>/`
- **Methods:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Permissions:** `IsAuthenticated`
- **Description:** Retrieve, update, or delete a book by its ID.

### Example Request (Create Book)

```json
POST /books/
Content-Type: application/json
Authorization: Token <your_token>

{
  "title": "New Book",
  "publication_year": 2024,
  "author": 1
}
