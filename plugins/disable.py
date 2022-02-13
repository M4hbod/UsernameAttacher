from pyrogram import Client, filters
from helpers.database import db

@Client.on_message(filters.channel & filters.regex("disable") & ~filters.forwarded, group=3)
async def disabler(c , m):
    me = await c.get_chat_member(m.chat.id, "me")
    if me.can_edit_messages:
        channel = await db.channel_status(m.chat.id)
        if channel['enabled'] == False:
            await m.edit("It's already turned off ✅")
        else:
            await db.set_disabled(m.chat.id)
            await m.edit("Disabled ❌")
    else:
        if not me.can_send_messages:
            try:
                await c.send_message(m.from_user.id , "Give me Edit Message permission then try again")
            except:
                pass
        else:
            try:
                await m.reply("Give me Edit Message permission then try again")
            except Exception as e:
                print(e)
                return