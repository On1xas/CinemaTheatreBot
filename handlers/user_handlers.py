from aiogram.filters import Command, CommandStart, Text
from aiogram import Router
from aiogram.types import Message

user_router: Router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Я живой')