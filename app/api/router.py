from fastapi import APIRouter

#from app.models.models import Suppliers

from .product.views import router as product_router
from .categories.views import router as categories_router
from .suppliers.views import router as suppliers_router
from .payment_methods.views import router as payment_methods_router
from .product_discount.views import router as product_discounts_router
from .coupon.views import router as coupon_router
from .customer.views import router as customer_router
from .address.views import router as address_router
from .user.views import router as user_router
from .auth.views import router as auth_router
from .order.views import router as order_router
from app.services.auth_service import authenticate, get_user


router = APIRouter()

router.include_router(product_router, prefix='/product')

router.include_router(categories_router, prefix='/categories')

router.include_router(suppliers_router, prefix='/suppliers')

router.include_router(product_discounts_router, prefix='/productdiscounts')

router.include_router(payment_methods_router, prefix='/paymentmethods')

router.include_router(coupon_router, prefix='/coupon')

router.include_router(customer_router, prefix='/customer')

router.include_router(address_router, prefix='/address')

router.include_router(user_router, prefix='/users')

router.include_router(auth_router, prefix='/auth', tags=['auth'])

router.include_router(order_router, prefix='/orders', tags=['orders'])