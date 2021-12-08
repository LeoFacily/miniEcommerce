from datetime import date
from pydantic import BaseModel

class CustomerSchema(BaseModel):

    first_name: str
    last_name: float
    phone_number: str
    genre: str
    document_id: str #Como fosse CPF nao pode alterar
    birth_date: date
    user_id: int

class ShowCustomerSchema(CustomerSchema):
    id: int
    first_name: str
    last_name: str

    class config:
        orm_mode = True

class UpdateCustomerSchema(CustomerSchema):
    first_name: str
    last_name: float
    phone_number: str
    genre: str
    birth_date: date

