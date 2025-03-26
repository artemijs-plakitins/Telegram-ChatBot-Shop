from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
import app.database.requests as rq

# State class

class Register(StatesGroup):
    nickname = State()
    email = State()
    phoneNumber = State()



router = Router()


# message handlers
@router.message(CommandStart())
async def commandStart(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Commands I undersatnd: /start, /shop, /register')


@router.message(F.text=='/shop')
async def enterShop(message: Message):
    await message.answer('You entered the Shop',reply_markup=kb.shopOpenKey)


# register handlers
@router.message(F.text=='/register')
async def showInformation(message: Message, state: FSMContext):
    await state.set_state(Register.nickname)
    await message.answer('Enter your nickname: ')

@router.message(Register.nickname)
async def registerName(message: Message, state: FSMContext):
    await state.update_data(nickname = message.text)
    await state.set_state(Register.email)
    await message.answer('Enter your Email address: ')

@router.message(Register.email)
async def registerName(message: Message, state: FSMContext):
    await state.update_data(email = message.text)
    await state.set_state(Register.phoneNumber)
    await message.answer('Enter your phone number: ')

@router.message(Register.phoneNumber)
async def registerPhoneNumber(message: Message, state: FSMContext):
    await state.update_data(phoneNumber = message.text)
    data = await state.get_data()
    await message.answer(
        f'Nickname: {data["nickname"]}\nEmail address: {data["email"]}\nPhone number: {data["phoneNumber"]}')
    await state.clear()


# keyboard handlers

@router.message(F.text=='Catalog')
async def openCatalog(message: Message):
    await message.answer('Select a category down bellow', reply_markup=kb.shopCatalogKey)


# callback handlers

@router.callback_query(F.data=='call-tShirts')
async def showTShirts(callback: CallbackQuery):
    await callback.answer('Category selected')
    await callback.message.answer('Selected category: T-Shirts')

@router.callback_query(F.data=='call-pants')
async def showTShirts(callback: CallbackQuery):
    await callback.answer('Category selected')
    await callback.message.answer('Selected category: Pants')

@router.callback_query(F.data=='call-sneakers')
async def showTShirts(callback: CallbackQuery):
    await callback.answer('Category selected')
    await callback.message.answer('Selected category: Sneakers')