from fastapi.encoders import jsonable_encoder
from bson import json_util
import json

from shopping_cart.persistence import users
from shopping_cart.persistence import address as address_users
from shopping_cart.schemas.users import UserSchema, AddressSchema
from shopping_cart.schemas import response


async def insert_user(user: UserSchema):
    exists = await get_user_by_email(user.email)
    if exists:
        return response.response_message("detail", "Já existe usuário cadastrado com este e-mail")

    result = await users.insert_user(jsonable_encoder(user))
    return response.response_message("user", json.loads(json_util.dumps(result)))

async def delete_user(email: str):
    user = await get_user_by_email(email)
    if not(user):
        return response.response_message("detail", "Não foi encontrado usuário cadastrado com este e-mail")

    result = await users.delete_user_by_id(user["_id"])
    return response.response_message("success", "Usuário excluído com sucesso")

async def get_user_by_id(user_id):
    result = await users.get_user_by_id(user_id)
    if result:
        return response.response_message("user", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado usuário cadastrado com este id")

async def get_user_by_email(user_email):
    result = await users.get_user_by_email(user_email)
    return result

async def get_user_by_name(user_name):
    result = await users.get_user_by_name(user_name)
    if result:
        return response.response_message("user", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado usuário cadastrado com este nome")

async def get_user_by_domain(domain):
    result = await users.get_user_by_domain(domain)
    if result:
        return response.response_message("emails", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi encontrado usuário cadastrado com e-mail deste domínio")

async def insert_address_user(user_email, address: AddressSchema):

    data_address = await address_users.get_address_by_user(user_email)
    if data_address:
        result = await address_users.add_address_user(data_address["_id"], jsonable_encoder(address), data_address.get("_id"))
        if result:
            return response.response_message("address", json.loads(json_util.dumps(result)))
        return response.response_message("detail", "Não foi possível cadastrar o endereço para o usuário")

    data_user = await get_user_by_email(user_email)
    if not(data_user):
        return response.response_message("detail", "Não foi encontrado cadastro para este usuário")

    result = await address_users.insert_address_user(jsonable_encoder(address), data_user)
    if result:
            return response.response_message("address", json.loads(json_util.dumps(result)))
    return response.response_message("detail", "Não foi possível cadastrar o endereço para o usuário")

async def get_address_by_user(user_email):

    result = await address_users.get_address_by_user(user_email)
    return result