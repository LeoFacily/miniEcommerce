from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.models.models import Category
from app.repositories.category_repository import CategoryRepository
from app.services.auth_service import only_admin
from .schemas import CategorySchema, ShowCategorySchema

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(category: CategorySchema, repository: CategoryRepository = Depends()):
    repository.create(Category(**category.dict()))

@router.get('/', response_model=List[ShowCategorySchema])
def index(repository: CategoryRepository = Depends()):
    return repository.get_all()

