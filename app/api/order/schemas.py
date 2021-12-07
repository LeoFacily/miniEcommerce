from datetime import date, datetime
from pydantic import BaseModel
from enum import Enum

class TypeMode(str, Enum):
    Value = 'value'
    Percentage = 'Percentage'

class CouponSchema(BaseModel):
    code: str
    expire_at: date
    limit: int
    type: TypeMode
    value: float

class UpdateCouponSchema(CouponSchema):
     id: int
     limit: int
     expire_at: datetime
     
class ShowCouponSchema(CouponSchema):
    code: str
    expire_at: date
    limit: int

    class config:
        orm_mode = True

