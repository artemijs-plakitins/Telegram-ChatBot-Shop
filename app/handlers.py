from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart


import app.keyboards as kb
import app.database.requests as rq


router = Router()


@router.message(CommandStart())
async def commandStart(message: Message) -> None:
    await rq.set_user(message.from_user.id)
    await message.answer(
        'Hi! Great to have you back at work! Before getting started,'
        ' please register your workday by sending /startworkday.')



@router.message(F.text=='/startworkday')
async def registerWorkDay(message: Message) -> None:
    await message.answer('Your workday has begun!', reply_markup=kb.workerMenuKeys)

@router.message(F.text=='Deliver today')
async def openCityKeys(message: Message) -> None:
    await message.answer('Select a city', reply_markup=kb.cityKeys)



@router.callback_query(F.data.in_(rq.cityList))
async def showCityOrders(callback: CallbackQuery) -> None:
    city = callback.data
    await callback.answer(f'{city} selected')
    orders_info = await rq.get_order_by_city(city)
    if orders_info:
        for order_id, address, paid_status in orders_info:
            await callback.message.answer(f"Order information --> Order ID: {order_id}, Address: {address}, Paid: {paid_status}")
    else:
        await callback.message.answer(f"No orders found for {city}.")