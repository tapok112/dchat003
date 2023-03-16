from sqlalchemy import BIGINT
from sqlalchemy import Column
from sqlalchemy import VARCHAR
from sqlalchemy.dialects.postgresql import JSONB

from bot.db import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BIGINT, unique=True, nullable=False, primary_key=True)
    username = Column(VARCHAR(32))
    messages = Column(JSONB)

    @property
    def stats(self) -> str:
        return ""

    def __str__(self) -> str:
        return f"<User:{self.user_id}>"

    def __repr__(self):
        return self.__str__()
