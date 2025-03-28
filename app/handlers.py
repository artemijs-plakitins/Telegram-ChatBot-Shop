from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup


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
async def openCatalog(message: Message):
    await message.answer('Your workday has begun!', reply_markup=kb.workerMenuKeys)

@router.message(F.text=='Deliver today')
async def openCatalog(message: Message):
    await message.answer('Select a city', reply_markup=kb.cityKeys)


# callback handlers

@router.callback_query(F.data=='rigaCity')
async def showTShirts(callback: CallbackQuery):
    await callback.answer('City selected')
    info_Riga_orders = await rq.get_order_by_city("Riga")
    await callback.message.answer(f'Oder information: {info_Riga_orders}')

@router.callback_query(F.data=='liepajaCity')
async def showTShirts(callback: CallbackQuery):
    await callback.answer('Category selected')
    await callback.message.answer('Selected City : Liepaja')

@router.callback_query(F.data=='daugavpilsCity')
async def showTShirts(callback: CallbackQuery):
    await callback.answer('Category selected')
    await callback.message.answer('Selected City : Daugavpils')