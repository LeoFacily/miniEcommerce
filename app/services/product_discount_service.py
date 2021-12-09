from fastapi.exceptions import HTTPException, status
from fastapi import Depends
from app.common.exceptions import PaymentMethodDiscountAlreadyExistsException, PaymentMethodsNotAvailableException
from app.models.models import ProductDiscount
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.api.product_discount.schemas import ProductDiscountSchema

class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, product_discount: ProductDiscountSchema):
        payment_method = self.payment_method_repository.get_by_id(
            product_discount.payment_method_id)

        if not payment_method or not payment_method.enabled:
            raise PaymentMethodsNotAvailableException()

        find_payment_method = self.product_discount_repository.filter({'product_id': product_discount.product_id, 'payment_method_id': product_discount.payment_method_id})

        if find_payment_method:
            raise PaymentMethodDiscountAlreadyExistsException()

        self.product_discount_repository.create(ProductDiscount(**product_discount.dict()))

    def update_discount(self, id: int, product_discount: ProductDiscountSchema):
        self.validate_discount_update(id, product_discount)
        self.product_discount_repository.update(id, product_discount.dict())

    def validate_discount(self, product_discount: ProductDiscountSchema):
        payment_method = self.payment_method_repository.get_by_id(product_discount.payment_method_id)

        if(self.session.query(self.model).filter_by(product_id=product_discount.product_id, payment_method_id=product_discount.payment_method_id).first()):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Payment method already used')  
        elif payment_method.enabled != True:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid method')  
        elif product_discount.value == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Is not a valid value')

    def validate_discount_update(self, id:int, discount: ProductDiscountSchema):
        payment_method = self.payment_method_repository.get_by_id(discount.payment_method_id)
        discount = self.product_discount_repository.get_by_product_and_payment_method(discount.product_id, discount.payment_method_id)
        if discount and discount.id != id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Payment method already used')  
        elif not payment_method or payment_method.enabled == False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid method')  
        elif discount.value == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid value')