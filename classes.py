from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.dialects.mysql import YEAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
books_authors = Table('books_authors', Base.metadata,
                      Column('bookId', Integer, ForeignKey('books.id')),
                      Column('authorId', Integer, ForeignKey('authors.id'))
                    )
Base.metadata.create_all(engine)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key = True)
    title = Column(String(255))
    isbn = Column(String(17))
    publicationYear = Column(YEAR)
    FK_author = Column(Integer, ForeignKey('authors.id'), nullable = False)
    FK_collection = Column(Integer, ForeignKey('collections.id'),
                           nullable = False)

    collection = relationship("collection", back_populates = "collections")

    authors = relationship(
                           "authors",
                           secondary=books_authors,
                           back_populates="authors")

    def __repr__(self):
        return ("<Book(title='%s')>" % self.title)

class Editor(Base):
    __tablename__ = 'editors'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    fondationYear = Column(YEAR, nullable=False)

    collectionsPossessed = relationship("collection",
                                        back_populates = "collections")

    def __repr__(self):
        return "<Editor(name='%s', year of fondation = '%d')" % (
            self.name, self.fondationYear)

class Collection(Base):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    FK_editor = Column(Integer, ForeignKey('editors.id'), nullable=False)

    editor = relationship("editor", back_populates = "editors")

    booksPublished = relationship("book", back_populates = "books")

    def __repr__(self):
        return "<Collection(name='%s', editor='%s')" % (self.name,
            self.FK_editor)

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False)

    books = relationship(
                           "books",
                           secondary=books_authors,
                           back_populates="books")
