import datetime
from typing import List, Optional

from pydantic import BaseModel

from ecommerce.products.schemas.product import ProductListing


class ShowOrderDetails(BaseModel):
    id: int
    order_id: int
    product_order_details: ProductListing
    # product_order_details = relationship("Product", back_populates="order_details") in models.py

    class Config:
        orm_mode = True


class ShowOrder(BaseModel):
    id: Optional[int]
    order_date: datetime.datetime
    order_amount: float
    order_status: str
    shipping_address: str
    order_details: List[ShowOrderDetails] = []

    class Config:
        orm_mode = True
