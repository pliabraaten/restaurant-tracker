
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Create base class for all models
Base = declarative_base()

# Define models (python classes) that will represent tables in db


# People Table
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# User Table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, ForeignKey('people.id'))
    username = Column(String)
    password = Column(String)

# Restaurant Table
class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String(15))
    date = Column(Date)
    cuisine = Column(String)
    rating = Column(Integer)
    tags = Column(String)

# Meal Table
class Meal(Base):
    __tablename__ = 'meals'
    id = Column(Integer, primary_key=True)
    rest_id = Column(Integer, ForeignKey('restaurants.id'))
    name = Column(String)
    price = Column(Integer)
    rating = Column(String)
    person = Column(Integer, ForeignKey('people.id'))
    notes = Column(String)  # Max 255 if need more - use TEXT datatype
    # TODO: photo attachment


