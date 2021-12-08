from datetime import date
from pydantic import BaseModel

class AddressSchema(BaseModel):
    addresses = str
    city = str
    state = str
    number = str
    zicode = str
    neighbourhood = str

class ShowAddressSchema(AddressSchema):
    addresses = str
    city = str
    state = str
    number = str
    zicode = str
    neighbourhood = str

    class config:
        orm_mode = True

