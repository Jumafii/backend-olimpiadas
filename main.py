from fastapi import FastAPI
from routers import product
from routers import users
from routers import auth
from database import engine, Base
from routers import orders
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Orígenes permitidos
    allow_credentials=True,           # Permitir cookies/autenticación
    allow_methods=["*"],              # Métodos HTTP permitidos
    allow_headers=["*"],              # Headers permitidos
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(orders.router) 

for route in app.include_router:
    print(f"{route.path} -> {route.name}")