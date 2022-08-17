import datetime

import motor.motor_asyncio
from config import BOT_USERNAME, DATABASE_URL


class Database:
    def __init__(self, uri, database_name):
        self._client=motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db=self._client[database_name]
        self.col=self.db

    def get_user_dict(self, chat_id: int):
        return dict(
            id=chat_id,
            join_date=datetime.date.today().isoformat()
        )

    def get_channel_dict(self, chat_id: int, defult_type: str):
        return dict(
                id=chat_id,
                join_date=datetime.date.today().isoformat(),
                settings=dict(
                    enabled=False,
                    mode=defult_type,
                    username='default'
                )
            )

    async def add_user(self, chat_id: int):
        user=self.get_user_dict(chat_id)
        await self.col.users.insert_one(user)
    
    async def add_channel(self, chat_id: int, defult_type: str):
        channel=self.get_channel_dict(chat_id, defult_type)
        await self.col.channels.insert_one(channel)

    async def is_user_exist(self, chat_id: int):
        user=await self.col.users.find_one({"id": chat_id})
        return bool(user)

    async def is_channel_exist(self, chat_id: int):
        channel=await self.col.channels.find_one({"id": chat_id})
        return bool(channel)

    async def get_channel_info(self, chat_id: int):
        default = dict(enabled=False, mode='normal', username='default')
        chat = await self.col.channels.find_one({"id": chat_id})
        return chat.get("settings", default)

    async def enable(self, chat_id: int):
        channel=await self.get_channel_info(chat_id)
        mode=channel['mode']
        username=channel['username']
        channel=dict(
            enabled=True,
            mode=mode,
            username=username
        )
        await self.col.channels.update_one({"id": chat_id}, {"$set": {"settings": channel}})

    async def disable(self, chat_id: int):
        channel=await self.get_channel_info(chat_id)
        mode=channel['mode']
        username=channel['username']
        channel=dict(
            enabled=False,
            mode=mode,
            username=username
        )
        await self.col.channels.update_one({"id": chat_id}, {"$set": {"settings": channel}})

    async def set_mode(self, chat_id: int, mode: str):
        channel=await self.get_channel_info(chat_id)
        status=channel['enabled']
        username=channel['username']
        channel=dict(
            enabled=status,
            mode=mode,
            username=username
        )   
        await self.col.channels.update_one({"id": chat_id}, {"$set": {"settings": channel}})
        
    async def set_username(self, chat_id: int, username: str):
        channel=await self.get_channel_info(chat_id)
        status=channel['enabled']
        mode=channel['mode']
        channel=dict(
            enabled=status,
            mode=mode,
            username=username
        )   
        await self.col.channels.update_one({"id": chat_id}, {"$set": {"settings": channel}})

# Database
db=Database(DATABASE_URL, BOT_USERNAME)
