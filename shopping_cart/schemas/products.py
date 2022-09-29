from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    image: str
    code: str