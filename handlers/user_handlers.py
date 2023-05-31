from aiogram.filters import Command, CommandStart, Text
from aiogram import Router
from aiogram.types import Message
from keyboards.keyboard_start import BUTTONS, kb_start, kb_inl
from keyboards.keyboards_afisha import kb_inl_afisha_main
from aiogram.types import CallbackQuery
from keyboards.keyboard_start import inl_button, create_inline_kb




user_router: Router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = create_inline_kb(2, last_btn=None, b_1='1', b_2='2', b_3='3', b_4='4', b_5='5', b_6='Последняя кнопка')
    await message.answer(text='Я живой', reply_markup=keyboard)

@user_router.message(Command(commands=['afisha']))
async def cmd_afisha(message: Message):
    await message.answer(text='Я живой', reply_markup=kb_inl_afisha_main)

@user_router.callback_query(Text(text='TEST_PRESSED'))
async def cb_test(callback: CallbackQuery):
    await callback.message.answer(text='Нажали кнопку TEST')
    await callback.answer(text="Нажат тест", show_alert=True)