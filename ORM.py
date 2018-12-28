from sqlalchemy import create_engine
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

if __name__ == "__main__":
    print(engine)
    create_editor('Gallimard', 1911)
