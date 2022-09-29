from fastapi import APIRouter
from bson import json_util
import json

from shopping_cart.schemas.users import UserSchema, AddressSchema
import shopping_cart.controller.users as users_controller
from shopping_cart.schemas import response


router_users = APIRouter(
    prefix="/user"
)

@router_users.post("/")
async def insert_user(user: UserSchema):
    result = await users_controller.insert_user(user)
    return result

@router_users.delete("/")
async def delete_user(email: str):
    result = await users_controller.delete_user(email)
    return result

@router_users.get("/")
async def get_user_by_id(id: str):
    result = await users_controller.get_user_by_id(id)
    return result

@router_users.get("/email")
async def get_user_by_email(email: str):
    result = await users_controller.get_user_by_email(email)
    if result:
        return response.response_message("user",  json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado usuário cadastrado com este e-mail")

@router_users.get("/name")
async def get_user_by_name(name: str):
    result = await users_controller.get_user_by_name(name)
    return result

@router_users.get("/list_emails")
async def get_user_by_domain(domain: str):
    result = await users_controller.get_user_by_domain(domain)
    return result

@router_users.post("/{email_user}/address/")
async def insert_address_user(email_user: str, address: AddressSchema):
    result = await users_controller.insert_address_user(email_user, address)
    return result

@router_users.get("/{email_user}/address/")
async def get_address_by_user(email_user: str):
    result = await users_controller.get_address_by_user(email_user)
    if result:
        return response.response_message("address",  json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado endereço cadastrado para o usuário")