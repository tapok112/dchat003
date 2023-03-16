from aiogram import F
from aiogram import Router

from bot.commands.exit_chat_command import exit_chat
from bot.commands.cancel_command import cancel_command


def register_user_commands(router: Router) -> None:
    router.callback_query.register(cancel_command, F.data == 'cancel')
    router.callback_query.register(cancel_command, F.data == 'Отмена')
    router.callback_query.register(exit_chat, F.data == 'exit_chat')
