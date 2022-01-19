from datetime import date, datetime
from itertools import product
from os import name
from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from sqlalchemy.sql.sqltypes import DateTime

import models, schemas


def get_user_by_username(db: Session, email: str, password: str):
    return db.query(models.UserInfo).filter(models.UserInfo.email == email, models.UserInfo.password == password).first()

def get_product_by_id(db: Session, id: str):
    return db.query(models.ProductInfo).filter(models.ProductInfo.id == id).first()

def get_products(db: Session):
    return db.query(models.ProductInfo).limit(10).all()

def update_product(db: Session, product: schemas.ProductInfoBase, id: str):
    db_product = models.ProductInfo(name = product.name, description = product.description, quantity = product.quantity, price = product.price, imageUrl = product.imageUrl)
    db.query(models.ProductInfo).filter(models.ProductInfo.id == id).update({models.ProductInfo.name: product.name,models.ProductInfo.imageUrl:product.imageUrl,  models.ProductInfo.description: product.description, models.ProductInfo.quantity: product.quantity, models.ProductInfo.price: product.price})
    db.commit()
    return db_product

def delete_product(db: Session, id: str):
    db.query(models.ProductInfo).filter(models.ProductInfo.id == id).delete()
    db.commit()
    return "Delete Success"

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.UserInfo(email = user.email, password = user.password, fullname = user.fullname, id = user.id, shopId=user.shopId, createdDate=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_product(db: Session, product: schemas.ProductInfoBase):
    db_product = models.ProductInfo(id = product.id, name = product.name, description = product.description, quantity = product.quantity, price = product.price, createdDate=datetime.now(), imageUrl = product.imageUrl)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_transaction(db: Session, transactions: schemas.TransactionsCreate):
    db_transactions = models.TransactionsInfo(id = transactions.id, quantity = transactions.quantity, sumPrice = transactions.sumPrice, productId = transactions.productId, info = transactions.info, createdDate = transactions.createdDate)
    db.add(db_transactions)
    db.commit()
    db.refresh(db_transactions)
    return db_transactions

def update_transaction(db: Session, transactions: schemas.TransactionsInfoBase, id: str):
    db_transactions = models.TransactionsInfo(quantity = transactions.quantity, sumPrice = transactions.sumPrice, productId = transactions.productId, info = transactions.info, createdDate = transactions.createdDate)
    db.query(models.TransactionsInfo).filter(models.TransactionsInfo.id == id).update({models.TransactionsInfo.quantity: transactions.quantity, models.TransactionsInfo.sumPrice: transactions.sumPrice, models.TransactionsInfo.productId: transactions.productId, models.TransactionsInfo.info: transactions.info, models.TransactionsInfo.createdDate: transactions.createdDate})
    db.commit()
    return db_transactions

def get_transaction_by_id(db: Session, id: str):
    return db.query(models.TransactionsInfo).filter(models.TransactionsInfo.id == id).first()

def get_transactions(db: Session):
    return db.query(models.TransactionsInfo).limit(10).all()