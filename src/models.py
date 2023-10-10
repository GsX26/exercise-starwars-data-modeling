import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(120), nullable=False)
    password = Column(String(20), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table character.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    height = Column(Integer)
    wheight = Column(Integer)
    birth_day = Column(String(10))
    gender = Column(Boolean(), nullable=False)
    eye_color = Column(String(20), nullable=False)
    hair_color = Column(String(20), nullable=False)
    home_word_id = Column(String(100))

class Favoritecharacter(Base):
    __tablename__ = 'favoritecharacter'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer)
    terraine = Column(String(200))
    gravity = Column(String(200))
    climate = Column(String(200))
    population = Column(Integer) 

class Favoriteplanet(Base):
    __tablename__ = 'favoriteplanet'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
