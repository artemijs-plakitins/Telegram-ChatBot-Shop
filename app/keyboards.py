from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

import app.database.requests


workerMenuKeys = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Deliver today')],
    [KeyboardButton(text='Already delivered')],
    [KeyboardButton(text='Work-Account')]],resize_keyboard=True,
      input_field_placeholder='Choose a button...')


cityKeys = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Riga',callback_data='Riga')],
    [InlineKeyboardButton(text='Liepaja',callback_data='Liepaja')],
    [InlineKeyboardButton(text='Daugavpils',callback_data='Daugavpils')]])