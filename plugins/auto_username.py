from pyrogram.enums import ParseMode

from helpers.database import db
from helpers.functions import get_caption
from pyrogram import Client, filters
from pyrogram.types import Message

GROUP_MEDIA = set()


@Client.on_message(filters.channel & ~filters.forwarded, group=1)
async def auto_username(client: Client, message: Message):
    channel = await db.get_channel_info(message.chat.id)
    if not message.chat.username and channel["username"] == "default":
        return
    me = await client.get_chat_member(message.chat.id, "me")
    if me.privileges.can_edit_messages and channel["enabled"] == True:
        if channel["username"] == "default":
            username = message.chat.username
        else:
            username = channel["username"]
        mode = channel["mode"]
        sign = ""
        if mode == "bold":
            sign = f"\n<b>@{username}</b>"
        elif mode == "italic":
            sign = f"\n<i>@{username}</i>"
        elif mode == "normal":
            sign = f"\n@{username}"
        elif mode == "strike":
            sign = f"\n<s>@{username}</s>"
        elif mode == "underline":
            sign = f"\n<u>@{username}</u>"
        caption = await get_caption(message)
        caption += sign
        if message.media_group_id:
            if message.media_group_id in GROUP_MEDIA:
                return
            else:
                GROUP_MEDIA.add(message.media_group_id)
        await message.edit(
            text=caption, disable_web_page_preview=True, parse_mode=ParseMode.HTML
        )
