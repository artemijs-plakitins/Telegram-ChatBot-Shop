from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart


import app.keyboards as kb
import app.database.requests as rq


router = Router()

# message handlers
@router.message(CommandStart())
async def commandStart(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(
        'Hi! Great to have you back at work! Before getting started,'
        ' please register your workday by sending /startworkday.')


# keyboard handlers

@router.message(F.text=='/startworkday')
async def registerWorkDay(message: Message):
    await message.answer('Your workday has begun!', reply_markup=kb.workerMenuKeys)

@router.message(F.text=='Deliver today')
async def openCityKeys(message: Message):
    await message.answer('Select a city', reply_markup=kb.cityKeys)


# callback handlers

@router.callback_query(F.data.in_(rq.cityList))
async def showCityOrders(callback: CallbackQuery):
    city = callback.data
    await callback.answer(f'{city} selected')
    orders_info = await rq.get_order_by_city(city)
    if orders_info:
        for order_id, address, paid_status in orders_info:
            await callback.message.answer(f"Order information --> Order ID: {order_id}, Address: {address}, Paid: {paid_status}")
    else:
        await callback.message.answer(f"No orders found for {city}.")