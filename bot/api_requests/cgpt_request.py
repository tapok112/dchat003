import openai
from aiogram.utils.markdown import hide_link
from openai.error import RateLimitError

from bot.config_reader import conf

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

from bot.db.commands import DataBase

openai.api_key = conf.cgpt.token
db = DataBase()


async def ai_response(prompt, user_id, chosen_ai):
    if chosen_ai == ('dalle'):
        return await dalle_response(prompt)
    else:
        return await chat_response(prompt, user_id)


@retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(3))
async def chat_response(prompt, user_id):
    await db.user.add_new_message(user_id, "user", prompt)
    user = await db.user.get_user(user_id)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=user.messages
        )
        await db.user.add_new_message(user_id, "assistant", response.choices[0]['message']['content'])
        return response.choices[0]['message']['content']

    except RateLimitError as error:
        return f"Ограничение скорости запросов: {str(error)}"


async def dalle_response(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return f"{prompt}{hide_link(response['data'][0]['url'])}"

    except RateLimitError as error:
        return f"Ограничение скорости запросов: {str(error)}"
