from pyrogram import Client, filters
from helpers.database import db
from asyncio import sleep

@Client.on_message(filters.channel & filters.text & filters.regex(r"^(enable)$") & ~filters.forwarded, group=-3)
async def enabler(c , m):
    me = await c.get_chat_member(m.chat.id, "me")
    if m.chat.username:
        if me.can_edit_messages:
            channel = await db.channel_status(m.chat.id)
            if channel['enabled'] == True:
                await m.edit("It's already turned ON ✅")
            else:
                await db.set_enabled(m.chat.id)
                await m.edit("Enabled ✅")
            await sleep(5)
            try:
                await m.delete()
            except:
                pass
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
    else:
        if me.can_edit_messages:
            await m.edit("Your channel is private so you can't use this bot!")