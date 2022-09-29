from fastapi.encoders import jsonable_encoder
from bson import json_util
import json

from shopping_cart.persistence import products
from shopping_cart.schemas.products import ProductSchema
from shopping_cart.schemas import response


async def insert_product(product: ProductSchema):
    exists = await get_product_by_code(product.code)
    if exists:
        return response.response_message("detail", "Já existe produto cadastrado com este código")

    result = await products.insert_product(jsonable_encoder(product))
    return response.response_message("product", json.loads(json_util.dumps(result)))

async def delete_product_by_code(code: str):
    product = await get_product_by_code(code)
    if not(product):
        return response.response_message("detail", "Não foi encontrado produto cadastrado com este código")

    result = await products.delete_product_by_code(product["code"])
    return response.response_message("success", "Produto excluído com sucesso")

async def get_product_by_id(product_id):
    result = await products.get_product_by_id(product_id)
    if result:
        return response.response_message("product", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado produto cadastrado com este id")

async def get_product_by_code(code):
    result = await products.get_product_by_code(code)
    return result

async def get_product_by_name(product_name):
    result = await products.get_product_by_name(product_name)
    if result:
        return response.response_message("product", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado produto cadastrado com este nome")

async def get_products():
    result = await products.get_products()
    if result:
        return response.response_message("products", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi possível exibir os produtos")