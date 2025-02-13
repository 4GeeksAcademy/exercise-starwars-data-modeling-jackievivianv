import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    id_films = Column(Integer, ForeignKey('films.id'))
    id_species = Column(Integer, ForeignKey('species.id'))
    id_starships = Column(Integer, ForeignKey('starships.id'))
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    favoritos_people = relationship('Favorites', backref = 'people', lazy = True)
    vehicles = relationship('Vehicles', backref = 'people', lazy = True)
    species = relationship('Species', backref = 'people', lazy = True)
    starships = relationship('Starships', backref = 'people', lazy = True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    id_films = Column(Integer, ForeignKey('films.id'))
    gravity = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    favoritos_planets = relationship('favorites', backref = 'planets', lazy = True)
    people = relationship('People', backref = 'planets', lazy = True)
    
class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    average_height = Column(String(250), nullable=False)
    average_lifespan = Column(String(250), nullable=False)
    eye_colors = Column(String(250), nullable=False)
    hair_colors = Column(String(250), nullable=False)
    skin_colors = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    id_people = Column(Integer, ForeignKey('people.id'))
    id_films = Column(Integer, ForeignKey('films.id'))
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    favoritos_species = relationship('Favorites', backref = 'species', lazy = True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    id_films = Column(Integer, ForeignKey('films.id'))
    id_people = Column(Integer, ForeignKey('people.id'))
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    favoritos_vehicles = relationship('Favorites', backref = 'vehicles', lazy = True)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model= Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passenger = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables= Column(String(250), nullable=False)
    id_films = Column(Integer, ForeignKey('films.id'))
    id_people = Column(Integer, ForeignKey('people.id'))
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    favoritos_starships = relationship('Favorites', backref = 'starships', lazy = True)

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    episode_id = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    producer = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=False)
    id_species = Column(Integer, ForeignKey('species.id'))
    id_starships = Column(Integer, ForeignKey('starships.id'))
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))
    id_people = Column(Integer, ForeignKey('people.id'))
    id_planets = Column(Integer, ForeignKey('planets.id'))
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    favoritos_films = relationship('Favorites', backref = 'films', lazy = True)
    people = relationship('People', backref = 'films', lazy = True)
    starships = relationship('Starships', backref = 'films', lazy = True)
    species = relationship('Species', backref = 'films', lazy = True)
    planets = relationship('Planets', backref = 'films', lazy = True)
    vehicles = relationship('Vehicles', backref = 'films', lazy = True)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=True)
    id_films = Column(Integer, ForeignKey('films.id'))
    id_people = Column(Integer, ForeignKey('people.id'))
    id_planets = Column(Integer, ForeignKey('planets.id'))
    id_species = Column(Integer, ForeignKey('species.id'))
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))
    id_starships = Column(Integer, ForeignKey('starships.id'))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favoritos_user = relationship('Favorites', backref = 'user', lazy = True)
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
