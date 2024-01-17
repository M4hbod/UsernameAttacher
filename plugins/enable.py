import contextlib
from asyncio import sleep

from helpers.database import db
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.channel & filters.text & filters.regex("^(enable)$") & ~filters.forwarded,
    group=-3,
)
async def enabler(client: Client, message: Message):
    me = await client.get_chat_member(message.chat.id, "me")
    channel = await db.get_channel_info(message.chat.id)

    if not message.chat.username and channel["username"] == "default":
        if me.privileges.can_edit_messages:
            await message.edit(
                "Your channel is private and you haven't set any username, so you can't use this bot!"
            )
        return

    if me.privileges.can_edit_messages:
        if channel["enabled"] == True:
            await message.edit("It's already turned ON✅")
        else:
            await db.enable(message.chat.id)
            await message.edit("Enabled✅")
        await sleep(5)
        with contextlib.suppress(Exception):
            await message.delete()
    elif me.privileges.can_post_messages:
        with contextlib.suppress(Exception):
            await message.reply("Give me Edit Message permission then try again")
    else:
        with contextlib.suppress(Exception):
            await client.send_message(
                message.from_user.id, "Give me Edit Message permission then try again"
            )
