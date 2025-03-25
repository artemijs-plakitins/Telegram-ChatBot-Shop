import os
import asyncio

# dotenv
from dotenv import load_dotenv

# aiogram
from aiogram import Bot, Dispatcher

# project
from app.handlers import router


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())