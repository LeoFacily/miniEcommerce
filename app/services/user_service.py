from fastapi import Depends, HTTPException, status
from app.api.coupon.schemas import CouponSchema
from app.api.user.schemas import UserSchema, ShowUserSchema
from app.models.models import User
from app.repositories.user_repository import UserRepository
import bcrypt

from app.services.auth_service import authenticate

class UserService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    def create_user(self, user: UserSchema = Depends(authenticate)):
        user.password = bcrypt.hashpw(
        user.password.encode('utf8'), bcrypt.gensalt())
    
        if self.user_repository.query(User).filter(User.email == user.email):
            raise HTTPException(status_code = status.HTTP_406_NOT_ACCEPTABLE, detail='Email nao pode ser alterado')
       
       
        UserRepository.create(User(**user.dict()))



