#We are going to write our pydantic models.  (Serializer)
from pydantic import BaseModel, constr, EmailStr

class User(BaseModel):
    name: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8, max_length=50)

class DisplayUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
