from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_

from ecommerce import db
from ecommerce.products.models import Product

from .models import Cart, CartItems


async def add_items(cart_id, product_id, databse: Session = Depends(db.get_db)):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    databse.add(cart_items)
    databse.commit()
    databse.refresh(cart_items)
    return cart_items


async def add_to_cart(product_id: int, database: Session):
    product_info = database.query(Product).get(product_id)
    if not product_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with id {product_id} not found")
    if product_info.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Product with id {product_id} is out of stock")

    if cart_info := database.query(Cart).filter(Cart.user_id == 3).first():
        await add_items(cart_info.id, product_info.id, database)
    else:
        new_cart = Cart(user_id=3)  # Manually set user_id to 1
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_items(new_cart.id, product_info.id, database)
    return {"message": "Product added to cart successfully"}


async def remove_cart_item(cart_item_id: int, database) -> None:
    cart_id = database.query(Cart).filter(Cart.user_id == 3).first()
    database.query(CartItems).filter(
        and_(CartItems.id == cart_item_id, CartItems.cart_id == cart_id.id)).delete()
    database.commit()
    return
