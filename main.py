import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import token
from handlers import user_handlers


logging = logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')


# Функция конфигурирования и запуска бота
async def main() -> None:
    # Инициализируем бот и диспетчер

    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_routers(user_handlers.router)


    #Регистрируем роутеры
    # dp.include_routers(user_handlers.router, inline_kb.router, reply_kb.router)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "callback_query"])


asyncio.run(main())
