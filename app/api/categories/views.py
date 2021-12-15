#from sqlalchemy.orm import Session
#from app.db.db import get_db

from typing import List
from fastapi import APIRouter, status, Depends
from app.db.db import get_db
from sqlalchemy.orm import Session

from app.models.models import Category
from app.repositories.category_repository import CategoryRepository
from app.services.auth_service import only_admin
from .schemas import CategorySchema, ShowCategorySchema

#router = APIRouter(dependencies=[Depends(only_admin)])
router = APIRouter()

@router.get('/', response_model=List[ShowCategorySchema])
def index(db: Session = Depends(get_db)):
    return db.query(Category).all()    

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowCategorySchema)
def create(category: CategorySchema, db: Session = Depends(get_db)):
    model = Category(**category.dict())
    db.add(Category(**category.dict()))
    db.commit()
    
    db.refresh(model)
    return model

#@router.post('/', status_code=status.HTTP_201_CREATED)
#def create(category: CategorySchema, repository: CategoryRepository = Depends()):
#    repository.create(Category(**category.dict()))

#@router.get('/', response_model=List[ShowCategorySchema])
#def index(repository: CategoryRepository = Depends(get_db)):
    #return repository.get_all()
 #   return CategoryRepository.get_all()
    #return db.query(Category).all()

#@router.get('/{id}', response_model=ShowCategorySchema)
#def show(id: int, db: Session = Depends(get_db)):
#    return db.query(Category).filter_by(id=id).first()
