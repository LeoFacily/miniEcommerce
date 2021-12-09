from fastapi import Depends, HTTPException, status
from app.api.coupon.schemas import CouponSchema
from app.models.models import Coupon
from app.repositories.coupon_repository import CouponRepository
from app.common.exceptions import CouponCodeAleradyExistsException 

class CouponService:
    def __init__(self, coupon_repository: CouponRepository = Depends()):
        self.coupon_repository = coupon_repository

    def create(self, coupon: CouponSchema):

        if self.coupon_repository.find_by_code(coupon.code):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='This coupon is already in use')

        try:
            self.coupon_repository.create(Coupon(**coupon.dict()))
        except CouponCodeAleradyExistsException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)

    def update_coupon(self, coupon: CouponSchema):
        self.coupon_repository.update(id, coupon.dict())

    def delete_coupon(self, coupon: CouponSchema):
        #self.coupon_repository.query.distinct()
        #CouponRepository.delete(id)
        result = self.coupon_repository.query(Coupon).filter(Coupon.code == coupon.code)
        try:
            self.delete(id=id)
        except CouponCodeAleradyExistsException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)

        self.session.commit()

    def get_coupon_type(self, coupon: CouponSchema):
        return self.coupon_repository.query(Coupon).filter(Coupon.code == coupon.code)