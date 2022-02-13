from helpers.database import db
from config import LOG_CHANNEL

async def handle_user_status(bot, cmd):
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        if "-100" in str(chat_id):
            await bot.send_message(
                chat_id=LOG_CHANNEL,
                text = f"**📣 Bot Notification.** \n\n#Channel **Start use your bot!** \n\n🧝🏻‍♂️ Name: {cmd.chat.title} \n📮 Chat id: `{cmd.chat.id}` \n",
            )
        else:
            await bot.send_message(
                LOG_CHANNEL,
                f"**📣 Bot Notification.** \n\n#User **started using your bot!** \n\n🏷 name: `{cmd.from_user.first_name}` \n📮 user id: `{cmd.from_user.id}` \n🧝🏻‍♂️ profile: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})",
            )   
    await cmd.continue_propagation()

async def get_caption(message):
    caption = ''
    if message.caption:
        caption = message.caption
    if message.text:
        caption = message.text
    return caption
        