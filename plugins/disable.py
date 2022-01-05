from pyrogram import Client, filters
from plugins.enable import ENABLED

@Client.on_message(filters.channel & filters.regex("disable") & ~filters.forwarded)
async def disabler(c: Client , m):
    if m.chat.id in ENABLED:
        a = await c.get_chat_member(m.chat.id, "me")
        if a.can_edit_messages:
            await m.edit("Disabled❌")
            ENABLED.remove(m.chat.id)
        else:
            if not a.can_send_messages:
                try:
                    await c.send_message(m.from_user.id , "Give me Edit Message permission then try again")
                except:
                    pass
            else:
                await m.reply("Give me Edit Message permission then try again")
    else:
        await m.edit("Its already Disabled :)")