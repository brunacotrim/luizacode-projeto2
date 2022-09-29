from bson import ObjectId


from shopping_cart.persistence.persistence_bd import (
    connect_client_mongo,
    access_colletion
)


users_collection = access_colletion(
    connect_client_mongo(),
    "users"
)

async def insert_user(user):
    try:
        result = await users_collection.insert_one(user)
        if result:
            data_user = await get_user_by_id(result.inserted_id)
            return data_user

    except Exception as error:
        print(f"insert_user.error: {error}")

async def delete_user_by_id(user_id):
    try:
        result = await users_collection.delete_one({'_id': ObjectId(user_id)})
        return

    except Exception as error:
        print(f"delete_user_by_id.error: {error}")

async def get_user_by_id(user_id):
    try:
        result = await users_collection.find_one({"_id": ObjectId(user_id)})
        return result

    except Exception as error:
        print(f"get_user_by_id.error: {error}")

async def get_user_by_email(user_email):
    try:
        result = await users_collection.find_one({"email": user_email})
        return result

    except Exception as error:
        print(f"get_user_by_email.error: {error}")

async def get_user_by_name(user_name):
    try:
        list_users = []
        cursor = users_collection.find({"name": {"$regex": user_name, "$options": "i"}})
        
        async for user in cursor:
            list_users.append(user)
        return list_users

    except Exception as error:
        print(f"get_user_by_name.error: {error}")

async def get_user_by_domain(domain):
    try:
        list_emails = []
        domain_filter = f"@{domain}\."
        cursor = users_collection.find({"email": {'$regex': domain_filter, "$options": "i"}})

        async for user in cursor:
                list_emails.append(user["email"])
        return list_emails

    except Exception as error:
        print(f"get_user_by_domain.error: {error}")
