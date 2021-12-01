from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Categories

from .schemas import CategorySchema

from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(category: CategorySchema, db: Session = Depends(get_db)):
    db.add(Categories(**category.dict()))
    db.commit()

#@router.get('/', response_model=List[ShowProductSchema])
@router.get('/')
def index(db: Session = Depends(get_db)):
    return db.query(Categories).all()


