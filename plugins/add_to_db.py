from pyrogram.enums import ChatType

from config import LOG_CHANNEL
from helpers.database import db
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message((filters.private | filters.channel), group=-1)
async def _(bot: Client, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        if not await db.is_user_exist(message.chat.id):
            await db.add_user(message.chat.id)
            await bot.send_message(
                chat_id=LOG_CHANNEL,
                text=f"**📣 Bot Notification.**\n\n📌 New #USER\n🧝🏻‍♂️ Name: {message.from_user.first_name}\n📮 Chat ID: `{message.chat.id}`\n🧝🏻‍♂️ Profile: {message.from_user.mention}",
            )
    elif message.chat.type == ChatType.CHANNEL:
        if not await db.is_channel_exist(message.chat.id):
            await db.add_channel(message.chat.id, "normal")
            await bot.send_message(
                chat_id=LOG_CHANNEL,
                text=f"**📣 Bot Notification.**\n\n📌 New #CHANNEL\n🧝🏻‍♂️ Name: {message.chat.title}\n📮 Chat ID: `{message.chat.id}`",
            )
    await message.continue_propagation()


@Client.on_message(filters.group, group=9)
async def leave_groups(client: Client, message: Message):
    await client.send_message(
        message.chat.id, "I'm not designed to work in groups.\nHave a great time :)"
    )
    await client.leave_chat(message.chat.id)
