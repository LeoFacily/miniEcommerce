#from sqlalchemy.orm import Session
#from app.db.db import get_db

from typing import List
from fastapi import APIRouter, status
from fastapi import Depends
from app.db.db import get_db

from app.models.models import Category
from app.repositories.category_repository import CategoryRepository
from app.services.auth_service import only_admin
from .schemas import CategorySchema, ShowCategorySchema

#router = APIRouter(dependencies=[Depends(only_admin)])
router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(category: CategorySchema, repository: CategoryRepository = Depends()):
    repository.create(Category(**category.dict()))

@router.get('/', response_model=List[ShowCategorySchema])
def index(repository: CategoryRepository = Depends(get_db)):
    #return repository.get_all()
    return CategoryRepository.get_all()
    #return db.query(Category).all()
    

#@router.post('/', status_code=status.HTTP_201_CREATED)
#def create(category: CategorySchema, db: Session = Depends(get_db)):
#    db.add(Category(**category.dict()))
#    db.commit()

#@router.get('/', response_model=List[ShowProductSchema])
#@router.get('/')
#def index(db: Session = Depends(get_db)):
#    return db.query(Category).all()    

#@router.get('/{id}', response_model=ShowCategorySchema)
#def show(id: int, db: Session = Depends(get_db)):
#    return db.query(Category).filter_by(id=id).first()
