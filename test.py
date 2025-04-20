from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import asyncio

engine = create_async_engine("mysql+asyncmy://charis:ayanfeoluwa@localhost:3306/bookly_db", echo=True)

async def test():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        print(result.all())

asyncio.run(test())
