from pyrogram import filters, Client
from config import BOT_USERNAME

@Client.on_message(filters.private & ~filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=4)
async def unknown_message_private(c , m):
    await m.reply("Use /start or /help man :)")
    
@Client.on_message(filters.private & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=5)
async def start_private(c , m):
    await m.reply(f"Hi {m.from_user.mention},\nAdd me to your channel and give me Edit Message permission then type `enable` in your channel:)\nIf you wanna turn it of type `disable` in your channel ;)\nThere is a few modes that you can use, send /modes to see them.")

@Client.on_message(filters.group & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=6)
async def start_groups(c , m):
    await m.reply(f"Message me in private bro :)")

@Client.on_message(filters.private & filters.command(["modes" , f"modes@{BOT_USERNAME}"]), group=8)
async def start_groups(c , m):
    await m.reply(f"So There is 6 modes available, you can send `set (mode name)` in your channel to choose a specific mode.\nE.x: set bold\nThese are the modes:\n`normal` - Just normal mode\n`bold` - **[@Telegram](https://t.me/Telegram)**\n`italic` - __[@Telegram](https://t.me/Telegram)__\n`underline` - --[@Telegram](https://t.me/Telegram)--\n`strike - ~~[@Telegram](https://t.me/Telegram)~~\n`spoiler` - ||@Telegram||\nMade with ❤️ by [Mahbod](https://t.me/M4hbod)")
