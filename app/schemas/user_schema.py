from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserPasswordUpdate(BaseModel):
    new_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True