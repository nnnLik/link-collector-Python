from pymongo import MongoClient


class MongoManager:
    db: MongoClient
    users: str
    links: str

    def setup_connection(self, url: str, database_name: str):
        mongo_client = MongoClient(url)

        self.db = mongo_client[database_name]
        self.users = self.db["users"]
        self.links = self.db["link"]


mongodb = MongoManager()
