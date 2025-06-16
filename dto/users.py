from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    rol: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    rol: str

    class Config:
        from_attributes = True  # Para Pydantic v2