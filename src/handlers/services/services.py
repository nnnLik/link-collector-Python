import time
import random
from src.configs.mongodb import mongodb


def send_link_to_user(bot, user_id):
    user_links = mongodb.links.find({"user_id": user_id})

    try:
        random_link = random.choice(list(user_links))
    except IndexError:
        return

    link = random_link["link"]
    bot.send_message(user_id, link)


def send_links_periodically(bot):
    while True:
        user_ids = mongodb.users.distinct("user_id")
        for user_id in user_ids:
            send_link_to_user(bot, user_id)
        time.sleep(10)

