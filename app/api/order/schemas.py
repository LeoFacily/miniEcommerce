from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

class OrderStatus(str, Enum):
    ORDER_PLACED = 'ORDER PLACED'
    ORDER_PAID = 'ORDER PAID'
    ORDER_SHIPPED = 'ORDER SHIPPED'
    ORDER_RECEIVED = 'ORDER RECEIVED'
    ORDER_COMPLETED = 'ORDER COMPLETED'
    ORDER_CANCELLED = 'ORDER CANCELLED'

class OrderProductSchema(BaseModel):
    id: int
    quantity: int

class OrderSchema(BaseModel):
    address_id: int
    payment_method: int
    coupon_code: Optional[str] = None
    products: List[OrderProductSchema]


