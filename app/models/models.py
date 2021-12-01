from sqlalchemy import Column
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean
from app.db.db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    technical_details = Column(String(255))
    image = column(String(255))
    visible = Column(Boolean, default=True)