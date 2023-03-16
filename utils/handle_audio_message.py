import os
import pathlib

import torch
from aiogram import Bot
from aiogram import Router
from aiogram.types import Message

from bot.api_requests.cgpt_request import ai_response
from utils.convert import audioconvert
from utils.speech2text import speech2text

router = Router()

WORKDIR = str(pathlib.Path(__file__).parent.absolute())
TEMODEL = "models/v2_4lang_q.pt"
tmodel = torch.package.PackageImporter(TEMODEL).load_pickle("te_model", "model")


async def handle_audio_message(message: Message, bot: Bot, chosen_ai):
    message_file = message.voice

    downpath = WORKDIR + "/" + message_file.file_unique_id
    await bot.download(file=message_file, destination=downpath)

    path = audioconvert(downpath)
    if not path:
        return False

    text = speech2text(path)
    os.remove(path)

    if not text or text == "" or text == " ":
        await message.answer('Не удалось распознать, или сообщение пустое, попробуйте еще раз')
        return False
    else:
        text = tmodel.enhance_text(text, 'ru')

    response = await ai_response(text, message.from_user.id, chosen_ai)

    return response

