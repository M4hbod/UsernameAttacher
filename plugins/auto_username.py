from pyrogram.types import Message
from pyrogram import Client, filters

from helpers.database import db
from helpers.functions import get_caption

GROUP_MEDIA=[]

@Client.on_message(filters.channel & ~filters.forwarded, group=1)
async def auto_username(client: Client, message: Message):
    if message.chat.username:
        me=await client.get_chat_member(message.chat.id, "me")
        if me.can_edit_messages:
            channel=await db.get_channel_info(message.chat.id)
            if channel['enabled'] == True:
                x=message.chat.username
                mode=channel['mode']
                if mode == 'normal':
                    sign=f'\n@{x}'

                if mode == 'bold':
                    sign=f'\n<b>@{x}</b>'

                if mode == 'italic':
                    sign=f'\n<i>@{x}</i>'

                if mode == 'underline':
                    sign=f'\n<u>@{x}</u>'

                if mode == 'strike':
                    sign=f'\n<s>@{x}</s>'

                caption=await get_caption(message)
                caption += sign
                if message.media_group_id:
                    if message.media_group_id in GROUP_MEDIA:
                        return
                    else:
                        GROUP_MEDIA.append(message.media_group_id)
                await message.edit(text=caption, disable_web_page_preview=True, parse_mode="html")
