from pydantic import BaseModel, constr

class Category(BaseModel):
    name: constr(min_length=3, max_length=50)

class Product(BaseModel):
    name: constr(min_length=3, max_length=50)
    description: constr(min_length=3, max_length=50)
    price: float
    category: Category