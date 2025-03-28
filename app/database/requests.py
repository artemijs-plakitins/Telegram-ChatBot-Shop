from sqlalchemy import select

from app.database.models import async_session
from app.database.models import User, Orders


async def set_user(telegram_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user:
            session.add(User(telegram_id = telegram_id))
            await session.commit()


async def get_order_by_city(city: str):
    async with async_session() as session:
        orders_address = await session.scalar(
            select(Orders.address_street).where(Orders.city == city))
        return orders_address