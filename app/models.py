
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from flask_login import UserMixin

from app import db

# Define models (python classes) that will represent tables in db

# People Table
class People(db.Model):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Establish one to one relationship with User table and one to many with Meal table
    user = relationship('User', back_populates='person', uselist=False)
    meals = relationship('Meal', back_populates='person')

# User Table
class User(db.Model, UserMixin):  # UserMixin allows Flask-Login methods to manage sessions
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    # Establish relationship with People
    person = relationship('People', back_populates='user')

# Restaurant Table
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String)
    phone_number = Column(String(15))
    cuisine = Column(String)
    rating = Column(Integer)
    # Establish many to one relationship with Meal and Tag
    meals = relationship('Meal', back_populates='restaurant')
    tags = relationship('Tag', back_populates='restaurant')

# Meal Table
class Meal(db.Model):
    __tablename__ = 'meals'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    price = Column(Float)
    rating = Column(String)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    notes = Column(String)  # Max 255 if need more - use TEXT datatype
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    # Establish relationship with Restaurant and People
    restaurant = relationship('Restaurant', back_populates='meals')
    person = relationship('People', back_populates='meals')

    # TODO: ADD PHOTO/IMAGE ATTACHMENT - HOW DOES THAT SAVE IN A DB? 

# Tags Table
class Tag(db.Model):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    # Establish relationship with Restaurant
    restaurant = relationship('Restaurant', back_populates='tags')