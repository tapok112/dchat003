from aiogram import F
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup
from aiogram.types import CallbackQuery
from aiogram.types import Message

from bot.api_requests.cgpt_request import ai_response
from bot.keyboards.exit_chat_button import exit_chat_button
from bot.keyboards.inline import available_ai_names
from bot.keyboards.inline import make_row_keyboard


class BotStates(StatesGroup):
    choice_ai = State()


router = Router()


@router.message(CommandStart())
async def handle_cmd_start(message: Message):
    await message.answer("Привет, исследователь!\n"
                         "Я помогу решить любую твою задачу за несколько мгновений.\n"
                         "Cкорее отправляй мне своей запрос!")


@router.callback_query(BotStates.choice_ai, F.data.in_(available_ai_names))
async def handle_select_ai_callback(callback: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_ai=callback.data.lower())
    await callback.message.delete()
    user_data = await state.get_data()
    message = await ai_response(user_data['prompt'], callback.from_user.id, user_data['chosen_ai'])

    prompt_answer = await callback.message.answer(text=message,
                                                  parse_mode="HTML",
                                                  reply_markup=exit_chat_button)
    await state.update_data(prompt_answer=prompt_answer)


@router.message(BotStates.choice_ai)
async def handle_next_prompt(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(prompt=message.text)
        user_data = await state.get_data()
        await user_data['prompt_answer'].edit_reply_markup()
        response = await ai_response(user_data['prompt'], message.from_user.id, user_data['chosen_ai'])

        prompt_answer = await message.answer(response,
                                             parse_mode="HTML",
                                             reply_markup=exit_chat_button)
        await state.update_data(prompt_answer=prompt_answer)
    else:
        await message.answer(
            'Я понимаю только текстовый ввод. \nОтправьте сообщение еще раз, но в формате понятном мне))!')


@router.message()
async def handle_prompt(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(prompt=message.text)
        ai_choose_callback_answer = await message.answer(
            text="Выберите ИИ:",
            reply_markup=make_row_keyboard(available_ai_names)
        )
        await state.update_data(ai_choose_callback_answer=ai_choose_callback_answer)
        await state.set_state(BotStates.choice_ai)
    else:
        await message.answer(
            'Я понимаю только текстовый ввод. \nОтправьте сообщение еще раз, но в формате понятном мне))!')
