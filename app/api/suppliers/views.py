from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Supplier
from .schemas import SupplierSchema, ShowSupplierSchema
from app.repositories.supplier_repository import SupplierRepository

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SupplierSchema, repository: SupplierRepository = Depends()):
    repository.create(Supplier(**supplier.dict()))

@router.get('/', response_model=List[ShowSupplierSchema])
def index(repository: SupplierRepository = Depends()):
    return repository.get_all()
