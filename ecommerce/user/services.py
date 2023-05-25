from typing import List

from fastapi import HTTPException, status

from . import models


async def new_user_register(request, db) -> models.User:
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


async def all_users(db) -> List[models.User]:
    return db.query(models.User).all()


async def get_user_by_id(user_id: int, db) -> models.User:
    if user_info := db.query(models.User).get(user_id):
        return user_info
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


async def delete_user_by_id(user_id, database):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()


async def delete_user_by_id(user_id, database):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
