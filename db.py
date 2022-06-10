"""This script has a set of functions of database.
This ORM use sqlalchemy"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def create_session():
    url = 'mysql://root:root_password@127.0.0.1:3306/josmar_db'

    engine = create_engine(url)
    session_maker = sessionmaker(bind=engine)

    return session_maker()

class User(Base):
    """User instace"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    access = Column(Integer)

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, access={self.access!r})'
    
    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'access': self.access
        }

class Key(Base):
    """Key instace"""
    __tablename__ = 'key'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    room = Column(Integer, ForeignKey('room.id'))
    user = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, room={self.room!r})'

class Room(Base):
    """Room instace"""
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    # keys

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r})'


class Request(Base):
    pass
    # """Room instace"""
    # __tablename__ = 'room'

    # id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String)
    # # keys

    # def __repr__(self):
    #     return f'{self.__class__.__name__}(id={self.id!r}, name={self.name!r})'
