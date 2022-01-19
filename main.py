from typing import List
from urllib import response

from sqlalchemy.sql.functions import user

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/signup", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, email=user.email, password=user.password)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def get_user(useremail: str, userpassword: str, db: Session = Depends(get_db)):
    username = crud.get_user_by_username(db, email=useremail, password=userpassword)
    if username:
        return username.email, username.password, username.pushTokens 
    raise HTTPException(status_code=400, detail="User not existed")

@app.post("/createProduct", response_model=schemas.ProductInfo)
def create_user(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.post("/deleteProduct")
def delete_product(id: str, db: Session = Depends(get_db)):
    return crud.delete_product(db=db, id=id)

@app.get("/product", response_model=schemas.ProductInfo)
def get_product(id: str, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, id=id)
    if product:
        return product
    raise HTTPException(status_code=400, detail="Product not existed")

@app.post("/updateProduct")
def update_product(id: str, product: schemas.ProductInfo , db: Session = Depends(get_db)):
    return crud.update_product(db, product=product, id=id)

@app.get("/products", response_model=List[schemas.ProductInfo])
def get_products(db: Session = Depends(get_db)):
    products = crud.get_products(db)
    if products:
        return products
    raise HTTPException(status_code=400, detail="Product not existed")

@app.post("/createTransaction", response_model=schemas.TransactionsInfo)
def create_transaction(transactions: schemas.TransactionsCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transactions=transactions)

@app.post("/updateTransaction")
def update_transaction(id: str, transactions: schemas.TransactionsInfo, db: Session = Depends(get_db)):
    return crud.update_transaction(db, transactions=transactions, id=id)

@app.get("/transaction", response_model=schemas.TransactionsInfoBase)
def get_transaction(id: str, db: Session = Depends(get_db)):
    transactions = crud.get_transaction_by_id(db, id=id)
    if transactions:
        return transactions
    raise HTTPException(status_code=400, detail="Transactions not existed")

@app.get("/transactions", response_model=List[schemas.TransactionsInfo])
def get_transactions(db: Session = Depends(get_db)):
    transactionss = crud.get_transactions(db)
    if transactionss:
        return transactionss
    raise HTTPException(status_code=400, detail="Transactions not existed")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)