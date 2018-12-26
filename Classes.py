from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import YEAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key = True)
    title = Column(String(255))
    isbn = Column(String(17))
    publicationYear = Column(YEAR)
    FK_author = Column(Integer)
    FK_collection = Column(Integer)

    def __repr__(self):
        return ("<Book(title='%s')>" % self.title)

class Editor(Base):
    __tablename__ = 'editor'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    fondationYear = Column(YEAR, nullable=False)

    def __repr__(self):
        return "<Editor(name='%s', year of fondation = '%d')" % (
            self.name, self.fondationYear)

class Collection(Base):
    __tablename__ = 'collection'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    FK_editor = Column(Integer, nullable=False)

    def __repr__:
        return "<Collection(name='%s', editor='%s')" % (self.name,
            self.FK_editor)

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False))
