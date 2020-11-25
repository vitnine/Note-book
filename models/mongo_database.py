from typing import List, Optional, Union
import addict
import pytz
from aiogram import types
from bson import ObjectId
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
                    'role': 'user'
                }
            },
            upsert=True,
        )

    async def get_user_state(self) -> None:
        user = await self.db.users.find_one({"user_id": self.user.id})
        return user['state']

    async def set_user_state(self, state: str, user_id=None) -> None:
        user_id_ = user_id
        if not user_id_:
            user_id_ = self.user.id
        await self.db.users.update_one(
            filter={"user_id": user_id_},
            update={
                '$set': {
                    f'state': state,
                }
            },
        )

    async def set_user_role(self, role, user_id) -> None:
        await self.db.users.update_one(
            filter={"user_id": user_id},
            update={
                '$set': {
                    f'role': role,
                }
            },
        )

    async def is_user_exist(self) -> bool:
        user = self.db.users.find(filter=self.chat_user_filter())
        if len(await user.to_list(100)) > 0:
            return True
        else:
            return False

    def chat_user_filter(self):
        return {
            'user_id': self.user.id,
            'chat_id': self.chat_id
        }

    async def set_new_field(self, name: str, name_type: str):
        await self.db.note_book.update_one(
            filter={'user_id': self.user.id, 'CREATOR': self.user.username},
            update={
                '$set': {
                    name_type: name,
                }
            },
            upsert=False
        )

    async def new_note(self) -> None:
        await self.db.note_book.update_one(
            filter={"user_id": self.user.id},
            update={
                '$set': {
                    'CREATOR': self.user.username,
                    'SELF_PHONE': '',
                    'HOME_PHONE': '',
                    'WORK_PHONE': '',
                    'NAME': '',
                    'SURNAME': '',
                    'MIDDLE_NAME': '',
                    'INDEX': '',
                    'AREA': '',
                    'SETTLEMENT': '',
                    'STREET': '',
                    'HOUSE': '',
                    'CORPUS': '',
                    'FLAT': ''
                }
            },
            upsert=True,
        )

    async def delete_not_finished_note(self) -> None:
        self.db.note_book.delete_many({"user_id": self.user.id})

    async def confirm_new_contact(self) -> None:
        self.db.note_book.update_one({"user_id": self.user.id}, {"$unset": {"user_id": 1}})

    async def confirm_changed_contact(self) -> None:
        self.db.note_book.update_one({"user_id": self.user.id}, {"$unset": {"user_id": 1, "changing": 1}})

    async def find_contact(self, inf) -> List[str]:
        inter = inf.split()
        for i, el in enumerate(inter):
            inter[i] = el.capitalize()
        inter = set(inter)
        coincidences = []

        contacts = self.db.note_book.find({},)
        async for contact in contacts:
            contact['CREATOR'] = contact['CREATOR'].capitalize()
            setted = set(contact.values())
            print(setted)
            result = setted.intersection(inter)
            print(result)
            contact['CREATOR'] = contact['CREATOR'].lower()
            if inter.issubset(setted):
                coincidences.append(contact)

        return coincidences

    async def delete_contact(self, id_) -> None:
        self.db.note_book.delete_many({"_id": ObjectId(id_)})

    async def check_id(self, id_) -> str:
        result = await self.db.note_book.find_one({"_id": ObjectId(id_)})
        return result

    async def get_contact_by_id(self, id_):
        return await self.db.note_book.find_one({"_id": ObjectId(id_)})

    async def get_contact_id(self):
        result = await self.db.note_book.find_one({'user_id': self.user.id})
        return result['_id']

    async def set_user_id_for_note(self, id_):
        await self.db.note_book.update_one(
            filter={"_id": ObjectId(id_)},
            update={
                '$set': {
                    'user_id': self.user.id,
                    'changing': True
                }
            },
            upsert=False,
        )

    async def check_changing_status(self) -> str:
        result = await self.db.note_book.find_one({'user_id': self.user.id, 'changing': True})
        return result

    async def get_user_role(self):
        result = await self.db.users.find_one({'user_id': self.user.id})
        return result['role']

    async def get_all_admins(self):
        admins = []
        result = self.db.users.find({'user_id': self.user.id})
        async for user in result:
            if user['role'] == 'admin':
                admins.append(user['user_id'])
        return admins
