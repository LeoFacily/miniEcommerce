from fastapi import Depends, HTTPException, status
from app.api.address.schemas import AddressSchema, ShowAddressSchema
from app.models.models import Address
from app.repositories.address_repository import AddressRepository

class AddressService:
    def __init__(self, address_repository: AddressRepository = Depends()):
        self.address_repository = address_repository

    def create_address(self, address: AddressSchema):
        AddressRepository.create(**address.dic())
                
    def update_address(self, address: AddressSchema):
        AddressRepository.update()

    