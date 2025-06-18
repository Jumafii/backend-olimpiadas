from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"))
    date = Column(DateTime, default=datetime.utcnow)
    price = Column(Float)
    status = Column(String, default="pendiente")

    user = relationship("User", back_populates="orders")
    details = relationship("DetailsOrders", back_populates="pedido", cascade="all, delete-orphan")
