from pyrogram import Client, filters
from plugins.enable import ENABLED

@Client.on_message(filters.channel & ~filters.edited & ~filters.forwarded)
async def auto_username(client: Client , message):
    if message.chat.id in ENABLED:
        a = await client.get_chat_member(message.chat.id, "me")
        if a.can_edit_messages:
            y = ''
            if message.caption:
                y = message.caption
            if message.text:
                y = message.text
            x = message.chat.username
            await message.edit(text = f'{y}\n**[@{x}](https://t.me/{x})**', disable_web_page_preview= True)