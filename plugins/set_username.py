import contextlib
from asyncio import sleep

from helpers.database import db
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.channel & filters.text & filters.regex("^(setusername)") & ~filters.forwarded, group=-3)
async def set_usernme(client: Client, message: Message):
    me = await client.get_chat_member(message.chat.id, "me")
    if me.can_edit_messages:
        channel_username = message.text.split()
        if len(channel_username) != 2:
            return await message.edit('Incorrect Usage!\nUsage: setusername <username>')
        channel_username = channel_username[1].strip()
        if channel_username.startswith('@'):
            channel_username = channel_username.replace('@', '')
        await db.set_username(message.chat.id, channel_username)
        with contextlib.suppress(Exception):
            await message.edit(f"Default Username Changed To -> {channel_username}")
        await sleep(5)
        with contextlib.suppress(Exception):
            await message.delete()
