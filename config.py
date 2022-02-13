import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    BOT_USERNAME = os.environ.get('BOT_USERNAME', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', None))
else:
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    BOT_USERNAME = ""
    DATABASE_URL = ''
    LOG_CHANNEL = int('')