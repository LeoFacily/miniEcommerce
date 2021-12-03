from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Customer
from .schemas import CustomerSchema
from app.repositories.customer_repository import CustomerRepository

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(costumer: CustomerSchema, repository : CustomerRepository = Depends()):
    repository.create(Customer(**costumer.dict()))

@router.get('/')
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()

