from dataclasses import dataclass
from os import getenv

from sqlalchemy.engine import URL


@dataclass
class Database:
    name: str = getenv("POSTGRES_DB")
    user: str = getenv("POSTGRES_USER")
    passwd: str = getenv("POSTGRES_PASSWORD")
    port: int = int(getenv("POSTGRES_PORT", 5432))
    host: str = getenv("POSTGRES_HOST")

    driver: str = "asyncpg"
    database_system: str = "postgresql"

    def build_connection_str(self) -> URL:
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            host=self.host,
            database=self.name,
            port=self.port,
            password=self.passwd,
        )


# @dataclass
# class Redis:
#     db: str = int(getenv("REDIS_DATABASE", 1))
#     host: str = getenv("REDIS_HOST")
#     port: int = int(getenv("REDIS_PORT", 6379))
#     passwd: int = getenv("REDIS_PASSWORD")
#     username: int = getenv("REDIS_USERNAME")
#     state_ttl: int = getenv("REDIS_TTL_STATE", None)
#     data_ttl: int = getenv("REDIS_TTL_DATA", None)


@dataclass
class Bot:
    token: str = getenv("TELEGRAM_API_KEY")
    admins: str = getenv("ADMIN_IDS")


@dataclass
class ChatGPT:
    token: str = getenv("OPENAI_API_KEY")


@dataclass
class Configuration:
    db = Database()
    # redis = Redis()
    bot = Bot()
    cgpt = ChatGPT()


conf = Configuration()
