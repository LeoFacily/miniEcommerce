from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import ProductDiscount
from .base_repository import BaseRepository

class ProductDiscountRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, ProductDiscount)

    def get_product_payment(self, product_id: int, payment_id: int):
        return self.session.query(self.model).filter(product_id = product_id, payment_id = payment_id).first()

   