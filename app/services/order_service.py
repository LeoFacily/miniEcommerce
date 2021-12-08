from datetime import datetime
from typing import List
from fastapi import HTTPException, status
from fastapi.param_functions import Depends
from app.api.categories.views import create
from app.api.order.schemas import OrderSchema, ProductSchema, OrderStatus, OrderStatusSchema, OrderProductSchema
from app.api.coupon.schemas import CouponType
from app.models.models import OrderProduct, OrderStatus, Order, User
from app.repositories.order_repository import OrderRepository
from app.repositories.order_product_repository import OrderProductRepository
from app.services.coupon_service import CouponService
from app.repositories.address_repository import AddressRepository
from app.repositories.order_status_repository import OrderStatusRepository
from app.repositories.order_product_repository import OrderStatusRepository
from app.repositories.customer_repository import CustomerRepository
from app.repositories.product_repository import ProductRepository
from random import randint

class OrderService:
    def __init__(self, orders_repository: OrderRepository = Depends(), order_product_repository: OrderProductRepository = Depends(), order_statuses_repository : OrderStatusRepository = Depends(),
                products_repository: ProductRepository = Depends(),customers_repository: CustomerRepository = Depends(),address_repository: AddressRepository = Depends(),
                coupon_service: CouponService = Depends()):
        self.orders_repository = orders_repository
        self.order_product_repository = order_product_repository
        self.order_statuses_repository = order_statuses_repository
        self.products_repository = products_repository
        self.customers_repository = customers_repository
        self.addresses_repository = address_repository
        self.coupons_service = coupon_service

    def create(self, order_schema: OrderSchema):
        order_schema = OrderSchema()
        order_schema.number = randint(0, 9999)
        order_schema.status = OrderStatus.ORDER_PLACED
        order_schema.created_at = datetime.now()
        order_schema.payment_form_id = order_schema.payment_form_id
        order_schema.customer_id = self.customers_repository.get_by_id(order_schema.customer_id)
        order_schema.address_id = order_schema.address_id
        order_schema.total_value = self.get_order_value(order_schema.products)
        order_schema.total_discount = self.get_discount(order_schema.coupon_code, order_schema.total_value)
        
        #Order Products
        self.orders_repository.create(Order(**order_schema.dict()))
        
        #Pega id Ordem
        order_id = self.orders_repository.get_by_number(order_schema.id)
        
        #Cria Status Ordem
        self.create_order_status(order_id,OrderStatus.ORDER_PLACED)
        
        #Cria Ordem vs Produtos
        #self.create_order_product(order_id,List[ProductSchema]

    def create_order_status(self, id: int, order_status_schema: OrderStatusSchema):
        self.order_statuses_repository.create(OrderStatus(**order_status_schema.dict()))

    def create_order_product(self, id: int, product_list: List[ProductSchema]):
        for p in List[product_list]:
            self.order_product_repository.create(OrderProduct(**product_list.dict()))

    def get_discount(self, code: str, total_value: float):
        coupon_type = self.coupons_service.get_coupon_type(code)

        if coupon_type(CouponType) == CouponType.Percentage:
            discount = (coupon_type.value * total_value)-total_value
        else:
            discount = coupon_type.value
        
        return discount

    def get_order_value(self, products_list: List[ProductSchema]):
        order_value: float = 0.00
        for product in products_list:
            order_value += (float(self.products_repository.get_by_id(product.id).price) * product.quantity)
        return order_value

    def validate_address(self, customer_id, address_id):
        query = self.addresses_repository.get_by_id(address_id) 
        if not query or query.customer_id != customer_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Inválid address')

  