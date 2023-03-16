from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

exit_chat_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Закончить генерацию',
                callback_data='exit_chat'
            )
        ]
    ])
