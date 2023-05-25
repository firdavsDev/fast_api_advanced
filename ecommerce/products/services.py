from . import models


async def create_new_category(request, db):
    new_category = models.Category(name=request.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
