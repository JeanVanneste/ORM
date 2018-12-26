from sqlalchemy import create_engine
from classes import Book, Editor, Collection, Author
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://jean:mcsuaptesbuf@localhost/library', echo = True)

if __name__ == "__main__":
    print("ok")
