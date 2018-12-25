from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://jean:mcsuaptesbuf@localhost/library', echo = True)

if __name__ == "__main__":
    print("ok")
