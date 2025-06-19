from fastapi import FastAPI
from routers.product import router as product_router
from routers.users import router as users_router
from routers.auth import router as auth_router
from database import engine, Base
from routers import product, orders, users, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(product.router)
app.include_router(orders.router) 


