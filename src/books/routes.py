from fastapi import APIRouter, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional
from typing import List
from src.books.books import Book, BookUpdate, books

book_routes = APIRouter()

@book_routes.get('/', response_model=List[Book])
async def get_all_books():
    """
    Retrieve a list of books.
    Returns:
        List[Book]: A list of Book objects.
    """
    return books

@book_routes.post('/', status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: Book) -> dict:
    """
    Create a new book.
    Args:
        book (Book): The book to create.
    Returns:
        Book: The created book.
    """
    book = book.model_dump()
    books.append(book)
    return book

@book_routes.get('/{book_id}')
async def get_book(book_id: int) -> dict:
    """
    Retrieve a book by its ID.
    Args:
        book_id (int): The ID of the book to retrieve.
    Returns:
        Book: The retrieved book.
    """
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

@book_routes.patch('/{book_id}')
async def update_book(book_id: int, update_data: BookUpdate) -> dict:
    """
    Update a book by its ID.
    Args:
        book_id (int): The ID of the book to update.
        update_data (BookUpdate): The updated book data.
    Returns:
        Book: The updated book.
    """
    for book in books:
        if book['id'] == book_id:
            book.update(update_data.model_dump())
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

@book_routes.delete('/{book_id}')
async def delete_book(book_id: int) -> dict:
    """
    Delete a book by its ID.
    Args:
        book_id (int): The ID of the book to delete.
    Returns:
        dict: A message indicating the deletion status.
    """
    for index, book in enumerate(books):
        if book['id'] == book_id:
            del books[index]
            return {"message": "Book deleted successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")






@book_routes.get('/')
async def home():
    return {"message": "Welcome to the Book API!"}

@book_routes.get('/greet/{name}')
async def greet(name: str, age: Optional[int] = 0) -> dict:
    return {"message": f"Hello, {name}! You are {age} years old."}

@book_routes.get('/get_headers')
async def get_headers(
    user_agent: str = Header(None), content_type: str = Header(None)) -> dict:
    return {
        "User-Agent": user_agent,
        "Content-Type": content_type
            }
