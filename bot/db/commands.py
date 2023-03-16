from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from bot.db.engine import get_session
from bot.db.sсhemas import User


class DataBase:
    def __init__(self):
        self.user = DBUser()


class DBUser:
    @staticmethod
    async def create_user(user_id: int, username: str, ):
        user = User(
            user_id=user_id,
            username=username
        )
        async with get_session() as session:
            session.add(user)
            try:
                await session.commit()
            except IntegrityError:
                await session.rollback()

    @staticmethod
    async def get_user(user_id: int):
        async with get_session() as session:
            user = await session.execute(select(User).where(User.user_id == user_id))
            return user.scalar()

    @staticmethod
    async def add_new_message(user_id, role, content):
        async with get_session() as session:
            user = await session.execute(select(User).where(User.user_id == user_id))
            messages = user.scalar().messages or []
            user_update = update(User).where(User.user_id == user_id)\
                .values({User.messages: messages + [{'role': role, 'content': content}]})
            await session.execute(user_update)
            await session.commit()

    @staticmethod
    async def delete_messages(user_id):
        async with get_session() as session:
            user_update = update(User).where(User.user_id == user_id) \
                .values({User.messages: []})
            await session.execute(user_update)
            await session.commit()
