from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    average_rating: float
    review_count: int
    published_year: int


class BookUpdate(BaseModel):
    title: str
    author: str
    average_rating: float
    review_count: int

books = [
      {
        "id": 1,
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "average_rating": 4.1,
        "review_count": 2534,
        "published_year": 2020
      },
      {
        "id": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "average_rating": 4.8,
        "review_count": 6789,
        "published_year": 2018
      },
      {
        "id": 3,
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "average_rating": 4.7,
        "review_count": 3411,
        "published_year": 2021
      },
      {
        "id": 4,
        "title": "Where the Crawdads Sing",
        "author": "Delia Owens",
        "average_rating": 4.5,
        "review_count": 8256,
        "published_year": 2018
      },
      {
        "id": 5,
        "title": "Educated",
        "author": "Tara Westover",
        "average_rating": 4.6,
        "review_count": 6092,
        "published_year": 2018
      }
    ]
  