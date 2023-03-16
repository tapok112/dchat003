from typing import Any
from typing import Awaitable
from typing import Callable
from typing import Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from bot.db.commands import DataBase


class RegisterCheck(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        db = DataBase()
        user = event.from_user
        auth_user = await db.user.get_user(user.id)

        if not auth_user:
            await db.user.create_user(user.id, user.username)

        return await handler(event, data)
