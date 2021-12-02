from pydantic import BaseModel

class PaymentMethodSchema(BaseModel):
    id: int
    name: str
    enabled: bool

class ShowPaymentMethodSchema(PaymentMethodSchema):
    name: str

    class config:
        orm_mode = True


