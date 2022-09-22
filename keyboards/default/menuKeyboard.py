from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kirish'),
            KeyboardButton(text='INFO')
        ],
    ],
    resize_keyboard=True
)