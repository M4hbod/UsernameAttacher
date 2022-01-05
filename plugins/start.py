from pyrogram import filters, Client
from Config import BOT_USERNAME

@Client.on_message(filters.private & ~filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]))
async def unknown_message_private(c , m):
    await m.reply("Use /start or /help man :)")
    
@Client.on_message(filters.private & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]))
async def start_private(c , m):
    await m.reply(f"Hi {m.from_user.mention},\nAdd me to your channel and give me Edit Message permission then type `enable` in your channel:)\nIf you wanna turn it of type `disable` in your channel ;)")

@Client.on_message(filters.group & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]))
async def start_groups(c , m):
    await m.reply(f"Message me in private bro :)")
