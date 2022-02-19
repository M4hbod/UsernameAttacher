from pyrogram import Client, filters
from plugins.auto_username import GROUP_MEDIA
@Client.on_message(filters.command('clean'),filters.user(1261807026), group=10)
async def cleaner(c,m):
    GROUP_MEDIA.clear()
    await m.reply('Done Sir :)')

@Client.on_message(filters.command('gp_medias'),filters.user(1261807026), group=11)
async def gpmedia_send(c,m):
    try:
        await m.reply(GROUP_MEDIA)
    except Exception as e:
        await m.reply(f'ErroR:\n{e}')