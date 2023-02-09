import openai

from bot.config_reader import conf

openai.api_key = conf.cgpt.token


def ai_response(prompt):
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
