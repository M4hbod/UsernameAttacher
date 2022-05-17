from pyrogram import Client, filters
from pyrogram.types import Message

from helpers.functions import handle_user_status

@Client.on_message(filters.private | filters.channel, group=-1)
async def _(bot: Client, message: Message):
    await handle_user_status(bot, message)

@Client.on_message(filters.group, group= 9)
async def leave_groups(client: Client, message: Message):
    await client.send_message(message.chat.id,"I'm not designed to work in groups.\nHave a good time :)")
    await client.leave_chat(message.chat.id)
