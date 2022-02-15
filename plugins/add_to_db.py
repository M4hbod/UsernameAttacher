from pyrogram import Client, filters
from helpers.utils import handle_user_status

@Client.on_message(filters.private | filters.channel ,group=-1)
async def _(bot: Client, cmd):
    await handle_user_status(bot, cmd)

@Client.on_message(filters.group, group= 9)
async def leave_groups(c: Client,m):
    await c.send_message(m.chat.id,"I'm not designed to work in groups.\nHave a good time :)")
    await c.leave_chat(m.chat.id)