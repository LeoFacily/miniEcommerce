from fastapi import APIRouter

#from app.models.models import Suppliers

from .product.views import router as product_router
from .categories.views import router as categories_router
from .suppliers.views import router as suppliers_router
from .payment_methods.views import router as payment_methods_router
from .product_discount.views import router as product_discounts_router

router = APIRouter()

router.include_router(product_router, prefix='/product')

router.include_router(categories_router, prefix='/categories')

router.include_router(suppliers_router, prefix='/suppliers')

router.include_router(product_discounts_router, prefix='/productdiscounts')

router.include_router(payment_methods_router, prefix='/paymentmethods')
