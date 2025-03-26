from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

# open shop (reply)
shopOpenKey = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Shopping cart')],
    [KeyboardButton(text='Account')],
    [KeyboardButton(text='About us')]],resize_keyboard=True, input_field_placeholder='Choose a button...')

# open catalog (inline)
shopCatalogKey = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='T-Shirts',callback_data='call-tShirts')],
    [InlineKeyboardButton(text='Pants',callback_data='call-pants')],
    [InlineKeyboardButton(text='Sneakers',callback_data='call-sneakers')]])