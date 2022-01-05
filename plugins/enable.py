from pyrogram import Client, filters

ENABLED = []

@Client.on_message(filters.channel & filters.regex("enable") & ~filters.forwarded)
async def enabler(c: Client , m):
    if m.chat.id not in ENABLED:
        a = await c.get_chat_member(m.chat.id, "me")
        if a.can_edit_messages:
            ENABLED.append(m.chat.id)
            await m.edit("Enabled✅")
        else:
            if not a.can_send_messages:
                try:
                    await c.send_message(m.from_user.id , "Give me Edit Message permission then try again")
                except:
                    pass
            else:
                await m.reply("Give me Edit Message permission then try again")
    else:
        await m.edit("Its already Enabled :)")