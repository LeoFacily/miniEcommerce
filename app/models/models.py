from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey
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

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = column(String(45))

class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = column(String(45))

class Product_Discounts(Base):
    __tablename__ = 'product_discounts'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.id))
    #product = relationship("Product", backref="produtos")
    mode = Column(String(45))
    value = Column(Float(10,2))
    payment_method_id = Column(Integer)