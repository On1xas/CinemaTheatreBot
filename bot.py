from aiogram import Bot, Dispatcher
from config.config import get_config, Config
from handlers.user_handlers import user_router
import asyncio

async def main():


    config: Config=get_config(".env")


    bot: Bot = Bot(config.token)
    dp: Dispatcher = Dispatcher()

    # Регистрация роутеров
    dp.include_router(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())