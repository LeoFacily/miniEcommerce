from fastapi import Depends, HTTPException, status
from app.api.address.schemas import AddressSchema, ShowAddressSchema
from app.models.models import Address
from app.repositories.address_repository import AddressRepository
from app.repositories.customer_repository import CustomerRepository

class AddressService:
    def __init__(self, address_repository: AddressRepository = Depends(), customer_repository: CustomerRepository = Depends()):
        self.address_repository = address_repository
        self.customer_repository = customer_repository

    def create_address(self, address: AddressSchema):

        if not self.customer_repository.get_by_id(address.customer_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Nota customer')
        if address.primary:
            self.address_repository.remove_primary()
            
        self.AddressRepository.create(**address.dic())
                
    def update_address(self, address: AddressSchema):
        AddressRepository.update()

    