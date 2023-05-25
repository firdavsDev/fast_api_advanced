from typing import List

from fastapi import Depends, Response, status
from sqlalchemy.orm import Session

from ecommerce import db

from ..schemas import category as category_schema
from ..services import category as category_service
from ..router import router

# CATEGORY CRUD OPERATIONS


@router.post("/category", status_code=status.HTTP_201_CREATED)
async def create_category(request: category_schema.Category, db: Session = Depends(db.get_db)):
    return await category_service.create_new_category(request, db)


@router.get('/categorires', status_code=status.HTTP_200_OK, response_model=List[category_schema.ListCategory])
async def get_all_categories(db: Session = Depends(db.get_db)):
    return await category_service.get_all_categories(db)


@router.get('category/{category_id}', response_model=category_schema.ListCategory, status_code=status.HTTP_200_OK)
async def get_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await category_service.get_category_by_id(category_id, database)


@router.delete('category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await category_service.delete_category_by_id(category_id, database)
