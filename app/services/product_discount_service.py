from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.product_discount.schemas import ProductDiscountSchema
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.models.models import Product, PaymentMethod, ProductDiscount

class ProductDiscountService:

    def __init__(self, product_discount_repository: ProductDiscountRepository = Depends(), payment_method_repository: PaymentMethodRepository = Depends()):
        self.product_discount_repository = product_discount_repository
        self.payment_method_repository = payment_method_repository

    def create_discount(self, product_discount: ProductDiscountSchema):
        self.product_discount_repository.create(**product_discount.dic())

    def discount_validation(self, id: int, product_discount: ProductDiscountSchema):
        payment_method = self.payment_method_repository.get_by_id(product_discount.payment_method_id)
        
        if not payment_method:
            raise HTTPException(status_code=status.HTTP_200_OK, detail='Desconto já existente')
        elif payment_method.query.enabled != True:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail='Invalid Payment')

    def delete(self, int:id):
        self.sessiproduct_discount_repository.query(self.model).filter(id=id).delete()
        self.session.commit()