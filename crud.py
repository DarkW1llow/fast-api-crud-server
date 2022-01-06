from datetime import date, datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from sqlalchemy.sql.sqltypes import DateTime

import models, schemas


def get_user_by_username(db: Session, email: str, password: str):
    return db.query(models.UserInfo).filter(models.UserInfo.email == email, models.UserInfo.password == password).first()

def get_product_by_id(db: Session, id: str):
    return db.query(models.ProductInfo).filter(models.ProductInfo.id == id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.UserInfo(email = user.email, password = user.password, fullname = user.fullname, id = user.id, shopId=user.shopId, createdDate=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.ProductInfo(id = product.id, name = product.name, description = product.description, quantity = product.quantity, price = product.price, createdDate=datetime.now())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product