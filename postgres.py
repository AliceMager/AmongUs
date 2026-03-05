from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/amongus_db"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)