from pydantic import BaseModel

class SupplierSchema(BaseModel):
    name: str

class ShowSupplierSchema(SupplierSchema):
    id: int

    class config:
        orm_mode = True


