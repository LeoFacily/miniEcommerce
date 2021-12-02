from pydantic import BaseModel
from app.api.suppliers.schemas import ShowSuppliersSchema
from app.api.categories.schemas import ShowCategorySchema

class ProductSchema(BaseModel):
    description: str
    price: float
    technical_details: str
    image: str
    visible: bool
    category_id: int
    supplier_id: int

class ShowProductSchema(ProductSchema):
    #id: int
    category: ShowCategorySchema
    supplier: ShowSuppliersSchema

    class config:
        orm_mode = True
