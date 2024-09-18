# Social Media API

## Setup

1. Install dependencies:

   ```bash
   pip install django djangorestframework

2. Create the database and apply migrations:

    python manage.py makemigrations accounts
    python manage.py migrate

3. Run the development server:

    python manage.py runserver
   
### Posts

- **List Posts**: `GET /api/posts/`
- **Create Post**: `POST /api/posts/`
- **Retrieve Post**: `GET /api/posts/{id}/`
- **Update Post**: `PUT /api/posts/{id}/`
- **Delete Post**: `DELETE /api/posts/{id}/`

**Request Example:**

```json
{
    "title": "New Post",
    "content": "This is the content of the new post."
}

### comments

- **List comments**: `GET /api/comments/`
- **Create comments**: `POST /api/comments/`
- **Retrieve comments**: `GET /api/comments/{id}/`
- **Update comments**: `PUT /api/comments/{id}/`
- **Delete comments**: `DELETE /api/comments/{id}/`

**Request Example:**

```json
{
    "post": 1,
    "content": "This is a comment."
}