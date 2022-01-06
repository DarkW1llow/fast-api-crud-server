from datetime import  date, datetime
from typing import List

from sqlalchemy import orm
from pydantic import BaseModel


class UserInfoBase(BaseModel):
    email: str
    password: str

class UserCreate(UserInfoBase):
    id: str
    fullname: str
    shopId: str
    createdDate: datetime

class UserInfo(UserInfoBase):
    class Config:
        orm_mode = True

class ProductInfoBase(BaseModel):
    id: str
    name: str
    description: str
    quantity: int
    price: int

class ProductCreate(ProductInfoBase):
    createdDate: datetime

class ProductInfo(ProductInfoBase):
    class Config:
        orm_mode = True
