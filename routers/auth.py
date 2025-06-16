from fastapi import APIRouter, HTTPException, Depends
from typing import List, Annotated
from database import  SessionLocal
from sqlalchemy.orm import  Session
import models.users
from dto.auth import LoginRequest
from dto.auth import UserRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/login")
def login(request:LoginRequest, db: db_dependency):
    user = db.query(models.user.User).filter(models.user.User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.password != request.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    return {"message": "Login successful", "user_id": user.id}

@router.post("/register")
def create_user(user: UserRequest, db: db_dependency):
    db_user = models.user.User(first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email,
                        password=user.password,
                        role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Register successful", "user_id": db_user.id}