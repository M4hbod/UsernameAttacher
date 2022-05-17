from pyrogram import Client, filters
from pyrogram.types import Message

from asyncio import sleep
from helpers.database import db


@Client.on_message(filters.channel & filters.text & filters.regex(r"^(enable)$") & ~filters.forwarded, group=-3)
async def enabler(client: Client, message: Message):
    me=await client.get_chat_member(message.chat.id, "me")
    if message.chat.username:
        if me.can_edit_messages:
            channel=await db.get_channel_info(message.chat.id)
            if channel['enabled'] == True:
                await message.edit("It's already turned ON ✅")
            else:
                await db.enable(message.chat.id)
                await message.edit("Enabled ✅")
            await sleep(5)
            try:
                await message.delete()
            except:
                pass
        else:
            if not me.can_send_messages:
                try:
                    await client.send_message(message.from_user.id , "Give me Edit Message permission then try again")
                except:
                    pass
            else:
                try:
                    await message.reply("Give me Edit Message permission then try again")
                except Exception as e:
                    print(e)
                    return
    else:
        if me.can_edit_messages:
            await message.edit("Your channel is private so you can't use this bot!")
