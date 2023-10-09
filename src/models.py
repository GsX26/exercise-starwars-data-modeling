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
    Full_name = Column(String(100), nullable=False)
    Height = Column(Integer)
    Wheight = Column(Integer)
    Birth_day = Column(String(10))
    Gender = Column(Boolean(), nullable=False)
    Eye_color = Column(String(20), nullable=False)
    Hair_color = Column(String(20), nullable=False)
    Home_word_id = Column(String(100))

class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacter'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Diameter = Column(Integer)
    Terraine = Column(String(200))
    Gravity = Column(String(200))
    Climate = Column(String(200))
    Population = Column(Integer) 

class FavoritePlanet(Base):
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
