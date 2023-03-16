from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery


async def cancel_command(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()
    await callback.message.answer(
        text="Действие отменено"
    )
