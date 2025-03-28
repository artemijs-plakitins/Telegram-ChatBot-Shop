from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

import app.database.requests


workerMenuKeys = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Deliver today')],
    [KeyboardButton(text='Already delivered')],
    [KeyboardButton(text='Work-Account')]],resize_keyboard=True, input_field_placeholder='Choose a button...')


cityKeys = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Riga',callback_data='rigaCity')],
    [InlineKeyboardButton(text='Liepaja',callback_data='liepajaCity')],
    [InlineKeyboardButton(text='Daugavpils',callback_data='daugavpilsCity')]])


cityKeys = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Riga',callback_data='rigaCity')],
    [InlineKeyboardButton(text='Liepaja',callback_data='liepajaCity')],
    [InlineKeyboardButton(text='Daugavpils',callback_data='daugavpilsCity')]])