from typing import List

from fastapi import HTTPException, status

from .. import models


async def create_new_category(request, db):
    new_category = models.Category(name=request.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

async def get_all_categories(db)-> List[models.Category]:
    return db.query(models.Category).all()

async def get_category_by_id(category_id: int, db):
    if category_info := db.query(models.Category).get(category_id):
        return category_info
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

async def delete_category_by_id(category_id: int, db):
    if category_info := db.query(models.Category).get(category_id):
        db.delete(category_info)
        db.commit()
        return "Category deleted successfully"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
