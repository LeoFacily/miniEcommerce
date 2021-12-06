from fastapi import Depends, HTTPException, status
from app.api.coupon.schemas import CouponSchema
from app.models.models import Coupon
from app.repositories.coupon_repository import CouponRepository

class CouponService:
    def __init__(self, coupon_repository: CouponRepository = Depends()):
        self.coupon_repository = coupon_repository

    def create_coupon(self, coupon: CouponSchema):

        #if self.coupon_repository.query_by_code(coupon.code):
        if self.coupon_repository.query(Coupon).filter(Coupon.code == coupon.code):
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail='Cupom já existente!')
            
        CouponRepository.create(**coupon.dic())
                
    def update_coupon(self, coupon: CouponSchema):
        CouponRepository.update(id, coupon.dict())

    def delete_coupon(self, coupon: CouponSchema):
        #self.coupon_repository.query.distinct()
        self.coupon_repository.query(Coupon).filter(Coupon.code == coupon.code)
        CouponRepository.delete(id)