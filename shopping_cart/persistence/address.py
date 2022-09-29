from shopping_cart.persistence.persistence_bd import (
    connect_client_mongo,
    access_colletion
)

from bson import ObjectId


address_collection = access_colletion(
    connect_client_mongo(),
    "address"
)

async def insert_address_user(address, data_user):
    try:
        result = await address_collection.insert_one(
                    {"user": data_user,
                    "address": [address]}
                )
        if result:
            data_address = await get_address_by_id(result.inserted_id)
            return data_address

    except Exception as error:
        print(f"insert_address_user.error: {error}")

async def add_address_user(id_address_data, address, address_id):
    try:
        result = await address_collection.update_one(
            {"_id": id_address_data},
            {"$addToSet": {"address": address}}
        )
        data_address = None
        if result.modified_count == 1:
            data_address = await get_address_by_id(address_id)
        return data_address

    except Exception as error:
        print(f"add_address_user.error: {error}")

async def get_address_by_user(user_email):
    try:
        result = await address_collection.find_one({"user.email": user_email})
        return result

    except Exception as error:
        print(f"get_address_by_user.error: {error}")
    
async def get_address_by_id(address_id):
    try:
        result = await address_collection.find_one({"_id": ObjectId(address_id)})
        return result

    except Exception as error:
        print(f"get_address_by_id.error: {error}")