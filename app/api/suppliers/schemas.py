from pydantic import BaseModel

class SuppliersSchema(BaseModel):
    id: int
    name: str
