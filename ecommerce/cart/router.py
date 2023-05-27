from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.auth.jwt import get_current_user
from ecommerce.user.models import User

from .models import Cart
from .schemas import ShowCart
from .services import add_to_cart, remove_cart_item

router = APIRouter(
    prefix='/cart',
    tags=['Cart']
)


@router.get('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int,
                              database: Session = Depends(db.get_db),
                              current_user: User = Depends(get_current_user)):
    return await add_to_cart(product_id, database, current_user)


@router.delete('/{cart_item_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_cart_item_by_id(cart_item_id: int,
                                 database: Session = Depends(db.get_db),
                                 current_user: User = Depends(get_current_user)):
    await remove_cart_item(cart_item_id, database, current_user)


@router.get('/', status_code=status.HTTP_200_OK, response_model=ShowCart)
async def get_all_cart_items(database: Session = Depends(db.get_db), current_user: User = Depends(get_current_user)):
    user_info = database.query(User).filter(
        User.email == current_user.email).first()
    return database.query(Cart).filter(
        Cart.user_id == user_info.id).first()
