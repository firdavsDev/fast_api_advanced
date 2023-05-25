from typing import Optional

from pydantic import BaseModel, constr


class Category(BaseModel):
    name: constr(min_length=3, max_length=50)


class ListCategory(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # this will allow us to return the data from the database as a dictionary


class ProductBase(BaseModel):
    id: Optional[int]
    name: str
    quantity: int
    description: str
    price: float

    class Config:
        orm_mode = True


class Product(ProductBase):
    category_id: int
