# Bookly API

## Description

Bookly is a RESTful API built with FastAPI for managing a collection of books. It provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on book resources. The API also includes additional features like greeting users and retrieving request headers.

## Features

- **Get All Books**: Retrieve a list of all books in the collection.
- **Get Book by ID**: Retrieve details of a specific book using its unique ID.
- **Create Book**: Add a new book to the collection.
- **Update Book**: Modify the details of an existing book.
- **Delete Book**: Remove a book from the collection.
- **Greet User**: A simple endpoint to greet users by name and age.
- **Get Headers**: Retrieve request headers for debugging or informational purposes.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- FastAPI
- Uvicorn (for running the server)
- A database (if persistence is required; currently, the project uses an in-memory list)

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd bookly
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3.12 -m venv .env
    source .env/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn src.__init__:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

### Environment Variables

Create a `.env` file in the root directory to configure environment variables. Example:
```env
PORT=8000
DEBUG=True
```

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Books Endpoints

| Method | Endpoint               | Description                     |
|--------|------------------------|---------------------------------|
| GET    | `/api/v1.0/books`      | Retrieve all books.             |
| GET    | `/api/v1.0/books/{id}` | Retrieve a book by its ID.      |
| POST   | `/api/v1.0/books`      | Create a new book.              |
| PATCH  | `/api/v1.0/books/{id}` | Update an existing book.        |
| DELETE | `/api/v1.0/books/{id}` | Delete a book by its ID.        |

### Utility Endpoints

| Method | Endpoint               | Description                     |
|--------|------------------------|---------------------------------|
| GET    | `/api/v1.0/greet/{name}` | Greet a user by name and age.   |
| GET    | `/api/v1.0/get_headers` | Retrieve request headers.       |

## Example Usage

### Get All Books
```bash
curl http://127.0.0.1:8000/api/v1.0/books
```

### Create a New Book
```bash
curl -X POST http://127.0.0.1:8000/api/v1.0/books \
-H "Content-Type: application/json" \
-d '{
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "genre": "Classic"
    }'
```

### Update a Book
```bash
curl -X PATCH http://127.0.0.1:8000/api/v1.0/books/1 \
-H "Content-Type: application/json" \
-d '{
      "genre": "Tragedy"
    }'
```

### Delete a Book
```bash
curl -X DELETE http://127.0.0.1:8000/api/v1.0/books/1
```

## Project Structure

```
bookly/
├── src/
│   ├── __init__.py       # FastAPI app initialization
│   ├── books/
│   │   ├── routes.py     # Book-related API routes
│   │   ├── books.py      # Book models and in-memory data
├── .env/                 # Virtual environment
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Contact

For support or inquiries, contact:
- **Name**: Bookly API Support
- **Email**: charisadu@bookly.com
- **Website**: [Bookly Support](https://bookly.com/support)
