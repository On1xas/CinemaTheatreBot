from aiogram.filters import Command, CommandStart, Text
from aiogram import Router
from aiogram.types import Message
from keyboards.keyboard_start import kb_start
from keyboards.keyboards_afisha import kb_inl_afisha_main
user_router: Router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Я живой', reply_markup=kb_start)

@user_router.message(Command(commands=['afisha']))
async def cmd_afisha(message: Message):
    await message.answer(text='Я живой', reply_markup=kb_inl_afisha_main)