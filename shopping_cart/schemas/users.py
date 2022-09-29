from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    nike_name: Optional[str]

class AddressSchema(BaseModel):
    street: str
    cep: str
    city: str
    state: str
