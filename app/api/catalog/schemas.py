from app.models.models import Supplier
from fastapi import Query
from pydantic import BaseModel
from typing import List

class CatalogFilter:
    def __init__(self, description: str = Query(None), 
                category_id: int = Query(None), 
                min_price: float = Query(None), 
                max_price: float = Query(None)):
        self.description = description
        self.category_id = category_id
        self.min_price = min_price
        self.max_price = max_price

class ShowCategorySchema(BaseModel):
    name: str
    id: int

    class config:
        orm_mode = True


class ShowSupplierSchema(BaseModel):
    id: int
    name: str

    class config:
        orm_mode = True    

class ShowDiscountSchema(BaseModel):
    mode: str
    value: float

    class config:
        orm_mode = True    

class ShowPaymentMethodSchema(BaseModel):
    name: str
    class config:
        orm_mode = True    

class ShowProductSchema(BaseModel):
    id: int
    description: str
    price: float
    category: ShowCategorySchema
    Supplier: ShowSupplierSchema
    discounts: List[ShowDiscountSchema]

    class config:
        orm_mode = True
