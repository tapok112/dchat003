from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart

from bot.api_requests.cgpt_request import ai_response

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Приветствую тебя в чат-боте GPTRUSSIA! Этот бот способен ответить на все твои вопросы, и даже больше — решить сложные и не очень задачи. Скорее пробуй!')


@router.message(Command("help"))
async def cmd_start(message: Message):
    await message.answer("GPRRUSSIA — мощный чат-бот на основе нейротехнологий OpenAI. Бот ответит на все твои вопросы и поможет решить задачи.")


@router.message(F.text)
async def text_message(message: Message):
    response = ai_response(message.text)
    await message.reply(text=response)


@router.message()
async def other_message(message: Message):
    await message.reply('Я понимаю только текстовый и голосовой ввод. \nОтправьте сообщение еще раз, но в формате понятном мне))!')
