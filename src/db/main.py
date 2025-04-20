from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from src.config import config
from src.books.models import Book

engine: AsyncEngine = create_async_engine(
        url=config.DATABASE_URL,
        echo=True
)

async def init_db():
    """
    Initialize the database by creating all tables.
    This function should be called when the application starts to ensure that the database schema is up to date.
    """
    async with engine.begin() as conn:
        # Create the tables in the database
        await conn.run_sync(Book.metadata.create_all)
        # Optionally, you can also drop all tables if needed
        # await conn.run_sync(Book.metadata.drop_all)
