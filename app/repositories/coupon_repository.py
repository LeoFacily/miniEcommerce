from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Coupon
from .base_repository import BaseRepository

class CouponRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Coupon)

    def find_by_code(self, code):
        return self.session.query(self.mode).filter(code=code).first()

    def delete(self, id: int):
        self.session.query(self.model).filter_by(id=id).delete()
        self.session.commit()