from datetime import date
from sqlite3 import Date
from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import INT, DateTime
from database import Base


class UserInfo(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)
    shopId = Column(String)
    createdDate = Column(DateTime)
    pushTokens = Column(String)

class ProductInfo(Base):
    __tablename__ = "product"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=true)
    description = Column(String, nullable=true)
    quantity = Column(INT, nullable=true)
    price = Column(INT, nullable=true)
    createdDate = Column(DateTime)
    modifiedDate = Column(DateTime, nullable=true)
    imageUrl = Column(String, nullable=true)

class TransactionsInfo(Base):
    __tablename__ = "transactions"
    id = Column(String, primary_key=True)
    quantity = Column(INT)
    sumPrice= Column(String)
    productId= Column(String)
    createdDate = Column(DateTime)
    info = Column(String, nullable=true)
