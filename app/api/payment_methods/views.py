from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import PaymentMethods
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodSchema, db: Session = Depends(get_db)):
    db.add(PaymentMethods(**payment_method.dict()))
    db.commit()

#@router.get('/', response_model=List[ShowPaymentMethodSchema])
@router.get('/')
def index(db: Session = Depends(get_db)):
    return db.query(PaymentMethods).all()    

@router.get('/{id}', response_model=ShowPaymentMethodSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(PaymentMethods).filter_by(id = id).first()

@router.put('/{id}')
def update(id: int, payment_method: PaymentMethodSchema, db: Session = Depends(get_db)):
    query = db.query(PaymentMethods).filter_by(id=id)
    query.update(payment_method.dict())
    db.commit()

