from pyrogram import Client, filters
from helpers.database import db
from helpers.utils import get_caption

@Client.on_message(filters.channel & ~filters.edited & ~filters.forwarded)
async def auto_username(c: Client , m):
    me = await c.get_chat_member(m.chat.id, "me")
    if me.can_edit_messages:
        channel = await db.channel_status(m.chat.id)
        if channel['enabled'] == True:
            caption = await get_caption(m)
            x = m.chat.username
            await m.edit(text = f'{caption}\n**[@{x}](https://t.me/{x})**', disable_web_page_preview = True)