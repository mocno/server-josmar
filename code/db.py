"""This script has a set of functions of database.
This ORM use sqlalchemy"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()


def create_session(uri):
    """This function create a session of database."""

    engine = create_engine(uri)
    session_maker = sessionmaker(bind=engine)

    return session_maker()

class User(BASE):
    """User instance"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    password = Column(String)
    access = Column(Integer)

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r})'

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'access': self.access
        }

class Key(BASE):
    """Key instance"""
    __tablename__ = 'key'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    room = Column(Integer, ForeignKey('room.id'))
    user = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, room={self.room!r})'

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'room': self.room,
            'user': self.user
        }

class Room(BASE):
    """Room instance"""
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    # keys

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r})'

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name
        }


# class Request(BASE):
#     """Request instance"""
#     __tablename__ = 'request'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     room = Column(Integer, ForeignKey('room.id'))

#     def __repr__(self):
#         return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r})'
