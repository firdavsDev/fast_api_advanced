from typing import List

from fastapi import HTTPException, status

from ecommerce.cart.models import Cart, CartItems
from ecommerce.orders.models import Order, OrderDetails
from ecommerce.user.models import User
from . import mail


async def initiate_order(database) -> Order:
    user_info = database.query(User).filter(
        User.email == "user2@example.com").first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    cart_items_objects = database.query(CartItems).filter(Cart.id == cart.id)
    if not cart_items_objects.count():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No Items found in Cart !")

    total_amount: float = 0.0
    for item in cart_items_objects:
        total_amount += item.products.price

    new_order = Order(order_amount=total_amount,
                      shipping_address="587 Hinkle Deegan Lake Road, Syracuse, New York",
                      customer_id=user_info.id)  # <-- I forgot to add this line, which has been rectified later.
    database.add(new_order)
    database.commit()
    database.refresh(new_order)

    bulk_order_details_objects = []
    for item in cart_items_objects:
        new_order_details = OrderDetails(order_id=new_order.id,
                                         product_id=item.products.id)
        bulk_order_details_objects.append(new_order_details)

    database.bulk_save_objects(bulk_order_details_objects)
    database.commit()

    # Send Email
    mail.order_notification(user_info.email)

    # clear items in cart once new order is placed
    database.query(CartItems).filter(CartItems.cart_id == cart.id).delete()
    database.commit()

    return new_order


async def get_order_listing(database) -> List[Order]:
    user_info = database.query(User).filter(
        User.email == "user2@example.com").first()
    return database.query(Order).filter(Order.customer_id == user_info.id).all()
