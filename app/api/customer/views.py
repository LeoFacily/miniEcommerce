from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.db.db import get_db
from sqlalchemy.orm import Session

from app.models.models import Customer
from .schemas import CustomerSchema, ShowCustomerSchema
from app.repositories.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(costumer: CustomerSchema, repository : CustomerRepository = Depends()):
    #repository.create(Customer(**costumer.dict()))
    CustomerService.create_customer(**costumer.dic())

#@router.get('/')
#def index(repository: CustomerRepository = Depends()):
#    return repository.get_all()

@router.get('/', response_model=List[ShowCustomerSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Customer).all()
