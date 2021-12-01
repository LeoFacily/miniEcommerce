from fastapi import APIRouter

from app.models.models import Suppliers
from .product.views import router as product_router
from .categories.views import router as categories_router
from .suppliers.views import router as suppliers_router

router = APIRouter()

router.include_router(product_router, prefix='/product')

router.include_router(categories_router, prefix='/categories')

router.include_router(suppliers_router, prefix='/suppliers')

