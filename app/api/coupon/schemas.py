from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum

class CouponMode(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'

class CouponSchema(BaseModel):
    code: str
    expire_at: Optional[datetime] = None
    limit: Optional[int] = None
    mode: CouponMode
    value: float

class UpdateCouponSchema(CouponSchema):
     limit: int
     expire_at: datetime

class UpdateCouponsSchema(BaseModel):
    limit: int
    expire_at: datetime     

class ShowCouponSchema(CouponSchema):
    id: int

    class config:
        orm_mode = True


