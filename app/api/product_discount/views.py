  
from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends

from app.db.db import get_db
from sqlalchemy.orm import Session

from app.repositories.product_discount_repository import ProductDiscountRepository
from app.models.models import ProductDiscount
from .schemas import ProductDiscountSchema, ShowProductDiscountSchema
from app.services.product_discount_service import ProductDiscountService
from app.services.auth_service import only_admin

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, repository: ProductDiscountRepository = Depends()):
    #repository.create(ProductDiscount(product_discount.dict()))
    ProductDiscountService.create_discount(product_discount)

@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
    #return repository.get_all()
    ProductDiscountService.listar()

@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(db: Session = Depends(get_db)):
    return db.query(ProductDiscount).all()
