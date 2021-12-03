from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Coupon
from .schemas import CouponSchema
from app.repositories.coupon_repository import CouponRepository

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, repository: CouponRepository = Depends()):
    repository.create(Coupon(**coupon.dict()))

@router.get('/')
def index(repository: CouponRepository = Depends()):
    return repository.get_all()

@router.put('/')
def put():
    pass

@router.delete('/')
def delete():
    pass

