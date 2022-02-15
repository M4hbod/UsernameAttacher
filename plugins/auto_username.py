from pyrogram.types import Message
from pyrogram import Client, filters
from helpers.database import db
from helpers.utils import get_caption

@Client.on_message(filters.channel & ~filters.edited & ~filters.forwarded, group=1)
async def auto_username(c: Client , m: Message):
    if m.chat.username:
        me = await c.get_chat_member(m.chat.id, "me")
        if me.can_edit_messages:
            channel = await db.channel_status(m.chat.id)
            if channel['enabled'] == True:
                x = m.chat.username
                mode = channel['mode']
                if mode == 'normal':
                    sign = f'\n@{x}'

                if mode == 'bold':
                    sign = f'\n<b>@{x}</b>'

                if mode == 'italic':
                    sign = f'\n<i>@{x}</i>'

                if mode == 'underline':
                    sign = f'\n<u>@{x}</u>'

                if mode == 'strike':
                    sign = f'\n<s>@{x}</s>'

                caption = await get_caption(m)
                caption += sign

                await m.edit(text = caption, disable_web_page_preview = True, parse_mode = "html")