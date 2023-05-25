from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.auth.jwt import get_current_user
from . import schema, services, validator

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user_register(request: schema.User, db: Session = Depends(db.get_db)):
    user = await validator.verify_email_exists(request.email, db)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    return await services.new_user_register(request, db)


@router.get('/list', response_model=List[schema.DisplayUser])
async def get_all_user(database: Session = Depends(db.get_db), current_user: schema.User = Depends(get_current_user)):
    return await services.all_users(database)


@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                         current_user: schema.User = Depends(get_current_user)):
    return await services.get_user_by_id(user_id, database)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                            current_user: schema.User = Depends(get_current_user)):
    return await services.delete_user_by_id(user_id, database)
