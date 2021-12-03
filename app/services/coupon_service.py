from fastapi import Depends

from app.api.coupon.schemas import CouponSchema

from app.repositories.coupon_repository import CouponRepository

class CouponService:
    def __init__(self, coupon_repository: CouponRepository = Depends()):
        self.coupon_repository = coupon_repository

    def create_coupon(self, coupon: CouponSchema):
        self.coupon_repository.create(**coupon.dic())
                
    def update_coupon(self, coupon: CouponSchema):
        self.coupon_repository.update()

    def delete_coupon(self, coupon: CouponSchema):
        self.coupon_repository.remove()