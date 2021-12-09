from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.db.db import get_db
from sqlalchemy.orm import Session

from app.models.models import Product
from app.repositories.product_repository import ProductRepository
from app.services.auth_service import only_admin
from .schemas import ProductSchema, ShowProductSchema

#router = APIRouter(dependencies=[Depends(only_admin)])
router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema, repository : ProductRepository = Depends()):
    repository.create(Product(**product.dict()))

#@router.get('/', response_model=List[ShowProductSchema])
#def index(repository: ProductRepository = Depends()):
#    return repository.get_all()

@router.get('/', response_model=List[ShowProductSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Product).all() 

#@router.get('/', response_model=List[ShowProductSchema]) 
#def index(db: ProductRepository = Depends()):
#    return db.get_all()

@router.get('/{id}', response_model=ShowProductSchema)
def show(id: int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)
