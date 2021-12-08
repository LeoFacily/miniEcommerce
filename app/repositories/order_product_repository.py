from app.db.db import Session, get_db
from app.models.models import OrderProduct
from app.repositories.base_repository import BaseRepository
from fastapi import Depends

class OrderProductRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(session, OrderProduct)

  