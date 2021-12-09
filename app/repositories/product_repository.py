from fastapi import Depends
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from app.api.catalog.schemas import CatalogFilter
from app.db.db import get_db
from app.models.models import Product
from .base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Product)

    def get_for_catalog(self, filter: CatalogFilter):
        queryset = [
            Product.visible == True
        ]
        if filter.category_id:
            queryset.append(Product.category_id == filter.category_id)
        if filter.supplier_id:
            queryset.append(Product.supplier_id == filter.supplier_id)

        #self.query().filter(Product.category_id == 1)

        #return self.queryset

