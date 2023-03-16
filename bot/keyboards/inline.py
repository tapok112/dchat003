from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def make_row_keyboard(items: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for item in items:
        builder.button(text=item, callback_data=str(item))
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите AI")


available_ai_names = ["ChatGPT", "DALLE", "Отмена"]