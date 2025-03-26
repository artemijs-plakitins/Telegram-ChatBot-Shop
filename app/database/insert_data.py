import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from app.database.models import Category, async_session
from app.database.models import engine


async def insert_shop_categories():
    async with async_session() as session:
    
        result = await session.execute(select(Category))
        categories = result.scalars().all()

        if not categories:
            session.add_all([
                Category(id=1, category_name="T-Shirts"),
                Category(id=2, category_name="Pants"),
                Category(id=3, category_name="Sneakers")
            ])
            await session.commit()
            print("Shop categories added!")
        else:
            print("Categories already exist, skipping insertion.")