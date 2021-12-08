from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Product
from app.repositories.product_repository import ProductRepository
from app.services.auth_service import only_admin
from .schemas import ProductSchema, ShowProductSchema

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema, repository : ProductRepository = Depends()):
    repository.create(Product(**product.dict()))

@router.get('/')
def index(repository: ProductRepository = Depends()):
    return repository.get_all()

