from fastapi import FastAPI
from src.books.routes import book_routes

version = 'v1.0'
description = """
## Books API
This API allows you to manage a collection of books. You can perform CRUD operations on the books, including creating, reading, updating, and deleting book records.
### Features
- **Get Book by ID**: Retrieve a book's details using its unique ID.
- **Update Book**: Modify the details of an existing book.
- **Delete Book**: Remove a book from the collection using its ID.
- **Get All Books**: Retrieve a list of all books in the collection.
- **Greet User**: A simple endpoint to greet the user by name and age.
"""

app = FastAPI(
    title="Bookly",
    description=description,
    version=version,
    contact={
        "name": "Bookly API Support",
        "url": "https://bookly.com/support",
        "email": "charisadu@bookly.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    terms_of_service="https://bookly.com/terms",
    openapi_tags=[
        {
            "name": "books",
            "description": "Operations with books"
        },
        {
            "name": "users",
            "description": "Operations with users"
        }
    ],
    openapi_url=f"/api/{version}/openapi.json",
    docs_url=f"/api/{version}/docs",
    redoc_url=f"/api/{version}/redoc",
    openapi_version="3.0.2",
)

app.include_router(book_routes, prefix=f'/api/{version}/books', tags=['books'])
