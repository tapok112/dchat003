from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.db.commands import DataBase


async def exit_chat(callback: CallbackQuery, state: FSMContext):
    db = DataBase()
    await state.clear()
    await db.user.delete_messages(callback.from_user.id)
    await callback.message.answer(
        text="Генерация окончена, теперь вы можете начать новый чат, или генерацию изображений"
    )
