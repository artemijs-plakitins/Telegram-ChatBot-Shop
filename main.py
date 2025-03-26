import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

# project
from app.handlers import router
from app.database.models import async_main
from app.database.insert_data import insert_shop_categories

async def main():
    await async_main()
    await insert_shop_categories()
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())