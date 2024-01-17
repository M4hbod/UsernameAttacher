import contextlib
from asyncio import sleep

from helpers.database import db
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.channel & filters.text & filters.regex("^(disable)$") & ~filters.forwarded,
    group=-2,
)
async def disabler(client: Client, message: Message):
    me = await client.get_chat_member(message.chat.id, "me")
    channel = await db.get_channel_info(message.chat.id)

    if me.privileges.can_edit_messages:
        if channel["enabled"] == False:
            await message.edit("It's already turned OFF❌")
        else:
            await db.disable(message.chat.id)
            await message.edit("Disabled❌")

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
