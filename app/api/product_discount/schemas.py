from pydantic import BaseModel
from app.api.product.schemas import ProductSchema
from app.api.payment_methods.schemas import PaymentMethodSchema
from enum import Enum

class DiscountMode(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'

class ProductDiscountSchema(BaseModel):
    id: int
    product_id: int
    mode: DiscountMode
    value: float
    payment_method_id: int

class ShowProductDiscountSchema(ProductDiscountSchema):
    id: int
    payment_methods: PaymentMethodSchema
    product: ProductSchema

    class config:
        orm_mode = True