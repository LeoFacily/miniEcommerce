from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
from datetime import datetime

class ProductSchema(BaseModel):
    id: int
    quantity: int

class OrderSchema(BaseModel):
    address_id: int
    payment_method: int
    coupon_code: Optional[str] = None
    products: List[ProductSchema]

class OrderStatus(str, Enum):
    ORDER_PLACED = 'ORDER PLACED'
    ORDER_PAID = 'ORDER PAID'
    ORDER_SHIPPED = 'ORDER SHIPPED'
    ORDER_RECEIVED = 'ORDER RECEIVED'
    ORDER_COMPLETED = 'ORDER COMPLETED'
    ORDER_CANCELLED = 'ORDER CANCELLED'

class OrderStatusSchema(BaseModel):
    status:OrderStatus
    created_at: datetime = datetime.now()

class OrderSchema(BaseModel):
    number: str = ''
    status: str = ''
    customer_id:int = 0
    created_at: datetime = datetime.now()
    address_id: int = 0
    total_value: float = 0
    payment_form_id: int = 0
    total_discount: float = 0

    class Config:
        orm_mode = True

