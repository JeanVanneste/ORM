from sqlalchemy import create_engine, and_
import database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://jean:mcsuaptesbuf@localhost/library', echo = True)
Session = sessionmaker(engine)


def create_editor(editorName, fondationYear):
    session = Session()

    editor = database.Editor()

    editor.name = editorName
    editor.fondationYear = fondationYear

    session.add(editor)
    session.commit()

def create_author(authorFirstName, authorLastName):
    session = Session()

    author = database.Author()

    author.firstName = authorFirstName
    author.lastName = authorLastName

    session.add(author)
    session.commit()

def create_collection(name, editorName):

    session = Session()

    collection = database.Collection()

    editor = session.query(database.Editor).filter(database.Editor.name==editorName).first()

    collection.name = name
    collection.editor = editor

    session.add(collection)
    session.commit()

def create_book(title, isbn, publicationYear, collectionName, authorFirstName, authorLastName):
    session = Session()

    book = database.Book()

    authors = session.query(database.Author).\
                    filter(and_(database.Author.firstName==authorFirstName, database.Author.lastName == authorLastName)).\
                    all()

    collection = session.query(database.Collection).\
                        filter_by(name=collectionName).\
                        one()
    book.authors = authors
    book.title = title
    book.isbn = isbn
    book.publicationYear = publicationYear
    book.collection = collection

    session.add(book)
    session.commit()

if __name__ == "__main__":
    pass