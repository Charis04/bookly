from sqlmodel import Field, SQLModel, Column
from sqlalchemy import String, DateTime
import uuid
from datetime import datetime


class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            String(36),
            nullable=False,
            primary_key=True, 
            index=True
    ))
    title: str
    author: str
    average_rating: float
    review_count: int
    published_year: int
    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(
            DateTime,
            nullable=False,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(
            DateTime,
            nullable=False,
            default=datetime.now,
            onupdate=datetime.now
        )
    )

    def __repr__(self):
        return f"Book({self.title} by {self.author} {self.published_year})"

    def __str__(self):
        return f"Book({self.title} by {self.author} {self.published_year})"
