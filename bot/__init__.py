import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "19886681"))
    API_HASH = os.environ.get("API_HASH", "600e799cf14a251134cd0c6ea8e08f27")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5142098805:AAFBUvAmCaAmMfzV7nS9zNSGxmmQmJPnLRA")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Droplinkurl_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
