import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from bot.commands.register_user_commands import register_user_commands
from bot.config_reader import conf
from bot.handlers.fsm import prompt_fsm
from bot.middlewares.register_check import RegisterCheck


async def main():
    logging.basicConfig(level=logging.DEBUG)

    dp = Dispatcher()

    dp.message.middleware(RegisterCheck())
    dp.callback_query.middleware(RegisterCheck())

    dp.include_router(prompt_fsm.router)

    bot = Bot(token=conf.bot.token)
    await bot.set_my_commands(commands=[])
    register_user_commands(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
