from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Coupon
from .schemas import CouponSchema, ShowCouponSchema, UpdateCouponSchema
from app.repositories.coupon_repository import CouponRepository
from app.services.coupon_service import CouponService


router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, repository: CouponRepository = Depends()):
    #repository.create(Coupon(**coupon.dict()))
    CouponService.create_coupon(Coupon(**Coupon.dict()))

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(coupon: CouponSchema, service: CouponService = Depends()):
    service.create(coupon)

@router.get('/', response_model=List[ShowCouponSchema])
def index(repository: CouponRepository = Depends()):
    return repository.get_all()

@router.get('/{id}', response_model=ShowCouponSchema)
def show(id: int, repository: CouponRepository = Depends()):
    return repository.get_by_id(id)

#3 - Somente os campos limit e expire_at poderão ser alterados
@router.put('/{id}')
def update(id: int, coupon: UpdateCouponSchema, repository: CouponRepository = Depends()):   
    CouponService.update_coupon(id, coupon)

#Cupons podem ser removidos
@router.delete('/{id}')
def delete(id: id, repository: CouponRepository = Depends()):
    repository.delete(id)

