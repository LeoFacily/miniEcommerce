from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import CheckConstraint, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Float, Boolean
from app.db.db import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    supplier_id = Column(Integer, ForeignKey(Supplier.id))
    supplier = relationship(Supplier)
    technical_details = Column(String(255))
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id))
    #category = relationship("Categories", backref="categories")
    visible = Column(Boolean, default=True)

class PaymentMethod(Base):
    __tablename__ = 'payment_methods'

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
    payment_method_id = Column(Integer, ForeignKey(PaymentMethod.id))
    payment_method = relationship(PaymentMethod)

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True, unique=True)
    code = Column(String(10))
    expire_at = Column(DateTime)
    limit = Column(Integer)
    type = Column(String(15))
    value = Column(Float(10,2))
    teste = Column(String(50))

