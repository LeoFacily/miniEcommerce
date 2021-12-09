from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.db.db import get_db
from sqlalchemy.orm import Session

from app.models.models import Address
from .schemas import AddressSchema, ShowAddressSchema
from app.repositories.address_repository import AddressRepository
from app.services.address_service import AddressService

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(address_schema: AddressSchema, repository : AddressRepository = Depends()):
    #repository.create(Customer(**costumer.dict()))
    AddressService.create_address(Address(**address_schema.dic()))

#@router.get('/')
#def index(repository: AddressRepository = Depends()):
#    return repository.get_all()

@router.get('/', response_model=List[ShowAddressSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Address).all()
