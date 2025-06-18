from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.orders import Orders
from models.details_orders import DetailsOrders
from dto.orders import OrdersCreate, OrdersResponse, ChangeStatusRequest

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
    responses={404: {"description": "Not found"}}
)

@router.get("/pendientes", response_model=List[OrdersResponse])
def get_pedidos_pendientes(db: Session = Depends(get_db)):
    return db.query(Orders).filter(Orders.status == "pendiente").all()

@router.post("/", response_model=OrdersResponse)
def crear_pedido(pedido_data: OrdersCreate, db: Session = Depends(get_db)):
    pedido = Orders(
        user_id=pedido_data.user_id,
        price=pedido_data.price,
        status="pendiente"
    )
    db.add(pedido)
    db.flush()

    for item in pedido_data.details:
        detalle = DetailsOrders(
            order_id=pedido.id,
            product_id=item.product_id,
            description=item.description,
            price=item.price
        )
        db.add(detalle)

    db.commit()
    db.refresh(pedido)
    return pedido

@router.put("/{order_id}/estado")
def cambiar_estado_pedido(order_id: int, data: ChangeStatusRequest, db: Session = Depends(get_db)):
    pedido = db.query(Orders).filter(Orders.id == order_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    if data.status not in ["pendiente", "aprobado", "anulado"]:
        raise HTTPException(status_code=400, detail="Estado inválido")

    pedido.status = data.status
    db.commit()
    db.refresh(pedido)
    return {"mensaje": f"Estado cambiado a '{data.status}'"}

@router.get("/{order_id}", response_model=OrdersResponse)
def get_pedido(order_id: int, db: Session = Depends(get_db)):
    pedido = db.query(Orders).filter(Orders.id == order_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido