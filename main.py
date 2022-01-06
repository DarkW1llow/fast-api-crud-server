from typing import List

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

@app.get("/login")
def get_user(useremail: str, userpassword: str, db: Session = Depends(get_db)):
    username = crud.get_user_by_username(db, email=useremail, password=userpassword)
    if username:
        return HTTPException(status_code=200, detail="Login Sucess")
    raise HTTPException(status_code=400, detail="User not existed")

@app.post("/createProduct", response_model=schemas.ProductInfo)
def create_user(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/product", response_model=schemas.ProductInfo)
def get_product(id: str, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, id=id)
    if product:
        return product
    raise HTTPException(status_code=400, detail="Product not existed")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)