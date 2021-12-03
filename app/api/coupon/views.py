from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Coupon
from .schemas import CouponSchema
from app.repositories.coupon_repository import CouponRepository
from app.services.coupon_service import CouponService


router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, repository: CouponRepository = Depends()):
    #repository.create(Coupon(**coupon.dict()))
    CouponService.create_coupon(Coupon(**Coupon.dict()))

@router.get('/')
def index(repository: CouponRepository = Depends()):
    return repository.get_all()

#3 - Somente os campos limit e expire_at poderão ser alterados
@router.put('/{id}')
def update(coupon: CouponSchema, repository: CouponRepository = Depends()):   
    repository.update(coupon.dict())

#Cupons podem ser removidos
@router.delete('/')
def delete(coupon: CouponSchema, repository: CouponRepository = Depends()):
    pass

