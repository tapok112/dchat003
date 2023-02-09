from dataclasses import dataclass
from os import getenv


@dataclass
class Bot:
    token: str = getenv("TELEGRAM_API_KEY")


@dataclass
class ChatGPT:
    token: str = getenv("OPENAI_API_KEY")


@dataclass
class Configuration:
    bot = Bot()
    cgpt = ChatGPT()


conf = Configuration()
