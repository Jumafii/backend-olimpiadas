from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Esto simula una de base de datos de usuarios
usuarios_db = {
    "oscar": {"password": "1234", "age": 30, "email": "oscar@email.com"},
    "ana": {"password": "abcd", "age": 25, "email": "ana@email.com"}
}

class User(BaseModel):
    user: str
    password: str

@router.post('/login')
async def login(user: User):
    usuario = usuarios_db.get(user.user)
    if not usuario or usuario["password"] != user.password:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    return {"mensaje": f"Bienvenido {user.user}", "email": usuario["email"], "age": usuario["age"]}