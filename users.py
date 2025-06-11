from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    user: str
    password: str
    age: int = None
    email: str = None

@router.post('/users')
async def crear_usuario(user: User):
    return f'Usuario {user.user} creado con éxito. Recuerde su email: {user.email}'