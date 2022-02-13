import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
    BOT_USERNAME = os.environ.get('BOT_USERNAME', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    LOG_CHANNEL = os.environ.get('DATABASE_URL', None)
else:
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    MUST_JOIN = "M4hbodBots"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
    BOT_USERNAME = ""
    DATABASE_URL = ''
    LOG_CHANNEL = ''