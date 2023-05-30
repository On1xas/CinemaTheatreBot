from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message

button_start=[KeyboardButton(text='Start')]

kb_start_bl=ReplyKeyboardBuilder()
kb_start_bl.row(*button_start)
kb_start=kb_start_bl.as_markup(resize_keyboard=True, one_time_keyboard=True)