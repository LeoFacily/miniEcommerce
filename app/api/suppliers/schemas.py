from os import name
from pydantic import BaseModel

class SuppliersSchema(BaseModel):
    id: int
    name: str

class ShowSuppliersSchema(SuppliersSchema):
    id: int

    class config:
        orm_mode = True


