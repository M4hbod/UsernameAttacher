from pyrogram.client import Client
from helpers.utils import handle_user_status

@Client.on_message(group=-1)
async def _(bot: Client, cmd):
    await handle_user_status(bot, cmd)