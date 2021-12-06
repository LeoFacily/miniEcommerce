from fastapi import Depends
from app.api.customer.schemas import CustomerSchema
from app.repositories.customer_repository import CustomerRepository

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository = Depends()):
        self.customer_repository = customer_repository

    def create_customer(self, customer: CustomerSchema):
        CustomerRepository.create(**customer.dic())
                
    def update_customer(self, customer: CustomerSchema):
        CustomerRepository.update()

    