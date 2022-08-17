from pyrogram import Client, idle
from pyrogram.errors import (AccessTokenInvalid, ApiIdInvalid,
                             ApiIdPublishedFlood)

from config import API_HASH, API_ID, BOT_TOKEN

app=Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
)

# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    
    uname=app.get_me().username
    print(f"@{uname} Started Successfully!")
    
    idle()
    app.stop()
    
    print("Bot stopped!")
