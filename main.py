from fastapi import FastAPI
from routers import product
from routers import users
from routers import auth
from database import engine, Base
from routers import orders

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(orders.router) 
