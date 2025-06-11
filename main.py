from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from users import router as users_router
from auth import router as auth_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)