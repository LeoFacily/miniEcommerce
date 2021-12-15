from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from .schemas import UserSchema
from app.models.models import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
import bcrypt

from app.db.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(user: UserSchema, db: Session = Depends(get_db)):
    db.add(User(**user.dict()))
    db.commit()

#@router.get('/')
#def index(repository: UserRepository = Depends()):
#    return repository.get_all()

@router.get('/', response_model=List[UserSchema])
def index(db: Session = Depends(get_db)):
    return db.query(User).all()
