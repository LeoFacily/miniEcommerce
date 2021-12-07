from fastapi import Depends
from sqlalchemy.sql.functions import user
from app.api.customer.schemas import CustomerSchema
from app.models.models import User
from app.repositories.customer_repository import CustomerRepository
from app.repositories.user_repository import UserRepository

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository = Depends(), user_repository: UserRepository = Depends()):
        self.customer_repository = customer_repository
        self.user_repository = user_repository

    def create_customer(self, customer: CustomerSchema):
        if not self.user_repository.query(User).filter(User.email == customer.email):
            UserRepository.create(**user.dict())
            CustomerRepository.create(**customer.dic())
                
    def update_customer(self, customer: CustomerSchema):
        CustomerRepository.update()

    