from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Product
from app.repositories.product_repository import ProductRepository
from .schemas import ProductSchema, ShowProductSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema, repository : ProductRepository = Depends()):
    repository.create(Product(**product.dict()))

@router.get('/')
def index(repository: ProductRepository = Depends()):
    return repository.get_all()

