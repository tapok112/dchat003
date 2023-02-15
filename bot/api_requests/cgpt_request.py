import openai
from openai.error import RateLimitError

from bot.config_reader import conf

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

openai.api_key = conf.cgpt.token


@retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(3))
def ai_response(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            temperature=0.95,
            prompt=prompt,
            max_tokens=1500,
            top_p=0.5,
            frequency_penalty=0.5,
            presence_penalty=0.5
        ).choices[0].text

        return response
    except RateLimitError:
        return "Ограничение скорости запросов, попробуйте еще раз позже"
