from fastapi import Depends

from app.api.product_discount.schemas import ProductDiscountSchema

from app.repositories.product_discount_repository import ProductDiscountRepository
from app.repositories.payment_method_repository import PaymentMethodRepository

class ProductDiscountService:

    def __init__(self, product_discount_repository: ProductDiscountRepository = Depends()):
        self.product_discount_repository = product_discount_repository

    def create_discount(self, product_discount: ProductDiscountSchema):
        ProductDiscountRepository.create(**product_discount.dic())

    