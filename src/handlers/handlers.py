import logging
import re
from src.configs.mongodb import mongodb
from src.configs.const import (
    ALREADY_REGISTERED_MESSAGE,
    WELCOME_MESSAGE,
    RESET_LINKS_SUCCESS_MESSAGE,
    HELP_MESSAGE,
    LINKS_FOUND_SUCCESS_MESSAGE,
    LINKS_NOT_FOUND_MESSAGE,
)

logger = logging.getLogger(__name__)


def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        user_id = message.from_user.id

        existing_user = mongodb.users.find_one({"user_id": user_id})
        if existing_user:
            logger.info(f"User with id {user_id} already exists.")
            bot.send_chat_action(message.chat.id, ALREADY_REGISTERED_MESSAGE)
        else:
            mongodb.users.insert_one({"user_id": user_id})
            logger.info(f"User with id {user_id} created.")
            bot.send_chat_action(message.chat.id, WELCOME_MESSAGE)

    @bot.message_handler(commands=["resetlinks"])
    def reset_links(message):
        user_id = message.from_user.id
        mongodb.links.delete_many({"user_id": user_id})
        logger.warning(f"User {user_id} deleted all his links.")
        bot.reply_to(message, RESET_LINKS_SUCCESS_MESSAGE)

    @bot.message_handler(commands=["help"])
    def help(message):
        bot.send_chat_action(message.chat.id, HELP_MESSAGE)

    @bot.message_handler(func=lambda message: True)
    def process_message(message):
        user_id = message.from_user.id
        text = message.text

        logger.info(f"Got message from user {user_id}.")

        links = re.findall(r"(?P<url>https?://[^\s]+)", text)
        if links:
            for link in links:
                is_exist = mongodb.links.find_one({"user_id": user_id, "link": link})
                if is_exist:
                    continue
                else:
                    mongodb.links.insert_one({"user_id": user_id, "link": link})

            logger.info(f"Links were found and saved in the database.")
            bot.reply_to(message, LINKS_FOUND_SUCCESS_MESSAGE)
        else:
            logger.info(f"Links were not found.")
            bot.reply_to(message, LINKS_NOT_FOUND_MESSAGE)
