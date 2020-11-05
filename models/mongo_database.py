from typing import List
import addict
import pytz
from aiogram import types
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase  # noqa


class ContextMixin:
    @property
    def chat_id(self):
        chat = types.Chat.get_current()
        return chat.id

    @property
    def user(self):
        user = types.User.get_current()
        return user


class MongoDB(ContextMixin):
    def __init__(
            self,
            mongo_client: AsyncIOMotorClient,
            mongo_database: AsyncIOMotorDatabase,
            collections: List[str],
    ) -> None:
        self._client = mongo_client
        self._database = mongo_database
        self.db = addict.Dict(**{name: self._database[name] for name in collections})
        self.timezone = pytz.timezone('Europe/Moscow')

    async def new_user(self, state: str) -> None:
        user = self.user
        await self.db.users.update_one(
            filter={"user_id": user.id, "chat_id": self.chat_id},
            update={
                '$set': {
                    f'additional_data.first_name': user.first_name,
                    f'additional_data.last_name': user.last_name,
                    f'additional_data.user_name': user.username,
                    f'state': state,
                    f'group_chat_ids': [],
                    "location": {"lat": 55.7504461, "lon": 37.6174943},  # TODO change
                    "timezone": "Europe/Moscow",  # TODO change
                    "entered_data": {},
                    "stage": "2"
                }
            },
            upsert=True,
        )
