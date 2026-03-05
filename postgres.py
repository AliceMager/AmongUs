from enum import Enum
from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = 'postgresql://postgres:postgres@localhost:5432/amongus_db'
engine = create_engine(SQLALCHEMY_DB_URL)

Session = sessionmaker(bind=engine)
Session = Session()

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
