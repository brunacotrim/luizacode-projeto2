from fastapi import APIRouter
from bson import json_util
import json

from shopping_cart.schemas.products import ProductSchema
import shopping_cart.controller.products as products_controller
from shopping_cart.schemas import response


router_products = APIRouter(
    prefix="/product"
)

@router_products.post("/")
async def insert_product(product: ProductSchema):
    result = await products_controller.insert_product(product)
    return result

@router_products.delete("/")
async def delete_product_by_code(code: str):
    result = await products_controller.delete_product_by_code(code)
    return result

@router_products.get("/")
async def get_product_by_id(id: str):
    result = await products_controller.get_product_by_id(id)
    return result

@router_products.get("/code")
async def get_product_by_code(code: str):
    result = await products_controller.get_product_by_code(code)
    if result:
        return response.response_message("product", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado produto cadastrado com este código")

@router_products.get("/name")
async def get_product_by_name(name: str):
    result = await products_controller.get_product_by_name(name)
    return result

@router_products.get("/all")
async def get_products():
    result = await products_controller.get_products()
    return result