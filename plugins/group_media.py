from pyrogram import Client, filters
from pyrogram.types import Message

from plugins.auto_username import GROUP_MEDIA

@Client.on_message(filters.command('clean'),filters.user(1261807026), group=-9)
async def cleaner(client: Client, message: Message):
    GROUP_MEDIA.clear()
    await message.reply('Done Sir :)')


@Client.on_message(filters.command('gp_medias'),filters.user(1261807026), group=-8)
async def gpmedia_send(client: Client, message: Message):
    try:
        await message.reply(GROUP_MEDIA)
    except Exception as e:
        await message.reply(f'ErroR:\n{e}')