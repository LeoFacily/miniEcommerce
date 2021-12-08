from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Coupon
from app.services.order_service import OrderService
from .schemas import OrderSchema, ProductSchema
from app.models.models import Order, User
from app.repositories.order_repository import OrderRepository
from app.repositories.coupon_repository import CouponRepository
from app.services.auth_service import get_user, only_admin

#router = APIRouter(dependencies=[Depends(get_user)])
router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(order_schema: OrderSchema, user: User = Depends(get_user), service: OrderService = Depends()):
    OrderService.create(Order)

@router.get('/', response_model=List[ProductSchema])
def index(repository: CouponRepository = Depends()):
    return repository.get_all()

@router.get('/{id}', response_model=OrderSchema)
def show(id: int, repository: CouponRepository = Depends()):
    return repository.get_by_id(id)


