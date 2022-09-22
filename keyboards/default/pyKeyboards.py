from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pyKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='something'),
            KeyboardButton(text='anything'),
            KeyboardButton(text='None'),
        ],
        [
            KeyboardButton(text='Back'),
            KeyboardButton(text='Home'),
        ],
    ],
    resize_keyboard=True
)