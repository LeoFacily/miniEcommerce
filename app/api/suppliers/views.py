from typing import List
from fastapi import APIRouter, status, Depends

from app.db.db import get_db
from sqlalchemy.orm import Session

from app.models.models import Supplier
from .schemas import SupplierSchema, ShowSupplierSchema
from app.repositories.supplier_repository import SupplierRepository
from app.services.auth_service import only_admin

#router = APIRouter(dependencies=[Depends(only_admin)])
router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SupplierSchema, repository: SupplierRepository = Depends()):
    repository.create(Supplier(**supplier.dict()))

#@router.get('/', response_model=List[ShowSupplierSchema])
#def index(repository: SupplierRepository = Depends()):
#    return repository.get_all()

@router.get('/', response_model=List[ShowSupplierSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Supplier).all()