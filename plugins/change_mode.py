from pyrogram import Client, filters
from helpers.database import db
from asyncio import sleep

@Client.on_message(filters.channel & filters.regex(r"^(set)") & ~filters.forwarded, group=7)
async def change_mode(c,m):
    me = await c.get_chat_member(m.chat.id, "me")
    if m.chat.username:
        if me.can_edit_messages:
            if m.text[4:].strip().lower() == 'normal':
                mode = 'normal'
            if m.text[4:].strip().lower() == 'bold':
                mode = 'bold'
            if m.text[4:].strip().lower() == 'italic':
                mode = 'italic'
            if m.text[4:].strip().lower() == 'underline':
                mode = 'underline'
            if m.text[4:].strip().lower() == 'strike':
                mode = 'strike'
            if m.text[4:].strip().lower() == 'spoiler':
                mode = 'spoiler'
            else:
                await m.edit('Incorrect mode!')
            try:
                await db.change_mode(m.chat.id, mode)
                await m.edit(f"Mode Changed To -> {mode.upper}")
            except Exception as e:
                print(e)
            sleep(5)
            try:
                await m.delete()
            except:
                pass
    else:
        if me.can_edit_messages:
            await m.edit("Your channel is private so you can't use this bot!")