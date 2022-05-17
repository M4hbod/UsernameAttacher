from pyrogram import Client, filters
from pyrogram.types import Message

from asyncio import sleep
from helpers.database import db

@Client.on_message(filters.channel & filters.regex(r"^(set)") & ~filters.forwarded, group=-4)
async def set_mode(client: Client, message: Message):
    me=await client.get_chat_member(message.chat.id, "me")
    if message.chat.username:
        if me.can_edit_messages:
            mode_text=message.text[4:].strip().lower()
            if mode_text in ['normal', 'bold', 'italic', 'underline', 'strike']:
                mode=mode_text
            else:
                await message.edit('Incorrect mode!')
                return
            try:
                await db.set_mode(message.chat.id, mode)
                await message.edit(f"Mode Changed To -> {mode}")
            except Exception as e:
                print(e)
            await sleep(5)
            try:
                await message.delete()
            except:
                pass
    else:
        if me.can_edit_messages:
            await message.edit("Your channel is private so you can't use this bot!")
