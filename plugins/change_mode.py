import contextlib
from asyncio import sleep

from helpers.database import db
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.channel & filters.regex("^(setmode)") & ~filters.forwarded, group=-4)
async def set_mode(client: Client, message: Message):
    me = await client.get_chat_member(message.chat.id, "me")
    channel = await db.get_channel_info(message.chat.id)

    if me.can_edit_messages:
        mode_text = message.text.split()
        if len(mode_text) != 2:
            return await message.edit('Incorrect mode!')
        mode_text = mode_text[1].strip().lower()
        
        if mode_text in ['normal', 'bold', 'italic', 'underline', 'strike']:
            mode = mode_text
        else:
            await message.edit('Incorrect mode!')
            return
        
        await db.set_mode(message.chat.id, mode)
        with contextlib.suppress(Exception):
            await message.edit(f"Mode Changed To -> {mode}")
        await sleep(5)
        
        with contextlib.suppress(Exception):
            await message.delete()
