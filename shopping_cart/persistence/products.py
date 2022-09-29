from bson import ObjectId

from shopping_cart.persistence.persistence_bd import (
    connect_client_mongo,
    access_colletion
)


products_collection = access_colletion(
    connect_client_mongo(),
    "products"
)

async def insert_product(product):
    try:
        result = await products_collection.insert_one(product)
        if result:
            data_product = await get_product_by_id(result.inserted_id)
            return data_product

    except Exception as error:
        print(f"insert_product.error: {error}")

async def delete_product_by_code(code):
    try:
        result = await products_collection.delete_one({'code': code})
        return

    except Exception as error:
        print(f"delete_product_by_code.error: {error}")

async def get_product_by_id(product_id):
    try:
        result = await products_collection.find_one({"_id": ObjectId(product_id)})
        return result

    except Exception as error:
        print(f"get_product_by_id.error: {error}")

async def get_product_by_code(code):
    try:
        result = await products_collection.find_one({"code": code})
        return result

    except Exception as error:
        print(f"get_product_by_code.error: {error}")

async def get_product_by_name(product_name):
    try:
        list_products = []
        cursor = products_collection.find({"name": {"$regex": product_name, "$options": "i"}})
        
        async for product in cursor:
            list_products.append(product)
        return list_products

    except Exception as error:
        print(f"get_product_by_name.error: {error}")

async def get_products():
    try:
        list_products = []
        cursor = products_collection.find()
        
        async for product in cursor:
            list_products.append(product)
        return list_products

    except Exception as error:
        print(f"get_products.error: {error}")