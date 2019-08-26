from sqlalchemy import create_engine, Float, Column, Integer, String, Boolean, ForeignKey, update, \
    Unicode, or_, and_, DateTime, literal, JSON, Text, DECIMAL, BIGINT, Table
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(DECIMAL)


class OrderProduct(Base):
    __tablename__ = 'order_products'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'))
    product = relationship('Product')

    order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'))
    order = relationship('Order', back_populates='order_products')



class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_products = relationship('OrderProduct', back_populates='order')




engine = create_engine('{}://{}:{}@{}/{}'.format("postgresql",
                                                 "postgres",
                                                 "1q2w3e4r5t6y",
                                                 "localhost",
                                                 "bootstrap"),
                       isolation_level="READ COMMITTED")

Base.metadata.create_all(bind=engine)

session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)
