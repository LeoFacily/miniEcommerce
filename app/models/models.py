from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import CheckConstraint, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean
from app.db.db import Base

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    supplier_id = Column(Integer, ForeignKey(Suppliers.id))
    supplier = relationship(Suppliers)
    technical_details = Column(String(255))
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey(Categories.id))
    #category = relationship("Categories", backref="categories")
    visible = Column(Boolean, default=True)

class PaymentMethods(Base):
    __tablename__ = 'paymentmethods'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    enabled = Column(Boolean)

class ProductDiscount(Base):
    __tablename__ = 'productdiscounts'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.id))
    product = relationship("Product")
    mode = Column(String(45))
    value = Column(Float(10,2))
    payment_method_id = Column(Integer, ForeignKey(PaymentMethods.id))
    payment_method = relationship(PaymentMethods)


