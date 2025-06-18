from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from database import Base

class DetailsOrders(Base):
    __tablename__ = "details_orders"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    description = Column(Text)
    price = Column(Float)

    pedido = relationship("Orders", back_populates="details")