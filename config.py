import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_USERNAME = getenv("BOT_USERNAME")
DATABASE_URL = getenv("DATABASE_URL")
LOG_CHANNEL = int(getenv("CHARGE_LOG_CHANNEL"))
