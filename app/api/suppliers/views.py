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

@router.get('/', response_model=List[ShowSupplierSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Supplier).all()
    
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowSupplierSchema)
def create(supplier: SupplierSchema, db: Session = Depends(get_db)):
    model = Supplier(**supplier.dict())
    db.add(Supplier(**supplier.dict()))
    db.commit()

    db.refresh(model)
    return model

#@router.get('/', response_model=List[ShowSupplierSchema])
#def index(repository: SupplierRepository = Depends()):
#    return repository.get_all()

