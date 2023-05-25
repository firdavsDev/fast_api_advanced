from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from ecommerce import db

from . import schemas, services, validators

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

async def create_category(request: schemas.Category, db: Session = Depends(db.get_db)):
    return services.create_new_category(request, db)
