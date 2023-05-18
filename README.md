# LinkCollector Bot

LinkCollector Bot is a Telegram bot that helps you save random useful links with information and regularly sends them to users throughout the day.

## How it Works

1. Add the bot to your Telegram contacts: [@LinkCollector](https://t.me/tg_linkerbot).
2. Register and obtain your user ID.
3. Use the bot's commands to manage links and receive useful information.

## Key Features

- Automatic Link Collection: Simply send any message containing links or a large text with multiple links to the bot. It will automatically identify and save the links for you.
- Regular Link Delivery: The bot periodically sends a curated set of random links to provide you with inspiration and knowledge.
- Link Personalization: Each user's links are stored separately, ensuring personalized link recommendations based on individual interests.

## Technologies Used

- **Telegram Bot API**: The bot is built using the Telegram Bot API, which provides a convenient interface for interacting with the Telegram platform.
- **Python**: The bot is implemented in Python, a versatile and powerful programming language.
- **MongoDB**: The bot utilizes MongoDB, a popular NoSQL database, to store and retrieve user data and links. MongoDB provides scalability and flexibility for handling large amounts of data.

## Getting Started

To run the bot locally, follow these steps:

1. Install the dependencies by running `pip install -r requirements.txt`.
2. Specify your Telegram API token and MongoDB connection details in the `config.py` file.
3. Start the bot by running `python main.py -token <telegram_token> -mongo <mongo_url> -db <mongo_db>`.

## TODO
- [ ] docker
- [ ] task scheduller
- [ ] async

## Contribution

Contributions to the LinkCollector Bot are welcome! If you have any ideas, bug reports, or feature requests, please submit them through the issue tracker or submit a pull request.
