from fastapi import Depends
from app.api.order.schemas import OrderSchema
from app.models.models import Order
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository

from app.services.auth_service import authenticate

class OrderService:
    def __init__(self, order_repository: OrderRepository = Depends(),
                 product_repository: ProductRepository = Depends()):
        self.order_repository: order_repository
        self.product_repository: product_repository

    def create(self, order: OrderSchema):
        self.order_repository.create(Order(**OrderSchema.dic()))

    def get_all(self):
        self.order_repository.get_all()

    def list_orders():
        pass

    def order_details():
        pass