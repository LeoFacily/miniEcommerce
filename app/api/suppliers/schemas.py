from os import name
from pydantic import BaseModel

class SupplierSchema(BaseModel):
    id: int
    name: str

class ShowSupplierSchema(SupplierSchema):
    id: int

    class config:
        orm_mode = True


