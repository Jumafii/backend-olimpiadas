from sqlalchemy import Column, Integer, String, Numeric, Text
from sqlalchemy.sql import func
from database import Base

# models/product.py
class ProductList(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10,2), nullable=False)
    category = Column(String(100))
