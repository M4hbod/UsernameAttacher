from pyrogram.types import Message


async def get_caption(message: Message) -> str:
    caption = ""
    if message.caption:
        caption = message.caption
    elif message.text:
        caption = message.text

    return caption
