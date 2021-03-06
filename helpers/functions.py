from pyrogram import Client
from pyrogram.types import Message

from helpers.database import db
from config import LOG_CHANNEL

async def handle_user_status(bot: Client, message: Message):
    if message.chat.type == 'private':
        if not await db.is_user_exist(message.chat.id):
            await db.add_user(message.chat.id)
            await bot.send_message(
                chat_id=LOG_CHANNEL,
                text=f'**š£ Bot Notification.**\n\nš New #USER\nš§š»āāļø Name: {message.from_user.first_name}\nš® Chat ID: `{message.chat.id}\nš§š»āāļø Profile: {message.from_user.mention}'
            )
    elif message.chat.type == 'channel':
        if not await db.is_channel_exist(message.chat.id):
            await db.add_channel(message.chat.id, 'normal')
            await bot.send_message(
                chat_id=LOG_CHANNEL,
                text=f'**š£ Bot Notification.**\n\nš New #CHANNEL\nš§š»āāļø Name: {message.from_user.first_name}\nš® Chat ID: `{message.chat.id}'
            )
    else:
        pass
    await message.continue_propagation()

async def get_caption(message: Message):
    caption=''
    if hasattr(message, 'caption'):
        caption=message.caption
    elif hasattr(message, 'text'):
        caption=message.text
    return caption
