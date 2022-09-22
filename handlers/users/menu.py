from cgitb import text
import imp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import pyKeyboards
# from keyboards.default import pyKeyboard
from keyboards.default.menuKeyboard import menu
from keyboards.default.pyKeyboards import pyKeyboard

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Choose one of THIS!", reply_markup=menu) 

@dp.message_handler(text="INFO")
async def send_link(message: Message):
    await message.answer("Choose one of THIS ! https://t.me/+7v0Tr9684TQyYWEy") 

@dp.message_handler(text="Kirish")
async def send_link(message: Message):
    await message.answer("Choose one of THIS !", reply_markup=pyKeyboard) 

@dp.message_handler(text="Home")
async def send_link(message: Message):
    await message.answer("Choose one of THIS !", reply_markup=menu)