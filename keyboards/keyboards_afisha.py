from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inl_button_afisha_main: list[InlineKeyboardButton] = [[InlineKeyboardButton(text="<", url='google.com'),InlineKeyboardButton(text=">", url='google.com')]]
kb_inl_afisha_main: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=inl_button_afisha_main)
