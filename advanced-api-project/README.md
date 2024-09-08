
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

## Testing

### Testing Strategy

We use Django’s built-in test framework to ensure the API endpoints for the `Book` model are functioning correctly. Tests cover CRUD operations, advanced query capabilities, and permission checks.

### Test Cases

1. **Create Book:** Verifies that a new book can be created and saved correctly.
2. **Read Book:** Ensures that retrieving a book by ID returns the correct data.
3. **Update Book:** Checks that updating a book reflects the changes in the database.
4. **Delete Book:** Confirms that a book can be deleted from the database.
5. **Filter Books:** Tests the filtering functionality based on various attributes.
6. **Search Books:** Validates that search functionality works as expected.
7. **Order Books:** Ensures that ordering works correctly based on specified fields.
8. **Permissions:** Tests access controls to ensure unauthenticated users are restricted.

### Running Tests

To run the tests, use the following command:

```bash
python manage.py test api
