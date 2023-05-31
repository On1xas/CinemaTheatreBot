from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

button_start=[KeyboardButton(text='Start')]

kb_start_bl=ReplyKeyboardBuilder()
kb_start_bl.row(*button_start)
kb_start=kb_start_bl.as_markup(resize_keyboard=True, one_time_keyboard=True)

inl_button=[[InlineKeyboardButton(text='TEST', callback_data='TEST_PRESSED')]]

kb_inl=InlineKeyboardMarkup(inline_keyboard=inl_button)

BUTTONS: dict[str, str] = {'btn_1': '1',
                           'btn_2': '2',
                           'btn_3': '3',
                           'btn_4': '4',
                           'btn_5': '5'}

LEXICON: dict[str, str] = {'but_1': '1',
                           'but_2': '2',
                           'but_3': '3',
                           'but_4': '4',
                           'but_5': '5'}

# Функция для генерации инлайн-клавиатур "на лету"
def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Добавляем в билдер последнюю кнопку, если она передана в функцию
    if last_btn:
        kb_builder.row(InlineKeyboardButton(
                            text=last_btn,
                            callback_data='last_btn'))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()