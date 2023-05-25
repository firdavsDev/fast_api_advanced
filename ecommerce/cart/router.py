from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ecommerce import db

from .models import Cart
from .schemas import ShowCart
from .services import add_to_cart

router = APIRouter(
    prefix='/cart',
    tags=['Cart']
)


@router.get('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int,
                              database: Session = Depends(db.get_db)):
    return await add_to_cart(product_id, database)


@router.get('/', status_code=status.HTTP_200_OK, response_model=ShowCart)
async def get_all_cart_items(database: Session = Depends(db.get_db)):
    return database.query(Cart).filter(
        Cart.user_id == 3).first()
