from pyrogram import filters, Client
from config import BOT_USERNAME

@Client.on_message(filters.private & ~filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=11)
async def unknown_message_private(c , m):
    await m.reply("Use /start or /help man :)")
    
@Client.on_message(filters.private & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=5)
async def start_private(c , m):
    await m.reply(f"Hi {m.from_user.mention},\nAdd me to your channel and give me Edit Message permission then type `enable` in your channel:)\nIf you wanna turn it of type `disable` in your channel ;)\nThere is a few modes that you can use, send /modes to see them.")

@Client.on_message(filters.group & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=10)
async def start_groups(c , m):
    await m.reply(f"Message me in private bro :)")

@Client.on_message(filters.private & filters.command(["modes" , f"modes@{BOT_USERNAME}"]), group=8)
async def start_groups(c , m):
    await m.reply(f"So There is 6 modes available, you can send <code>set (mode name)</code> in your channel to choose a specific mode.\nE.x: set bold\nThese are the modes:\n<code>normal</code> - @Telegram\n<code>bold</code> - <b>@Telegram</b>\n<code>italic</code> - <i>@Telegram</i>\n<code>underline</code> - <u>@Telegram</u>\n<code>strike</code> - <s>@Telegram</s>\nMade with ❤️ by <a href='https://t.me/M4hbod'>Mahbod</a>", parse_mode = "html", disable_web_page_preview=True)
