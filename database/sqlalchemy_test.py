from sqlalchemy.orm import create_engine, Session
engine = create_engine("postgres+psycopg2://postgres:pass@localhost/mydb")
from sqlalchemy.orm import sessionmaker, Session

Session = sessionmaker(bind=engine)
session = Session(bind=engine)

session = Session ()