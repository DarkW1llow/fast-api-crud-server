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
    pushTokens: str

class UserInfo(UserInfoBase):
    class Config:
        orm_mode = True

class ProductInfoBase(BaseModel):
    name: str
    description: str
    quantity: int
    price: int
    id: str
    imageUrl: str

class ProductCreate(ProductInfoBase):
    createdDate: datetime

class ProductInfo(ProductInfoBase):
    class Config:
        orm_mode = True

class TransactionsInfoBase(BaseModel):
    id: str
    quantity: int
    sumPrice: int
    productId: str
    info: str
    createdDate: datetime

class TransactionsCreate(TransactionsInfoBase):
    createdDate: datetime

class TransactionsInfo(TransactionsInfoBase):
    class Config:
        orm_mode = True
