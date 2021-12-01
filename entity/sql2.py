from datetime import date

from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.elements import collate
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

engine = create_engine("sqlite:///dbProdutos.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    birthday = Column(Date)

    def __repr__(self) -> str:
        return f"Pessoa(name={self.name})"

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    discount = Column(Float)
    is_active = Column(Boolean, default=true)
    pessoa_id = Column(Integer, ForeignKey(Pessoa.id))
    pessoa = relationship("Pessoa", backref="pessoas")

    def __repr__(self) -> str:
        return f"Produto(name={self.name}"

class CategoriaTipo(Base):
    __table__name = "categoriatipo"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self) -> str:
        return f"CategoriaTipo(name={self.name}"

class Categoria(Base):
    __tablename__ = "Categoria"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    categoria_tipo_id = Column(Integer, ForeignKey(CategoriaTipo.id))
    produto_id = Column(Integer, ForeignKey(Produto.id))
    produto = relationship("Produto", backref="produtos")

    def __repr__(self) -> str:
        return f"Categoria(name={self.name})"


Base.metadata.create_all(engine)

p1 = Pessoa(name="Leonardo", age=25, birthday=date(2020, 1, 20), cpf="322335345342323")
p2 = Pessoa(name="Val", age=22, birthday=date(2019, 3, 23), cpf="4242234234424")
pd1 = Produto(name="Livro", description="Um livro qualquer", price=10.50, pessoa=p1)
pd2 = Produto(name="CD", description="Um cd qualquer", price=20.50, pessoa=p2)
ct1 = Categoria(name="Livros", description="Categoria de Livros geral", Produto=p1)
ctp1 = Categoria(name="Ficção", description="Fição e magia")

session.add_all([p1,p2,pd1,pd2,ct1,ctp1])
session.commit()