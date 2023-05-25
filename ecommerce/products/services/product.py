from .. import models
from asyncio.log import logger


async def create_new_product(request, database) -> models.Product:
    new_product = models.Product(name=request.name, quantity=request.quantity,
                                 description=request.description, price=request.price,
                                 category_id=request.category_id)
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


async def get_all_products(database):
    return database.query(models.Product).all()


async def update_product_by_id(product_id: int, request, database) -> models.Product:
    try:
        product = database.query(models.Product).filter(
            models.Product.id == product_id).first()
        product.name = request.name
        product.quantity = request.quantity
        product.description = request.description
        product.price = request.price
        product.category_id = request.category_id
        database.commit()
        database.refresh(product)
        return product
    except Exception as e:
        logger.error(e)
        return None


async def delete_product_by_id(product_id: int, database) -> models.Product:
    try:
        product = database.query(models.Product).filter(
            models.Product.id == product_id).first()
        database.delete(product)
        database.commit()
        return product
    except Exception as e:
        logger.error(e)
        return None
