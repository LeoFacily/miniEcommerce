from fastapi import APIRouter
from fastapi.params import Depends

from app.api.catalog.schemas import CatalogFilter
from app.repositories.product_repository import ProductRepository
from .schemas import ShowProductSchema

router = APIRouter()

#@router.get('/', response_model=Page[ShowProductSchema])
#def index(filter: CatalogFilter = Depends(), product_repository: ProductRepository = Depends()):
#    return product_repository.get_for_catalog()