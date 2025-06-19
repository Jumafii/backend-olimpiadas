from pydantic import BaseModel
from datetime import datetime
from typing import List

class DetailsOrdersCreate(BaseModel):
    product_id: int
    description: str
    price: float

class OrdersCreate(BaseModel):
    user_id: int
    price: float
    details: List[DetailsOrdersCreate]

class DetailsResponse(DetailsOrdersCreate):
    id: int

    class Config:
        from_attributes = True

class OrdersResponse(BaseModel):
    id: int
    user_id: int
    date: datetime
    price: float
    status: str
    details: List[DetailsResponse]

    class Config:
        from_attributes = True

class ChangeStatusRequest(BaseModel):
    status: str  # "pendiente", "aprobado" o "anulado"
