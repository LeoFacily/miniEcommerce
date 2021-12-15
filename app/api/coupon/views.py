from typing import List
from fastapi import APIRouter, status, Depends

from app.db.db import get_db
from sqlalchemy.orm import Session

from app.models.models import Coupon
from .schemas import CouponSchema, ShowCouponSchema, UpdateCouponSchema
from app.repositories.coupon_repository import CouponRepository
from app.services.coupon_service import CouponService
from app.services.auth_service import only_admin

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, db: Session = Depends(get_db)):
    model = Coupon(**coupon.dict())
    db.add(Coupon(**coupon.dict()))
    db.commit

    db.refresh(model)
    return model

@router.get('/', response_model=List[ShowCouponSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Coupon).all()

#@router.get('/', response_model=List[ShowCouponSchema])
#def index(repository: CouponRepository = Depends()):
#    return repository.get_all()

@router.get('/{id}', response_model=ShowCouponSchema)
def show(id: int, repository: CouponRepository = Depends()):
    return repository.get_by_id(id)

#3 - Somente os campos limit e expire_at poderão ser alterados
@router.put('/{id}')
def update(id: int, coupon: UpdateCouponSchema, repository: CouponRepository = Depends()):   
    repository.update(id, coupon.dict())

#Cupons podem ser removidos
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, repository: CouponRepository = Depends()):
    repository.delete(id)