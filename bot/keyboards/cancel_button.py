from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

cancel_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ]
    ])
