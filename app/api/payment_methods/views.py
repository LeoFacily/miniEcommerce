from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.db.db import get_db
from sqlalchemy.orm import Session

from app.repositories.payment_method_repository import PaymentMethodRepository
from app.models.models import PaymentMethod
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema
from app.services.auth_service import only_admin

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodSchema, repository: PaymentMethodRepository = Depends()):
    repository.create(PaymentMethod(**payment_method.dict()))


#@router.get('/', response_model=List[ShowPaymentMethodSchema])
#def index(repository: PaymentMethodRepository = Depends()):
#    return repository.get_all()

@router.get('/', response_model=List[ShowPaymentMethodSchema])
def index(db: Session = Depends(get_db)):
    return db.query(PaymentMethod).all()

@router.get('/{id}', response_model=ShowPaymentMethodSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(PaymentMethod).filter_by(id = id).first()

