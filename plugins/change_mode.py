from pyrogram import Client, filters
from helpers.database import db
from asyncio import sleep

@Client.on_message(filters.channel & filters.regex(r"^(set)") & ~filters.forwarded, group=-4)
async def change_mode(c,m):
    me = await c.get_chat_member(m.chat.id, "me")
    if m.chat.username:
        if me.can_edit_messages:
            mode_text = m.text[4:].strip().lower()
            if mode_text == 'normal':
                mode = 'normal'
            if mode_text == 'bold':
                mode = 'bold'
            if mode_text == 'italic':
                mode = 'italic'
            if mode_text == 'underline':
                mode = 'underline'
            if mode_text == 'strike':
                mode = 'strike'
            if mode_text == 'spoiler':
                mode = 'spoiler'
            # if mode:
            #     print(mode)
            else:
                await m.edit('Incorrect mode!')
                return
            try:
                await db.change_mode(m.chat.id, mode)
                await m.edit(f"Mode Changed To -> {mode}")
            except Exception as e:
                print(e)
            await sleep(5)
            try:
                await m.delete()
            except:
                pass
    else:
        if me.can_edit_messages:
            await m.edit("Your channel is private so you can't use this bot!")