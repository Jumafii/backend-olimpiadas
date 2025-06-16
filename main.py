from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from models.users import router as users_router
from dto.auth import router as auth_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)