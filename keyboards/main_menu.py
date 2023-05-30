from aiogram.types import BotCommand
from aiogram import Bot

async def main_menu(bot: Bot):
    main_menu_commands=[
        BotCommand(command='/start', description='Вернуться в Главное меню'),
        BotCommand(command='/contact', description='Как c нами связаться'),
        BotCommand(command='/help', description='Справка по взаимодействию в ботом'),
        BotCommand(command='/afisha', description='Кинофильмы в прокате')
    ]
    await bot.set_my_commands(main_menu_commands)
