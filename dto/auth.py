from pydantic import BaseModel

class LoginRequest(BaseModel):   
    email: str
    password: str

class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    role: str