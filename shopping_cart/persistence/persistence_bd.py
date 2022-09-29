from motor.motor_asyncio import AsyncIOMotorClient

from shopping_cart.config import load_settings


def connect_client_mongo() -> AsyncIOMotorClient:
    setting = load_settings()
    client_mongo = AsyncIOMotorClient(setting.database_uri)
    return client_mongo

def access_database(client_mongo: AsyncIOMotorClient):
    return client_mongo.get_default_database()

def access_colletion(client_mongo: AsyncIOMotorClient, name_collection: str):
    bd = access_database(client_mongo)
    return bd[name_collection]