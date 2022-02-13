import datetime
from pyrogram import Client
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from config import BOT_USERNAME, DATABASE_URL


class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        if "-100" in str(id):
            return dict(
                id = id,
                settings = dict(
                    join_date=datetime.date.today().isoformat(),
                    enabled=False,
                    mode='Normal'
                )
            )
        else:
            return dict(
                id=id,
                join_date=datetime.date.today().isoformat()
            )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def channel_status(self, chat_id):
        default = dict(
            join_date=datetime.date.today().isoformat(),
            enabled=False,
            mode='Normal'
        )
        chat = await self.col.find_one({"id": int(chat_id)})
        return chat.get("settings", default)

    async def set_enabled(self, chat_id):
        channel = dict(
            id=chat_id,
            enabled=True,
        )
        await self.col.update_one({"id": id}, {"$set": {"settings": channel}})

    async def set_disabled(self, chat_id):
        channel = dict(
            id=chat_id,
            enabled=False,
        )
        await self.col.update_one({"id": id}, {"$set": {"settings": channel}})

# Database
db = Database(DATABASE_URL, BOT_USERNAME)
