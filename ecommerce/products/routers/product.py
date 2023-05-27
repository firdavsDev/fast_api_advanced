
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ecommerce import db

from .. import validators
from ..router import router
from ..schemas import product as schemas
from ..services import product as services


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_product(request: schemas.Product, database: Session = Depends(db.get_db)):
    category = await validators.verify_category_exist(request.category_id, database)
    if not category:
        raise HTTPException(
            status_code=400,
            detail="You have provided invalid category id.",
        )

    return await services.create_new_product(request, database)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ProductListing])
async def get_all_products(database: Session = Depends(db.get_db)):
    return await services.get_all_products(database)


@router.get('/{product_id}', status_code=status.HTTP_200_OK, response_model=schemas.ProductListing)
async def get_product_by_id(product_id: int, database: Session = Depends(db.get_db)):
    product = await validators.verify_product_exist(product_id, database)
    if not product:
        raise HTTPException(
            status_code=400,
            detail="You have provided invalid product id.",
        )
    return product


@router.put('/{product_id}', status_code=status.HTTP_200_OK, response_model=schemas.ProductListing)
async def update_product_by_id(product_id: int, request: schemas.Product, database: Session = Depends(db.get_db)):
    product = await validators.verify_product_exist(product_id, database)
    if not product:
        raise HTTPException(
            status_code=400,
            detail="You have provided invalid product id.",
        )
    return await services.update_product_by_id(product_id, request, database)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_by_id(product_id: int, database: Session = Depends(db.get_db)):
    product = await validators.verify_product_exist(product_id, database)
    if not product:
        raise HTTPException(
            status_code=400,
            detail="You have provided invalid product id.",
        )
    return await services.delete_product_by_id(product_id, database)
