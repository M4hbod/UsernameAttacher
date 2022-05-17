from pyrogram import filters, Client
from pyrogram.types import Message

from config import BOT_USERNAME

@Client.on_message(filters.private & ~filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}", "modes" , f"modes@{BOT_USERNAME}"]), group=11)
async def unknown_message_private(client: Client, message: Message):
    await message.reply("Use /start or /help man :)")


@Client.on_message(filters.private & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=5)
async def start_private(client: Client, message: Message):
    await message.reply(f"""Hi {message.from_user.mention},
    Add me to your channel and give me Edit Message permission then send **enable** command in your channel:)
    If you wanna turn it of type `disable` in your channel ;)
    There is a few modes that you can use, send /modes to see them.""")


@Client.on_message(filters.group & filters.command(["start" , f"start@{BOT_USERNAME}" , "help" , f"help@{BOT_USERNAME}"]), group=10)
async def start_groups(client: Client, message: Message):
    await message.reply("Message me in private bro :)")


@Client.on_message(filters.private & filters.command(["modes" , f"modes@{BOT_USERNAME}"]), group=8)
async def start_groups(client: Client, message: Message):
    await message.reply(f"""So There is 6 modes available, you can send <code>set (mode name)</code> in your channel to choose a specific mode.

    E.x: set bold
    These are the modes:
    <code>normal</code> - @Telegram
    <code>bold</code> - <b>@Telegram</b>
    <code>italic</code> - <i>@Telegram</i>
    <code>underline</code> - <u>@Telegram</u>
    <code>strike</code> - <s>@Telegram</s>
    <b>⚠️NOTE: DON'T FORGET TO ENABLE THE BOT IN YOUR CHANNEL</b>
    
    Made with ❤️ by <a href='https://t.me/M4hbod'>Mahbod</a>""",
    parse_mode="html",
    disable_web_page_preview=True)
