from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Suppliers
from .schemas import SuppliersSchema

from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SuppliersSchema, db: Session = Depends(get_db)):
    db.add(Suppliers(**supplier.dict()))
    db.commit()

#@router.get('/', response_model=List[ShowProductSchema])
@router.get('/')
def index(db: Session = Depends(get_db)):
    return db.query(Suppliers).all()


