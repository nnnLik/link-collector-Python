import threading
import argparse
import logging
import telebot

from src.configs.mongodb import mongodb
from src.handlers.handlers import register_handlers
from src.handlers.services.services import send_links_periodically

logger = logging.getLogger(__name__)


def main():
    bot = telebot.TeleBot(API_TOKEN)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logger.info("Server started")

    register_handlers(bot)
    threading.Thread(target=send_links_periodically, args=(bot,)).start()

    bot.infinity_polling()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-token", help="Telegram API token")
    parser.add_argument("-mongo", help="MongoDB connection URI")
    parser.add_argument("-db", help="MongoDB database name")

    args = parser.parse_args()

    API_TOKEN = args.token
    MONGODB_URI = args.mongo
    DB_NAME = args.db

    mongodb.setup_connection(MONGODB_URI, DB_NAME)

    main()
