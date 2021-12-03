  
from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends

from app.repositories.product_discount_repository import ProductDiscountRepository
from app.models.models import ProductDiscount
from .schemas import ProductDiscountSchema, ShowProductDiscountSchema

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, repository: ProductDiscountRepository = Depends()):
    repository.create(ProductDiscount(product_discount.dict()))

@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
    return repository.get_all()

