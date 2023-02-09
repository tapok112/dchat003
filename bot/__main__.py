import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config_reader import conf
from bot.handlers import handle_message_types


async def main():
    logging.basicConfig(level=logging.DEBUG)

    dp = Dispatcher()

    dp.include_router(handle_message_types.router)

    bot = Bot(token=conf.bot.token)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
