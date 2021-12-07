from enum import unique
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import CheckConstraint, ForeignKey
from sqlalchemy.sql.sqltypes import Date, DateTime, Integer, String, Float, Boolean
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

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    display_name = Column(String(100))
    email = Column(String(50), unique=True)
    role = Column(String(10))
    password = Column(String(100))

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name= Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45))
    birth_date = Column(Date)
    user_id = Column(Integer, ForeignKey(User.id))

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    addresses = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zipcode = Column(String(6))
    neighbourhood = Column(String(45))
    primary = Column(Boolean)
    customer_id = Column(Integer, ForeignKey(Customer.id))

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    number = Column(String(10))
    status = Column(String(15))
    customer_id = Column(Integer, ForeignKey(Customer.id))
    created_at = Column(DateTime)
    address_id = Column(Integer, ForeignKey(Address.id))
    total_value = Column(Float(10,2))
    payment_form_id = Column(Integer, ForeignKey(PaymentMethod.id))
    total_discount = Column(Float(10,2))


